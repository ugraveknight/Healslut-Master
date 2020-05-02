from pyautogui import locateAll, center
from glob import glob
from itertools import cycle
from time import sleep, time
from enum import Enum
import os.path
import color_utils

def is_close_to_positions(positions, position):
	for known_position in positions:
		if (abs(position.x - known_position.x) < 5 and abs(position.y - known_position.y) < 5):
			return True
	return False

def get_team_from_color(color):
	blue = (67, 200, 244) # Colors are actually a bit transparent, so it's not possible to define the exact color
	red = (243, 24, 45)
	return 'Blue' if color_utils.get_closest_color([blue, red], color) == blue else 'Red'

def get_hero_from_path(path):
	return os.path.basename(path)[0:-4].replace(' Assist', '')

class Hero:
	def __init__(self, hero, team):
		self.hero = hero
		self.team = team

	def __repr__(self):
		return f'{self.hero} ({self.team})'

	def __eq__(self, other):
		return str(self) == str(other)

class Action(Enum):
	KILL = 'KILL'
	SUICIDE = 'SUICIDE'
	RESURRECT = 'RESURRECT'

class KillfeedItem:
	def __init__(self, affected_hero: Hero, action: Action, active_hero = None, assists = []):
		self.affected_hero = affected_hero
		self.action = action
		self.active_hero = active_hero
		self.assists = assists

	def __str__(self):
		active_hero = self.active_hero or ''
		assists_joined = ', '.join([str(assist) for assist in self.assists])
		assists = f' ({assists_joined})' if len(self.assists) else ''
		return f'{active_hero}{assists} {self.action.name} {self.affected_hero}'.lstrip()

	def __eq__(self, other):
		return str(self) == str(other)

	def is_plausible(self):
		# Filter out all "Suicides", as these are mostly wrong detected
		if self.action == Action.SUICIDE:
			return False
		if self.action == Action.RESURRECT and self.active_hero.hero != 'Mercy':
			return False
		if len(self.assists) > 0 and self.assists[0].team != self.active_hero.team:
			return False
		return True

last_feed_items = []
MY_TEAM = 'Blue'

def Main(im,Files,Sub,Dom,Cords,c_killfeed,KFPath,BorderPixels,Debug=False):
	class RecognizedObject:
		def __init__(self, hero, position, team):
			self.hero = hero
			self.position = position
			self.team = team

	# TODO:
	# Here are some optimizations possible based on the game mode. For example it might be enough to search only for a few heroes and not
	# all. Or you can stop searching when you found out that the team's Mercy is not in the feed.

	recognized_objects = []
	for file in Files:
		# Find image of hero in killfeed
		found_positions = [center(position) for position in locateAll(file, im, confidence=0.7, region=Cords)]

		# The identical image might be found multiple times with only a few pixes offset, so remove duplicates
		cleaned_positions = []
		for found_position in found_positions:
			# Only add if not very close position already in list
			if not is_close_to_positions(cleaned_positions, found_position):
				cleaned_positions.append(found_position)

		for position in cleaned_positions:
			# Get team
			color = im.getpixel((int(position.x - BorderPixels[0 if 'Assist' in file else 1]), int(position.y)))
			team = get_team_from_color(color) # TODO: This should also work with custom team colors

			recognized_objects.append(RecognizedObject(get_hero_from_path(file), position, team))

	# Group objects by line (= y position)
	lines = []
	recognized_objects.sort(key=lambda element: element.position.y)
	for recognized_object in recognized_objects:
		y = recognized_object.position.y
		found_line = False
		for line in lines:
			if abs(line[0] - y) < 5:
				line[1].append(recognized_object)
				found_line = True
				break
		if not found_line:
			lines.append((y, [recognized_object]))

	# Generate feed object
	feed_items = []
	for line in lines:
		objects = line[1]
		# Sort objects in lines from left to right
		objects.sort(key=lambda element: element.position.x)

		active_hero = Hero(objects[0].hero, objects[0].team) if len(objects) > 1 else None
		assist_objects = objects[1:-1] if len(objects) > 2 else []
		assists = [Hero(element.hero, element.team) for element in assist_objects]
		affected_hero = Hero(objects[-1].hero, objects[-1].team)

		# Detect action
		action = Action.KILL
		if active_hero == None:
			action = Action.SUICIDE
		elif active_hero.team == affected_hero.team:
			action = Action.RESURRECT

		feed_items.append(KillfeedItem(affected_hero, action, active_hero, assists))

	# Plausibility check
	plausible_feed_items = list(filter(lambda feed_item: feed_item.is_plausible(), feed_items))

	# Sort feed items from old to new
	plausible_feed_items.reverse()

	# Remove feed items already detected
	unique_feed_items = list(filter(lambda feed_item: feed_item not in last_feed_items, plausible_feed_items))
	last_feed_items.extend(unique_feed_items)
	for _ in range(len(last_feed_items) - 5):
		last_feed_items.pop(0)

	# Console output
	for feed_item in unique_feed_items:
		print('feed', feed_item)

	# Fire events
	for feed_item in unique_feed_items:
		if feed_item.action == Action.KILL:
			if feed_item.affected_hero.team == MY_TEAM:
				if feed_item.affected_hero.hero == Sub:
					c_killfeed.send('SubDeath')
				elif feed_item.affected_hero.hero == Dom:
					c_killfeed.send('DomDeath')
				else:
					c_killfeed.send('TeamDeath')
			else:
				if feed_item.active_hero.hero == Sub:
					c_killfeed.send('Kill')
				elif Hero(Sub, MY_TEAM) in feed_item.assists:
					c_killfeed.send('Assist')

###########################################
# ####################################### #
###########################################	

def GenCords(self,screen_x=0,screen_y=0):	#Imported
	screen_x = self.master.winfo_screenwidth() if screen_x == 0 else screen_x
	screen_y = self.master.winfo_screenheight() if screen_y == 0 else screen_y
	StartXPos = int(screen_x * .75)
	EndXPos = int(screen_x * .25)
	EndYPos = int(screen_y * .25)
	KillFeedBorderPixels = [int(screen_x * .005859375),
							int(screen_x * .01367875),
							int(screen_x * .02734375)]
	return (StartXPos,0, EndXPos, EndYPos), KillFeedBorderPixels

def LogTime(file,Files,newtime):	#Debug
	if file == Files[0]:
		lasttime = time()
		print(lasttime-newtime)
		newtime = lasttime		
	return newtime

def RunTest():	#Debug
	import multiprocessing as mp
	from pyautogui import screenshot
	p_killfeed, c_killfeed = mp.Pipe()
	Cords, BorderPixels = GenCords('',1920,1080)
	Freeplay=False
	Sub = 'Mercy'
	Dom = 'Ana'
	KFPath = 'Resources\\Killfeed\\2560x1440\\Overwatch\\'
	if Freeplay == True:
		Files = glob(KFPath+'*.png')
	else:
		Files = [KFPath+Sub+'.png', KFPath+Dom+'.png']
	while True:
		sleep(5)
		im = screenshot()
		Main(im,Files,Sub,Dom,Cords,c_killfeed,KFPath,BorderPixels)
		if p_killfeed.poll() == True:
			print(p_killfeed.recv())

if __name__ == '__main__':
	RunTest()
	i=2560
	#KillFeedBorderPixels = [int(self.master.winfo_screenwidth()*.005859375),
							#int(self.master.winfo_screenwidth()*.01367875),
							#int(self.master.winfo_screenwidth()*.02734375)
							#]
	for i in KillFeedBorderPixels:
		print(i)
	for i in [1920,2560]:
		print(i,int(i*.005859375))
		print(i,int(i*.01367875))
		print(i,int(i*.02734375))
		
	
	

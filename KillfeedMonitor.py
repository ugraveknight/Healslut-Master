from pyautogui import locateAll, center
from glob import glob
from itertools import cycle
from time import sleep, time
	
def TreatSub(info,name,ListOfCycles,c_killfeed):
	info_values = \
	{
		'SubDeath' : 0,
		'DomDeath' : 1,
		'TeamDeath': 2,
		'Assist'   : 3,
		'Kill'     : 4,
	}
	i = info_values.get(info, '')
	try:
		c_killfeed.send(next(ListOfCycles[i]))
	except StopIteration:
		pass

def TrackDeath(name,TeamColor,Sub,Dom,ListOfCycles,c_killfeed):
	print('Death:',TeamColor,name)
	TreatStr = 'DomDeath'  if name == Dom.replace('Resources\\Killfeed\\Overwatch\\','').replace('.png','') and TeamColor == 'Blue' else \
			   'SubDeath'  if name == Sub else \
			   'TeamDeath' if TeamColor == 'Blue' else 'Kill'
	print(TreatStr,TeamColor,name)
	TreatSub(TreatStr,name,ListOfCycles,c_killfeed) if TreatStr != '' else 0
	
def GenTeamColor(im, x, y):
	BorderRed,_,BorderBlue = im.getpixel((int(x), int(y)))
	return 'Red' if BorderRed > BorderBlue else 'Blue'

def Main(im,Files,Sub,Dom,Cords,ListOfCycles,c_killfeed,KFPath,BorderPixels,Debug=False):
	try:
		newtime = time() if Debug==True else 0
		for file in Files:
			newtime = LogTime(file,Files,newtime) if Debug==True else 0
			for userloc in locateAll(file, im, confidence=0.9, region=Cords):
				x, y = center(userloc)
				if not 'Assist' in file:
					TeamColor = GenTeamColor(im, x-BorderPixels[1], y)
					red, green, blue = im.getpixel((int(x)-BorderPixels[2], int(y)))
					if red > 250 and green > 245 and      blue > 240 or \
					   red > 250 and green < 20  and 30 < blue < 50:
						name = file.replace(KFPath,'').replace('.png','')
						if TeamColor == 'Blue':
							TrackDeath(name,TeamColor,Sub,Dom,ListOfCycles,c_killfeed)
				else:
					TeamColor = GenTeamColor(im, x-BorderPixels[0], y)	#BorderPixels = 15 on 2560
					name = file.replace(KFPath,'').replace('.png','')
					print(Sub,name)
					if Sub in name and TeamColor == 'Blue':
						TreatSub('Assist',name,ListOfCycles,c_killfeed)
	except KeyboardInterrupt:
		pass

###########################################
# ####################################### #
###########################################	

def GenCycles():
	GamesPath = 'Resources\\Healslut Games\\Overwatch '
	with open(GamesPath+'DeathSub.txt', 'r') as f:
		SubCycle = cycle(f.readlines())
	with open(GamesPath+'DeathDom.txt', 'r') as f:
		DomCycle = cycle(f.readlines())
	with open(GamesPath+'DeathTeam.txt', 'r') as f:
		TeamCycle = cycle(f.readlines())
	with open(GamesPath+'DeathAssist.txt', 'r') as f:
		AssistCycle = cycle(f.readlines())
	with open(GamesPath+'DeathKill.txt', 'r') as f:
		KillsCycle = cycle(f.readlines())
	return [SubCycle,DomCycle,TeamCycle,AssistCycle,KillsCycle]

def GenCords(self,screen_x=0,screen_y=0):	#Imported
	screen_x = self.master.winfo_screenwidth() if screen_x == 0 else screen_x
	screen_y = self.master.winfo_screenheight() if screen_y == 0 else screen_y
	StartXPos = int(screen_x*.75)
	EndXPos = int(screen_x*.25)
	EndYPos = int(screen_y*.25)
	KillFeedBorderPixels = [int(screen_x*.005859375),
							int(screen_x*.01367875),
							int(screen_x*.02734375)]
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
	ListOfCycles = GenCycles()
	#Cords, KillFeedBorderPixels = GenCords('',2560,1440)
	Cords, BorderPixels = GenCords('',1920,1080)
	Freeplay=False
	Sub = 'Mercy'
	Dom = 'Ana'
	#KFPath = 'Resources\\Killfeed\\Overwatch\\'
	KFPath = 'Resources\\Killfeed\\OW - 1920\\'
	Files = glob(KFPath+'*.png') if Freeplay == True else \
				[KFPath+Sub+'.png', KFPath+Dom+'.png']
	while True:
		sleep(5)
		im = screenshot()
		Main(im,Files,Sub,Dom,Cords,ListOfCycles,c_killfeed,KFPath,BorderPixels)
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
		

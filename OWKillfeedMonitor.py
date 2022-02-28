from pyautogui import locateAll, center
from glob import glob
from itertools import cycle
from time import sleep, time
from timeit import default_timer as timer

HSDEBUG = False
#HSDEBUG = True
	
def TreatSub(Mark,TreatStr,Log,c_killfeed):
	c_killfeed.send((Mark,TreatStr,Log))
	
def GenTeamColor(im, x, y):
	BorderRed,_,BorderBlue = im.getpixel((int(x), int(y)))
	if BorderRed > 250 and BorderBlue < 250:
		return 'Red'
	elif BorderRed < BorderBlue:
		return 'Blue'
	else:
		return 'Red'

def FindActivity(im,Files,Sub,Dom,Cords,c_killfeed,KFPath,BorderPixels):
	FoundDict = {}
	for file in Files:
		for userloc in locateAll(file, im, confidence=0.9, region=Cords):
			x, y = center(userloc)
			if not 'Assist' in file:
				TeamColor = GenTeamColor(im, x-BorderPixels[1], y)
				name = file.replace(KFPath,'').replace('.png','')
				FoundDict[TeamColor+'|'+name+'|'+str(x)] = (x,y,timer())
			else:
				TeamColor = GenTeamColor(im, x-BorderPixels[0], y)	#BorderPixels = 15 on 2560
				name = file.replace(KFPath,'').replace('.png','')
				TreatStr = 'Assist'
				if Sub in name and TeamColor == 'Blue':
					Log = '%s got an assist!'%(TeamColor+'|'+name)
					TreatSub(timer(),TreatStr,Log,c_killfeed)
	return FoundDict
	
def Main(im,Files,Sub,Dom,Cords,c_killfeed,KFPath,BorderPixels):
	try:
		FoundDict = FindActivity(im,Files,Sub,Dom,Cords,c_killfeed,KFPath,BorderPixels)
		
		Output = []
		for Tup,xy in FoundDict.items():
			TeamColor, name, _ = Tup.split('|')
			Tup = Tup.replace('|'+_,'')
			x,y,Mark = xy
			for nTup,nxy in FoundDict.items():
				nTeamColor, nname, _ = nTup.split('|')
				nTup = nTup.replace('|'+_,'')
				if TeamColor != nTeamColor:
					nx,ny,_ = nxy
					
					if y-2 < ny < y+2 and x < nx:
						if TeamColor == 'Blue':
							if name == Sub:
								Log = '%s killed %s'%(Tup,nTup)
								TreatStr = 'Kill'
							else:
								Log = '%s, not you, killed %s'%(Tup,nTup)
								TreatStr = 'TeamKill'
						
						else:
							if nname == Sub:
								Log = 'You were killed by %s'%Tup
								TreatStr = 'SubDeath'
							elif nname == Dom:
								Log = 'Your Dom, Blue|%s was killed by %s'%(Dom,Tup)
								TreatStr = 'DomDeath'
							else:
								Log = 'Your Teammate, Blue|%s was killed by %s'%(nname,Tup)
								TreatStr = 'TeamDeath'
						Output.append((Mark,TreatStr,Log))
				elif Tup != nTup and TeamColor == 'Blue':
					if   name  == 'Mercy':
						Log = '%s Ressurected %s'%(Tup,nTup)
						TreatStr = 'Ressurect'
						Output.append((Mark,TreatStr,Log))
					elif nname == 'Mercy':
						Log = '%s Ressurected %s'%(nTup,Tup)
						TreatStr = 'Ressurect'
						Output.append((Mark,TreatStr,Log))
			
				# look this code here is designed to capture player suicide, but it
				#  sometimes catches the killfeed dropping out and throws false positives
				#  for the health of the game and for my own mental health, I'm only going
				#  to act on logs that we can prove happened such as:
				#		Red|Tracer kills Blue|Mercy
			if len(FoundDict) == 1 and False:
				# We go in here and double check this twice.
				sleep(.2)
				if len(FindActivity(im,Files,Sub,Dom,Cords,c_killfeed,KFPath,BorderPixels)) == 1:
					sleep(.2)
					if len(FindActivity(im,Files,Sub,Dom,Cords,c_killfeed,KFPath,BorderPixels)) == 1:
					
						Log = '%s commited suicide'%Tup
						if TeamColor == 'Blue':
							if name == Sub:
								TreatStr = 'SubDeath'
							else:
								TreatStr = 'TeamDeath'
							Output.append((Mark,TreatStr,Log))
					else:
						print('That was a close call, potentially another false positive')
				else:
					print('That was a false positive')
			
		for Mark,TreatStr,Log in Output:
			TreatSub(Mark,TreatStr,Log,c_killfeed)
	except KeyboardInterrupt:
		pass

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
	if screen_x == 3440:
		KillFeedBorderPixels = [int(screen_x * .005859375),
							int(35),
							int(70)]
	
	#width=800
	#height=800
	#relx=.75, rely=.25
	return (StartXPos,0, EndXPos, EndYPos), KillFeedBorderPixels

def LogTime(file,Files,newtime):	#Debug
	if file == Files[0]:
		lasttime = time()
		#print(lasttime-newtime)
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
		
	
	

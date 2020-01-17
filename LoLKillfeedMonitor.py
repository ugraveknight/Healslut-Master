from pyautogui import locateAll, center,locateCenterOnScreen
from glob import glob
from itertools import cycle
from time import sleep, time
from multiprocessing import Pipe	

def TreatSub(info,name,c_killfeed):
	c_killfeed.send(info)

def SubDeath(file,c_killfeed):
	x, y = None, None
	try:
		x, y = locateCenterOnScreen(file+'SubDeath.png', confidence=0.8)
	except TypeError:
		pass
	if x:
		TreatSub('SubDeath','Sub',c_killfeed)

def RunTest():	#Debug
	c_killfeed, p_killfeed = Pipe()
	newtime = time() if Debug==True else 0
	while True:
		newtime = LogTime(newtime) if Debug==True else 0
		SubDeath('Resources/Killfeed/2560x1440/LOL/SubDeath.png',c_killfeed)
		sleep(1)
		
def LogTime(newtime):	#Debug
	lasttime = time()
	print(lasttime-newtime)
	newtime = lasttime		
	return newtime
	
Debug = False
if __name__ == '__main__':
	#Debug = True
	RunTest()

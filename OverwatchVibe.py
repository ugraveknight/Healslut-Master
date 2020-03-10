from pyautogui import screenshot,locateOnScreen
from time import sleep
from ctypes import windll
	
def getcolors(im,x,y):
	red, blue, green = im.getpixel((int(x), int(y)))
	mark = 10 if 37  < red < 165 and 223 < blue        and 248 < green \
			  or 62  < red < 122 and 138 < blue <  234 and 246 < red \
			  or 248 < red       and 250 < blue        and 250 < green \
			  else 0
	yield mark
	
def mean(numbers): return float(sum(numbers)) / max(len(numbers), 1)
def cleanmarks(markslist,marks):
	marks = int(mean(marks))*10
	marks = 100	if marks > 100 else marks
	markslist.append(marks)
	markslist.pop(0)
	base_speed = 100 if any(marks == 100 for marks in markslist) else int(mean(markslist))
	return markslist, base_speed

def go(positions, markslist, im):
	marks=[]
	for x,y in positions.items():
		for mark in getcolors(im,x,y):
			marks.append(mark)
	markslist, base_speed = cleanmarks(markslist,marks)
	return markslist, base_speed

###########################################
# ####################################### #
###########################################	

def GenPositions():		#Imported
	user32 = windll.user32
	screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	userx, usery = screensize
	oripos = \
	[
		'400,1320',
		'415,1320',
		'445,1320',
		'475,1315',	
		'510,1315',
		'540,1310',
		'570,1310',
		'600,1305',
		'610,1305',
		'630,1305'
	]
	positions = {}
	for value in oripos:	
		x,sep,y=value.partition(',')
		x = round((userx/2560) * int(x))
		y = round((usery/1440) * int(y))
		positions.update({x:y})
	return positions
	
def RunTest():		#Debug
	markslist = [0,0,0,0]
	positions = GenPositions()
	while True:
		im = screenshot()
		markslist, base_speed = go(positions,markslist,im)
		print(base_speed, markslist)
		sleep(1)
		
def CheckLoadingScreen(p_CharSelect):
	try:
		if locateOnScreen('Resources/Loading Screen Tip.png', confidence=0.9):
			p_CharSelect.send(True)
			return True
	except TypeError:
		pass
		
if __name__ == '__main__':	
	#RunTest()
	from multiprocessing import Pipe
	p_CharSelect,c_CharSelect = Pipe()
	while True:
		CheckLoadingScreen(p_CharSelect)
		sleep(1)

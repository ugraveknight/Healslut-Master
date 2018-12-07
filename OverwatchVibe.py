from pyautogui import screenshot
from time import sleep

def getcolors(im,location1x,location1y):
	red, blue, green = im.getpixel((int(location1x), int(location1y)))
	if 37 < red < 165 and 223 < blue <= 255 and 248 < green <= 255:
		mark = 10
	elif 62 < red < 122 and 138 < blue < 234 and 246 < red <= 255:
		mark = 10
	elif 248 < red and 250 < blue and 250 < green:
		mark = 10
	else:
		mark = 0
	yield mark

def cleanmarks(markslist,marks):
	marks = int(mean(marks))*10
	if marks > 100:
		marks = 100	
	markslist.append(marks)
	markslist.pop(0)
	if any(marks == 100 for marks in markslist):
		level=100
	else:
		level=int(mean(markslist))
	return markslist, level

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)	

def go(positions, markslist):
	marks=[]
	im = screenshot()
	time.sleep(1)
	for x,y in positions.items():
		for mark in getcolors(im,x,y):
			marks.append(mark)
	markslist, base_speed = cleanmarks(markslist,marks)
	return markslist, base_speed
	
	
	
###########################################
# ####################################### #
###########################################	
	
	
def genpositions():
	user32 = ctypes.windll.user32
	screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	userx, usery = screensize
	oripos =	[
		'400,1320',
		'415,1320',
		'445,1320',
		'475,1315',	
		'510,1315',
		'540,1310',
		'570,1310',
		'600,1305',
		'610,1305',
		'630,1305']	
	positions = {}
	for value in oripos:	
		x,sep,y=value.partition(',')
		x = round((userx/2560) * int(x))
		y = round((usery/1440) * int(y))
		positions.update({x:y})
	return positions	
	
if __name__ == '__main__':
	import ctypes
	markslist = [0,0,0,0]
	positions = genpositions()
	while True:
		markslist, base_speed = go(positions,markslist)
		print(base_speed, markslist)
		time.sleep(1)

from win32gui import FindWindow, SetWindowLong
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE
from traceback import format_exc
from random import randint, choice

TRANS_CLR = '#f7e9f1'	#Haha, Pride!
TRANS_CLR_ALT = '#000000'
FONT0 = ("Impact", 44)
FONT1 = ("Impact", 28)
FONT2 = ("Impact", 20)
FONT3 = ("Impact", 15)

def set_written_line(humiliation, dom='Female', sub='Girl'):
	try:
		line=(choice(humiliation)).strip('\n')
		if line == '': 
			line='i love being a healslut'
		if '99' in line:
			gendervar = randint(1,2) if dom == 'None' else 0
			if dom == 'Male' or gendervar == 1:
				ReplaceList = ['masters','master','his','his','sir','cocks','cock']
			elif dom == 'Female' or gendervar == 2:
				ReplaceList = ['mistresses','mistress','hers','her','miss','pussies','pussy']
			BaseList = ['m99s','m99','s99s','s99','n99','p99s','p99']
			for i in range(0,len(BaseList)):
				line = line.replace(BaseList[i], ReplaceList[i])
		if '00' in line:
			if   sub == 'Sub' : ReplaceList = ['sub','parts','part']
			elif sub == 'Boy' : ReplaceList = ['boy','balls','dick']
			elif sub == 'Girl': ReplaceList = ['girl','tits','cunt']
			BaseList = ['m00','p00s','p00']
			for i in range(0,len(BaseList)):
				line = line.replace(BaseList[i], ReplaceList[i])
		return line	
	except Exception as e:
		handleError(format_exc(2), e, 'set_written_line', subj='')

def set_clickthrough(windowname="Healslut Hypnotherapy"):
	try:
		hwnd = FindWindow(None, windowname)
		windowStyles = WS_EX_LAYERED | WS_EX_TRANSPARENT
		SetWindowLong(hwnd, GWL_EXSTYLE, windowStyles)
	except Exception as e:
		handleError(format_exc(2), e, 'set_clickthrough', subj='')

def remove_clickthrough(windowname="Healslut Hypnotherapy"):
	try:
		hwnd = FindWindow(None, windowname)
		windowStyles = WS_EX_LAYERED
		SetWindowLong(hwnd, GWL_EXSTYLE, windowStyles)
	except Exception as e:
		handleError(format_exc(2), e, 'remove_clickthrough', subj='')

def handleError(tb, e, func, subj=''):
	def handlewriter(tb, e, func, subj):
		e=str(e)
		print(func+' Error '+e)
		file = 'Resources\\Errors\\'+func+'.txt'
		with open(file, 'a') as f:
			f.write(tb+'\n'+subj)
	try:
		handlewriter(tb, e, func, subj='')
	except Exception as e:
		handlewriter(tb, e, 'handleError', subj='')



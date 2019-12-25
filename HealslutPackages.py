from win32gui import FindWindow, SetWindowLong
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE

TRANS_CLR = '#f7e9f1'	#Haha, Pride!
TRANS_CLR_ALT = '#000000'
FONT0 = ("Impact", 44)
FONT1 = ("Impact", 28)
FONT2 = ("Impact", 20)
FONT3 = ("Impact", 15)

def set_clickthrough(windowname="Healslut Hypnotherapy"):
	try:
		hwnd = FindWindow(None, windowname)
		windowStyles = WS_EX_LAYERED | WS_EX_TRANSPARENT
		SetWindowLong(hwnd, GWL_EXSTYLE, windowStyles)
	except Exception as e:
		handleError(format_exc(2), e, 'set_clickthrough', subj='')

def remove_clickthrough():
	try:
		hwnd = FindWindow(None, "Healslut Hypnotherapy")
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



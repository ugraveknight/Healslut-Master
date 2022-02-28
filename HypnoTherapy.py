from tkinter import *
from multiprocessing import Pipe, Process
from threading import Thread
from PIL import Image, ImageTk
from itertools import cycle
from glob import glob
from random import choice, randint, shuffle
from time import time, sleep
from traceback import format_exc
from sys import exit
from os import path
from playsound import playsound
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGBA
from mutagen.mp3 import MP3
from traceback import format_exc
from win32gui import FindWindow, SetWindowLong
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE
import sys

import HealslutPackages as HP
from TextLibs import TextLibs
from Banner import create_banner
import HomeworkLibs
import HypnoBG


HSDEBUG = False
#HSDEBUG = True


class Hypnotherapy(Frame):
	def __init__(self, master, image_files, delay, opacity, game, 
				homework, wordcount, hypno, dom, sub, pinup, banwords,
				tranbanr, s_rulename, fontsize, display_rules, loopingAudio,
				AudioType, gifset, FemSex, ColorList, c_vid, c_txt, c_pinup, 
				c_homework, c_wordknt, c_CharSelect, c_hypno, p_bg, c_bg,
				p_homework, *pargs):
		Frame.__init__(self, master, *pargs)
		try:
			if HSDEBUG: print('Prepping Hypnotherapy Variables')
			self.master = master
			self.screenwidth = self.master.winfo_screenwidth()
			self.screenheight = self.master.winfo_screenheight()
			self.master.overrideredirect(1)
			self.image_files = image_files
			self.delay = delay
			self.opacity = opacity
			self.game = game
			self.homework = homework
			self.wordcountOriginal = wordcount
			self.wordcount = wordcount
			self.pinupvar = 0
			self.banner_var = 4
			self.freshtext = False
			self.endtime = time()
			self.user_line = ''
			self.DoingHW = False
			self.processing_image = False
			self.ready_for_images = False
			self.playingvideo = False
			self.vs = None
			self.c_wordknt = c_wordknt
			self.c_CharSelect = c_CharSelect
			self.c_hypno = c_hypno
			self.enable_hypno = hypno
			self.prefer_dom = dom
			self.prefer_sub = sub
			self.enable_pinup = pinup
			self.banwords = banwords
			self.tranbanr = tranbanr
			self.c_vid = c_vid
			self.c_txt = c_txt
			self.c_pinup = c_pinup
			self.c_homework = c_homework
			self.p_bg = p_bg
			self.c_bg = c_bg
			self.p_homework = p_homework
			self.s_rulename = s_rulename
			self.fontsize = fontsize
			self.display_rules = display_rules
			self.loopingAudio = loopingAudio
			self.AudioType = AudioType
			self.gifset = gifset
			self.FemSex = FemSex
			self.ColorList = ColorList
			self.output = ''
			self.p_opacity, self.c_opacity = Pipe()
			self.p_pinupdims, self.c_pinupdims = Pipe()
			self.p_pininfo, self.c_pininfo = Pipe()
			self.p_hwlog, self.c_hwlog = Pipe()
			self.TextWidth = self.screenwidth - 300
			self.Curve = 0
			
			self.NxtHWTime=time()+5
			self.HWRemain = 0
			self.hwlog = 0
			
			
			self.x_cen = int(self.screenwidth  * .5)
			self.x_lef = int(self.screenwidth  * .4)
			self.x_rgt = int(self.screenwidth  * .6)
			self.y_cen = int(self.screenheight * .5)
			self.y_upr = int(self.screenheight * .33)
			self.y_low = int(self.screenheight * .66)
			
			if HSDEBUG: print('Configuring Hypnotherapy Overlay')
			self.MakeBackground()
			
			if self.display_rules != 0:
				self.BuildRules()
				
			if HSDEBUG: print('Prepping Banner')
			self.PrepBanner()
			
			if HSDEBUG: print('Initializing Pinup Object')
			self.bg.fg = self.bg.create_image(self.x_cen, self.y_cen, image='')
			
			if HSDEBUG: print('Building Rules')
			self.BuildRules()
			
			if HSDEBUG: print('Prepping Background Loop')
			self.LaunchBG()
			
			if HSDEBUG: print('Prepping Homework')
			self.LaunchWFM()
			
			if HSDEBUG: print('Initializing TextLibs')
			self.TextLibWrapper()
			
			if HSDEBUG: print('Prepping Slides Loop')
			self.slides()
			
			if HSDEBUG: print('Prepping Audio Loop')
			self.setaudioloop()
			
			self.master.after(1000,SetClickthrough)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'hypno.init', subj='')
		
	def TextLibWrapper(self):
		self.TL = TextLibs(self.bg,self.banwords,self.ColorList,self.DoingHW,
				self.wordcount,self.screenwidth,self.screenheight,
				self.x_cen,self.x_lef,self.x_rgt,self.y_cen,self.y_upr,self.y_low)
			
	def MakeBackground(self):
		self.bg = Canvas(self,width=self.screenwidth,height=self.screenheight, highlightthickness=0)
		self.bg.config(bg=HP.TRANS_CLR())
		self.bg.pack(fill=BOTH, expand=YES)
		_,_,x,y = HP.CenterWindow(self.master, 50, 275)
		self.HWTxt = self.bg.create_text(x+50, y+290,text='',fill='yellow',font=('impact bold', 12),anchor=E)
		
		self.master.wm_attributes("-transparentcolor", HP.TRANS_CLR())
		if self.game == 'OW':
			self.bg.ChatPort = Canvas(self.bg,bg=HP.TRANS_CLR(),width=650,height=450,highlightthickness=0)
			self.bg.ChatPort.place(relx=0, rely=1, anchor=SW)
			self.bg.KillfeedPort = Canvas(self.bg,bg=HP.TRANS_CLR(),width=1000,height=800,highlightthickness=0)
			self.bg.KillfeedPort.place(relx=.75, rely=.25, anchor=SW)
		if self.game == 'LoL':
			KfWidth = 1100
			KfHeight = 150
			self.bg.KillfeedPort = Canvas(self.bg,bg=HP.TRANS_CLR(),width=KfWidth,height=KfHeight,highlightthickness=0)
			self.bg.KillfeedPort.place(x=(self.screenwidth/2)-(KfWidth/2), y=self.screenheight-KfHeight)
	
	def BuildRules(self):
		Filepath = path.abspath('Resources\\Healslut Games\\'+self.s_rulename+'\\Rules.txt')
		with open(Filepath, 'r') as f:
			lines = f.readlines()
		for line in lines:
			self.output = self.output+line
	
	def PrepBanner(self):
		def RunTransBanner():
			try:
				self.banner_var+=1
				if self.banner_var >= 4:
					self.BannerLine = HP.SetWrittenLine(self.Humiliation, self.prefer_dom, self.prefer_sub)
					self.banner_var = 0
					self.linecolor = choice(self.ColorList)
				self.bg.delete(self.tmp_banner)
				self.tmp_banner = self.bg.create_text(self.screenwidth/2, self.screenheight/1.3, 
													text=self.BannerLine.upper(),width=self.TextWidth,anchor=CENTER,
													font=(HP.GlobalFont(), 44), fill=self.linecolor)
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'RunTransBanner', subj='')
			self.master.after(self.delay, RunTransBanner)
		# ################################################# #
		try:
			Filepath = path.abspath('Resources\\Text\\Humiliation.txt')
			with open(Filepath, 'r') as f:
				self.Humiliation = f.read().split('\n')
			if self.FemSex != 'None':
				Filepath = path.abspath('Resources\\Text\\Feminization.txt')
				with open(Filepath, 'r') as f:
					self.Humiliation += f.read().split('\n')
			self.c_images, self.p_images = Pipe()
			
			if HSDEBUG: print('Starting Banner Layer...')
			dom = self.prefer_dom
			sub = self.prefer_sub
			delay = self.delay
			Humiliation = self.Humiliation
			banwords = self.banwords
			ColorList = self.ColorList
			wordcount = self.wordcount
			tranbanr = self.tranbanr
			homework = self.homework
			output = self.output
			display_rules = self.display_rules
			fontsize = self.fontsize
			c_images = self.c_images
			c_txt = self.c_txt
			c_wordknt = self.c_wordknt
			c_CharSelect = self.c_CharSelect
			c_hypno = self.c_hypno
			Thread(target=create_banner, args=(delay,dom,sub,Humiliation,
							ColorList,banwords,wordcount,tranbanr,homework,
							output,display_rules,fontsize,c_images,c_txt,
							c_wordknt,c_CharSelect,c_hypno)).start()
			if self.tranbanr == 1 and self.homework == 'Banner':
				self.tmp_banner = self.bg.create_text(0, 0, text='')
				RunTransBanner()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'PrepBanner', subj='')
	
	def BuildRules(self):
		if self.display_rules == 1:
			self.bg.create_text(0,self.y_cen,text=self.output,fill='hot pink',
					font=("Impact",self.fontsize),justify=LEFT,anchor=W)
	
	# # # # # # # # # #
	#      Audio      #
	# # # # # # # # # #		
	def setaudioloop(self):
		if not self.loopingAudio == 0:
			Filepath = path.abspath('Resources/Tracks')
			if self.AudioType == 'Spoken':
				self.audiolist = glob(Filepath+'/Spoken/*.mp3')
			elif self.AudioType == 'Music':
				self.audiolist = glob(Filepath+'/Music/*.mp3')
			else:
				self.audiolist = glob(Filepath+'/Spoken/*.mp3')+glob(Filepath+'/Music/*.mp3')
			self.audiocycle = cycle(self.audiolist)
			self.after(25, self.runaudioloop)
			
	def runaudioloop(self):
		try:
			if self.loopingAudio == 1:
				currenttrack = next(self.audiocycle)
			if self.loopingAudio == 2:
				currenttrack = choice(self.audiolist)
			playsound(currenttrack, False)
			audio = MP3(currenttrack)
			audiolength = int(audio.info.length)*1000
			self.after(audiolength, self.runaudioloop)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'runaudioloop', subj='')
			
	# # # # # # # # # #
	#      Pinup      #
	# # # # # # # # # #
	def HandleImages(self):
		#while True:
		if 1:
			try:
				try:
					self.foregrounds = cycle([ImageTk.PhotoImage(file=self.image_files[0])])
				except (OSError, TclError):
					pass
				shuffle(self.image_files)
			except RuntimeError:
				self.quit()
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'loadnewpic', subj='')

		try:
			self.img_object = next(self.foregrounds)
			self.bg.itemconfig(self.bg.fg, image=self.img_object)
			self.bg.update()
			self.p_pinupdims.send((self.img_object.width(),self.img_object.height()))
		except StopIteration:
			HP.HandleError(format_exc(2), e, 'slides', subj='Hey, you probably have the wrong format for your $pinup setting.')
			self.p_pinupdims.send((0,0))


	# # # # # # # # # #
	#     MainLoop    #
	# # # # # # # # # #	
	def slides(self):
		try:
			Mark = time()
			if HSDEBUG: print('  Slides -')
			
				# Handle our homework
			while self.p_homework.poll() == True:
				self.DoingHW,self.HWRemain,text = self.p_homework.recv()
				self.bg.itemconfig(self.HWTxt,text=text)
			if self.homework != 'Never':
				while self.p_homework.poll() == True:
					self.Curve += self.p_homework.recv()
					print('I am grading on a curve, Sweetie...',self.Curve)
				while self.p_hwlog.poll() == True:
					self.HWRemain = self.p_hwlog.recv()
				self.NxtHWTime,self.HWRemain = HomeworkLibs.GenHomework(self.homework,self.NxtHWTime,self.HWRemain,self.Curve)
				if not self.c_homework.poll():
					self.p_homework.send(self.HWRemain)
			if HSDEBUG: print('  Slides - Homework complete')
			
				# Check to see if there is new Pinup folder selected
			while self.c_pinup.poll() == True:
				NewPinups = GenImageFiles(self.c_pinup.recv(),self.enable_pinup)
				if len(NewPinups) > 0:
					self.image_files = NewPinups
			if HSDEBUG: print('  Slides - Confirmed active Pinups')
				
				# Do Main Pinup work
			if self.enable_pinup == 1 and not self.playingvideo == True:
				if self.DoingHW == False:
					self.HandleImages()
				else:
					self.bg.itemconfig(self.bg.fg, image='')
					self.p_pinupdims.send((0,0))
			if HSDEBUG: print('  Slides - Pinup refreshed')
			
				# Show Video if any
			if self.c_vid.poll() == True or self.playingvideo == True:
				self.TL.ClearScreen()
				while self.c_vid.poll() == True:
					self.video_filename = self.c_vid.recv()
					self.videostarttime = time()
				self.SetVideo()
				self.AfterTarget = 25
				self.StartTime = time()
			
				# Handle On Screen Text
			else:
				if self.banwords == 1:
					self.TL.UpdateText(self.wordcount,True)
					self.after(int(self.delay/2), self.TL.UpdateText(self.wordcount))
				self.AfterTarget = self.delay
				self.StartTime = time()
			if HSDEBUG: print('  Slides - Text updated')
				
				# Lets change up the word count!
			if self.c_wordknt.poll() == True:
				while self.c_wordknt.poll():
					newcount = self.c_wordknt.recv()
				if self.banwords == 1 and self.wordcount != newcount:
					self.TL.ClearScreen()
					self.wordcount = newcount
			if HSDEBUG: print('  Slides - Wordcount updated')
					
				# Get that cool transparancy effect
			if self.DoingHW == False:
				self.BreatheTransp()
			if HSDEBUG: print('  Slides - Transparancy loop')
			
				# Better than after since we can still check on things
			self.LetsWait()
			
			print('Slides Loop:',int((time()-Mark)*1000))
			
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'slides', subj='')
			
	def LetsWait(self):
		if self.c_hypno.poll() == True:
			if HSDEBUG: print('Hypnotherapy Exiting...\n')
			exit()
		if (time() - self.StartTime)*1000 >= self.AfterTarget:
			self.slides()
		else:
			self.after(25, self.LetsWait)
	
	# # # # # # # # # #
	#   Play Video    #
	# # # # # # # # # #	
	def SetVideo(self):
		try:
			if self.playingvideo == False:
				self.playingvideo = True
				if not self.c_bg.poll():
					self.p_bg.send(True)
			
			if self.vs == None:
				self.vs = VideoCapture(self.video_filename) # capture video frames, 0 is your default video camera
				self.current_image = None	# current image from the camera
			
			ok, frame = self.vs.read()		# read frame from video stream
			if ok:
				cv2image = cvtColor(frame, COLOR_BGR2RGBA)		# convert colors from BGR to RGBA
				self.current_image = Image.fromarray(cv2image)  # convert image for PIL
				self.imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter 
				self.bg.itemconfig(self.bg.fg, image=self.imgtk)
				del frame	# memory leak prevention
				del cv2image
				del ok
			
			else:
				self.TL.ClearScreen()
				self.p_bg.send(False)
				try:
					del self.current_image	# memory leak prevention
					del self.imgtk
				except AttributeError as e:
					print('Video not found. Is it spelled and formatted correctly, and in the right place? This is where I think it is')
					print(path.abspath(self.video_filename))
				self.vs.release()
				self.vs = None
				self.playingvideo = False
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'SetVideo', subj='')
			
	# # # # # # # # # #
	# Background Gif  #	
	# # # # # # # # # #
	def BreatheTransp(self):
		try:
			if not self.opacity == 4:
				if self.playingvideo == True:
					self.tmp_opacity = self.opacity+1
				else:
					self.tmp_opacity = self.opacity
				now = int(str(time() % 60).split('.')[0])
				if   0 <= now <= 15: now = (now-30) * -1
				elif 15 < now <= 30: pass
				elif 30 < now <= 45: now = (now-60) * -1
				elif 45 < now <= 60: now = now-30
					
				if self.tmp_opacity == 0:
					opacity = (now*.01)*1-.15
				else:
					opacity = (now*.01)*self.tmp_opacity
			else:
				opacity = 1 # because Opacity level 4 is fully opaque
			self.master.attributes('-alpha', opacity)
			if HSDEBUG: print('Opacity Set')
			if self.enable_hypno >= 1:	
				self.p_opacity.send(opacity)
				if HSDEBUG: print('Opacity Sent')
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'BreatheTransp', subj='')
			
	def LaunchBG(self):
		try:	
			HypnoBG.StartHypnoBG(self.game,self.enable_hypno,self.gifset,
					self.c_hypno,self.p_bg,self.c_bg,self.c_opacity,self.c_pinupdims)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'LaunchBG', subj='')
			
	def LaunchWFM(self):
		try:	
			HomeworkLibs.StartHomeworkPane(self.DoingHW,self.c_homework,self.p_pinupdims,
							self.homework,self.enable_hypno,self.game,self.Humiliation,
							self.prefer_dom,self.prefer_sub,self.c_hypno,self.c_hwlog)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'LaunchWFM', subj='')
	# # # # # # # # # #
	# # # # # # # # # #
	

class StartHypnoProcess(Process):
	def __init__(self, delay,opacity,game,
						homework,wordcount,hypno,dom,sub,pinup,banwords,tranbanr,
						globfile,s_rulename,fontsize,display_rules,loopingAudio,AudioType,
						gifset,FemSex,ColorList,c_vid,c_txt,c_pinup,c_homework,c_wordknt,c_CharSelect,
						c_hypno,p_bg,c_bg,p_homework):
		try:
			self.delay = delay
			self.opacity = opacity
			self.game = game
			self.homework = homework
			self.wordcount = wordcount
			self.OverlayActive = hypno
			self.dom = dom
			self.sub = sub
			self.pinup = pinup
			self.banwords = banwords
			self.tranbanr = tranbanr
			self.globfile = globfile
			self.s_rulename = s_rulename
			self.fontsize = fontsize
			self.display_rules = display_rules
			self.loopingAudio = loopingAudio
			self.AudioType = AudioType
			self.gifset = gifset
			self.FemSex = FemSex
			self.ColorList = ColorList
			self.c_vid = c_vid
			self.c_txt = c_txt
			self.c_pinup = c_pinup
			self.c_homework = c_homework
			self.c_wordknt = c_wordknt
			self.c_CharSelect = c_CharSelect
			self.c_hypno = c_hypno
			self.p_bg = p_bg
			self.c_bg = c_bg
			self.p_homework = p_homework
			
			Process.__init__(self)
			self.start()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'StartHypnoProcess.init', subj='')
			
	def run(self):
		try:
			if HSDEBUG: print('Launching HypnoTherapy Layer...')
			launch(self.delay,self.opacity,self.game,
				self.homework,self.wordcount,self.OverlayActive,self.dom,self.sub,self.pinup,self.banwords,self.tranbanr,
				self.globfile,self.s_rulename,self.fontsize,self.display_rules,self.loopingAudio,self.AudioType,self.gifset,
				self.FemSex,self.ColorList,self.c_vid,self.c_txt,self.c_pinup,self.c_homework,self.c_wordknt,self.c_CharSelect,
				self.c_hypno,self.p_bg,self.c_bg,self.p_homework)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'StartHypnoProcess.run', subj='')


#####################################
# ####################################
#####################################
# ####################################

def QueueForegrounds(p_pininfo,image_files):
	try:
		try:
			cyc = cycle([Image.open(img) for img in image_files[0:1]])
			p_pininfo.send(cyc)
		except TclError:
			del image_files[0:1]
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'QueueForegrounds', subj='')

def GenImageFiles(globfile,pinup):
	if HSDEBUG: print('Generating Pinup Files...')
	if pinup == 1:
		if globfile == 'All':
			Filepath = path.abspath('Resources/Images')
			image_files = glob(Filepath+'/*/*.png', recursive=True)
			print(len(glob(Filepath+'/*/*.png')))
			
			print('All images found:', len(image_files))
		else:
			globfile = path.abspath('Resources\\Images\\'+globfile+'\\')
			image_files = glob(globfile+'/*.png', recursive=True)
			print(globfile,'found', len(image_files), 'images...')
	else:
		image_files = ''
	shuffle(image_files)
	return image_files

def SetClickthrough(windowname="Healslut Hypnotherapy"): #I want this to be in HP, but doesnt work when imported
	try:
		hwnd = FindWindow(None, windowname)
		if HSDEBUG: print('Cloaking Hypnotherapy...', windowname, hwnd)
		windowStyles = WS_EX_LAYERED | WS_EX_TRANSPARENT
		SetWindowLong(hwnd, GWL_EXSTYLE, windowStyles)
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'Hypnotherapy_SetClickthrough', subj='')	
		
def launch(delay,opacity,game,homework,wordcount,hypno,
				dom,sub,pinup,banwords,tranbanr,globfile,
				s_rulename,fontsize,display_rules,loopingAudio,
				AudioType,gifset,FemSex,ColorList,c_vid,c_txt,
				c_pinup,c_homework,c_wordknt,c_CharSelect,c_hypno,
				p_bg,c_bg,p_homework):
	try:
		root = Tk()
		width = root.winfo_screenwidth()
		height = root.winfo_screenheight()
		root.geometry('%dx%d' % (width, height))
		root.configure(background="#000000")
		root.attributes('-alpha', 0.3)
		root.title("Healslut Hypnotherapy")
		root.wm_attributes("-topmost", 1)
		
		image_files = GenImageFiles(globfile,pinup)
				
		if c_hypno.poll() == True:
			print('Exiting before we even started')
			exit()
		
		if HSDEBUG: print('Building Hypnotherapy Object...')
		e = Hypnotherapy(root, image_files, delay, opacity, game,  
					homework, wordcount, hypno, dom, sub, pinup, banwords, 
					tranbanr, s_rulename, fontsize, display_rules, loopingAudio, 
					AudioType,gifset, FemSex, ColorList, c_vid, c_txt, c_pinup,
					c_homework, c_wordknt, c_CharSelect, c_hypno, p_bg, c_bg,
					p_homework)
		e.pack(fill=BOTH, expand=YES)
		root.mainloop()
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'Hypnotherapy.launch', subj='')
	
if __name__ == '__main__':
	pass

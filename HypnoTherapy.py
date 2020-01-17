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

from Banner import create_banner
import HealslutPackages as HP

DEBUG = False

class Hypnotherapy(Frame):
	def __init__(self, master, image_files, delay, opacity, game, 
				homework, wordcount, hypno, dom, sub, pinup, banwords,
				tranbanr, s_rulename, fontsize, display_rules, loopingAudio,
				gifset, c_vid, c_txt, c_pinup, c_homework, c_hypno, *pargs):
		Frame.__init__(self, master, *pargs)
		try:
			
			if DEBUG: print('Prepping Hypnotherapy Variables')
			self.master = master
			self.screenwidth = self.master.winfo_screenwidth()
			self.screenheight = self.master.winfo_screenheight()
			self.image_files = image_files
			self.delay = delay
			self.opacity = opacity
			self.game = game
			self.homework = homework
			self.wordcount = wordcount
			self.HWRemain = 0
			self.pinupvar = 0
			self.banner_var = 4		
			self.InsaneWordsA = 1
			self.InsaneWordsB = 1
			self.freshtext = False
			self.endtime = time()
			self.user_line = ''
			self.DoingHW = False
			self.processing_image = False
			self.ready_for_images = False
			self.playingvideo = False
			self.vs = None
			self.NxtHWTime=time()+5
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
			self.s_rulename = s_rulename
			self.fontsize = fontsize
			self.display_rules = display_rules
			self.loopingAudio = loopingAudio
			self.gifset = gifset
			self.output = ''
			self.p_PinupAssassin, self.c_PinupAssassin = Pipe()
			
			if DEBUG: print('Configuring Hypnotherapy Overlay')
			self.master.overrideredirect(1)
			self.make_background()
			self.formatgif()
			self.build_ports()
			if self.display_rules != 0:
				self.build_rules()
			self.PrepBanner()
			self.pinup()
			self.setup_text()
			
			if DEBUG: print('Prepping Background Loop')
			self.updategif()
			
			if DEBUG: print('Prepping Slides Loop')
			self.slides()
			
			if DEBUG: print('Prepping Audio Loop')
			self.setaudioloop()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'hypno.init', subj='')
		
	def make_background(self):
		self.x_cen = int(self.screenwidth*.5)
		self.x_lef = int(self.screenwidth*.4)
		self.x_rgt = int(self.screenwidth*.6)
		self.y_cen = int(self.screenheight*.5)
		self.y_upr = int(self.screenheight*.33)
		self.y_low = int(self.screenheight*.66)
		
		self.bg = Canvas(self,width=self.screenwidth,height=self.screenheight, highlightthickness=0)
		if self.enable_hypno >= 1:
			self.bg.gif_create = self.bg.create_image(self.screenwidth/2,self.screenheight/2,image='')
		else:
			self.bg.config(bg=HP.TRANS_CLR())
		self.bg.pack(fill=BOTH, expand=YES)
		
	def formatgif(self):
		imagelist = glob('Resources\\Hypno Gif\\'+self.gifset+'\\*.gif', recursive=True)		
		self.gifcycle = [(PhotoImage(file=image)) for image in imagelist]
		self.gifcycle = cycle(self.gifcycle)
		
	def build_ports(self):
		self.master.wm_attributes("-transparentcolor", HP.TRANS_CLR())
		if self.game == 'OW':
			self.bg.ChatPort = Canvas(self.bg,bg=HP.TRANS_CLR(),width=650,height=200,highlightthickness=0)
			self.bg.ChatPort.place(relx=0, rely=1, anchor=SW)
			self.bg.KillfeedPort = Canvas(self.bg,bg=HP.TRANS_CLR(),width=800,height=800,highlightthickness=0)
			self.bg.KillfeedPort.place(relx=.75, rely=.25, anchor=SW)
		if self.game == 'LoL':
			KfWidth = 1100
			KfHeight = 150
			self.bg.KillfeedPort = Canvas(self.bg,bg=HP.TRANS_CLR(),width=KfWidth,height=KfHeight,highlightthickness=0)
			self.bg.KillfeedPort.place(x=(self.screenwidth/2)-(KfWidth/2), y=self.screenheight-KfHeight)
		self.bg.right_port = Canvas(self.bg,bg=HP.TRANS_CLR(),width=50,height=270,highlightthickness=0)
		self.bg.right_port.place(relx=1, rely=.5, anchor=E)	

	def build_rules(self):
		with open('Resources\\Healslut Games\\'+self.s_rulename+'\\Rules.txt', 'r') as f:
			lines = f.readlines()
			for line in lines:
				self.output = self.output+line
	
	def setup_text(self):
		with open('Resources\\Text\\Healslut Adjectives.txt', 'r') as a:
			self.alines=a.readlines()
		with open('Resources\\Text\\Healslut Subjects.txt', 'r') as s:
			self.slines=s.readlines()
		
		self.TopTextA = self.bg.create_text(0, 0, text='')
		self.TopTextB = self.bg.create_text(0, 0, text='')
		self.TopTextC = self.bg.create_text(0, 0, text='')
		self.BotTextA = self.bg.create_text(0, 0, text='')
		self.BotTextB = self.bg.create_text(0, 0, text='')
		self.BotTextC = self.bg.create_text(0, 0, text='')
		self.LefTextA = self.bg.create_text(0, 0, text='')
		self.LefTextB = self.bg.create_text(0, 0, text='')
		self.LefTextC = self.bg.create_text(0, 0, text='')
		self.RgtTextA = self.bg.create_text(0, 0, text='')
		self.RgtTextB = self.bg.create_text(0, 0, text='')
		self.RgtTextC = self.bg.create_text(0, 0, text='')
		if self.wordcount > 5 and self.banwords == 1:
			self.TAa = self.bg.create_text(0, 0, text='')
			self.TBa = self.bg.create_text(0, 0, text='')
			self.TCa = self.bg.create_text(0, 0, text='')
			self.TDa = self.bg.create_text(0, 0, text='')
			self.TEa = self.bg.create_text(0, 0, text='')
			self.TFa = self.bg.create_text(0, 0, text='')
			self.TGa = self.bg.create_text(0, 0, text='')
			self.THa = self.bg.create_text(0, 0, text='')
			self.TIa = self.bg.create_text(0, 0, text='')
			self.TJa = self.bg.create_text(0, 0, text='')
			self.TKa = self.bg.create_text(0, 0, text='')
			self.TLa = self.bg.create_text(0, 0, text='')
			self.TMa = self.bg.create_text(0, 0, text='')
			self.TNa = self.bg.create_text(0, 0, text='')
			self.TOa = self.bg.create_text(0, 0, text='')
			self.TPa = self.bg.create_text(0, 0, text='')
			self.TQa = self.bg.create_text(0, 0, text='')
			self.TRa = self.bg.create_text(0, 0, text='')
			self.TSa = self.bg.create_text(0, 0, text='')
			self.TTa = self.bg.create_text(0, 0, text='')
			self.TUa = self.bg.create_text(0, 0, text='')
			self.TVa = self.bg.create_text(0, 0, text='')
			self.TWa = self.bg.create_text(0, 0, text='')
			self.TXa = self.bg.create_text(0, 0, text='')
			self.TYa = self.bg.create_text(0, 0, text='')
			self.TZa = self.bg.create_text(0, 0, text='')
			self.TAb = self.bg.create_text(0, 0, text='')
			self.TBb = self.bg.create_text(0, 0, text='')
			self.TCb = self.bg.create_text(0, 0, text='')
			self.TDb = self.bg.create_text(0, 0, text='')
			self.TEb = self.bg.create_text(0, 0, text='')
			self.TFb = self.bg.create_text(0, 0, text='')
			self.TGb = self.bg.create_text(0, 0, text='')
			self.THb = self.bg.create_text(0, 0, text='')
			self.TIb = self.bg.create_text(0, 0, text='')
			self.TJb = self.bg.create_text(0, 0, text='')
			self.TKb = self.bg.create_text(0, 0, text='')
			self.TLb = self.bg.create_text(0, 0, text='')
			self.TMb = self.bg.create_text(0, 0, text='')
			self.TNb = self.bg.create_text(0, 0, text='')
			self.TOb = self.bg.create_text(0, 0, text='')
			self.TPb = self.bg.create_text(0, 0, text='')
			self.TQb = self.bg.create_text(0, 0, text='')
			self.TRb = self.bg.create_text(0, 0, text='')
			self.TSb = self.bg.create_text(0, 0, text='')
			self.TTb = self.bg.create_text(0, 0, text='')
			self.TUb = self.bg.create_text(0, 0, text='')
			self.TVb = self.bg.create_text(0, 0, text='')
			self.TWb = self.bg.create_text(0, 0, text='')
			self.TXb = self.bg.create_text(0, 0, text='')
			self.TYb = self.bg.create_text(0, 0, text='')
			self.TZb = self.bg.create_text(0, 0, text='')
			
		if self.display_rules == 1:
			self.bg.create_text(0,self.y_cen,text=self.output,fill='hot pink',
					font=("Impact",self.fontsize),justify=LEFT,anchor=W)
		
	def PrepBanner(self):
		def RunTransBanner():
			try:
				self.banner_var+=1
				if self.banner_var >= 4:
					self.BannerLine = HP.SetWrittenLine(self.humiliation, self.prefer_dom, self.prefer_sub)
					self.banner_var = 0
					self.linecolor = choice(self.color_list)
				self.bg.delete(self.tmp_banner)
				self.tmp_banner = self.bg.create_text(self.screenwidth/2, self.screenheight/1.3, 
													text=self.BannerLine.upper(),anchor=CENTER,
													font=("Impact", 44), fill=self.linecolor)
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'RunTransBanner', subj='')
			self.master.after(self.delay, RunTransBanner)
		# ################################################# #
		try:
			with open('Resources\\Text\\Humiliation.txt', 'r') as f:
				self.humiliation = f.readlines()
			self.color_list = []
			with open('Resources\\Text\\Text Colors.txt', 'r') as f:
				colors = f.readlines()
				for line in colors:
					self.color_list.append(line.strip('\n'))
			self.c_images, self.p_images = Pipe()
			if self.homework == 'Banner' and self.tranbanr == 0 or self.banwords == 0 or self.display_rules == 2:
				if DEBUG: print('Starting Banner Layer...')
				dom = self.prefer_dom
				sub = self.prefer_sub
				delay = self.delay
				humiliation = self.humiliation
				banwords = self.banwords
				color_list = self.color_list
				wordcount = self.wordcount
				tranbanr = self.tranbanr
				homework = self.homework
				output = self.output
				display_rules = self.display_rules
				fontsize = self.fontsize
				c_images = self.c_images
				c_txt = self.c_txt
				c_hypno = self.c_hypno
				Thread(target=create_banner, args=(delay,dom,sub,humiliation,
								color_list,banwords,wordcount,tranbanr,homework,
								output,display_rules,fontsize,c_images,c_txt,
								c_hypno)).start()
			if self.tranbanr == 1 and self.homework == 'Banner':
				self.tmp_banner = self.bg.create_text(0, 0, text='')
				RunTransBanner()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'PrepBanner', subj='')
			
	def setaudioloop(self):
		if not self.loopingAudio == 0:
			self.audiolist = glob('Resources/Tracks/*.mp3', recursive=True)
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
		
	def pinup(self):
		try:
			if self.enable_pinup == 1:
				self.slideiter = 0
				self.r_nextchunk = True
				self.foregrounds = cycle([(PhotoImage(file=image))
								for image in self.image_files[0:5]])
				self.img_object = next(self.foregrounds) 
				self.bg.fg = self.bg.create_image(self.x_cen, self.y_cen, image=self.img_object)
				self.t = Thread(target=self.loadnewpic).start()
			else:
				self.bg.fg = self.bg.create_image(self.x_cen, self.y_cen, image='')
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'pinup', subj='')
	
	def slides(self):
		try:
			if self.c_hypno.poll() == True:
				self.master.quit()
			if self.enable_pinup == 1 and not self.playingvideo == True:
				self.handleimages()
			if self.c_pinup.poll() == True:
				self.c_PinupAssassin.send(True)
				self.image_files = GenImageFiles(self.c_pinup.recv(),self.enable_pinup)
			if self.c_vid.poll() == True or self.playingvideo == True:
				if self.c_vid.poll() == True:
					self.video_filename = self.c_vid.recv()
					self.videostarttime = time()
				self.playingvideo = True
				self.clear_screen()
				self.set_video()
				self.after(25, self.slides)
			else:
				self.maintext_var = True
				if self.banwords == 1:
					self.update_text()
					self.after(int(self.delay/2), self.update_text)				
				self.after(self.delay, self.slides)
			if not self.DoingHW==True:
				self.breathe_transp()
			self.assign_homework()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'slides', subj='')
	
	def handleimages(self):
		if self.slideiter == 1:
			self.r_nextchunk = True
			self.slideiter = 0
		self.slideiter +=1
		self.img_object = next(self.foregrounds)
		self.bg.itemconfig(self.bg.fg, image=self.img_object)
		
	def loadnewpic(self):
		if self.c_PinupAssassin.poll() == True:
			self.c_PinupAssassin.recv()
			return
		try:
			if self.r_nextchunk == True:
				try:
					self.foregrounds = cycle([PhotoImage(file=image) 
						for image in self.image_files[0:1]])
					self.r_nextchunk = False
				except TclError:
					pass
				shuffle(self.image_files)
		except RuntimeError:
			self.quit()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'loadnewpic', subj='')
		if self.c_hypno.poll() == True:
			self.quit()
		else:
			sleep(1)
			self.t = Thread(target=self.loadnewpic).start()
		
	def clear_screen(self):
		self.bg.delete(self.TopTextA)
		self.bg.delete(self.TopTextB)
		self.bg.delete(self.TopTextC)
		self.bg.delete(self.BotTextA)
		self.bg.delete(self.BotTextB)
		self.bg.delete(self.BotTextC)
		self.bg.delete(self.LefTextA)
		self.bg.delete(self.LefTextB)
		self.bg.delete(self.LefTextC)
		self.bg.delete(self.RgtTextA)
		self.bg.delete(self.RgtTextB)
		self.bg.delete(self.RgtTextC)
		self.TopTextA = self.bg.create_text(0, 0, text='')
		self.TopTextB = self.bg.create_text(0, 0, text='')
		self.TopTextC = self.bg.create_text(0, 0, text='')
		self.BotTextA = self.bg.create_text(0, 0, text='')
		self.BotTextB = self.bg.create_text(0, 0, text='')
		self.BotTextC = self.bg.create_text(0, 0, text='')
		self.LefTextA = self.bg.create_text(0, 0, text='')
		self.LefTextB = self.bg.create_text(0, 0, text='')
		self.LefTextC = self.bg.create_text(0, 0, text='')
		self.RgtTextA = self.bg.create_text(0, 0, text='')
		self.RgtTextB = self.bg.create_text(0, 0, text='')
		self.RgtTextC = self.bg.create_text(0, 0, text='')
		if self.wordcount > 5 and self.banwords == 1:
			self.bg.delete(self.TAa)
			self.bg.delete(self.TBa)
			self.bg.delete(self.TCa)
			self.bg.delete(self.TDa)
			self.bg.delete(self.TEa)
			self.bg.delete(self.TFa)
			self.bg.delete(self.TGa)
			self.bg.delete(self.THa)
			self.bg.delete(self.TIa)
			self.bg.delete(self.TJa)
			self.bg.delete(self.TKa)
			self.bg.delete(self.TLa)
			self.bg.delete(self.TMa)
			self.bg.delete(self.TNa)
			self.bg.delete(self.TOa)
			self.bg.delete(self.TPa)
			self.bg.delete(self.TQa)
			self.bg.delete(self.TRa)
			self.bg.delete(self.TSa)
			self.bg.delete(self.TTa)
			self.bg.delete(self.TUa)
			self.bg.delete(self.TVa)
			self.bg.delete(self.TWa)
			self.bg.delete(self.TXa)
			self.bg.delete(self.TYa)
			self.bg.delete(self.TZa)
			self.bg.delete(self.TAb)
			self.bg.delete(self.TBb)
			self.bg.delete(self.TCb)
			self.bg.delete(self.TDb)
			self.bg.delete(self.TEb)
			self.bg.delete(self.TFb)
			self.bg.delete(self.TGb)
			self.bg.delete(self.THb)
			self.bg.delete(self.TIb)
			self.bg.delete(self.TJb)
			self.bg.delete(self.TKb)
			self.bg.delete(self.TLb)
			self.bg.delete(self.TMb)
			self.bg.delete(self.TNb)
			self.bg.delete(self.TOb)
			self.bg.delete(self.TPb)
			self.bg.delete(self.TQb)
			self.bg.delete(self.TRb)
			self.bg.delete(self.TSb)
			self.bg.delete(self.TTb)
			self.bg.delete(self.TUb)
			self.bg.delete(self.TVb)
			self.bg.delete(self.TWb)
			self.bg.delete(self.TXb)
			self.bg.delete(self.TYb)
			self.bg.delete(self.TZb)
			self.TAa = self.bg.create_text(0, 0, text='')
			self.TBa = self.bg.create_text(0, 0, text='')
			self.TCa = self.bg.create_text(0, 0, text='')
			self.TDa = self.bg.create_text(0, 0, text='')
			self.TEa = self.bg.create_text(0, 0, text='')
			self.TFa = self.bg.create_text(0, 0, text='')
			self.TGa = self.bg.create_text(0, 0, text='')
			self.THa = self.bg.create_text(0, 0, text='')
			self.TIa = self.bg.create_text(0, 0, text='')
			self.TJa = self.bg.create_text(0, 0, text='')
			self.TKa = self.bg.create_text(0, 0, text='')
			self.TLa = self.bg.create_text(0, 0, text='')
			self.TMa = self.bg.create_text(0, 0, text='')
			self.TNa = self.bg.create_text(0, 0, text='')
			self.TOa = self.bg.create_text(0, 0, text='')
			self.TPa = self.bg.create_text(0, 0, text='')
			self.TQa = self.bg.create_text(0, 0, text='')
			self.TRa = self.bg.create_text(0, 0, text='')
			self.TSa = self.bg.create_text(0, 0, text='')
			self.TTa = self.bg.create_text(0, 0, text='')
			self.TUa = self.bg.create_text(0, 0, text='')
			self.TVa = self.bg.create_text(0, 0, text='')
			self.TWa = self.bg.create_text(0, 0, text='')
			self.TXa = self.bg.create_text(0, 0, text='')
			self.TYa = self.bg.create_text(0, 0, text='')
			self.TZa = self.bg.create_text(0, 0, text='')
			self.TAb = self.bg.create_text(0, 0, text='')
			self.TBb = self.bg.create_text(0, 0, text='')
			self.TCb = self.bg.create_text(0, 0, text='')
			self.TDb = self.bg.create_text(0, 0, text='')
			self.TEb = self.bg.create_text(0, 0, text='')
			self.TFb = self.bg.create_text(0, 0, text='')
			self.TGb = self.bg.create_text(0, 0, text='')
			self.THb = self.bg.create_text(0, 0, text='')
			self.TIb = self.bg.create_text(0, 0, text='')
			self.TJb = self.bg.create_text(0, 0, text='')
			self.TKb = self.bg.create_text(0, 0, text='')
			self.TLb = self.bg.create_text(0, 0, text='')
			self.TMb = self.bg.create_text(0, 0, text='')
			self.TNb = self.bg.create_text(0, 0, text='')
			self.TOb = self.bg.create_text(0, 0, text='')
			self.TPb = self.bg.create_text(0, 0, text='')
			self.TQb = self.bg.create_text(0, 0, text='')
			self.TRb = self.bg.create_text(0, 0, text='')
			self.TSb = self.bg.create_text(0, 0, text='')
			self.TTb = self.bg.create_text(0, 0, text='')
			self.TUb = self.bg.create_text(0, 0, text='')
			self.TVb = self.bg.create_text(0, 0, text='')
			self.TWb = self.bg.create_text(0, 0, text='')
			self.TXb = self.bg.create_text(0, 0, text='')
			self.TYb = self.bg.create_text(0, 0, text='')
			self.TZb = self.bg.create_text(0, 0, text='')
			
	def set_video(self):
		try:
			self.playingvideo = True
			if self.DoingHW == True:
				self.bg.right_port.config(bg=HP.TRANS_CLR_ALT())
			else:
				self.bg.right_port.config(bg=HP.TRANS_CLR())
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
			else:
				self.clear_screen()
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
			HP.HandleError(format_exc(2), e, 'set_video', subj='')
			
	def assign_homework(self):
		try:
			self.DoingHW,self.NxtHWTime,self.HWRemain = GenHomework(self.homework,self.DoingHW,self.NxtHWTime,self.HWRemain)
			if self.c_homework.poll() == True:
				self.HWRemain = self.c_homework.recv()
				print('homework recieved', self.HWRemain)
			self.do_homework()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'assign_homework', subj='')	
		
	def do_homework(self):
		try:
			if self.HWRemain > 0 and self.DoingHW == False:
				print('homework=', self.HWRemain)
				self.DoingHW = True
				self.master.overrideredirect(1)
				if self.do_homework == 'Always':
					oldtop = self.top
				self.master.wm_attributes("-transparentcolor", "#000000")
				self.master.attributes('-alpha', 1)
				self.bg.right_port.config(bg=HP.TRANS_CLR_ALT())
				self.bg.right_port.place(relx=1, rely=.5, anchor=E)	
				if self.enable_hypno == 0:
					self.bg.config(bg=HP.TRANS_CLR_ALT())
				if self.game == 'OW':
					self.bg.ChatPort.config(bg=HP.TRANS_CLR_ALT())
					self.bg.KillfeedPort.config(bg=HP.TRANS_CLR_ALT())	
					self.bg.KillfeedPort.place(relx=1, rely=0, anchor=SW)
		
				if self.game == 'LoL':
					self.bg.KillfeedPort.config(bg=HP.TRANS_CLR_ALT())
					
				self.written_line = HP.SetWrittenLine(self.humiliation, self.prefer_dom, self.prefer_sub)
				if len(self.written_line) < 33:
					width, height = 1200,150
				else:
					width, height = 1500,150
				x = (self.screenwidth/2) - (width/2)
				y = (self.screenheight/2) - (height/2)
				self.GenTopLevel(width, height, x, y)
				
				if self.do_homework == 'Always':
					oldtop.destroy()
				
				Label(self.top, text='"'+self.written_line.lower()+'"', font=('Arial', 38, 'italic'), bg='gray30').pack(fill=BOTH)

				self.top.e = Entry(self.top, font=('Arial', 38, 'italic'))
				self.top.e.pack()
				self.top.bind('<Return>',self.getbox) 
				self.HWRemain-=1
						
				self.top.lift()
				self.top.focus_force()
				self.top.grab_set()
				self.top.grab_release()
				self.top.e.focus_set()
				self.top.e.focus()

			if self.DoingHW == False:
				self.master.wm_attributes("-transparentcolor", HP.TRANS_CLR())
				if self.game == 'OW':
					self.bg.ChatPort.config(bg=HP.TRANS_CLR())
					self.bg.KillfeedPort.config(bg=HP.TRANS_CLR())
					self.bg.KillfeedPort.place(relx=.75, rely=.25, anchor=SW)
				if self.game == 'LoL':
					self.bg.KillfeedPort.config(bg=HP.TRANS_CLR())
				self.bg.config(bg=HP.TRANS_CLR())
				self.bg.right_port.config(bg=HP.TRANS_CLR())
				HP.SetClickthrough()
			if self.DoingHW==True:
				self.top.lift()
				self.top.e.focus_set()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'do_homework', subj='')
			
	def GenTopLevel(self, width, height, x, y):
		try:
			self.top = Toplevel(self.master, bg='gray30', takefocus=True)
			self.top.overrideredirect(1)
			self.top.title('Write For Me...')
			self.top.geometry('%dx%d+%d+%d' % (width, height, x, y))
			self.top.wm_attributes("-topmost", 1)
			HP.RemoveClickthrough()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'GenTopLevel', subj='')
		
	def getbox(self,event):
		try:
			self.user_line = self.top.e.get()
			self.top.e.delete(0, END)
			desired_var = self.written_line.lower().strip()
			input_var = self.user_line.lower().strip()
			if input_var == desired_var:
				self.user_line=''
				if self.homework == 'Always':
					self.do_homework()
				else:
					self.do_homework()
					self.top.destroy() 
				self.DoingHW=False
			elif '[]' in input_var:	# a cheat to escape Write For Me
				self.HWRemain = 0
				self.do_homework()
				self.top.destroy() 
				self.DoingHW=False
			else:
				try:
					playsound('Resources\\Audio\\Punishment Buzz.mp3', False)
				except Exception:
					pass
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'getbox', subj='')
		
	def GenColor(self): return HP.TRANS_CLR_ALT() if self.DoingHW else choice(self.color_list)
	def update_text(self):
		try:
			if self.wordcount > 0:
				if self.maintext_var == True:
					colorx1 = self.GenColor()
					adjx1 = choice(self.alines).upper()
					subx1 = choice(self.slines).upper()	
					
					self.bg.delete(self.TopTextA)
					self.bg.delete(self.BotTextA)
					self.TopTextA = self.bg.create_text(self.x_cen,self.y_upr,text=adjx1,font=HP.FONT0(),fill=colorx1,justify=CENTER)
					self.BotTextA = self.bg.create_text(self.x_cen,self.y_low,text=subx1,font=HP.FONT0(),fill=colorx1,justify=CENTER)
				if self.wordcount > 1:				# L+R words	
					lx = float(randint(int(self.x_lef*.9),int(self.x_lef*1.1)))
					ly = float(randint(int(self.y_cen*.9),int(self.y_cen*1.1)))
					rx = float(randint(int(self.x_rgt*.9),int(self.x_rgt*1.1)))
					ry = float(randint(int(self.y_cen*.9),int(self.y_cen*1.1)))	
					colory1 = self.GenColor()
					adjy1 = choice(self.alines).upper()
					suby1 = choice(self.slines).upper()
					
					self.bg.delete(self.RgtTextA)
					self.bg.delete(self.LefTextA)
					self.LefTextA = self.bg.create_text(lx, ly,text=adjy1,font=HP.FONT1(),fill=colory1,justify=CENTER)
					self.RgtTextA = self.bg.create_text(rx, ry,text=suby1,font=HP.FONT1(),fill=colory1,justify=CENTER)
				if self.wordcount > 2:				#T+B extra words	
					colorx2 = self.GenColor()
					colorx3 = self.GenColor()
					adjx2 = choice(self.alines).upper()
					subx2 = choice(self.slines).upper()
					adjx3 = choice(self.alines).upper()
					subx3 = choice(self.slines).upper()
					
					self.bg.delete(self.TopTextB)
					self.bg.delete(self.TopTextC)
					self.bg.delete(self.BotTextB)
					self.bg.delete(self.BotTextC)						
					Top_offset = self.x_cen+randint(-30,30)
					self.TopTextB = self.bg.create_text(Top_offset   ,self.y_upr-68,text=adjx2,font=HP.FONT2(),fill=colorx2,justify=CENTER)
					self.TopTextC = self.bg.create_text(Top_offset*-1,self.y_upr+20,text=subx2,font=HP.FONT2(),fill=colorx2,justify=CENTER)
					self.BotTextB = self.bg.create_text(Top_offset   ,self.y_low+-68,text=adjx3,font=HP.FONT2(),fill=colorx3,justify=CENTER)
					self.BotTextC = self.bg.create_text(Top_offset*-1,self.y_low+20,text=subx3,font=HP.FONT2(),fill=colorx3,justify=CENTER)
				if self.wordcount > 3:			#L+R extra words
					colory2 = self.GenColor()
					colory3 = self.GenColor()
					adjy2 = choice(self.alines).upper()
					suby2 = choice(self.slines).upper()
					adjy3 = choice(self.alines).upper()
					suby3 = choice(self.slines).upper()
					
					self.bg.delete(self.RgtTextB)
					self.bg.delete(self.RgtTextC)
					self.bg.delete(self.LefTextB)
					self.bg.delete(self.LefTextC)
					Lef_offset = lx+randint(-30,30)
					Rgt_offset = rx+randint(-30,30)
					self.RgtTextB = self.bg.create_text(Rgt_offset   ,ry-45,text=adjy3,font=HP.FONT3(),fill=colory3,justify=CENTER)
					self.RgtTextC = self.bg.create_text(Rgt_offset*-1,ry+18,text=suby3,font=HP.FONT3(),fill=colory3,justify=CENTER)
					self.LefTextB = self.bg.create_text(Lef_offset   ,ly-45,text=adjy2,font=HP.FONT3(),fill=colory2,justify=CENTER)
					self.LefTextC = self.bg.create_text(Lef_offset*-1,ly+18,text=suby2,font=HP.FONT3(),fill=colory2,justify=CENTER)
				
				if not self.wordcount > 4:
					self.maintext_var = False
				if self.wordcount > 5 and self.banwords == 1:
					self.UnleashWords()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'hypno.update_text', subj='')
		
	def UnleashWords(self):
		def RandX(): return randint(100,self.screenwidth-100)
		def RandY(): return randint(50,self.screenheight-50)
		def LineText(): return choice(self.alines).upper()+' '+choice(self.slines).upper()
		# ###################### #
		if self.InsaneWordsA == 1:
			self.InsaneWordsA = 2
			self.bg.delete(self.TAa)
			self.bg.delete(self.TBa)
			self.bg.delete(self.TCa)
			self.bg.delete(self.TDa)
			self.bg.delete(self.TEa)
			self.bg.delete(self.TFa)
			self.bg.delete(self.TGa)
			self.bg.delete(self.THa)
			self.bg.delete(self.TIa)
			self.TAa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TBa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TCa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TDa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TEa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TFa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TGa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.THa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TIa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)

		elif self.InsaneWordsA == 2:
			self.InsaneWordsA = 3
			self.bg.delete(self.TJa)
			self.bg.delete(self.TKa)
			self.bg.delete(self.TLa)
			self.bg.delete(self.TMa)
			self.bg.delete(self.TNa)
			self.bg.delete(self.TOa)
			self.bg.delete(self.TPa)
			self.bg.delete(self.TQa)
			self.bg.delete(self.TRa)
			self.TJa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TKa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TLa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TMa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TNa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TOa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TPa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TQa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TRa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)

		elif self.InsaneWordsA == 3:
			self.InsaneWordsA = 1
			self.bg.delete(self.TSa)
			self.bg.delete(self.TTa)
			self.bg.delete(self.TUa)
			self.bg.delete(self.TVa)
			self.bg.delete(self.TWa)
			self.bg.delete(self.TXa)
			self.bg.delete(self.TYa)
			self.bg.delete(self.TZa)
			self.TSa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TTa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TUa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TVa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TWa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TXa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TYa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TZa = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
		
		if self.InsaneWordsB == 1:
			self.InsaneWordsB = 2
			self.bg.delete(self.TAb)
			self.bg.delete(self.TBb)
			self.bg.delete(self.TCb)
			self.bg.delete(self.TDb)
			self.bg.delete(self.TEb)
			self.bg.delete(self.TFb)
			self.bg.delete(self.TGb)
			self.bg.delete(self.THb)
			self.bg.delete(self.TIb)
			self.TAb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TBb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TCb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TDb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TEb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TFb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TGb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.THb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
			self.TIb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)

		elif self.InsaneWordsB == 2:
			self.InsaneWordsB = 3
			self.bg.delete(self.TJb)
			self.bg.delete(self.TKb)
			self.bg.delete(self.TLb)
			self.bg.delete(self.TMb)
			self.bg.delete(self.TNb)
			self.bg.delete(self.TOb)
			self.bg.delete(self.TPb)
			self.bg.delete(self.TQb)
			self.bg.delete(self.TRb)
			self.TJb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TKb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TLb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TMb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TNb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TOb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TPb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TQb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
			self.TRb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)

		elif self.InsaneWordsB == 3:
			self.InsaneWordsB = 1
			self.bg.delete(self.TSb)
			self.bg.delete(self.TTb)
			self.bg.delete(self.TUb)
			self.bg.delete(self.TVb)
			self.bg.delete(self.TWb)
			self.bg.delete(self.TXb)
			self.bg.delete(self.TYb)
			self.bg.delete(self.TZb)
			self.TSb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TTb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TUb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TVb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TWb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TXb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TYb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			self.TZb = self.bg.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
		
	def breathe_transp(self):
		try:
			if not self.opacity == 4:
				if self.playingvideo == True:
					self.tmp_opacity = self.opacity+1
				else:
					self.tmp_opacity = self.opacity
				now,_,_ = str(time() % 60).partition('.')
				now = int(now)
				if   0 <= now <= 15: now=(now-30)*-1
				elif 15 < now <= 30: pass
				elif 30 < now <= 45: now=(now-60)*-1
				elif 45 < now <= 60: now=now-30
					
				if self.tmp_opacity == 0:
					opacity = (now*.01)*1-.15
				else:
					opacity = (now*.01)*self.tmp_opacity
			else:
				opacity = 1 # because Opacity level 4 is fully opaque
			self.master.overrideredirect(1)
			self.master.attributes('-alpha', opacity)	
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'breathe_transp', subj='')
			
	def updategif(self):
		try:
			if self.enable_hypno >= 1:
				if self.playingvideo == False:
					self.bg_image=next(self.gifcycle)
					self.bg.itemconfig(self.bg.gif_create, image=self.bg_image)
				else:
					self.bg.itemconfig(self.bg.gif_create, image='')
				if   self.enable_hypno == 1: self.after(30, self.updategif)
				elif self.enable_hypno == 2: self.after(1, self.updategif)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'updategif', subj='')

#####################################
# ####################################
#####################################
# ####################################

def GenHomework(homework,DoingHW,NxtHWTime,HWRemain):
	for k,v in {'Never' :(0,-1),			'Not Often' :(90,randint(1,2)),
				'Often' :(60,randint(2,4)),	'Very Often':(45,randint(2,4)),
				'Always':(-1,20)}.items():
		if homework == 'Never':
			DoingHW == False
		elif homework == k:	
			if NxtHWTime < time():
				TimeAdd, NewHomeWork = v
				NxtHWTime=time()+TimeAdd
				HWRemain = HWRemain+NewHomeWork
	if   HWRemain > 20: HWRemain = 20  
	elif HWRemain < 1 : HWRemain = 0
	return DoingHW,NxtHWTime,HWRemain

def GenImageFiles(globfile,pinup):
	if pinup == 1:
		if globfile == 'All':
			image_files = glob('Resources/Images/*/*.png', recursive=True)
			print('All images found:', len(image_files))
		else:
			image_files = glob(globfile+'/*.png', recursive=True)
			print(globfile,'found', len(image_files), 'images...')
	else:
		image_files = ''
	shuffle(image_files)
	return image_files

def launch(delay,opacity,game,homework,wordcount,hypno,
				dom,sub,pinup,banwords,tranbanr,globfile,
				s_rulename,fontsize,display_rules,loopingAudio,
				gifset,c_vid,c_txt,c_pinup,c_homework,c_hypno):
	try:
		root = Tk()
		width = root.winfo_screenwidth()
		height = root.winfo_screenheight()
		root.geometry('%dx%d' % (width, height))
		root.configure(background="#000000")
		root.attributes('-alpha', 0.3)
		root.title("Healslut Hypnotherapy")
		root.wm_attributes("-topmost", 1)
		
		if DEBUG: print('Cloaking Hypnotherapy Background...')
		HP.SetClickthrough()
		image_files = GenImageFiles(globfile,pinup)
		if c_hypno.poll() == True:
			exit()
		
		if DEBUG: print('Building Hypnotherapy Object...')
		e = Hypnotherapy(root, image_files, delay, opacity, game, homework, 
					wordcount, hypno, dom, sub, pinup, banwords, tranbanr, 
					s_rulename, fontsize, display_rules, loopingAudio,
					gifset,c_vid, c_txt, c_pinup, c_homework, c_hypno)
		e.pack(fill=BOTH, expand=YES)
		if DEBUG: print('Hypnotherapy Mainloop...')
		root.mainloop()
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'Hypnotherapy.launch', subj='')
		
if __name__ == '__main__':
	pass

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
from os import path, getpid
from playsound import playsound
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGBA
from mutagen.mp3 import MP3
from traceback import format_exc
from win32gui import FindWindow, SetWindowLong, GetWindowLong, SetLayeredWindowAttributes
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE, LWA_ALPHA, WS_EX_COMPOSITED, WS_EX_TOPMOST
import sys

import HealslutPackages as HP

HSDEBUG = True

class HypnotherapyBG(Frame):
	def __init__(self, master, game, enable_hypno, gifset, 
					c_hypno, p_bg, c_bg, c_opacity, 
					c_pinupdims, *pargs):
		Frame.__init__(self, master, *pargs)
		try:
			self.master = master
			self.screenwidth = self.master.winfo_screenwidth()
			self.screenheight = self.master.winfo_screenheight()
			self.master.overrideredirect(1)
			self.playingvideo = False
			self.game = game
			self.enable_hypno = enable_hypno
			self.gifset = gifset
			self.c_hypno = c_hypno
			self.p_bg = p_bg
			self.c_bg = c_bg
			self.c_opacity = c_opacity
			self.c_pinupdims = c_pinupdims
			self.DoingHW = False
			self.bgDict = {}
			self.knt = 0
			self.w,self.h = 0,0
			
			self.MakeBackground()
			
			if HSDEBUG: print('Caching Gif')
			self.FormatGif()

			if HSDEBUG: print('Beginning Gif Loop')
			self.UpdateBackground()
			
			self.after(1000,SetClickthrough)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'HypnotherapyBG.init', subj='')
		
	def MakeBackground(self):
		self.bg = Canvas(self,width=self.screenwidth,height=self.screenheight, highlightthickness=0)
		self.bg.config(bg=HP.TRANS_CLR())
		self.bg.pack(fill=BOTH, expand=YES)
		
		self.master.wm_attributes("-transparentcolor", HP.TRANS_CLR())
		self.PinupPort = Canvas(self.bg,bg=HP.TRANS_CLR(),width=0,height=0,highlightthickness=0)
		self.PinupPort.place(relx=.5, rely=.5, anchor=CENTER)
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

	def FormatGif(self):
		try:
			if self.enable_hypno >= 1:
				Filepath = path.abspath('Resources\\Hypno Gif')
				imagelist = glob(Filepath+'\\'+self.gifset+'\\*.gif', recursive=True)
				for i,image in enumerate([image for image in imagelist]):
					photoimg = PhotoImage(file=image)
					self.bgDict[i] = \
					{
						'obj':self.bg.create_image(self.screenwidth/2,self.screenheight/2,image=photoimg),
						'img':photoimg
					}
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'FormatGif', subj='')

	def UpdateBackground(self):
			# Should I die?
		if self.c_hypno.poll() == True:
			print('Killing HypnoBG')
			exit()
				
			# Hide or show BG while playing video
		if self.c_bg.poll():
			while self.c_bg.poll():
				self.playingvideo = self.c_bg.recv()
			if self.playingvideo == True:
				print(self.playingvideo,'Hiding')
				for i in self.bgDict:
					self.bg.itemconfigure(self.bgDict[i]['obj'], state='hidden')
			else:
				for i in self.bgDict:
					self.bg.itemconfigure(self.bgDict[i]['obj'], state='normal')
		
			# Adjust the box which hides BG behind Pinup
		self.CheckPinupPort()
		
		# Cycle to next gif frame
		if not self.playingvideo and self.enable_hypno != 0:
			self.knt += 1
			if not self.knt in self.bgDict:
				self.knt = 0
			self.bg.tag_raise(self.bgDict[self.knt]['obj'])
			
			# Blind user during homework
		if self.DoingHW == False:
			if self.c_opacity.poll():
				while self.c_opacity.poll():
					opacity = self.c_opacity.recv()
				self.master.attributes('-alpha', opacity)
			
			# Gif speed
		if self.enable_hypno < 2: 
			self.after(50,self.UpdateBackground)
			for i in range(0,25):
				self.after(i*2,self.CheckPinupPort)
		elif self.enable_hypno == 2: 
			self.after(25,self.UpdateBackground)
			for i in range(0,12):
				self.after(i*2,self.CheckPinupPort)
	
	def CheckPinupPort(self):
		if self.c_pinupdims.poll():
			while self.c_pinupdims.poll():
				w,h = self.c_pinupdims.recv()
			self.PinupPort.config(width=w,height=h)
		
def SetClickthrough(windowname='HealslutBG'): #I want this to be in HP, but doesnt work when imported
	try:
		hwnd = FindWindow(None, windowname)
		if HSDEBUG: print('Cloaking Hypnotherapy Background...', windowname, hwnd)
		windowStyles = WS_EX_LAYERED | WS_EX_TRANSPARENT
		SetWindowLong(hwnd, GWL_EXSTYLE, windowStyles)
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'HypnotherapyBG_SetClickthrough', subj='')	
		
def launch(game,enable_hypno,gifset,c_hypno,p_bg,c_bg,c_opacity,c_pinupdims):
	try:
		root = Tk()
		width = root.winfo_screenwidth()
		height = root.winfo_screenheight()
		root.geometry('%dx%d' % (width, height))
		root.configure(background="#000000")
		root.attributes('-alpha', 0.3)
		root.title("HealslutBG")
		root.wm_attributes("-topmost", 1)
		
		if c_hypno.poll() == True:
			print('Exiting before we even started')
			exit()
		if HSDEBUG: print('Building Hypnotherapy BG Object...')
		e = HypnotherapyBG(root, game, enable_hypno, gifset, 
					c_hypno, p_bg, c_bg, c_opacity, c_pinupdims)
		e.pack(fill=BOTH, expand=YES)
		root.mainloop()
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'HypnotherapyBG.launch', subj='')
	
class StartHypnoBG(Process):
	def __init__(self,game,enable_hypno,gifset,c_hypno,p_bg,c_bg,c_opacity,c_pinupdims):
		try:
			self.game = game
			self.enable_hypno = enable_hypno
			self.gifset = gifset
			self.c_hypno = c_hypno
			self.p_bg = p_bg
			self.c_bg = c_bg
			self.c_opacity = c_opacity
			self.c_pinupdims = c_pinupdims
			Process.__init__(self)
			self.start()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'StartHypnoProcess.init', subj='')
			
	def run(self):
		try:
			if HSDEBUG: print('Launching HypnoTherapy BG...')
			launch(self.game,self.enable_hypno,self.gifset,self.c_hypno,
					self.p_bg,self.c_bg,self.c_opacity,self.c_pinupdims)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'StartHypnoProcess.run', subj='')

if __name__ == '__main__':
	from multiprocessing import Pipe
	game = ['None','OW','LoL'][0]
	enable_hypno = [0,1][1]
	gifset = ['Blk Wht Column Thick'][0]
	p_bg,c_hypno = Pipe()
	p_bg,c_bg = Pipe()
	p_opacity,c_opacity = Pipe()
	p_pinupdims,c_pinupdims = Pipe()
	launch(game,enable_hypno,gifset,c_hypno,p_bg,c_bg,c_opacity,c_pinupdims)

import HypnoTherapy
import OverwatchVibe
import KillfeedMonitor
import WordSearch

from tkinter import *
from tkinter.ttk import Notebook
from win32gui import FindWindow, GetForegroundWindow, ShowWindow, SetWindowLong
from win32con import SW_MINIMIZE
from PIL import Image, ImageTk
from itertools import cycle
from time import time, sleep
from multiprocessing import freeze_support, Process, Pipe
from threading import Thread
from glob import iglob, glob
from playsound import playsound, PlaysoundException
from ctypes import windll
from os import remove, path, makedirs
from traceback import format_exc
from functools import partial
from bs4 import BeautifulSoup
from urllib.request import urlopen	
from smtplib import SMTP, SMTPAuthenticationError	
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from requests import get, exceptions
from cv2 import VideoCapture, imwrite
from pyautogui import screenshot
from random import choice, randint
	
	###########################  Info  ##############################
	#																#
	# 					Created by u/Graveknight1					#
	#																#
	# Please contact me via reddit for questions or requests. if	#
	# you would like to donate to my work, checkout my paypal.		#
	#																#
	# This program is not for sale, if someone charged you for it,  #
	# you've been ripped off.										#
	#																#
	# This code was written for the Healsluts community. If you		#
	# like what you see, check them out at r/healsluts				#
	#																#
	#################################################################
	#				use this line to compile the .exe				#
	#	For me														#
	# pyinstaller -F --icon=ProgDeveloper\hs.ico HealslutMaster.py	#
	#																#
	#	For you	(No Icon)											#
	# pyinstaller -F HealslutMaster.py								#
	#																#
	#################################################################
	#																#
	# https://lovense.com/developer/docs/session-control			#
	# https://lovense.com/developer/docs/lan-connect-pc				#
	#																#
	#################################################################
	
#go to to https://www.reddit.com/r/iateacrayon/wiki/list for images broad range of images
#thanks to Lewd-Zko	(twitter.com/LewdZko) for the image of crystal which was modified and placed on the wordsearch page

Version='v1.4.3'

TRANS_CLR = '#f7e9f1'	#Haha, Pride!

class HealslutMaster(Frame):
	def __init__(self,master,hyp_folders,userinfo,background_list,prefdict,*pargs):
		Frame.__init__(self, master, *pargs)
		try:
			self.master = master
			self.master.overrideredirect(1)
			self.SetupVars(background_list,prefdict,hyp_folders)
			self.SetupPunRwd()
			self.SetupEmail(userinfo)
			self.SetupMenu()
			self.SavePref()
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'healslutmaster.init', subj='')
	
	def SetupVars(self,background_list,prefdict,hyp_folders):
		self.p_hypno, self.c_hypno = Pipe()
		self.p_ow, self.c_ow = Pipe()
		self.p_vid, self.c_vid = Pipe()
		self.p_txt, self.c_txt = Pipe()
		self.p_pinup, self.c_pinup = Pipe()
		self.p_rules, self.c_rules = Pipe()
		self.p_homework, self.c_homework = Pipe()
		
		self.background_list = background_list
		self.background_select = StringVar(self.master)
		self.background_select_var = int(prefdict['background_select_var'])
		self.background_select.set(background_list[self.background_select_var])
		
		self.screenwidth = self.master.winfo_screenwidth()
		self.screenheight = self.master.winfo_screenheight()		
		
		self.hyp_delay = StringVar(self.master)
		self.hyp_delay.set(prefdict['hyp_delay'])
		self.hyp_game = StringVar(self.master)
		self.hyp_game.set(prefdict['hyp_game'])
		self.hyp_opacity = StringVar(self.master)
		self.hyp_opacity.set(prefdict['hyp_opacity'])
		self.hyp_homework = StringVar(self.master)
		self.hyp_homework.set(prefdict['hyp_homework'])
		self.hyp_words = StringVar(self.master)
		self.hyp_words.set(prefdict['hyp_words'])
		self.loopingAudio = StringVar(self.master)
		self.loopingAudio.set(prefdict['loopingAudio'])
		self.hyp_able = IntVar(self.master)
		self.hyp_able.set(int(prefdict['hyp_able']))
		self.hyp_pinup = IntVar(self.master)
		self.hyp_pinup.set(int(prefdict['hyp_pinup']))
		self.s_playing = IntVar(self.master)
		self.s_playing.set(int(prefdict['s_playing']))
		self.Freeplay = IntVar(self.master)
		self.Freeplay.set(int(prefdict['Freeplay']))
		self.hyp_banword = IntVar(self.master)
		self.hyp_banword.set(int(prefdict['hyp_banword']))
		self.hyp_tranbanr = IntVar(self.master)
		self.hyp_tranbanr.set(int(prefdict['hyp_tranbanr']))
		self.display_rules = IntVar(self.master)
		self.display_rules.set(int(prefdict['display_rules']))
		self.delold = IntVar(self.master)
		self.delold.set(int(prefdict['delold']))
		self.s_decay = StringVar(self.master)
		self.s_decay.set(prefdict['s_decay'])
		self.s_decay_pow = StringVar(self.master)
		self.s_decay_pow.set(prefdict['s_decay_pow']) #'-1', '-3', '-10', '-20', '3/4', '1/2', '1/4'
		self.hyp_dom = StringVar(self.master)
		self.hyp_dom.set(prefdict['hyp_dom'])
		self.hyp_sub = StringVar(self.master)
		self.hyp_sub.set(prefdict['hyp_sub'])
		self.fontsize = StringVar(self.master)
		self.fontsize.set(prefdict['fontsize'])
		self.HSSub = StringVar(self.master)
		self.HSSub.set(prefdict['sub'])
		self.HSDom = StringVar(self.master)
		self.HSDom.set(prefdict['dom'])
		self.Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		self.KillFeedPath = 'Resources\\Killfeed\\%sx%s\\Overwatch\\'%(self.screenwidth,self.screenheight)
		self.convfolder = StringVar(self.master)
		self.convfolder.set('')
		self.s_rulename = StringVar(self.master)
		self.s_rulename.set(prefdict['s_rulename'])
		self.hyp_gfile = StringVar(self.master)
		self.hyp_gfile_var = int(prefdict['hyp_gfile_var'])
		
		self.AllCharList = ['No Images']
		self.hyp_folders = hyp_folders
		self.hyp_gfile.set(hyp_folders[self.hyp_gfile_var])
		self.conv_hyp_folders = hyp_folders
		
		self.textwdith = StringVar()
		self.textwdith.set(self.screenwidth)
		self.textheight = StringVar()
		self.textheight.set(self.screenheight)
		
		self.hypno = False
		self.vibe = False
		self.editting = False
		self.rules_okay = False
		self.ActionMenuOpen = False
		self.GameWindowOpen = False
		self.base_speed = 0
		self.vibe_speed = 0
		self.rotr_speed = 0
		self.air_speed = 0
			
	def SetupEmail(self,userinfo):
		try:
			self.usermail = str(userinfo[0]).replace('\n','')
			self.userpass = str(userinfo[1]).replace('\n','')
			self.usersecure = str(userinfo[2]).replace('\n','')
		except IndexError:
			self.usermail = 'myemail@gmail.com'
			self.userpass = 'mypassword'
			self.usersecure = '0'
		try:
			self.ToEmail = str(userinfo[3]).replace('\n','')
		except IndexError:
			self.ToEmail = 'ugraveknight@gmail.com'	
			
	def SetupMenu(self):
		self.master.wm_attributes("-transparentcolor", TRANS_CLR)
		self.frame = Frame(self.master, width=50, height=1000,#height=270,
						   borderwidth=2, bg=TRANS_CLR, relief=RAISED)
		self.frame.grid(row=0,column=0)
		self.bg = Label(self.frame, bg='gray30', width=50, height=270, anchor=E)
		self.bg.place(x=0,y=20)
		self.bg.grip = Label(self.frame, height=1, bg='Gray50', text="<Move>", font=('Times', 8))
		self.bg.grip.place(x=0,y=0)
		self.bg.grip.bind("<ButtonPress-1>", self.StartMoveMM)
		self.bg.grip.bind("<ButtonRelease-1>", self.StopMoveMM)
		self.bg.grip.bind("<B1-Motion>", self.MainMenuOnMotion)
		
		self.RwdBtn = Button(self.bg, bg='green',text="Rwrd",width=5,command=partial(self.HandleCycles,self.rewardcycle))
		self.RwdBtn.grid(row=1, column=0)
		self.PnshBtn = Button(self.bg, bg='red', text="Pnsh", width=5,command=partial(self.HandleCycles,self.punishcycle))
		self.PnshBtn.grid(row=2, column=0)
		self.bOW = Button(self.bg, text="Start\nVibe",width=5,command=self.LaunchVibe)
		self.bOW.grid(row=3, column=0)
		self.bHypno = Button(self.bg,text="Start\nHypno",width=5,command=self.launch_hypno)
		self.bHypno.grid(row=4, column=0)
		self.EditBtn = Button(self.bg, text="Edit",width=5,command=self.edit_hypno)
		self.EditBtn.grid(row=5, column=0)
		self.bQuit = Button(self.bg, text="Quit",width=5,command=self.shutdown)
		self.bQuit.grid(row=6, column=0)
		self.master.config(takefocus=1)
	
	def LaunchVibe(self):
		try:	
			if self.vibe == False:
				self.vibe = True
				if self.c_ow.poll() == True:
					self.c_ow.recv()
				self.bOW.config(text='End\nVibe')
				self.markslist = [0,0,0,0]
				self.Positions = OverwatchVibe.GenPositions()
				self.ListOfCycles = KillfeedMonitor.GenCycles()
				self.Cords, self.BorderPixels = KillfeedMonitor.GenCords(self)
				self.KillFeedFiles = glob(self.KillFeedPath+'*.png') if self.Freeplay.get() == True else \
							[self.KillFeedPath+self.HSSub.get()+'.png', 
							self.KillFeedPath+self.HSSub.get()+' Assist.png', 
							self.KillFeedPath+self.HSDom.get()+'.png']
				self.p_killfeed, self.c_killfeed = Pipe()
				self.vibeloop()
			else:
				self.vibe = False
				self.bOW.config(text='Start\nVibe')
				URL='http://localhost.lovense.com:20010/'
				for url in [URL+'Vibrate?v=0',URL+'RotateAntiClockwise?v=0',URL+'AirAuto?v=0']:	
					Thread(target=do_request, args=(url,5)).start()
				if self.c_rules.poll() == False:
					self.p_rules.send(True)
					self.rules_okay = False
				if self.c_ow.poll() == False:
					self.p_ow.send(True)
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'LaunchVibe', subj='')
	
	def GenKillfeedList(self):
		l = glob(self.KillFeedPath+'*.png')
		AllCharList = []
		for i in l:
			if not 'Assist' in i:
				i = i.replace(self.KillFeedPath,'').replace('.png','')
				AllCharList.append(i)
		if not AllCharList == []:
			self.AllCharList = AllCharList
	
	def vibeloop(self):
		try:
			if self.hyp_game.get() == 'OW' and self.vibe == True:
				im = screenshot()
				self.markslist, self.base_speed = OverwatchVibe.go(self.Positions,self.markslist,im)
				KillfeedMonitor.Main(im,self.KillFeedFiles,
									self.HSSub.get(),self.HSDom.get(),
									self.Cords,self.ListOfCycles,
									self.c_killfeed,self.KillFeedPath,
									self.BorderPixels)
				if self.p_killfeed.poll() == True:
					self.do_macro(self.p_killfeed.recv())
				
			vibespeed = self.base_speed+self.vibe_speed
			rotaspeed = self.base_speed+self.rotr_speed
			self.check_decay()
			print('Vibe:',vibespeed,', Rotate:',rotaspeed)
			
				#This is the area where we will communicate to the buttplug server
			URL='http://localhost.lovense.com:20010/'
			urllist=[URL+'Vibrate?v='+str(vibespeed)]
			urllist.append(URL+'RotateAntiClockwise?v='+str(rotaspeed))
			urllist.append(URL+'AirAuto?v='+str(self.air_speed))
			for url in urllist:
				Thread(target=do_request, args=(url,)).start()
				
			if self.vibe == True:			
				self.after(2000, self.vibeloop)
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'vibeloop', subj='')	

	def check_decay(self):
		if not self.s_decay == '0' and time() > self.decaytimer:
			sec = int(self.s_decay.get())
			self.decaytimer=time()+sec
			
				# Thanks Github User this-is-embarrassing!
			#the change in speed and rotr associated with each value
			speed_changes = \
			{
				'-1' : lambda x: x - 1,
				'-3' : lambda x: x - 3,
				'-10': lambda x: x - 10,
				'-20': lambda x: x - 20,
				'3/4': lambda x: x * .75,
				'1/2': lambda x: x * .5,
				'1/4': lambda x: x * .25,
			}
			
			if self.vibe_speed > 0 or self.rotr_speed > 0:
				new_speed = speed_changes.get(self.s_decay_pow.get(), lambda x: x)
				self.vibe_speed = new_speed(self.vibe_speed)
				self.rotr_speed = new_speed(self.rotr_speed)
				
		if not self.s_decay == '0' and time() > self.air_decaytimer:
			sec = int(self.s_decay.get())*3
			self.air_decaytimer=time()+sec
			self.air_speed -= 1
		self.air_speed  = 0 if self.air_speed  <  0 else 3   if self.air_speed  >  3   else self.air_speed
		self.rotr_speed = 0 if self.rotr_speed <= 0 else 100 if self.rotr_speed >= 100 else self.rotr_speed
		self.vibe_speed = 0 if self.vibe_speed <= 0 else 100 if self.vibe_speed >= 100 else self.vibe_speed
		self.rotr_speed = int(self.rotr_speed/5)
		self.vibe_speed = int(self.vibe_speed/5)
	
	def launch_hypno(self):
		try:
			if self.hypno == False and self.editting == False:
				self.hypno = True
				self.rules_okay = False
				self.bHypno.config(text='End\nHypno')
				if self.c_hypno.poll() == True:
					self.c_hypno.recv()
					
				delay = int(self.hyp_delay.get())
				opacity = int(self.hyp_opacity.get())
				game = str(self.hyp_game.get())
				homework = str(self.hyp_homework.get())
				hypno = self.hyp_able.get()
				wordcount = str(self.hyp_words.get())
				dom = str(self.hyp_dom.get())
				sub = str(self.hyp_sub.get())
				pinup = self.hyp_pinup.get()
				banwords = self.hyp_banword.get()
				tranbanr = self.hyp_tranbanr.get()
				globfile = self.hyp_gfile.get()
				s_rulename = self.s_rulename.get()
				fontsize = self.fontsize.get()
				display_rules = self.display_rules.get()
				loopingAudio = self.loopingAudio.get()
				c_rules = self.c_rules
				loopingAudio = 0 if loopingAudio== 'None' else 1 if loopingAudio == 'List' else 2
				wordcount = 0 if wordcount == 'None' else 1 if wordcount == 'Low' else 2 if wordcount == 'Medium' \
					   else 3 if wordcount == 'High' else 4 if wordcount == 'Very High' else 5
				pinup = 0 if hypno == 2 else pinup
				gifset = self.background_select.get().replace('.gif','')
				
				StartHypnoProcess(delay,opacity,game,
							homework,wordcount,hypno,dom,sub,pinup,banwords,tranbanr,
							globfile,s_rulename,fontsize,display_rules,loopingAudio,gifset,
							c_rules,self.c_vid,self.c_txt,self.c_pinup,self.c_homework,
							self.c_hypno)
				self.establish_rules()
			else:
				self.hypno = False
				self.bHypno.config(text='Start\nHypno')
				if self.c_hypno.poll() == False:
					self.p_hypno.send(True)
				self.DestroyActions()
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'launch_hypno', subj='')
			
	def edit_hypno(self):
		try:
			if self.hypno == False and self.editting == False:
				self.editting = True
				if self.c_hypno.poll() == True:
					self.c_hypno.recv()
				if not self.c_rules.poll() == True:
					self.p_rules.send(True)
					
				self.top = Toplevel()
				self.top.title("HypnoTherapy Settings")
				self.top.overrideredirect(True)
				width, height = 1200,415
				x = (self.screenwidth  / 2) - (width  / 2)
				y = (self.screenheight / 2) - (height / 2)
				
				self.top.geometry('%dx%d+%d+%d' % (width, height, x, y))
				
				self.note = Notebook(self.top)
				self.tab1 = Frame(self.note, width=width-100, height=height-100, borderwidth=0, relief=RAISED)
				self.tab2 = Frame(self.note)
				self.tab3 = Frame(self.note)
				
				self.SetupTab1()
				self.SetupTab2()
				self.SetupTab3()
				
				self.note.add(self.tab1, text = "Background and Pinup")
				self.note.add(self.tab2, text = "Rules and Games")
				self.note.add(self.tab3, text = "Text and Vibrator")
				self.note.place(x=50,y=0)
				
					# #Paypal box
				self.bgPaypal = Label(self.top, bg='gray75')
				self.bgPaypal.place(x=10,y=height-65)
				msg = Label(self.bgPaypal, width=22, text='Play Support on Paypal')
				msg.grid(row=0, column=0, columnspan=2, sticky=E+W)
				w = Text(self.bgPaypal, height=1, width=22, borderwidth=0, font=('Times', 14))
				w.insert(1.0, 'ugraveknight@gmail.com')
				w.grid(row=1, columnspan=2)
				w.configure(state="disabled")
					# #Exit button
				self.button = Button(self.top, text="Dismiss", command=self.end_edit)
				self.button.place(x=width-115,y=height-65)
				self.after(25, self.updategif)
			else:
				self.hypno = False
				self.vibe = False
				self.bHypno.config(text='Start\nHypno')
				self.bOW.config(text='Start\nVibe')
				self.editting = False
				self.p_hypno.send(True)
				if self.c_rules.poll() == False:
					self.p_rules.send(True)
					self.rules_okay = False
				if self.c_ow.poll() == False:
					self.p_ow.send(True)
				URL='http://localhost.lovense.com:20010/'
				for url in [URL+'Vibrate?v=0',URL+'RotateAntiClockwise?v=0',URL+'AirAuto?v=0']:
					Thread(target=do_request, args=(url,5)).start()
				self.DestroyActions()
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'edit_hypno', subj='')

	def SetupTab1(self):
			# #Handle Gif# #
		self.handlegif = Canvas(self.tab1, bg='gray50',width=250, height=300)
		self.handlegif.place(x=15,y=5)
		OptionMenu(self.handlegif, self.background_select, *self.background_list,command=self.buildgifset).place(x=15,y=7)
		self.gifcanvas = Canvas(self.handlegif, width=250, height=250, bg='gray75')
		self.gifcanvas.place(x=0,y=50)
		self.buildgifset('')
		try:
			self.gifpreview = self.gifcanvas.create_image(1,1,image=next(self.gifcycle), anchor=NW)
		except StopIteration:
			Label(self.gifcanvas,width=25,font=('Times',12),text='!Format Gif Before Running',anchor=W,bg='gray75').place(x=0,y=0)
			# ############ #
			# #Format gif# #
		self.bggif = Label(self.tab1, bg='gray50',width=300)
		self.bggif.place(x=870,y=240)
		Label(self.bggif, width=6, font=('Times', 12),text='Width', anchor=W).grid(row=0,column=0, pady=2)
		Label(self.bggif, width=6, font=('Times', 12),text='Height', anchor=W).grid(row=1,column=0, pady=2)
		Entry(self.bggif, width=5, borderwidth=0, font=('Times', 14), textvariable=self.textwdith).grid(row=0,column=1)
		Entry(self.bggif, width=5, borderwidth=0, font=('Times', 14), textvariable=self.textheight).grid(row=1,column=1)
		Button(self.bggif, text="Format Gifs", command=self.buildgifs).grid(row=1,column=2)
			# ############ #
			#  Convert png #
		self.bgConvert = Label(self.tab1, bg='gray50')
		self.bgConvert.place(x=500,y=240)
		Button(self.bgConvert, text="Convert jpg to png", command=self.handleimage).grid(row=0, column=0, sticky=W+E)
		Checkbutton(self.bgConvert, text="Delete jpgs", variable=self.delold).grid(row=0, column=1, sticky=E)
		OptionMenu(self.bgConvert, self.convfolder, *self.conv_hyp_folders).grid(row=1,column=0, columnspan=3, sticky=E+W)
			# ############ #
		Message(self.tab1, text='Overlay Opacity').place(x=300,y=25)
		Message(self.tab1, text='Cycle Delay').place(x=300,y=75)
		Message(self.tab1, text='Image Folder').place(x=300,y=125)
		OptionMenu(self.tab1, self.hyp_opacity, '0', '1', '2', '3', '4').place(x=400,y=25)
		OptionMenu(self.tab1, self.hyp_delay, '250', '500', '1000', '1500', '3000').place(x=400,y=75)
		OptionMenu(self.tab1, self.hyp_gfile, *self.hyp_folders).place(x=400,y=125)
		Radiobutton(self.tab1, text="None", variable=self.hyp_able,value=0).place(x=300,y=200)
		Radiobutton(self.tab1, text="Hypno Background", variable=self.hyp_able,value=1).place(x=300,y=225)
		Radiobutton(self.tab1, text="Turbo Hypno", variable=self.hyp_able,value=2).place(x=300,y=250)
		Checkbutton(self.tab1, text="Enable Pinups", variable=self.hyp_pinup).place(x=300,y=275)
	
	def SetupTab2(self):
		owlvl = 250
		Message(self.tab2, text='Rule set').place(x=25,y=20)
		Message(self.tab2, text='Rule Font Size').place(x=25,y=70)
		Message(self.tab2, text='Image Game Holes').place(x=25,y=120)
		OptionMenu(self.tab2, self.s_rulename, *self.rulesets).place(x=125,y=20)
		OptionMenu(self.tab2, self.fontsize, '12', '18', '20', '24', '30').place(x=125,y=70)
		OptionMenu(self.tab2, self.hyp_game, "None", "OW").place(x=125,y=120)
		
		self.GenKillfeedList()
		Message(self.tab2, text='Sub Character').place(x=25,y=owlvl)
		Message(self.tab2, text='Dom Character').place(x=300,y=owlvl)
		OptionMenu(self.tab2, self.HSSub, *self.AllCharList).place(x=125,y=owlvl)
		OptionMenu(self.tab2, self.HSDom, *self.AllCharList).place(x=400,y=owlvl)
		Checkbutton(self.tab2, text="Freeplay", variable=self.Freeplay).place(x=550,y=owlvl+5)
		
		Radiobutton(self.tab2, text="No Rules", variable=self.display_rules,value=0).place(x=300,y=25)
		Radiobutton(self.tab2, text="Transparent Rules", variable=self.display_rules,value=1).place(x=300,y=50)
		Radiobutton(self.tab2, text="Opaque Rules", variable=self.display_rules,value=2).place(x=300,y=75)
		Checkbutton(self.tab2, text="Punishments/Rewards", variable=self.s_playing).place(x=300,y=100)
		
	def SetupTab3(self):
		Message(self.tab3, text='Dom Gender').place(x=25,y=20)
		Message(self.tab3, text='Self Gender').place(x=25,y=70)
		Message(self.tab3, text='Word Count').place(x=25,y=120)
		Message(self.tab3, text='Write For Me').place(x=25,y=170)
		Message(self.tab3, text='Looping Audio').place(x=25,y=220)
		Message(self.tab3, text='Speed Decay Timer').place(x=350,y=20)
		Message(self.tab3, text='Speed Decay Strengh').place(x=350,y=70)
		
		OptionMenu(self.tab3, self.hyp_dom, "None", "Male", "Female").place(x=125,y=20)
		OptionMenu(self.tab3, self.hyp_sub, "Sub", "Boy", "Girl").place(x=125,y=70)
		OptionMenu(self.tab3, self.hyp_homework, "Never", "Not Often", "Often", "Very Often", "Always", "Banner").place(x=125,y=120)
		OptionMenu(self.tab3, self.hyp_words, "None", "Low", "Medium", "High", "Very High", "Max").place(x=125,y=170)
		OptionMenu(self.tab3, self.loopingAudio, "None", "List", "Shuffle").place(x=125,y=220)
		OptionMenu(self.tab3, self.s_decay, '0', '3', '10', '30', '45', '60', '75', '90').place(x=450,y=20)
		OptionMenu(self.tab3, self.s_decay_pow, '0', '-1', '-3', '-10', '-20', '3/4', '1/2', '1/4').place(x=450,y=70)
		
		Checkbutton(self.tab3, text="Transparent Banner", variable=self.hyp_tranbanr).place(x=350,y=150)
		Checkbutton(self.tab3, text="Transparent Words",  variable=self.hyp_banword).place(x=350,y=175)
		
		
	def buildgifset(self, event):
		self.globpath = 'Resources\\Hypno Gif\\'+self.background_select.get().replace('.gif','')+'\\*.gif'
		self.imagelist = glob(self.globpath, recursive=True)
		self.imagelist.sort()
		self.gifcyclist = []
		for myimage in self.imagelist:
			self.gifcyclist.append(ImageTk.PhotoImage(Image.open(myimage).resize((250, 250), Image.LANCZOS)))
		self.gifcycle = cycle(self.gifcyclist)
		
	def updategif(self):
		try:
			if self.editting == True:
				self.gifcanvas.itemconfig(self.gifpreview, image=next(self.gifcycle))
				self.after(25, self.updategif)
		except Exception:
			pass
		
	def end_edit(self):
		try:
			self.editting = False
			self.top.destroy()
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'end_edit', subj='')
	
	def handleimage(self):
		folder = self.convfolder.get()
		if folder == 'All':
			for folder in self.hyp_folders:
				if not folder == 'All':
					convertimage(folder,self.delold.get(),
						self.screenwidth,self.screenheight)
		else:
			convertimage(folder,self.delold.get(),
				self.screenwidth,self.screenheight)
			
	def extractFrames(self,mygif,filepath,mywidth,myheight):
		frame = Image.open(filepath+mygif)
		nframes = 0
		namecount = 0.1
		while frame:
			sizeframe = frame.resize((mywidth,myheight))
			if not path.exists('Resources\Hypno Gif\\'+mygif.replace('.gif','')+'\\'):
				makedirs('Resources\Hypno Gif\\'+mygif.replace('.gif','')+'\\')
			cnt = str(namecount) if len(str(namecount)) == 4 else '0'+str(namecount)
			sizeframe.save( '%s/%s-%s.gif' % ('Resources\Hypno Gif\\'+mygif.replace('.gif','')+'\\', path.basename(mygif), cnt ) , 'GIF')
			nframes += 1
			namecount = round(namecount+.1,1)
			try:
				frame.seek(nframes)
			except EOFError:
				break;
		return True
   
	def buildgifs(self):
		mywidth,myheight = int(self.textwdith.get()),int(self.textheight.get())
		filepath = 'Resources\\Background Gif original\\'
		og_giflist = glob(filepath+'*.gif', recursive=True)
		for mygif in og_giflist:
			mygif=mygif.replace(filepath,'')
			if not mygif == '.gif':
				self.extractFrames(mygif,filepath,mywidth,myheight)
		self.background_list = GenBackgroundList()
		print('Done.')
					
	def SavePref(self):
		self.hyp_gfile_var = 0
		for item in self.hyp_folders:
			if item == self.hyp_gfile.get():
				break
			self.hyp_gfile_var +=1
		self.background_select_var = 0
		for item in self.background_list:
			if item == self.background_select.get():
				break
			self.background_select_var +=1
		PrefDictList = [
			'hyp_delay:'+str(self.hyp_delay.get()),
			'hyp_game:'+str(self.hyp_game.get()),
			'hyp_opacity:'+str(self.hyp_opacity.get()),
			'hyp_homework:'+str(self.hyp_homework.get()),
			'hyp_words:'+str(self.hyp_words.get()),
			'loopingAudio:'+str(self.loopingAudio.get()),
			'hyp_able:'+str(self.hyp_able.get()),
			'hyp_pinup:'+str(self.hyp_pinup.get()),
			's_playing:'+str(self.s_playing.get()),
			'Freeplay:'+str(self.Freeplay.get()),
			'hyp_banword:'+str(self.hyp_banword.get()),
			'hyp_tranbanr:'+str(self.hyp_tranbanr.get()),
			'display_rules:'+str(self.display_rules.get()),
			'delold:'+str(self.delold.get()),
			's_decay:'+str(self.s_decay.get()),
			's_decay_pow:'+str(self.s_decay_pow.get()),
			'hyp_dom:'+str(self.hyp_dom.get()),
			'hyp_sub:'+str(self.hyp_sub.get()),
			'fontsize:'+str(self.fontsize.get()),
			'hyp_gfile_var:'+str(self.hyp_gfile_var),
			'background_select_var:'+str(self.background_select_var),
			's_rulename:'+str(self.s_rulename.get()),
			'sub:'+str(self.HSSub.get()),
			'dom:'+str(self.HSDom.get())
			]
		
		with open('Resources\\Preferences.txt', 'w') as f:
			f.write('')
		with open('Resources\\Preferences.txt', 'a') as f:
			for line in PrefDictList:
				f.write(line+'\n')
			
	def shutdown(self):
		self.SavePref()
		try:
			self.WSFrame.destroy()
		except AttributeError:
			pass
		if self.hypno == True and self.editting == True:
			self.bHypno.config(text='Start\nHypno')
			self.hypno = False
			self.editting = False
			self.p_hypno.send(True)
			if not self.c_rules.poll() == True:
				self.p_rules.send(True)
			try:
				self.top.destroy()
			except AttributeError:
				pass
			self.after(1000, self.shutdown)
		else:
			try:
				self.p_hypno.send(True)
				self.p_ow.send(True)
				self.p_rules.send(True)
				self.master.quit()
				try:
					self.top.destroy()
				except AttributeError:
					pass
			except KeyboardInterrupt:
				pass
			except Exception as e:
				tb = format_exc(2);handleError(tb, e, 'shutdown', subj='')
		
	#########################
	# Begin Buttons Manager #
	#########################
	
	def SetupPunRwd(self):
		self.rulesets = []
		for filename in iglob('Resources\\Healslut Games\\* Rules.txt', recursive=True):
			head, sep, tail = filename.rpartition('\\')
			filename, sep, tail = tail.partition(' ')
			self.rulesets.append(filename)	
		self.rewardcycle = []
		self.punishcycle = []
		self.ActionListA = []
		self.ActionListB = []
		self.ActionListC = []
		self.ActionListD = []
		self.ActionListE = []
		self.ActionListF = []
		self.ActionListG = []
		self.ActionListH = []
		self.ActionListI = []
		self.ActionListJ = []
		self.decaytimer=time()
		self.air_decaytimer=time()	
		
	def setup_menu_actions(self):
		if self.ActionMenuOpen == False:
			if path.isfile('Resources/Healslut Games/'+self.s_rulename.get()+' ButtonA.txt'):
				self.ActionMenuOpen = True
				self.ActionMenu = Toplevel(self, bg=TRANS_CLR, highlightthickness=0)
				self.ActionMenu.overrideredirect(True)
				self.ActionMenu.wm_attributes("-topmost", 1)
				self.ActionMenu.wm_attributes("-transparentcolor", TRANS_CLR)
				self.ActionFrame = Frame(self.ActionMenu, width=50, height=50, bg=TRANS_CLR,
								   borderwidth=0, relief=RAISED,)
				self.ActionFrame.grid(row=0,column=0)

				# ########### #
				# MOVING GRIP #
				self.grip = Label(self.ActionFrame, height=1, bg='Gray50', text="< Hold to Move >", font=('Times', 8))
				self.grip.grid(row=0,column=0,columnspan=2)
				self.grip.bind("<ButtonPress-1>", self.StartMoveAM)
				self.grip.bind("<ButtonRelease-1>", self.StopMoveAM)
				self.grip.bind("<B1-Motion>", self.ActionMenuOnMotion)
				# ########### #
				
				x = (self.screenwidth -300)
				y = (self.screenheight *.4)
				self.ActionMenu.geometry('%dx%d+%d+%d' % (115, 310, x, y))
				if not self.rwdicon == '':
					self.imageRwd = self.GenButtonImage(self.rwdicon)
					self.RwdBtn.config(image=self.imageRwd,bd=0,highlightthickness=0)
				if not self.punicon == '':
					self.imagePun = self.GenButtonImage(self.punicon)
					self.RwdBtn.config(image=self.imageRwd,bd=0,highlightthickness=0)
				self.RwdBtn.config(command=partial(self.HandleCycles,self.rewardcycle))
				self.PnshBtn.config(command=partial(self.HandleCycles,self.punishcycle))
		
				try:
				
					self.imageA = self.GenButtonImage(self.IconA)
					self.ButtonA = Button(self.ActionFrame, image=self.imageA, text="A",
						command=partial(self.HandleCycles,self.ActionCycleA)).grid(row=1,column=0,sticky=W+E+N+S)
					self.imageB = self.GenButtonImage(self.IconB)
					self.ButtonB = Button(self.ActionFrame, image=self.imageB, text="A",
						command=partial(self.HandleCycles,self.ActionCycleB)).grid(row=1,column=1,sticky=W+E+N+S)
					self.imageC = self.GenButtonImage(self.IconC)
					self.ButtonC = Button(self.ActionFrame, image=self.imageC, text="A",
						command=partial(self.HandleCycles,self.ActionCycleC)).grid(row=2,column=0,sticky=W+E+N+S)
					self.imageD = self.GenButtonImage(self.IconD)
					self.ButtonD = Button(self.ActionFrame, image=self.imageD, text="A",
						command=partial(self.HandleCycles,self.ActionCycleD)).grid(row=2,column=1,sticky=W+E+N+S)
					self.imageE = self.GenButtonImage(self.IconE)
					self.ButtonE = Button(self.ActionFrame, image=self.imageE, text="A",
						command=partial(self.HandleCycles,self.ActionCycleE)).grid(row=3,column=0,sticky=W+E+N+S)
					self.imageF = self.GenButtonImage(self.IconF)
					self.ButtonF = Button(self.ActionFrame, image=self.imageF, text="A",
						command=partial(self.HandleCycles,self.ActionCycleF)).grid(row=3,column=1,sticky=W+E+N+S)
					self.imageG = self.GenButtonImage(self.IconG)
					self.ButtonG = Button(self.ActionFrame, image=self.imageG, text="A",
						command=partial(self.HandleCycles,self.ActionCycleG)).grid(row=4,column=0,sticky=W+E+N+S)
					self.imageH = self.GenButtonImage(self.IconH)
					self.ButtonH = Button(self.ActionFrame, image=self.imageH, text="A",
						command=partial(self.HandleCycles,self.ActionCycleH)).grid(row=4,column=1,sticky=W+E+N+S)
					self.imageI = self.GenButtonImage(self.IconI)
					self.ButtonI = Button(self.ActionFrame, image=self.imageI, text="A",
						command=partial(self.HandleCycles,self.ActionCycleI)).grid(row=5,column=0,sticky=W+E+N+S)
					self.imageJ = self.GenButtonImage(self.IconJ)
					self.ButtonJ = Button(self.ActionFrame, image=self.imageJ, text="A",
						command=partial(self.HandleCycles,self.ActionCycleJ)).grid(row=5,column=1,sticky=W+E+N+S)
				except Exception as e:
					pass
					
		# ####################### #
		# MORE MOVING GRIP ACTION #
	def StartMoveMM(self, event):
		self.MMy = event.y
	def StopMoveMM(self, event):
		self.MMy = None
	def MainMenuOnMotion(self, event):
		deltay = event.y - self.MMy
		x = self.master.winfo_x()
		y = self.master.winfo_y() + deltay
		self.master.geometry("+%s+%s" % (x, y))
		
	def StartMoveWS(self, event):
		self.WSx = event.x
		self.WSy = event.y
	def StopMoveWS(self, event):
		self.WSx = None
		self.WSy = None
	def WordSearchOnMotion(self, event):
		deltax = event.x - self.WSx
		deltay = event.y - self.WSy
		x = self.WSFrame.winfo_x() + deltax
		y = self.WSFrame.winfo_y() + deltay
		self.WSFrame.geometry("+%s+%s" % (x, y))
		
	def StartMoveAM(self, event):
		self.AMx = event.x
		self.AMy = event.y
	def StopMoveAM(self, event):
		self.AMx = None
		self.AMy = None
	def ActionMenuOnMotion(self, event):
		deltax = event.x - self.AMx
		deltay = event.y - self.AMy
		x = self.ActionMenu.winfo_x() + deltax
		y = self.ActionMenu.winfo_y() + deltay
		self.ActionMenu.geometry("+%s+%s" % (x, y))
		# ####################### #
		
	def establish_rules(self):
		try:
			if self.rules_okay == False and self.s_playing.get() == 1:
				self.topwindow_isopen = False
				try:
					self.rwdicon, self.rewardlist, self.rewardcycle = self.GenButtonLines(self.s_rulename.get()+' Rewards.txt')
					self.punicon, self.punishlist, self.punishcycle = self.GenButtonLines(self.s_rulename.get()+' Punishments.txt')	
					self.RwdBtn.config(command=partial(self.HandleCycles,self.rewardcycle))
					self.PnshBtn.config(command=partial(self.HandleCycles,self.punishcycle))
				except IndexError:
					pass
				iterlist = []
				iterlist.append(self.rewardlist)
				iterlist.append(self.punishlist)
				try:
					FirstIconFound = False
					self.IconA, self.ActionListA, self.ActionCycleA = self.GenButtonLines(self.s_rulename.get()+' ButtonA.txt')
					FirstIconFound = True
					iterlist.append(self.ActionListA)
					self.IconB, self.ActionListB, self.ActionCycleB = self.GenButtonLines(self.s_rulename.get()+' ButtonB.txt')
					iterlist.append(self.ActionListB)
					self.IconC, self.ActionListC, self.ActionCycleC = self.GenButtonLines(self.s_rulename.get()+' ButtonC.txt')
					iterlist.append(self.ActionListC)
					self.IconD, self.ActionListD, self.ActionCycleD = self.GenButtonLines(self.s_rulename.get()+' ButtonD.txt')
					iterlist.append(self.ActionListD)
					self.IconE, self.ActionListE, self.ActionCycleE = self.GenButtonLines(self.s_rulename.get()+' ButtonE.txt')
					iterlist.append(self.ActionListE)
					self.IconF, self.ActionListF, self.ActionCycleF = self.GenButtonLines(self.s_rulename.get()+' ButtonF.txt')
					iterlist.append(self.ActionListF)
					self.IconG, self.ActionListG, self.ActionCycleG = self.GenButtonLines(self.s_rulename.get()+' ButtonG.txt')
					iterlist.append(self.ActionListG)
					self.IconH, self.ActionListH, self.ActionCycleH = self.GenButtonLines(self.s_rulename.get()+' ButtonH.txt')
					iterlist.append(self.ActionListH)
					self.IconI, self.ActionListI, self.ActionCycleI = self.GenButtonLines(self.s_rulename.get()+' ButtonI.txt')
					iterlist.append(self.ActionListI)
					self.IconJ, self.ActionListJ, self.ActionCycleJ = self.GenButtonLines(self.s_rulename.get()+' ButtonJ.txt')
					iterlist.append(self.ActionListJ)
				except FileNotFoundError as e:
					if FirstIconFound == False:
						self.DestroyActions()
				except Exception as e:
					print(e)
				for list in iterlist:
					for line in list:
						self.CheckForPictue(line)
				self.rules_okay = True
				self.setup_menu_actions()
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'establish_rules', subj='')
			
	def CheckForPictue(self,line):
		if '$picture' in line:
			if not self.usersecure == '1':
				if self.topwindow_isopen == False:
					self.topwindow_isopen = True
					self.popup_bonus()

	def popup_bonus(self):
		try:
			self.win = Toplevel()
			self.win.wm_title("Email Picture Enabler")
			width, height = 900,100
			x = (self.screenwidth  / 2) - (width  / 2)
			y = (self.screenheight / 2) - (height / 2)
			self.win.geometry('%dx%d+%d+%d' % (width, height, x, y))
			bg = Label(self.win, bg='gray75', width=500, height=50)
			bg.pack(fill=X, expand=YES)
			msg = Label(bg, width=20, font=('Times', 12),
					text='To use the $picture function, enable less secure access in the following link. See README.txt for more')
			msg.pack(fill=X, expand=YES)
			w = Text(bg, height=1, width=21, borderwidth=0, font=('Times', 14))
			w.insert(1.0, 'https://myaccount.google.com/lesssecureapps')
			w.pack(fill=X, expand=YES)
			w.configure(state="disabled")
			b = Button(self.win, text="I've done it, please dont show this again.", command=self.record_secure)
			b.pack()
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'popup_bonus', subj='')

	def record_secure(self):
		with open('Resources\\Cam Info.txt', 'w') as f:
			f.write('')
		with open('Resources\\Cam Info.txt', 'a') as f:
			f.write(self.usermail+'\n')
			f.write(self.userpass+'\n')
			f.write('1')
		self.usersecure = '1'
		self.win.destroy()
			
	def GenButtonLines(self,rulefilename):
		with open('Resources\\Healslut Games\\'+rulefilename, 'r') as f:
			self.templines = f.readlines()
			if '.jpg' in self.templines[0].replace('\n',''):
				icon = self.templines[0].replace('\n','')
				self.templines.remove(self.templines[0])
			else:
				icon = ''
			return icon, self.templines, cycle(self.templines)	

	def GenButtonImage(self, filename):
		tempphoto = Image.open('Resources\\Buttonlabels\\'+filename)
		tempphoto = tempphoto.resize((50, 50), Image.LANCZOS)
		return ImageTk.PhotoImage(tempphoto)

	def do_macro(self,macro):
		macro=macro.replace('\n','')
		print(macro)
		if '$playsound' in macro:
			file = macro.replace('$playsound ','')
			try:
				playsound('Resources\\Audio\\'+file, False)
			except PlaysoundException:
				print(file, 'not found in Resources\\Audio\\')
		if '$playvideo' in macro:
			file = macro.replace('$playvideo ','')
			filename = 'Resources\\Video\\'+ file
			self.p_vid.send(filename)
		if '$text' in macro:
			macro=macro+' '
			text = macro.replace('$text','').upper()
			self.p_txt.send(text)
		if '$+vibe' in macro:
			self.vibe_speed += int(macro.replace('$+vibe',''))
		if '$-vibe' in macro:
			self.vibe_speed -= int(macro.replace('$-vibe',''))
		if '$+rotate' in macro:
			self.rotr_speed += int(macro.replace('$+rotate',''))
		if '$-rotate' in macro:
			self.rotr_speed -= int(macro.replace('$-rotate',''))
		if '$+air' in macro:
			self.air_speed += int(macro.replace('$+air',''))
		if '$-air' in macro:
			self.air_speed -= int(macro.replace('$-air',''))
		if '$pinup' in macro:
			pin = 'Resources\\Images\\'+macro.replace('$pinup ','')+'\\'
			self.p_pinup.send(pin)
		if '$picture' in macro:
			Thread(target=take_pic, args=(self.usermail, self.userpass, self.ToEmail)).start()
		if '$writeforme' in macro:
			homeworkcount = int(macro.replace('$writeforme',''))
			print(homeworkcount)
			self.p_homework.send(homeworkcount)
		if '$wordsearch' in macro:
			self.Difficulty = macro.replace('$wordsearch ','').upper()
			if self.GameWindowOpen == True:
				self.GameWindowOpen = False
				try:
					self.WSFrame.destroy()
				except AttributeError:
					pass
			else:
				self.GameWindowOpen = True
				self.WordSearchFrame()
		if '$diceroll' in macro:
			Dice = macro.replace('$diceroll','').upper()
			text,sep,tail = Dice.partition(' ')
			count,sep,die = tail.partition('D')
			for i in range(int(count)):
				x=i+1
				text = text+' '+str(self.Alphabet[-x])+':'+str(randint(1,int(die)))
			self.p_txt.send(text)

	def WordSearchFrame(self):
		while True:
			try:
				width, height = 800,738
				WordList = GenWordSearchList(self.Difficulty)
				grid,SavedCords = WordSearch.Main(WordList,self.Difficulty)
				self.WSFrame = Toplevel(self, bg=TRANS_CLR, highlightthickness=0)
				self.WSFrame.wm_title("Word Search")
				self.WSFrame.overrideredirect(True)
				self.WSFrame.wm_attributes("-topmost", 1)
				self.WSFrame.wm_attributes("-transparentcolor", TRANS_CLR)
				x = (self.screenwidth  / 2) - (width  / 2)
				y = (self.screenheight / 2) - (height / 2)
				self.WSFrame.geometry('%dx%d+%d+%d' % (width, height, x, y))
				
				# ########### #
				# MOVING GRIP #
				self.grip = Label(self.WSFrame, height=1, bg='Gray50', text="< Hold to Move >", font=('Times', 8))
				self.grip.pack(fill=X)
				self.grip.bind("<ButtonPress-1>", self.StartMoveWS)
				self.grip.bind("<ButtonRelease-1>", self.StopMoveWS)
				self.grip.bind("<B1-Motion>", self.WordSearchOnMotion)
				# ########### #
				
				FontColor = 'pink'
				self.WSFrame.bg = Canvas(self.WSFrame, bg='light blue', width=300, height=height*2)
				self.WSFrame.bg.pack(fill=X)
				WordListStr1 = '\n\n\n'
				WordListStr2 = ''
				img = 'Resources/ButtonLabels/Misc/WordSearchBackgroundDark.png'
				image = Image.open(img)
				self.WordSearchImg = ImageTk.PhotoImage(image)
				self.WordSearchBackground = self.WSFrame.bg.create_image(width/2, height/2, image=self.WordSearchImg)
				
				for word in WordList[0:int(len(WordList)*.5)]:
					WordListStr1 += word+'\n'
				for word in WordList[int(len(WordList)*.5):-1]:
					WordListStr2 += word+'\n'
				WordListStr2+='\n\n\n'
				self.WSFrame.bg.create_text((5,height/2), font=('Impact', 14),
					text=WordListStr1, fill=FontColor, justify=LEFT, anchor=W)
				self.WSFrame.bg.create_text((width-5,height/2), font=('Impact', 14),
					text=WordListStr2, fill=FontColor, justify=RIGHT, anchor=E)
				self.WordSearchBG = self.WSFrame.bg.create_text((width/2,height/2), fill='#FF7FED', font=("Courier", 16, "bold"),
					text="\n".join(map(lambda row: " ".join(row), grid)))
				self.WordSearchGrid=grid
				self.WordSearchSavedCords=SavedCords
				self.WordList=WordList
				break
				
			except KeyboardInterrupt:
				pass
			except Exception as e:
				tb = format_exc(2);handleError(tb, e, 'WordSearchFrame', subj='')
		self.after(15000, self.ScrambleGrid)
		
	def ScrambleGrid(self):
		grid=self.WordSearchGrid
		SavedCords=self.WordSearchSavedCords
		if self.GameWindowOpen == True:
			width, height = WordSearch.GenDimensions(self.WordList,self.Difficulty)
			grid = WordSearch.GenBlankGrid(self.Difficulty,width,height,SavedCords)
			self.WSFrame.bg.itemconfig(self.WordSearchBG, text="\n".join(map(lambda row: " ".join(row), grid)))
			self.after(30000, self.ScrambleGrid)

	def HandleCycles(self,mycycle):
		try:
			if self.s_playing.get() == 1:
				cyc = next(mycycle)
				line = str(cyc).split(',')
				for macro in line:
					self.do_macro(macro)
		except KeyboardInterrupt:
			pass
		except Exception as e:
			try:
				tb = format_exc(2);handleError(tb, e, 'HandleCycles', subj=[k for k,v in locals().items() if v == mycycle][0])
			except Exception as e:
				tb = format_exc(2);handleError(tb, e, 'DumbCyclesString', subj='Failed to iterate locals')

	def DestroyActions(self):	#self.DestroyActions()
		self.ActionMenuOpen = False
		self.GameWindowOpen = False
		try:
			self.ActionMenu.destroy()
		except AttributeError:
			pass
		try:
			self.WSFrame.destroy()
		except AttributeError:
			pass
		try:
			self.top.destroy()
		except AttributeError:
			pass
	
	
	
	

class StartHypnoProcess(Process):
	def __init__(self, delay,opacity,game,
						homework,wordcount,hypno,dom,sub,pinup,banwords,tranbanr,
						globfile,s_rulename,fontsize,display_rules,loopingAudio,gifset,
						c_rules,c_vid,c_txt,c_pinup,c_homework,c_hypno):
		try:
			self.delay = delay
			self.opacity = opacity
			self.game = game
			self.homework = homework
			self.wordcount = wordcount
			self.hypno = hypno
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
			self.gifset = gifset
			self.c_rules = c_rules
			self.c_vid = c_vid
			self.c_txt = c_txt
			self.c_pinup = c_pinup
			self.c_homework = c_homework
			self.c_hypno = c_hypno	

			Process.__init__(self)
			self.start()
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'StartHypnoProcess.init', subj='')
			
	def run(self):
		try:
			HypnoTherapy.launch(self.delay,self.opacity,self.game,
				self.homework,self.wordcount,self.hypno,self.dom,self.sub,self.pinup,self.banwords,self.tranbanr,
				self.globfile,self.s_rulename,self.fontsize,self.display_rules,self.loopingAudio,self.gifset,
				self.c_rules,self.c_vid,self.c_txt,self.c_pinup,self.c_homework,self.c_hypno)
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'StartHypnoProcess.run', subj='')


# ##################################
## ##################################
# ##################################
## ##################################

def convertimage(folder, DelOld, screenwidth, screenheight):
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

def ResizeImg(img,name,screenwidth,screenheight):
	ImgW, ImgH = img.size	
	fract = None
	if ImgW > screenwidth -100:
		fract = (ImgW - 100 - 3000 % screenwidth)/ImgW 
	elif ImgH > screenheight -100:
		fract = (ImgW - 100 - 3000 % screenheight)/ImgH 
	if fract:
		w = int(ImgW*fract)
		h = int(ImgH*fract)
		reimg = img.resize((w,h), Image.ANTIALIAS)
		reimg.save(name+'.png', "PNG")
		return reimg
	return img

def GenWordSearchList(Difficulty):
	if Difficulty=='MEDIUM':	WordCount = 20
	elif Difficulty=='HARD':	WordCount = 28
	else:						WordCount = 12
	with open('Resources/Text/Healslut Adjectives.txt','r') as f:
		alines = f.readlines()
	with open('Resources/Text/Healslut Subjects.txt','r') as f:
		blines = f.readlines()
	totallines = alines+blines
	WordList = []
	for i in range(0,WordCount):
		while True:
			word = choice(totallines).replace('\n','').replace('-','').replace(' ','').upper()
			if not word == '' and not word in WordList and not len(word) > 9:
				WordList.append(word)
				break
	return WordList


def take_pic(usermail, userpass, ToEmail):
	try:
		cam = VideoCapture(0)
		s, img = cam.read()
		if s:
			imwrite("Resources\Healslut.jpg",img)
			send_email(usermail, userpass, ToEmail)
			remove("Resources\Healslut.jpg")
		else:
			print('No Video Found')
	except KeyboardInterrupt:
		pass
	except Exception as e:
		tb = format_exc(2);handleError(tb, e, 'take_pic', subj='')
	
		
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
	except KeyboardInterrupt:
		pass
	except Exception as e:
		tb = format_exc(2);handleError(tb, e, 'send_email', subj='')
			
def do_request(url,delay=0):
	sleep(delay)
	try:
		r = get(url)
	except exceptions.ConnectionError:
		pass
	except KeyboardInterrupt:
		pass
	except Exception as e:
		tb = format_exc(2);handleError(tb, e, 'do_request', subj='')
	
def center_window(root, width, height):
	screenwidth = root.winfo_screenwidth()
	screenheight = root.winfo_screenheight()
	x = screenwidth - width
	y = (screenheight / 2) - (height / 2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	
def GenFolders():
	foundimage=False
	hyp_folders = []
	for filename in iglob('Resources\\Images/*.png', recursive=True):
		hyp_folders.append('Resources\\Images\\')
		foundimage=True
	for filename in iglob('Resources\\Images/*/', recursive=True):
		hyp_folders.append(filename)
		foundimage=True
	if foundimage==False:
		hyp_folders.append('No .png files found')
	hyp_folders.append('All')
	return hyp_folders
	
def genuserinfo():
	try:
		with open('Resources\\Cam Info.txt', 'r') as f:
			userlines = f.readlines()
			
	except FileNotFoundError:
		userlines=['myemail@gmail.com','mypassword','0']
	return userlines	
	
def genuserpref():
	try:
		with open('Resources\\Preferences.txt', 'r') as f:
			lines = f.readlines()
			prefdict = {}
			for line in lines:
				line=line.replace('\n','')
				key, sep, value = line.partition(':')
				prefdict[key] = value
	except FileNotFoundError:
		prefdict = {
			'hyp_delay':'500',
			'hyp_game':'None',
			'hyp_opacity':'3',
			'hyp_homework':'Banner',
			'hyp_words':'High',
			'loopingAudio':'None',
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
			'fontsize':'20',
			'hyp_gfile_var':0,
			'background_select_var':0,
			's_rulename':'Verbal',
			'sub':'Mercy',
			'dom':'Roadhog'
			
			
		}
	return prefdict
	
def GenBackgroundList():
	BGPath = 'Resources\\Background Gif original\\'
	mylist = glob(BGPath+'*.gif', recursive=True)
	background_list = []
	for item in mylist:
		background_list.append(item.replace(BGPath,''))
	return background_list
	
def handleError(tb, e, func, subj=''):
	try:
		handlewriter(tb, e, func, subj='')
	except Exception as e:
		handlewriter(tb, e, 'handleError', subj='')

def handlewriter(tb, e, func, subj):
	e=str(e)
	print(func+' Error '+e)
	file = 'Resources\\Errors\\'+func+'.txt'
	with open(file, 'a') as f:
		f.write(tb+'\n'+subj)
		
def VersionCheck():
	print('if you believe this program has frozen, press ctrl + c, then check the Errors folder for details')
	print('Version number:',Version)
	try:
		url = 'https://github.com/ugraveknight/Healslut-Master/releases'
		source = urlopen(url).read()
		soup = BeautifulSoup(source,'lxml')
		for t in soup.html.find_all('ul', attrs={'class':'d-none d-md-block mt-2 list-style-none'}):
			NewestRelease = t.find_next('a').get('title')
			break
		if not NewestRelease == Version:
			print('A new version is available! Visit:', url)
		else:
			print('Your version is up to date')
	except Exception as e:
		print('Error connecting to Github, automatic verison check failed.')
			
def go():
	try:
		VersionCheck()
		hwnd = FindWindow(None, 'HealslutMaster.exe')
		Minimize = GetForegroundWindow()
		ShowWindow(Minimize, SW_MINIMIZE)
		root = Tk()
		center_window(root, 50, 275)
		root.wm_attributes("-topmost", 1)
		
		hyp_folders = GenFolders()
		userinfo = genuserinfo()
		prefdict = genuserpref()
		background_list = GenBackgroundList()
		
		e = HealslutMaster(root, hyp_folders, userinfo, background_list, prefdict)
		print('Healslut Master is now live')
		print()
		root.mainloop()
		
	except KeyboardInterrupt:
		pass
	except Exception as e:
		tb = format_exc(2);handleError(tb, e, 'healslutmaster.go', subj='')
		
if __name__ == '__main__':
	freeze_support()
	go()

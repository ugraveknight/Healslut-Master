from tkinter import *
from tkinter.ttk import Notebook
from win32gui import GetForegroundWindow, ShowWindow
from win32con import SW_MINIMIZE
from PIL import Image, ImageTk
from itertools import cycle
from time import time
from multiprocessing import freeze_support, Process, Pipe
from threading import Thread
from glob import iglob, glob
from playsound import playsound, PlaysoundException
from os import path
from traceback import format_exc
from functools import partial
from pyautogui import screenshot
from random import randint
from sys import exit
from timeit import default_timer as timer

import sys
sys.path.insert(1, 'Libs/')
from TextLibs import GenColorList, ReadTextColors
import HypnoTherapy
import OWVibe
import OWKillfeedMonitor
import LoLKillfeedMonitor
import WordSearch
import SimonSays
import HealslutPackages as HP

URL='http://localhost.lovense.com:20010/'
	
HSDEBUG = False
#HSDEBUG = True


		
    ###########################  Info  ##############################
    #                                                               #
    #                   Created by u/Graveknight1                   #
    #                                                               #
    # Please contact me via reddit for questions or requests.       #
    #                                                               #
    # This program is not for sale, if someone charged you for it,  #
    # you've been ripped off.                                       #
    #                                                               #
    # This code was written for the Healsluts community. If you     #
    # like what you see, check them out at r/healsluts              #
    #                                                               #
    #################################################################
    #               use this line to compile the .exe               #
    #   For me                                                      #
    # pyinstaller -F --icon=ProgDeveloper\hs.ico HealslutMaster.py  #
    #                                                               #
    #   For you                                                     #
    # pyinstaller -F HealslutMaster.py                              #
    #                                                               #
    #################################################################
    #                                                               #
    # https://lovense.com/developer/docs/session-control            #
    # https://lovense.com/developer/docs/lan-connect-pc             #
    #                                                               #
    #################################################################
	
#thanks to Lewd-Zko	(twitter.com/LewdZko) for the image of crystal which was modified 
# and placed on the wordsearch page
#thanks also to everyone else who has shared their time and ideas

				
class HealslutMaster(Frame):
	def __init__(self,master,hyp_folders,background_list,prefdict,
					Insults,Praise,*pargs):
		Frame.__init__(self, master, *pargs)
		try:
			self.master = master
			self.master.overrideredirect(1)
			self.SetupVars(background_list,prefdict,hyp_folders,Insults,Praise)
			self.SetupMenu()
			self.SavePrefDict()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'healslutmaster.init', subj='')
	
	def SetupVars(self,background_list,prefdict,hyp_folders,Insults,Praise):
		try:
			self.p_hypno,		self.c_hypno = Pipe()
			self.p_killfeed,	self.c_killfeed = Pipe()
			self.p_Vibe,		self.c_Vibe = Pipe()
			self.p_vid,			self.c_vid = Pipe()
			self.p_txt,			self.c_txt = Pipe()
			self.p_pinup,		self.c_pinup = Pipe()
			self.p_homework,	self.c_homework = Pipe()
			self.p_wordknt,		self.c_wordknt = Pipe()
			self.p_CharSelect,	self.c_CharSelect = Pipe()
			self.p_bg,			self.c_bg = Pipe()
			self.p_ss,			self.c_ss = Pipe()
			self.p_ssloc,		self.c_ssloc = Pipe()
			
			self.background_list = background_list
			self.background_select = StringVar(self.master)
			if len(background_list) < int(prefdict['background_select_var']):
				prefdict['background_select_var'] = 0
			self.background_select_var = int(prefdict['background_select_var'])
			self.background_select.set(background_list[self.background_select_var])
			
			self.screenwidth = self.master.winfo_screenwidth()
			self.screenheight = self.master.winfo_screenheight()		

			self.hyp_delay = StringVar(self.master)
			self.hyp_game = StringVar(self.master)
			self.hyp_opacity = StringVar(self.master)
			self.hyp_homework = StringVar(self.master)
			self.hyp_words = StringVar(self.master)
			self.loopingAudio = StringVar(self.master)
			self.PlayAudio = IntVar(self.master)
			self.AudioType = StringVar(self.master)
			self.hyp_able = IntVar(self.master)
			self.hyp_pinup = IntVar(self.master)
			self.UseActionMenu = IntVar(self.master)
			self.Freeplay = IntVar(self.master)
			self.hyp_banword = IntVar(self.master)
			self.hyp_tranbanr = IntVar(self.master)
			self.display_rules = IntVar(self.master)
			self.delold = IntVar(self.master)
			self.s_decay = StringVar(self.master)
			self.s_decay_pow = StringVar(self.master)
			self.hyp_dom = StringVar(self.master)
			self.hyp_sub = StringVar(self.master)
			self.FemSex = StringVar(self.master)
			self.ColorList = StringVar(self.master)
			self.fontsize = StringVar(self.master)
			self.HSSub = StringVar(self.master)
			self.HSDom = StringVar(self.master)
			self.UseHSBackground = IntVar(self.master)
			self.convfolder = StringVar(self.master)
			self.s_rulename = StringVar(self.master)
			self.hyp_gfile = StringVar(self.master)
			self.DoVibeLoop = IntVar(self.master)
			self.SizeSettings = IntVar(self.master)
			self.SSOpaque = IntVar(self.master)
			self.AlternateSimon = IntVar(self.master)
			self.textwdith = StringVar()
			self.textheight = StringVar()
			
			print('All Vars intitalized.')
			
			
			self.hyp_delay.set(prefdict['hyp_delay'])
			self.hyp_game.set(prefdict['hyp_game'])
			self.hyp_opacity.set(prefdict['hyp_opacity'])
			self.hyp_homework.set(prefdict['hyp_homework'])
			self.hyp_words.set(prefdict['hyp_words'])
			self.loopingAudio.set(prefdict['loopingAudio'])
			self.PlayAudio.set(prefdict['PlayAudio'])
			self.AudioType.set(prefdict['AudioType'])
			self.hyp_able.set(int(prefdict['hyp_able']))
			self.hyp_pinup.set(int(prefdict['hyp_pinup']))
			self.UseActionMenu.set(int(prefdict['s_playing']))
			self.Freeplay.set(int(prefdict['Freeplay']))
			self.hyp_banword.set(int(prefdict['hyp_banword']))
			self.hyp_tranbanr.set(int(prefdict['hyp_tranbanr']))
			self.display_rules.set(int(prefdict['display_rules']))
			self.delold.set(int(prefdict['delold']))
			self.s_decay.set(prefdict['s_decay'])
			self.s_decay_pow.set(prefdict['s_decay_pow'])
			self.hyp_dom.set(prefdict['hyp_dom'])
			self.hyp_sub.set(prefdict['hyp_sub'])
			self.FemSex.set(prefdict['FemSex'])
			self.ColorList.set(prefdict['ColorList'])
			self.ColorOpts = GenColorList()
			self.fontsize.set(prefdict['fontsize'])
			self.HSSub.set(prefdict['sub'])
			self.HSDom.set(prefdict['dom'])
			self.UseHSBackground.set(prefdict['UseHSBackground'])		
			self.Old_UseHSBackground = int(prefdict['UseHSBackground'])
			self.s_rulename.set(prefdict['s_rulename'])
			self.hyp_gfile_var = int(prefdict['hyp_gfile_var'])
			self.DoVibeLoop.set(prefdict['DoVibeLoop'])
			self.SizeSettings.set(prefdict['SizeSettings'])
			self.SSOpaque.set(prefdict['SSOpaque'])
			self.AlternateSimon.set(prefdict['AlternateSimon'])
			
			if self.UseHSBackground.get() == 1:
				HP.HandleOSBackground(1)
			self.Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
			self.KillFeedPath = path.abspath('Resources\\Killfeed\\%sx%s\\Overwatch'%(self.screenwidth,self.screenheight))+'\\'
			
			self.textwdith.set(self.screenwidth)
			self.textheight.set(self.screenheight)
			self.convfolder.set(' '*30)
			
			
			self.AllCharList = ['No Images']
			self.hyp_folders = hyp_folders
			try:
				self.hyp_gfile.set(hyp_folders[self.hyp_gfile_var])
			except IndexError:
				self.hyp_gfile.set(hyp_folders[0])
			self.conv_hyp_folders = hyp_folders
			
					
			self.OverlayActive = False
			self.Editting = False
			self.ActionMenuOpen = False
			
			self.BaseSpeed = 0
			self.VibeSpeed = 0
			self.RotrSpeed = 0
			self.AirSpeed = 0
			
			self.KillfeedMemory = {}
			
			self.rulesets = []
			Filepath = path.abspath('Resources\\Healslut Games')
			for filename in iglob(Filepath+'\\*\\', recursive=True):
				filename = filename.split(Filepath)[-1].replace('\\','')
				self.rulesets.append(filename)
			self.rewardcycle = []
			self.punishcycle = []
			self.decaytimer=time()
			self.air_decaytimer=time()
			
			self.Insults = Insults
			self.Praise = Praise
		except KeyError as e:
			self.LoadPrefDict(True)
			self.SetupVars(background_list,self.prefdict,hyp_folders,Insults,Praise)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'SetupVars', subj='')
	# # # # # # # # # #
	#    Edit Menu    #
	# # # # # # # # # #	
	def SetupMenu(self):
		def StartMoveMM(event):
			self.MMy = event.y
		def StopMoveMM(event):
			self.MMy = None
		def MainMenuOnMotion(event):
			deltay = event.y - self.MMy
			x = self.master.winfo_x()
			y = self.master.winfo_y() + deltay
			self.master.geometry("+%s+%s" % (x, y))
		# ################################# #
		self.master.wm_attributes("-transparentcolor", HP.TRANS_CLR())
		MainMenuHeight = 270
		self.frame = Frame(self.master, width=50, height=MainMenuHeight+5,
						   borderwidth=0, bg=HP.TRANS_CLR(), relief=RAISED)
		self.frame.grid(row=0,column=0)
		self.bg = Label(self.frame, bg='gray30', width=50, height=MainMenuHeight, anchor=E)
		self.bg.place(x=0,y=20)
		self.bg.grip = Label(self.frame, height=1, bg='Gray50', text="<Move>", font=('Times', 8))
		self.bg.grip.place(x=0,y=0)
		self.bg.grip.bind("<ButtonPress-1>", StartMoveMM)
		self.bg.grip.bind("<ButtonRelease-1>", StopMoveMM)
		self.bg.grip.bind("<B1-Motion>", MainMenuOnMotion)
		self.BtnRwrd = Button(self.bg, bg='green',text="Rwrd",width=5,command=partial(self.HandleCycles,self.rewardcycle))
		self.BtnRwrd.grid(row=1, column=0)
		self.BtnPnsh = Button(self.bg, bg='red', text="Pnsh", width=5,command=partial(self.HandleCycles,self.punishcycle))
		self.BtnPnsh.grid(row=2, column=0)
		self.BtnStopVibe = Button(self.bg,text="Stop\nVibe",width=5,command=HP.StopVibe)
		self.BtnStopVibe.grid(row=3, column=0)
		self.BtnHypno = Button(self.bg,text="Start\nHypno",width=5,command=self.LaunchHypno)
		self.BtnHypno.grid(row=4, column=0)
		self.BtnEdit = Button(self.bg, text="Edit",width=5,command=self.EditHypno)
		self.BtnEdit.grid(row=5, column=0)
		self.BtnQuit = Button(self.bg, text="Quit",width=5,command=self.Shutdown)
		self.BtnQuit.grid(row=6, column=0)
		self.master.config(takefocus=1)
		self.AlwaysOnTop()
		
	def EditHypno(self):
		def UpdateEditMenu():
			try:
				if self.Editting == True:
					if self.gifcanvas:
						self.gifcanvas.itemconfig(self.gifpreview, image=next(self.GifCycle))
					if self.hyp_game.get() == 'OW':
						self.optSub.configure(state=NORMAL)
						self.optDom.configure(state=NORMAL)
						self.chkFP.configure(state=NORMAL)
					else:
						self.optSub.configure(state=DISABLED)
						self.optDom.configure(state=DISABLED)
						self.chkFP.configure(state=DISABLED)
					if self.c_hypno.poll() == False:
						self.p_hypno.send(True)
					self.after(25, UpdateEditMenu)
			except AttributeError as e:
				print('Gif Preview failed.')
				print('Please configure the Width and Height and press Format Gifs ')
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'UpdateEditMenu', subj='')
		def CloseEditMenu():
			try:
				self.Editting = False
				self.EditMenu.destroy()
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'CloseEditMenu', subj='')
		# ###################################################### #
		try:
			if self.OverlayActive == False and self.Editting == False:
				self.Editting = True
				#if self.c_hypno.poll() == True:
				while self.c_hypno.poll() == True:
					self.c_hypno.recv()
					
				self.EditMenu = Toplevel()
				self.EditMenu.title("HypnoTherapy Settings")
				self.EditMenu.overrideredirect(True)
				width, height = 970,440
				x = 1770 - (width  / 2)
				y = 770 - (height / 2) 
				self.EditMenu.geometry('%dx%d+%d+%d'%(width, height, x, y))
				
				self.note = Notebook(self.EditMenu)
				
				self.tab1 = Frame(self.note, width=width-50, height=height-75, borderwidth=0, relief=RAISED)
				self.tab2 = Frame(self.note)
				self.tab3 = Frame(self.note)
				
				self.SetupTab1()
				self.SetupTab2()
				self.SetupTab3()
				
				self.note.add(self.tab1, text = "Background and Pinup")
				self.note.add(self.tab2, text = "Rules and Games")
				self.note.add(self.tab3, text = "Text and Vibrator")
				self.note.place(x=25,y=0)

					# Exit button
				Button(self.EditMenu, text="Dismiss", command=CloseEditMenu).place(x=width-115,y=height-40)
				
				self.after(25, UpdateEditMenu)
			else:
				if self.OverlayActive:
					self.after(25, self.EditHypno)
				self.DestroyActions()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'EditHypno', subj='')
		
	def SetupTab1(self):
		def GenGifCycle(event=None):
			self.gifcyclist = []
			i = self.background_select.get().replace('.gif','').split('\\')[-1]
			Filepath = 'Resources\\Hypno Gif\\'+i+'\\*.gif'
			for myimage in sorted(glob(Filepath, recursive=True)):
				self.gifcyclist.append(ImageTk.PhotoImage(Image.open(myimage).resize((250, 250), Image.LANCZOS)))
			self.GifCycle = cycle(self.gifcyclist)
		def HandleImgConvert():
			print('Converting Images...')
			if self.convfolder.get() == 'All':
				for folder in self.hyp_folders:
					if not folder == 'All':
						HP.ConvertImg(folder,self.delold.get(),
							self.screenwidth,self.screenheight)
			else:
				HP.ConvertImg(self.convfolder.get(),self.delold.get(),
					self.screenwidth,self.screenheight)
			print('Done.')
		def FormatGifs():
			print('Formatting Gifs...')
			mywidth,myheight = int(self.textwdith.get()),int(self.textheight.get())
			Filepath = path.abspath('Resources\\Background Gif Original')
			HP.ExtractFrames(mywidth,myheight,Filepath)
			self.background_list = HP.GenBackgroundList()
			print('Done.')
		# ########################### #
		
			# # # # # # # # # #
			# BG Gif Preview  #
			# # # # # # # # # #
		TextLbl = Canvas(self.tab1, width=285,height=335,highlightthickness=1, highlightbackground="Gray85")
		TextLbl.place(x=15, y=15)
		Label(TextLbl,text='Hypno Background Settings').place(x=25, y=10)
		OptionMenu(TextLbl, self.background_select, *self.background_list,command=GenGifCycle).place(x=15,y=35)
		self.gifcanvas = Canvas(TextLbl, width=250, height=250, bg='gray75')
		self.gifcanvas.place(x=18,y=70)
		GenGifCycle()
		try:
			self.gifpreview = self.gifcanvas.create_image(1,1,image=next(self.GifCycle), anchor=NW)
		except StopIteration:
			Label(self.gifcanvas,width=25,font=('Times',12),text='!Format Gif Before Running',anchor=W,bg='gray75').place(x=0,y=0)
		
			# # # # # # # # # # #
			# Format and Resize #
			# # # # # # # # # # #
		TextLbl = Canvas(self.tab1, width=285,height=335,highlightthickness=1, highlightbackground="Gray85")
		TextLbl.place(x=615, y=15)
		Label(TextLbl,text='Hypno Background Settings').place(x=25, y=10)
		inc = 40
		y = 35
		Label(TextLbl, width=6, font=('Times', 12),text='Width', anchor=W).place(x=65,y=y)
		Entry(TextLbl, width=5, borderwidth=0, font=('Times', 14), textvariable=self.textwdith ).place(x=150,y=y)
		y += inc*.6
		Label(TextLbl, width=6, font=('Times', 12),text='Height',anchor=W).place(x=65,y=y)
		Entry(TextLbl, width=5, borderwidth=0, font=('Times', 14), textvariable=self.textheight).place(x=150,y=y)
		y += inc*.8
		Label(TextLbl,text='Format and Resize \nGifs to Screen Size').place(x=40, y=y)
		Button(TextLbl, text="Format Gifs", command=FormatGifs).place(x=150,y=y)
		y += inc*2
		y += inc
		OptionMenu(TextLbl, self.convfolder, *self.conv_hyp_folders).place(x=45,y=y)
		y += inc
		Checkbutton(TextLbl, text="Delete jpgs", variable=self.delold).place(x=45,y=y)
		y += inc
		Label(TextLbl,text='Format and Resize \nPics to Screen Size').place(x=40, y=y)
		Button(TextLbl, text="Convert jpg to png", command=HandleImgConvert).place(x=150,y=y)
		
			# # # # # # # # # #
			# BG Gif Preview  #
			# # # # # # # # # #
		TextLbl = Canvas(self.tab1, width=285,height=335,highlightthickness=1, highlightbackground="Gray85")
		TextLbl.place(x=315, y=15)
		Label(TextLbl,text='Pinup and Hypno Settings').place(x=25, y=10)
		inc = 40
		y = 35
		Message(TextLbl, text='Overlay Opacity').place(x=45,y=y)
		OptionMenu(TextLbl, self.hyp_opacity, '0', '1', '2', '3', '4').place(x=150,y=y)
		y += inc
		Message(TextLbl, text='Cycle Delay').place(x=45,y=y)
		OptionMenu(TextLbl, self.hyp_delay, '250', '500', '1000', '1500', '3000').place(x=150,y=y)
		y += inc
		Message(TextLbl, text='Image Folder').place(x=45,y=y)
		OptionMenu(TextLbl, self.hyp_gfile, *self.hyp_folders).place(x=150,y=y)
		y += inc
		Radiobutton(TextLbl, text="None", variable=self.hyp_able,value=0).place(x=45,y=y)
		y += inc*.6
		Radiobutton(TextLbl, text="Hypno Background", variable=self.hyp_able,value=1).place(x=45,y=y)
		y += inc*.6
		Radiobutton(TextLbl, text="Turbo Hypno", variable=self.hyp_able,value=2).place(x=45,y=y)
		y += inc*.6
		Checkbutton(TextLbl, text="Enable Pinups", variable=self.hyp_pinup).place(x=45,y=y)
		y += inc*.6
		Checkbutton(TextLbl, text="Healslut Desktop Background", variable=self.UseHSBackground).place(x=800,y=50)
	
	def SetupTab2(self):
		def GenKillfeedList():
			AllCharList = []
			for i in glob(self.KillFeedPath+'*.png'):
				if not 'Assist' in i:
					AllCharList.append(i.replace(self.KillFeedPath,'').replace('.png',''))
			if not AllCharList == []:
				self.AllCharList = AllCharList
		# ############################# #
		
			# # # # # # # # #
			# Game Settings #
			# # # # # # # # #
		TextLbl = Canvas(self.tab2, width=285,height=335,highlightthickness=1, highlightbackground="Gray85")
		TextLbl.place(x=15, y=15)
		Label(TextLbl,text='Rule and Macro Settings').place(x=25, y=10)
		inc = 40
		y = 35
		Message(TextLbl, width=200, text='Rule set').place(x=45,y=y)
		OptionMenu(TextLbl, self.s_rulename, *self.rulesets).place(x=150,y=y)
		y += inc
		Button(TextLbl, text="Load Premade Rules", command=self.LoadPrefDict).place(x=150,y=y)
		y += inc
		Message(TextLbl, width=200, text='Rule Font Size').place(x=45,y=y)
		OptionMenu(TextLbl, self.fontsize, '12', '18', '20', '24', '30').place(x=150,y=y)
		y += inc
		Message(TextLbl, width=200, text='Game',aspect=200).place(x=45,y=y)
		OptionMenu(TextLbl, self.hyp_game, 'None', 'OW', 'LoL').place(x=150,y=y)
		y += inc
		GenKillfeedList()
		Radiobutton(TextLbl, text="No On-screen Rules", variable=self.display_rules,value=0).place(x=45,y=y)
		y += inc*.6
		Radiobutton(TextLbl, text="Transparent Rules",	variable=self.display_rules,value=1).place(x=45,y=y)
		y += inc*.6
		Radiobutton(TextLbl, text="Opaque Rules",		variable=self.display_rules,value=2).place(x=45,y=y)
		y += inc*.6
		Checkbutton(TextLbl, text="Use ActionMenu",		variable=self.UseActionMenu).place(x=45,y=y)
		
			# # # # # # # #
			# OW Settings #
			# # # # # # # #
		TextLbl = Canvas(self.tab2, width=285,height=335,highlightthickness=1, highlightbackground="Gray85")
		TextLbl.place(x=315, y=15)
		Label(TextLbl,text='Overwatch Settings').place(x=25, y=10)
		self.optSub = OptionMenu(TextLbl, self.HSSub, *self.AllCharList)
		self.optDom = OptionMenu(TextLbl, self.HSDom, *self.AllCharList)
		self.chkFP = Checkbutton(TextLbl, text="Freeplay", variable=self.Freeplay)
		y = 35
		Message(TextLbl, width=200, text='Sub Character').place(x=45,y=y)
		self.optSub.place(x=150,y=y)
		y += inc
		Message(TextLbl, width=200, text='Dom Character').place(x=45,y=y)
		self.optDom.place(x=150,y=y)
		y += inc
		self.chkFP.place(x=150,y=y)
		
		
		
		
		TextLbl = Canvas(self.tab2, width=285,height=335,highlightthickness=1, highlightbackground="Gray85")
		TextLbl.place(x=615, y=15)
		Label(TextLbl,text='Simon Says Settings').place(x=25, y=10)
		y = 35
		Checkbutton(TextLbl, text="Smaller", variable=self.SizeSettings).place(x=45,y=y)
		y += inc*.6
		Checkbutton(TextLbl, text="Transparent", variable=self.SSOpaque).place(x=45,y=y)
		y += inc*.6
		Radiobutton(TextLbl, text="Alt-WSAD Scheme", variable=self.display_rules,value=1).place(x=45,y=y)
		y += inc*.6
		Radiobutton(TextLbl, text="Arrowkey Scheme", variable=self.display_rules,value=2).place(x=45,y=y)
		
		'''
		self.SizeSettings
		self.SSOpaque
		self.AlternateSimon
		'''
				
	def SetupTab3(self):
		
			# # # # # # # # #
			# Text Settings #
			# # # # # # # # #
		TextLbl = Canvas(self.tab3, width=285,height=335,highlightthickness=1, highlightbackground="Gray85")
		TextLbl.place(x=15, y=15)
		hdlist = ["None", "Male",  "Female"]
		hslist = ["Sub",  "Boy",   "Girl"  ]
		fslist = ["None", "Bimbo", "Sissy" ]
		hwlist = ["Never", "Seldom", "Not Often", "Often", "Very Often", "Always", "Banner"]
		wdlist = ["None",  "Low",    "Medium",    "High",  "Very High",  "Max",    "Unlimited"]
		inc = 40
		Label(TextLbl,text='Text Settings').place(x=25, y=10)
		y = 35
		Message(TextLbl, width=200, text='Dom Gender'	).place(x=45, y=y)
		y += inc
		Message(TextLbl, width=200, text='Self Gender'	).place(x=45, y=y)
		y += inc
		Message(TextLbl, width=200, text='Feminization'	).place(x=45, y=y)
		y += inc
		Message(TextLbl, width=200, text='Write For Me'	).place(x=45, y=y)
		y += inc
		Message(TextLbl, width=200, text='Word Count'	).place(x=45, y=y)
		y += inc
		Message(TextLbl, width=200, text='Text Color'	).place(x=45, y=y)
		y = 35
		OptionMenu(TextLbl, self.hyp_dom,      *hdlist).place(x=150,y=y)
		y += inc
		OptionMenu(TextLbl, self.hyp_sub,      *hslist).place(x=150,y=y)
		y += inc
		OptionMenu(TextLbl, self.FemSex,       *fslist).place(x=150,y=y)
		y += inc
		OptionMenu(TextLbl, self.hyp_homework, *hwlist).place(x=150,y=y)
		y += inc
		OptionMenu(TextLbl, self.hyp_words,    *wdlist).place(x=150,y=y)
		y += inc
		OptionMenu(TextLbl, self.ColorList, *self.ColorOpts).place(x=150,y=y)
		y += inc
		Checkbutton(TextLbl, text="Transparent Banner", variable=self.hyp_tranbanr).place(x=45,y=y)
		y += inc*.6
		Checkbutton(TextLbl, text="Transparent Words",  variable=self.hyp_banword ).place(x=45,y=y)
		
			# # # # # # # # # #
			# Audio Settings  #
			# # # # # # # # # #
		TextLbl = Canvas(self.tab3, width=285,height=335,highlightthickness=1, highlightbackground="Gray85")
		TextLbl.place(x=315, y=15)
		Checkbutton(TextLbl, text="Play Audio", variable=self.PlayAudio).place(x=25,y=10)
		y = 35
		Message(TextLbl, width=200, text='Looping Audio'	).place(x=45, y=y)
		y += inc
		Message(TextLbl, width=200, text='Track Type'		).place(x=45, y=y)
		y = 35
		OptionMenu(TextLbl, self.loopingAudio, "List", "Shuffle").place(x=150,y=y)
		y += inc
		OptionMenu(TextLbl, self.AudioType, "Either", "Music", "Spoken").place(x=150,y=y)
		
			# # # # # # # # # # #
			# Vibrator Settings #
			# # # # # # # # # # #
		TextLbl = Canvas(self.tab3, width=285,height=335,highlightthickness=1, highlightbackground="Gray85")
		TextLbl.place(x=615, y=15)
		Checkbutton(TextLbl, text="Vibrator Interface", variable=self.DoVibeLoop).place(x=25,y=10)
		y = 35
		Message(TextLbl, width=200, text='Speed Decay Timer'	).place(x=45,y=y)
		y += inc
		Message(TextLbl, width=200, text='Speed Decay Strengh').place(x=45,y=y)
		y = 35
		OptionMenu(TextLbl, self.s_decay, '0', '3', '10', '30', '45', '60', '75', '90').place(x=175,y=y)
		y += inc
		OptionMenu(TextLbl, self.s_decay_pow, '0', '-1', '-3', '-10', '-20', '3/4', '1/2', '1/4').place(x=175,y=y)
		
	# # # # # # # # # #
	#  Launch Hypno   #
	# # # # # # # # # #	
	def LaunchHypno(self):
		try:
			if self.Editting == True:
				self.DestroyActions()
			if self.OverlayActive == False:
				self.BtnHypno.config(text='End\nHypno')
				self.OverlayActive = True
				self.RulesOkay = False
				while self.c_hypno.poll() == True:
					self.c_hypno.recv()
					
				delay = int(self.hyp_delay.get())
				opacity = int(self.hyp_opacity.get())
				game = str(self.hyp_game.get())
				homework = str(self.hyp_homework.get())
				hypno = self.hyp_able.get()
				wordcount = str(self.hyp_words.get())
				if   wordcount == 'None': 		wordcount = 0
				elif wordcount == 'Low': 		wordcount = 1
				elif wordcount == 'Medium': 	wordcount = 2
				elif wordcount == 'High': 		wordcount = 3
				elif wordcount == 'Very High': 	wordcount = 4
				elif wordcount == 'Max': 		wordcount = 5
				elif wordcount == 'Unlimited': 	wordcount = 6
				self.wordcountInt = wordcount
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
				if   loopingAudio == 'None':	loopingAudio = 0
				elif loopingAudio == 'List':	loopingAudio = 1
				elif loopingAudio == 'Shuffle':	loopingAudio = 2
				if self.PlayAudio.get() == 0:
					loopingAudio = 0
				AudioType = self.AudioType.get()
				gifset = self.background_select.get().replace('.gif','')
				FemSex = str(self.FemSex.get())
				ColorList = ReadTextColors(self.ColorList.get())
				
				HypnoTherapy.StartHypnoProcess(delay,opacity,game,
							homework,wordcount,hypno,dom,sub,pinup,banwords,tranbanr,
							globfile,s_rulename,fontsize,display_rules,loopingAudio,AudioType,
							gifset,FemSex,ColorList,self.c_vid,self.c_txt,self.c_pinup,self.c_homework,
							self.c_wordknt,self.c_CharSelect,self.c_hypno,self.p_bg,self.c_bg,
							self.p_homework)
				self.EstablishRules()
				self.LaunchVibe()
			else:
				self.DestroyActions()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'LaunchHypno', subj='')

	# # # # # # # # # #
	# Exit & Closure  #
	# # # # # # # # # #	
	def DestroyActions(self):
		def pipe_full(conn):
			r, w, x = select.select([], [conn], [], 0.0)
			return 0 == len(w)
		# ##################### #
		if self.Editting or self.OverlayActive:
			self.Editting = False
			self.ActionMenuOpen = False
			self.OverlayActive = False
			self.BtnHypno.config(text='Start\nHypno')
			self.ClearActionMenu()
			d = \
			{
				'self.p_hypno':self.p_hypno,
				'self.c_hypno':self.c_hypno,
				'self.p_killfeed':self.p_killfeed,
				'self.c_killfeed':self.c_killfeed,
				'self.p_Vibe':self.p_Vibe,
				'self.c_Vibe':self.c_Vibe,
				'self.p_vid':self.p_vid,
				'self.c_vid':self.c_vid,
				'self.p_txt':self.p_txt,
				'self.c_txt':self.c_txt,
				'self.p_pinup':self.p_pinup,
				'self.c_pinup':self.c_pinup,
				'self.p_homework':self.p_homework,
				'self.c_homework':self.c_homework,
				'self.p_wordknt':self.p_wordknt,
				'self.c_wordknt':self.c_wordknt,
				'self.p_CharSelect':self.p_CharSelect,
				'self.c_CharSelect':self.c_CharSelect,
				'self.p_bg':self.p_bg,
				'self.c_bg':self.c_bg,
				'self.p_ss':self.p_ss,
				'self.c_ss':self.c_ss,
				'self.p_ssloc':self.p_ssloc,
				'self.c_ssloc':self.c_ssloc,
				}
			for name, pipe in d.items():
				i = 0
				while pipe.poll():
					pipe.recv()
					i += 1
				print(name, i)
			
			
			if self.c_Vibe.poll() == False:
				self.p_Vibe.send(True)
			if self.c_hypno.poll() == False:
				self.p_hypno.send(True)
			try:
				self.ActionMenu.destroy()
			except AttributeError:
				pass
			try:
				self.WSLibs.Die()
			except AttributeError:
				pass
			try:
				self.SSLibs.Die()
			except (TclError,AttributeError):
				pass
			try:
				self.EditMenu.destroy()
			except AttributeError:
				pass
	
	def LoadPrefDict(self,Main=False):
		try:
			if Main:
				Filepaths = [path.abspath('Resources/Preferences.txt')]
			else:
				Filepaths = glob(path.abspath('Resources/Healslut Games/'+self.s_rulename.get()+'/Preferences.txt'))
			for i in Filepaths:
				prefdict = HP.GenUserPref(i,Main)
				print('resetting vars')
				self.background_select_var = int(prefdict['background_select_var'])
				self.background_select.set(self.background_list[self.background_select_var])
				self.hyp_delay.set(prefdict['hyp_delay'])
				self.hyp_game.set(prefdict['hyp_game'])
				self.hyp_opacity.set(prefdict['hyp_opacity'])
				self.hyp_homework.set(prefdict['hyp_homework'])
				self.hyp_words.set(prefdict['hyp_words'])
				self.loopingAudio.set(prefdict['loopingAudio'])
				self.PlayAudio.set(prefdict['PlayAudio'])
				self.AudioType.set(prefdict['AudioType'])
				self.hyp_able.set(int(prefdict['hyp_able']))
				self.hyp_pinup.set(int(prefdict['hyp_pinup']))
				self.UseActionMenu.set(int(prefdict['s_playing']))
				self.Freeplay.set(int(prefdict['Freeplay']))
				self.hyp_banword.set(int(prefdict['hyp_banword']))
				self.hyp_tranbanr.set(int(prefdict['hyp_tranbanr']))
				self.display_rules.set(int(prefdict['display_rules']))
				self.delold.set(int(prefdict['delold']))
				self.s_decay.set(prefdict['s_decay'])
				self.s_decay_pow.set(prefdict['s_decay_pow'])
				self.hyp_dom.set(prefdict['hyp_dom'])
				self.hyp_sub.set(prefdict['hyp_sub'])
				self.DoVibeLoop.set(prefdict['DoVibeLoop'])
				self.SizeSettings.set(prefdict['SizeSettings'])
				self.SSOpaque.set(prefdict['SSOpaque'])
				self.AlternateSimon.set(prefdict['AlternateSimon'])
				self.FemSex.set(prefdict['FemSex'])
				self.ColorList.set(prefdict['ColorList'])
				self.fontsize.set(prefdict['fontsize'])
				self.HSSub.set(prefdict['sub'])
				self.HSDom.set(prefdict['dom'])
				self.UseHSBackground.set(prefdict['UseHSBackground'])		
				self.Old_UseHSBackground = int(prefdict['UseHSBackground'])
				self.s_rulename.set(prefdict['s_rulename'])
				self.hyp_gfile_var = int(prefdict['hyp_gfile_var'])
				self.prefdict = prefdict
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'LoadPrefDict', subj='')
		
	def SavePrefDict(self):
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
			'PlayAudio:'+str(self.PlayAudio.get()),
			'AudioType:'+str(self.AudioType.get()),
			'hyp_able:'+str(self.hyp_able.get()),
			'hyp_pinup:'+str(self.hyp_pinup.get()),
			's_playing:'+str(self.UseActionMenu.get()),
			'Freeplay:'+str(self.Freeplay.get()),
			'hyp_banword:'+str(self.hyp_banword.get()),
			'hyp_tranbanr:'+str(self.hyp_tranbanr.get()),
			'display_rules:'+str(self.display_rules.get()),
			'delold:'+str(self.delold.get()),
			's_decay:'+str(self.s_decay.get()),
			's_decay_pow:'+str(self.s_decay_pow.get()),
			'hyp_dom:'+str(self.hyp_dom.get()),
			'hyp_sub:'+str(self.hyp_sub.get()),
			'DoVibeLoop:'+str(self.DoVibeLoop.get()),
			'SizeSettings:'+str(self.SizeSettings.get()),
			'SSOpaque:'+str(self.SSOpaque.get()),
			'AlternateSimon:'+str(self.AlternateSimon.get()),
			'hyp_sub:'+str(self.hyp_sub.get()),
			'FemSex:'+str(self.FemSex.get()),
			'ColorList:'+str(self.ColorList.get()),
			'fontsize:'+str(self.fontsize.get()),
			'hyp_gfile_var:'+str(self.hyp_gfile_var),
			'background_select_var:'+str(self.background_select_var),
			's_rulename:'+str(self.s_rulename.get()),
			'sub:'+str(self.HSSub.get()),
			'dom:'+str(self.HSDom.get()),
			'UseHSBackground:'+str(self.UseHSBackground.get())
			]
		Filepath = path.abspath('Resources\\Preferences.txt')
		with open(Filepath, 'w') as f:
			for line in PrefDictList:
				f.write(line+'\n')	
	
	def AlwaysOnTop(self):
		self.master.lift()
		self.after(500,self.AlwaysOnTop)
	
	def Shutdown(self):				
		try:
			self.SavePrefDict()
			if self.Old_UseHSBackground == 1 or self.UseHSBackground.get() == 1:
				HP.HandleOSBackground('Exit')
			self.p_hypno.send(True)
			self.DestroyActions()
			self.master.quit()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'Shutdown', subj='')

# ##################################
## ##################################
# ##################################
	
	# # # # # # # # # #
	#   Launch Vibe   #
	# # # # # # # # # #	
	def LaunchVibe(self):
		try:	
			if HSDEBUG: print('Clearing Vibe Pipe')
			while self.c_Vibe.poll() == True:
				self.c_Vibe.recv()
				
			if self.DoVibeLoop.get():
				if HSDEBUG: 
					print('Launching vibeloop')
					for i in self.KillFeedFiles:
						print('\t'+i)
				self.VibeLoop()
			
			if self.hyp_game.get() in ['OW','LoL']:
				if self.hyp_game.get() == 'OW':
					self.markslist = [0,0,0,0]
					self.Positions = OWVibe.GenPositions(self.screenwidth,self.screenheight)
					self.Cords, self.BorderPixels = OWKillfeedMonitor.GenCords(self)
					if self.Freeplay.get() == True:
						self.KillFeedFiles = glob(self.KillFeedPath+'*.png')
					else:
						self.KillFeedFiles = \
						[
							path.abspath(self.KillFeedPath+self.HSSub.get()+'.png'),  
							path.abspath(self.KillFeedPath+self.HSDom.get()+'.png'),
						]
						AssistPath = path.abspath(self.KillFeedPath+self.HSSub.get()+' Assist.png')
						if path.exists(AssistPath):
							self.KillFeedFiles.append(AssistPath)
				self.KillfeedWarning = True
				self.ScreencapLoop()
			#self.SelectLoop()	#$ character select loop, will be used with banner one day
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'LaunchVibe', subj='')
	
	def ScreencapLoop(self):
		try:
			if not self.c_Vibe.poll():
				
				KillfeedDuartion = 5
				
					# # # # # # #
					# Overwatch #
					# # # # # # #
				if self.hyp_game.get() == 'OW':
					im = screenshot()
					if HSDEBUG: print(' - OW Vibe Loop')
						
						# # # # # # # # #
						# On Fire Meter #
						# # # # # # # # #
					self.markslist, self.BaseSpeed = OWVibe.go(self.Positions,self.markslist,im)
					while self.c_wordknt.poll():
						self.c_wordknt.recv()
					if self.BaseSpeed > 70: 
						self.p_wordknt.send(6)
					else:
						self.p_wordknt.send(self.wordcountInt)
						
						# # # # # # #
						# KillFeed  #
						# # # # # # #
					OWKillfeedMonitor.Main(im,self.KillFeedFiles,
										self.HSSub.get(),self.HSDom.get(),self.Cords,
										self.c_killfeed,self.KillFeedPath,self.BorderPixels)
					while self.p_killfeed.poll() == True:
						Mark,KillFeedItem,Log = self.p_killfeed.recv()
						if not Log in self.KillfeedMemory and round(timer()-Mark, 2) < KillfeedDuartion:
							#print(round(timer()-Mark, 2),'seconds ago',Log)
							if KillFeedItem in self.KillfeedCycleDict:
								self.HandleCycles(self.KillfeedCycleDict[KillFeedItem])
								self.KillfeedMemory[Log] = Mark
							elif self.KillfeedWarning:
								self.KillfeedWarning = False
								print('WARNING. You have selected a game mode that is not properly configured to connect with the killfeed monitor.')
								print(' you can fix this by either adding the necessary files, setting "Game" to "None", or changing your rule set to a folder that has already been configured.')
						else:
							if HSDEBUG: print(Log,'but its too recent to count')
						
						# # # # # # # # # # # # # # # #
						# Clear Expired Killfeed Log  #
						# # # # # # # # # # # # # # # #
					dellist = []
					for Log,Mark in self.KillfeedMemory.items():
						if round(timer()-Mark,2) > KillfeedDuartion:
							dellist.append(Log)
							print('DelList:', dellist)
					for Log in dellist:
						del self.KillfeedMemory[Log]
						
						
					# # # # # # # # # # #
					# League of Legends #
					# # # # # # # # # # #
				if self.hyp_game.get() == 'LoL':
					Filepath = path.abspath('Resources/Killfeed/%sx%s/LOL'%(self.screenwidth,self.screenheight))+'/'
					LoLKillfeedMonitor.SubDeath(Filepath,self.c_killfeed)
					while self.p_killfeed.poll() == True:
						self.HandleCycles(self.KillfeedCycleDict[self.p_killfeed.recv()])
				
				self.after(250, self.ScreencapLoop)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'ScreencapLoop', subj='')

	def VibeLoop(self):
		def CheckDecay():
			self.RotrSpeed = 0 if self.RotrSpeed <= 0 else 100 if self.RotrSpeed >= 100 else self.RotrSpeed
			self.VibeSpeed = 0 if self.VibeSpeed <= 0 else 100 if self.VibeSpeed >= 100 else self.VibeSpeed
			if not self.s_decay == '0' and time() > self.decaytimer:
				sec = int(self.s_decay.get())
				self.decaytimer=time()+sec
					# Thanks Github User this-is-embarrassing!
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
				if self.VibeSpeed > 0 or self.RotrSpeed > 0:
					new_speed = speed_changes.get(self.s_decay_pow.get(), lambda x: x)
					self.VibeSpeed = new_speed(self.VibeSpeed)
					self.RotrSpeed = new_speed(self.RotrSpeed)
				self.RotrSpeed = int(self.RotrSpeed/5)
				self.VibeSpeed = int(self.VibeSpeed/5)
			if not self.s_decay == '0' and time() > self.air_decaytimer:
				self.air_decaytimer=time()+int(self.s_decay.get())*3
				self.AirSpeed -= 1
			self.AirSpeed  = 0 if self.AirSpeed  <  0 else 3   if self.AirSpeed  >  3   else self.AirSpeed
		# ###################################### #
		try:
			if not self.c_Vibe.poll():
				vibespeed = self.BaseSpeed+self.VibeSpeed
				rotrspeed = self.BaseSpeed+self.RotrSpeed
				CheckDecay()
				print('Vibe: %s, Rotate: %s'%(vibespeed,rotrspeed), end="\r")
				
					#This is the area where we will communicate to the buttplug server
				for url in [URL+'Vibrate?v=%s'%(vibespeed),URL+'RotateAntiClockwise?v=%s'%(rotrspeed),URL+'AirAuto?v=%s'%(self.AirSpeed)]:
					if self.OverlayActive and not self.c_Vibe.poll():	#a chance to break midway through
						Thread(target=HP.DoRequest, args=(url,1)).start()	
				if self.OverlayActive:
					self.after(250, self.VibeLoop)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'VibeLoop', subj='')	

# ##################################
## ##################################
# ##################################

	# # # # # # # # # #
	# Button Manager  #
	# # # # # # # # # #	
	def ClearActionMenu(self):
		try:
			del self.IconA
			del self.ActionCycleA
			del self.IconB
			del self.ActionCycleB
			del self.IconC
			del self.ActionCycleC
			del self.IconD
			del self.ActionCycleD
			del self.IconE
			del self.ActionCycleE
			del self.IconF
			del self.ActionCycleF
			del self.IconG
			del self.ActionCycleG
			del self.IconH
			del self.ActionCycleH
			del self.IconI
			del self.ActionCycleI
			del self.IconJ
			del self.ActionCycleJ
		except Exception as e:
			pass
	
	def EstablishRules(self):
		try:
			if self.RulesOkay == False:
				self.ActiveEmailWarning = False
				iterlist = []
				self.ClearActionMenu()
				
				
					# # # # # # # # # # # # # #
					# Main Menu Pnsh and Rwrd #
					# # # # # # # # # # # # # #
				try:
					self.rwdicon, rewardlist, self.rewardcycle = HP.GenButtonLines(self.s_rulename.get()+'/Rewards.txt')
					self.punicon, punishlist, self.punishcycle = HP.GenButtonLines(self.s_rulename.get()+'/Punishments.txt')
					iterlist.append(rewardlist)
					iterlist.append(punishlist)
					self.BtnRwrd.config(command=partial(self.HandleCycles,self.rewardcycle))
					self.BtnPnsh.config(command=partial(self.HandleCycles,self.punishcycle))
				except IndexError:
					pass
				
				
					# # # # # # # # # # #
					# Killfeed Triggers #
					# # # # # # # # # # #
				self.KillfeedCycleDict = {}
				try:
					if self.hyp_game.get() == 'OW':
						_, kfAsstList, self.kfAsstCycle = HP.GenButtonLines(self.s_rulename.get()+'/DeathAssist.txt')
						iterlist.append(kfAsstList)
						self.KillfeedCycleDict['Assist'] = self.kfAsstCycle
						
						_, kfDomsList, self.kfDomsCycle = HP.GenButtonLines(self.s_rulename.get()+'/DeathDom.txt')	
						iterlist.append(kfDomsList)
						self.KillfeedCycleDict['DomDeath'] = self.kfDomsCycle
						
						_, kfKillList, self.kfKillCycle = HP.GenButtonLines(self.s_rulename.get()+'/DeathKill.txt')	
						iterlist.append(kfKillList)
						self.KillfeedCycleDict['Kill'] = self.kfKillCycle
						
						_, kfSubsList, self.kfRezzCycle = HP.GenButtonLines(self.s_rulename.get()+'/DeathKill.txt')	
						iterlist.append(kfSubsList)
						self.KillfeedCycleDict['Ressurect'] = self.kfRezzCycle
						
						_, kfRezzList, self.kfSubsCycle = HP.GenButtonLines(self.s_rulename.get()+'/DeathSub.txt')	
						iterlist.append(kfRezzList)
						self.KillfeedCycleDict['SubDeath'] = self.kfSubsCycle
						
						_, kfTeamList, self.kfTeamCycle = HP.GenButtonLines(self.s_rulename.get()+'/DeathTeam.txt')	
						iterlist.append(kfTeamList)
						self.KillfeedCycleDict['TeamDeath'] = self.kfTeamCycle
						
						_, kfTmKlList, self.kfTmKlCycle = HP.GenButtonLines(self.s_rulename.get()+'/DeathTeamKill.txt')	
						iterlist.append(kfTmKlList)
						self.KillfeedCycleDict['TeamKill'] = self.kfTmKlCycle
					
					elif self.hyp_game.get() == 'LoL':
						_, kfSubsList, self.kfSubsCycle = HP.GenButtonLines(self.s_rulename.get()+'/DeathSub.txt')	
						iterlist.append(kfSubsList)	
						self.KillfeedCycleDict['SubDeath'] = self.kfSubsCycle
				except (IndexError,FileNotFoundError):
					pass
					
				
					# # # # # # # #
					# The Buttons #
					# # # # # # # #
				if self.UseActionMenu.get() == 1:
					try:
						self.IconA, ActionListA, self.ActionCycleA = HP.GenButtonLines(self.s_rulename.get()+'/ButtonA.txt')
						iterlist.append(ActionListA)
						
						self.IconB, ActionListB, self.ActionCycleB = HP.GenButtonLines(self.s_rulename.get()+'/ButtonB.txt')
						iterlist.append(ActionListB)
						
						self.IconC, ActionListC, self.ActionCycleC = HP.GenButtonLines(self.s_rulename.get()+'/ButtonC.txt')
						iterlist.append(ActionListC)
						
						self.IconD, ActionListD, self.ActionCycleD = HP.GenButtonLines(self.s_rulename.get()+'/ButtonD.txt')
						iterlist.append(ActionListD)
						
						self.IconE, ActionListE, self.ActionCycleE = HP.GenButtonLines(self.s_rulename.get()+'/ButtonE.txt')
						iterlist.append(ActionListE)
						
						self.IconF, ActionListF, self.ActionCycleF = HP.GenButtonLines(self.s_rulename.get()+'/ButtonF.txt')
						iterlist.append(ActionListF)
						
						self.IconG, ActionListG, self.ActionCycleG = HP.GenButtonLines(self.s_rulename.get()+'/ButtonG.txt')
						iterlist.append(ActionListG)
						
						self.IconH, ActionListH, self.ActionCycleH = HP.GenButtonLines(self.s_rulename.get()+'/ButtonH.txt')
						iterlist.append(ActionListH)
						
						self.IconI, ActionListI, self.ActionCycleI = HP.GenButtonLines(self.s_rulename.get()+'/ButtonI.txt')
						iterlist.append(ActionListI)
						
						self.IconJ, ActionListJ, self.ActionCycleJ = HP.GenButtonLines(self.s_rulename.get()+'/ButtonJ.txt')
						iterlist.append(ActionListJ)
					except (FileNotFoundError, AttributeError) as e:
						pass
					except Exception as e:
						if HSDEBUG: print('EstablishRules error, this usually isnt a problem', e)
				
					# # # # # # # # # # # # # # # # #
					# Check for any special macros  #
					# # # # # # # # # # # # # # # # #
				
				self.WordSearchInit = False
				self.SimonSaysInit  = False

				for list in iterlist:
					for line in list:
						self.CheckForGames(line)
				self.RulesOkay = True
				self.BuildActionMenu()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'EstablishRules', subj='')

	def CheckForGames(self,line):
		try:
			if '$wordsearch' in line and self.WordSearchInit == False:
				self.WSLibs = WordSearch.WordSearchLibs(self.master,self.screenwidth,self.screenheight)
				self.WordSearchInit = True
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'CheckForGames.WordSearch', subj='')
		try:
			if '$simonsays' in line and self.SimonSaysInit == False:
				x,y = 0,0
				while self.p_ssloc.poll():
					x,y = self.p_ssloc.recv()
				self.SSLibs = SimonSays.SimonSaysLibs(self.master,self.p_ss,self.c_ss,self.c_hypno,self.c_ssloc,
						self.SizeSettings.get(),self.SSOpaque.get(),self.AlternateSimon.get(),x,y)
				self.SimonSaysInit = True
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'CheckForGames.SimonSays', subj='')
			
	def BuildActionMenu(self):
		def StartMoveAM(event):
			self.AMx, self.AMy = event.x, event.y
		def StopMoveAM(event):
			self.AMx,self.AMy = None, None
		def ActionMenuOnMotion(event):
			x = self.ActionMenu.winfo_x() + event.x - self.AMx
			y = self.ActionMenu.winfo_y() + event.y - self.AMy
			self.ActionMenu.geometry("+%s+%s" % (x, y))
		# ##################################### #
		if self.ActionMenuOpen == False and self.UseActionMenu.get() == 1:
			
			if HSDEBUG: print('Building Action Menu')
			Filepath = path.abspath('Resources/Healslut Games/'+self.s_rulename.get()+'/ButtonA.txt')
			if path.isfile(Filepath):
				self.ActionMenuOpen = True
				self.ActionMenu = Toplevel(self, bg=HP.TRANS_CLR(), highlightthickness=0)
				self.ActionMenu.overrideredirect(True)
				self.ActionMenu.wm_attributes("-topmost", 1)
				self.ActionMenu.wm_attributes("-transparentcolor", HP.TRANS_CLR())
				self.ActionFrame = Frame(self.ActionMenu, width=50, height=50, bg=HP.TRANS_CLR(),
								   borderwidth=0, relief=RAISED,)
				self.ActionFrame.grid(row=0,column=0)

					# MOVING GRIP
				self.grip = Label(self.ActionFrame, height=1, bg='Gray50', text="< Hold to Move >", font=('Times', 8))
				self.grip.grid(row=0,column=0,columnspan=2)
				self.grip.bind("<ButtonPress-1>", StartMoveAM)
				self.grip.bind("<ButtonRelease-1>", StopMoveAM)
				self.grip.bind("<B1-Motion>", ActionMenuOnMotion)
				
				x = (self.screenwidth -300)
				y = (self.screenheight *.4)
				self.ActionMenu.geometry('%dx%d+%d+%d' % (115, 310, x, y))
				
				if not self.rwdicon == '':
					self.imageRwd = HP.GenButtonImage(self.rwdicon)
					self.BtnRwrd.config(image=self.imageRwd,bd=0,highlightthickness=0)
				if not self.punicon == '':
					self.imagePun = HP.GenButtonImage(self.punicon)
					self.BtnRwrd.config(image=self.imageRwd,bd=0,highlightthickness=0)
				
				self.BtnRwrd.config(command=partial(self.HandleCycles,self.rewardcycle))
				self.BtnPnsh.config(command=partial(self.HandleCycles,self.punishcycle))
				
				try:
					# # # # # # # #
					# The Buttons #
					# # # # # # # #
					self.imageA = HP.GenButtonImage(self.IconA)
					Button(self.ActionFrame, image=self.imageA, text="A",
							command=partial(self.HandleCycles,self.ActionCycleA)
							).grid(row=1,column=0,sticky=W+E+N+S)
					
					self.imageB = HP.GenButtonImage(self.IconB)
					Button(self.ActionFrame, image=self.imageB, text="B",
							command=partial(self.HandleCycles,self.ActionCycleB)
							).grid(row=1,column=1,sticky=W+E+N+S)
					
					self.imageC = HP.GenButtonImage(self.IconC)
					Button(self.ActionFrame, image=self.imageC, text="C",
							command=partial(self.HandleCycles,self.ActionCycleC)
							).grid(row=2,column=0,sticky=W+E+N+S)
					
					self.imageD = HP.GenButtonImage(self.IconD)
					Button(self.ActionFrame, image=self.imageD, text="D",
							command=partial(self.HandleCycles,self.ActionCycleD)
							).grid(row=2,column=1,sticky=W+E+N+S)
					
					self.imageE = HP.GenButtonImage(self.IconE)
					Button(self.ActionFrame, image=self.imageE, text="E",
							command=partial(self.HandleCycles,self.ActionCycleE)
							).grid(row=3,column=0,sticky=W+E+N+S)
					
					self.imageF = HP.GenButtonImage(self.IconF)
					Button(self.ActionFrame, image=self.imageF, text="F",
							command=partial(self.HandleCycles,self.ActionCycleF)
							).grid(row=3,column=1,sticky=W+E+N+S)
					
					self.imageG = HP.GenButtonImage(self.IconG)
					Button(self.ActionFrame, image=self.imageG, text="G",
							command=partial(self.HandleCycles,self.ActionCycleG)
							).grid(row=4,column=0,sticky=W+E+N+S)
					
					self.imageH = HP.GenButtonImage(self.IconH)
					Button(self.ActionFrame, image=self.imageH, text="H",
							command=partial(self.HandleCycles,self.ActionCycleH)
							).grid(row=4,column=1,sticky=W+E+N+S)
					
					self.imageI = HP.GenButtonImage(self.IconI)
					Button(self.ActionFrame, image=self.imageI, text="I",
							command=partial(self.HandleCycles,self.ActionCycleI)
							).grid(row=5,column=0,sticky=W+E+N+S)
					
					self.imageJ = HP.GenButtonImage(self.IconJ)
					Button(self.ActionFrame, image=self.imageJ, text="J",
							command=partial(self.HandleCycles,self.ActionCycleJ)
							).grid(row=5,column=1,sticky=W+E+N+S)
				except Exception as e:
					if HSDEBUG: print('BuildActionMenu error, this usually isnt a problem', e)
				
	def HandleCycles(self,mycycle):
		try:
			cyc = next(mycycle)
			line = str(cyc).split(',')
			MacroList = line
			for i,Macro in enumerate(line):
				self.DoMacro(Macro.replace('\n',''),MacroList[i+1:])
				if '$wait' in Macro:
					break
		except Exception as e:
			print(e)
			print('Please Start the Hypno before using Rwrd and Pnsh Buttons')
		except Exception as e:
			try:
				HP.HandleError(format_exc(2), e, 'HandleCycles', subj=[k for k,v in locals().items() if v == mycycle][0])
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'DumbCyclesString', subj='Failed to iterate locals')
	
	def MacroWaitHandler(self,MacroList):
		for Macro in MacroList:
			self.DoMacro(Macro.replace('\n',''),MacroList)
	
	def DoMacro(self,Macro,MacroList):
		#p_vid,p_txt,p_pinup,p_homework
		#self.Praise,self.hyp_dom.get(),self.hyp_sub.get(),self.FemSex.get()
		#self.VibeSpeed,self.RotrSpeed,self.AirSpeed
		
		MacroOptions = \
		[
			'$playsound',
			'$playvideo',
			'$text',
			'$RandText',
			'$+vibe',
			'$-vibe',
			'$+rotate',
			'$-rotate',
			'$+air',
			'$-air',
			'$pinup',
			'$writeforme',
			'$wordsearch',
			'$diceroll',
			'$wait',
			'$simonsays',
			'$+curve',
			'$-curve',
		]
		
		try:
			if '$playsound' in Macro:
				file = Macro.replace('$playsound ','')
				try:
					Filepath = path.abspath('Resources\\Audio\\'+file)
					playsound(Filepath, False)
				except PlaysoundException:
					print(file, 'not found in Resources\\Audio\\')
			if '$playvideo' in Macro:
				file = Macro.replace('$playvideo ','')
				Filepath = path.abspath('Resources\\Video\\'+file)
				self.p_vid.send(Filepath)
			if '$text' in Macro:
				Macro=Macro+' '
				text = Macro.replace('$text','').upper()
				self.p_txt.send(text)
			if '$RandText' in Macro:
				text = Macro.replace('$RandText-','').upper()
				if 'INSULT' in text:
					line = HP.SetWrittenLine(self.Insults,self.hyp_dom.get(),self.hyp_sub.get(),self.FemSex.get())
					text = text.replace('INSULT','')+' '+line
				elif 'PRAISE' in text:
					line = HP.SetWrittenLine(self.Praise,self.hyp_dom.get(),self.hyp_sub.get(),self.FemSex.get())
					text = text.replace('PRAISE','')+' '+line
				self.p_txt.send(text)
			if '$+vibe' in Macro:
				self.VibeSpeed += int(Macro.replace('$+vibe',''))
			if '$-vibe' in Macro:
				self.VibeSpeed -= int(Macro.replace('$-vibe',''))
			if '$+rotate' in Macro:
				self.RotrSpeed += int(Macro.replace('$+rotate',''))
			if '$-rotate' in Macro:
				self.RotrSpeed -= int(Macro.replace('$-rotate',''))
			if '$+air' in Macro:
				self.AirSpeed += int(Macro.replace('$+air',''))
			if '$-air' in Macro:
				self.AirSpeed -= int(Macro.replace('$-air',''))
			if '$pinup' in Macro:
				Filepath = Macro.replace('$pinup ','')+'\\'
				self.p_pinup.send(Filepath)
			if '$writeforme' in Macro:
				homeworkcount = int(Macro.replace('$writeforme',''))
				self.p_homework.send(homeworkcount)
			if '$wordsearch' in Macro:
				Difficulty = Macro.replace('$wordsearch ','').upper()
				self.WSLibs.WordSearchFrame(Difficulty)
			if '$diceroll' in Macro:
				Dice = Macro.replace('$diceroll','').upper()
				text,sep,tail = Dice.partition(' ')
				count,sep,die = tail.partition('D')
				for i in range(int(count)):
					text = text+' '+str(self.Alphabet[-i+1])+':'+str(randint(1,int(die)))
				self.p_txt.send(text)
			if '$wait' in Macro:
				Duration = int(Macro.replace('$wait',''))*1000
				self.after(Duration, lambda:self.MacroWaitHandler(MacroList))
			if '$simonsays' in Macro:
				Length = int(Macro.replace('$simonsays','')) 
				x,y = 0,0
				while self.p_ssloc.poll():
					x,y = self.p_ssloc.recv()
				self.SSLibs.NewGame(Length,x,y)
			if '$+curve' in Macro:
				while self.p_homework.poll() == True:
					self.p_homework.recv()
				self.c_homework.send(int(Macro.replace('$+curve ','')))
				print('Sending', int(Macro.replace('$+curve ',''))*-1)
			if '$-curve' in Macro:
				while self.p_homework.poll() == True:
					self.p_homework.recv()
				self.c_homework.send(int(Macro.replace('$-curve ',''))*-1)
				print('Sending', int(Macro.replace('$-curve ',''))*-1)
			#if '$setwords' in Macro:
			if not any(i in Macro for i in MacroOptions):
				print(Macro)
				print('I didnt recognize your macro. An Error log has been created.')
				HP.HandleError(format_exc(2), '', 'DoMacro', subj=Macro)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'DoMacro', subj='')

# ##################################
## ##################################
# ##################################

def go():
	try:
		#HP.VersionCheck()
		#exit()
		ShowWindow(GetForegroundWindow(), SW_MINIMIZE)
		root = Tk()
		root.geometry('%dx%d+%d+%d' % HP.CenterWindow(root, 50, 275))
		root.wm_attributes("-topmost", 1)
		#print(root.eval("tk::pkgconfig get fontsystem"))
		#exit()
		Insults,Praise = HP.GenInsultsNPraise()
		e = HealslutMaster(root,  HP.GenFolders(), 
			HP.GenBackgroundList(), HP.GenUserPref(), Insults, Praise)
		print('Healslut Master is now live \n')
		root.mainloop()
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'healslutmaster.go', subj='')
		
if __name__ == '__main__':
	freeze_support()
	go()
	

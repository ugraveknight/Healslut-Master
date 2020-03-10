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

import HypnoTherapy
import OWVibe
import OWKillfeedMonitor
import LoLKillfeedMonitor
import WordSearch
import HealslutPackages as HP
	
URL='http://localhost.lovense.com:20010/'
	
HSDEBUG = False
		
    ###########################  Info  ##############################
    #                                                               #
    #                   Created by u/Graveknight1                   #
    #                                                               #
    # Please contact me via reddit for questions or requests. if    #
    # you would like to donate to my work, checkout my paypal.      #
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
	
#go to to https://www.reddit.com/r/iateacrayon/wiki/list for images broad range of images
#thanks to Lewd-Zko	(twitter.com/LewdZko) for the image of crystal which was modified and placed on the wordsearch page
#thanks also to Assistant.

				
class HealslutMaster(Frame):
	def __init__(self,master,hyp_folders,userinfo,background_list,prefdict,
					Insults,Praise,*pargs):
		Frame.__init__(self, master, *pargs)
		try:
			self.master = master
			self.master.overrideredirect(1)
			self.SetupVars(background_list,prefdict,hyp_folders,userinfo,Insults,Praise)
			self.SetupMenu()
			self.SavePref()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'healslutmaster.init', subj='')
	
	def SetupVars(self,background_list,prefdict,hyp_folders,userinfo,Insults,Praise):
		self.p_hypno,		self.c_hypno = Pipe()
		self.p_killfeed,	self.c_killfeed = Pipe()
		self.p_Vibe,		self.c_Vibe = Pipe()
		self.p_vid,			self.c_vid = Pipe()
		self.p_txt,			self.c_txt = Pipe()
		self.p_pinup,		self.c_pinup = Pipe()
		self.p_homework,	self.c_homework = Pipe()
		self.p_wordknt,		self.c_wordknt = Pipe()
		self.p_CharSelect,	self.c_CharSelect = Pipe()
		
		self.background_list = background_list
		self.background_select = StringVar(self.master)
		if len(background_list) < int(prefdict['background_select_var']):
			prefdict['background_select_var'] = 0
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
		self.AudioType = StringVar(self.master)
		self.AudioType.set(prefdict['AudioType'])
		self.hyp_able = IntVar(self.master)
		self.hyp_able.set(int(prefdict['hyp_able']))
		self.hyp_pinup = IntVar(self.master)
		self.hyp_pinup.set(int(prefdict['hyp_pinup']))
		self.UseActionMenu = IntVar(self.master)
		self.UseActionMenu.set(int(prefdict['s_playing']))
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
		self.s_decay_pow.set(prefdict['s_decay_pow'])
		self.hyp_dom = StringVar(self.master)
		self.hyp_dom.set(prefdict['hyp_dom'])
		self.hyp_sub = StringVar(self.master)
		self.hyp_sub.set(prefdict['hyp_sub'])
		self.FemSex = StringVar(self.master)
		self.FemSex.set(prefdict['FemSex'])
		self.fontsize = StringVar(self.master)
		self.fontsize.set(prefdict['fontsize'])
		self.HSSub = StringVar(self.master)
		self.HSSub.set(prefdict['sub'])
		self.HSDom = StringVar(self.master)
		self.HSDom.set(prefdict['dom'])
		self.UseHSBackground = IntVar(self.master)
		self.UseHSBackground.set(prefdict['UseHSBackground'])		
		self.Old_UseHSBackground = int(prefdict['UseHSBackground'])
		if self.UseHSBackground.get() == 1:
			HP.HandleOSBackground(1)
		self.Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		self.KillFeedPath = path.abspath('Resources\\Killfeed\\%sx%s\\Overwatch'%(self.screenwidth,self.screenheight))+'\\'
		self.convfolder = StringVar(self.master)
		self.convfolder.set('                                              ')
		self.s_rulename = StringVar(self.master)
		self.s_rulename.set(prefdict['s_rulename'])
		self.hyp_gfile = StringVar(self.master)
		self.hyp_gfile_var = int(prefdict['hyp_gfile_var'])
		self.AllCharList = ['No Images']
		self.hyp_folders = hyp_folders
		try:
			self.hyp_gfile.set(hyp_folders[self.hyp_gfile_var])
		except IndexError:
			self.hyp_gfile.set(hyp_folders[0])
		self.conv_hyp_folders = hyp_folders
		
		self.textwdith = StringVar()
		self.textwdith.set(self.screenwidth)
		self.textheight = StringVar()
		self.textheight.set(self.screenheight)
		
		self.OverlayActive = False
		self.Editting = False
		self.RulesOkay = False
		self.ActionMenuOpen = False
		self.WSActive = False
		self.BaseSpeed = 0
		self.VibeSpeed = 0
		self.RotrSpeed = 0
		self.AirSpeed = 0
		
		self.rulesets = []
		Filepath = path.abspath('Resources\\Healslut Games')
		for filename in iglob(Filepath+'\\*\\', recursive=True):
			filename = filename.split(Filepath)[-1].replace('\\','')
			self.rulesets.append(filename)	
		self.rewardcycle = []
		self.punishcycle = []
		self.decaytimer=time()
		self.air_decaytimer=time()
		
		self.usermail,self.userpass,self.usersecure,self.ToEmail = HP.SetupEmail(userinfo)
		self.Insults = Insults
		self.Praise = Praise

	def LoadPreDict(self):
		Filepath = path.abspath('Resources/Healslut Games/'+self.s_rulename.get()+'/Preferences.txt')
		for i in glob(Filepath):
			self.ResetPrefDict(HP.GenUserPref(i))
	def ResetPrefDict(self,prefdict):
		print('resetting vars')
		self.background_select_var = int(prefdict['background_select_var'])
		self.background_select.set(self.background_list[self.background_select_var])
		self.hyp_delay.set(prefdict['hyp_delay'])
		self.hyp_game.set(prefdict['hyp_game'])
		self.hyp_opacity.set(prefdict['hyp_opacity'])
		self.hyp_homework.set(prefdict['hyp_homework'])
		self.hyp_words.set(prefdict['hyp_words'])
		self.loopingAudio.set(prefdict['loopingAudio'])
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
		self.fontsize.set(prefdict['fontsize'])
		self.HSSub.set(prefdict['sub'])
		self.HSDom.set(prefdict['dom'])
		self.UseHSBackground.set(prefdict['UseHSBackground'])		
		self.Old_UseHSBackground = int(prefdict['UseHSBackground'])
		self.s_rulename.set(prefdict['s_rulename'])
		self.hyp_gfile_var = int(prefdict['hyp_gfile_var'])
	
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
		self.frame = Frame(self.master, width=50, height=1000,#height=270,
						   borderwidth=2, bg=HP.TRANS_CLR(), relief=RAISED)
		self.frame.grid(row=0,column=0)
		self.bg = Label(self.frame, bg='gray30', width=50, height=270, anchor=E)
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
	
	def LaunchVibe(self):
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
		def vibeloop():
			try:
				if not self.c_Vibe.poll():
					if self.hyp_game.get() == 'OW':
						im = screenshot()
						self.markslist, self.BaseSpeed = OWVibe.go(self.Positions,self.markslist,im)
						OWKillfeedMonitor.Main(im,self.KillFeedFiles,
											self.HSSub.get(),self.HSDom.get(),self.Cords,
											self.c_killfeed,self.KillFeedPath,self.BorderPixels)
						if self.p_killfeed.poll() == True:
							self.HandleCycles(self.KillfeedCycleDict[self.p_killfeed.recv()])
					if self.hyp_game.get() == 'LoL':
						Filepath = path.abspath('Resources/Killfeed/%sx%s/LOL'%(self.screenwidth,self.screenheight))+'/'
						LoLKillfeedMonitor.SubDeath(Filepath,self.c_killfeed)
						if self.p_killfeed.poll() == True:
							print('Killfeed event detected!')
							self.HandleCycles(self.KillfeedCycleDict[self.p_killfeed.recv()])
					#if self.hyp_game.get() == 'WoW':
						#Stuff
					vibespeed = self.BaseSpeed+self.VibeSpeed
					rotrspeed = self.BaseSpeed+self.RotrSpeed
					if self.BaseSpeed > 70: self.p_wordknt.send(6)
					else:					self.p_wordknt.send(self.wordcountInt)
					CheckDecay()
					print('Vibe: %s, Rotate: %s'%(vibespeed,rotrspeed), end="\r")
				if not self.c_Vibe.poll():
						#This is the area where we will communicate to the buttplug server
					for url in [URL+'Vibrate?v=%s'%(vibespeed),URL+'RotateAntiClockwise?v=%s'%(rotrspeed),URL+'AirAuto?v=%s'%(self.AirSpeed)]:
						if self.OverlayActive and not self.c_Vibe.poll():	#a chance to break midway through
							Thread(target=HP.DoRequest, args=(url,1)).start()	
					if self.OverlayActive:
						self.after(2500, vibeloop)
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'vibeloop', subj='')	
		def SelectLoop():
			xFound = OWVibe.CheckLoadingScreen(self.p_CharSelect)
			if self.OverlayActive:
				if xFound == True:
					print('Found it')
					self.after(300000, SelectLoop)
				else:
					self.after(500, SelectLoop)
		# ################################# #
		try:	
			if HSDEBUG: print('Clearing Vibe Pipe')
			while self.c_Vibe.poll() == True:
				self.c_Vibe.recv()
			if self.hyp_game.get() == 'OW':
				self.markslist = [0,0,0,0]
				self.Positions = OWVibe.GenPositions()
				self.Cords, self.BorderPixels = OWKillfeedMonitor.GenCords(self)
				if self.Freeplay.get() == True:
					self.KillFeedFiles = glob(self.KillFeedPath+'*.png')
				else:
					self.KillFeedFiles = \
					[
						path.abspath(self.KillFeedPath+self.HSSub.get()+'.png'), 
						path.abspath(self.KillFeedPath+self.HSSub.get()+' Assist.png'), 
						path.abspath(self.KillFeedPath+self.HSDom.get()+'.png')
					]
			if HSDEBUG: print('Launching vibeloop')
			vibeloop()
			#SelectLoop()	#$ character select loop, will be used with banner one day
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'LaunchVibe', subj='')

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
				globfile = path.abspath(self.hyp_gfile.get())
				s_rulename = self.s_rulename.get()
				fontsize = self.fontsize.get()
				display_rules = self.display_rules.get()
				loopingAudio = self.loopingAudio.get()
				if   loopingAudio == 'None':	loopingAudio = 0
				elif loopingAudio == 'List':	loopingAudio = 1
				elif loopingAudio == 'Shuffle':	loopingAudio = 2
				AudioType = self.AudioType.get()
				gifset = self.background_select.get().replace('.gif','')
				FemSex = str(self.FemSex.get())
				
				StartHypnoProcess(delay,opacity,game,
							homework,wordcount,hypno,dom,sub,pinup,banwords,tranbanr,
							globfile,s_rulename,fontsize,display_rules,loopingAudio,AudioType,
							gifset,FemSex,self.c_vid,self.c_txt,self.c_pinup,self.c_homework,
							self.c_wordknt,self.c_CharSelect,self.c_hypno)
				self.EstablishRules()
				self.LaunchVibe()
			else:
				self.DestroyActions()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'LaunchHypno', subj='')
			
	def EstablishRules(self):
		def GenButtonLines(rulefilename):
			Filepath = path.abspath('Resources\\Healslut Games\\'+rulefilename)
			with open(Filepath, 'r') as f:
				self.templines = f.readlines()
				if '.jpg' in self.templines[0].replace('\n',''):
					icon = self.templines[0].replace('\n','')
					self.templines.remove(self.templines[0])
				else:
					icon = ''
				return icon, self.templines, cycle(self.templines)	
		# ###################################### #
		try:
			if self.RulesOkay == False:
				self.ActiveEmailWarning = False
				iterlist = []
				try:
					self.rwdicon, rewardlist, self.rewardcycle = GenButtonLines(self.s_rulename.get()+'/Rewards.txt')
					self.punicon, punishlist, self.punishcycle = GenButtonLines(self.s_rulename.get()+'/Punishments.txt')
					iterlist.append(rewardlist)
					iterlist.append(punishlist)
					self.BtnRwrd.config(command=partial(self.HandleCycles,self.rewardcycle))
					self.BtnPnsh.config(command=partial(self.HandleCycles,self.punishcycle))
				except IndexError:
					pass
				self.KillfeedCycleDict = {}
				try:
					if self.hyp_game.get() == 'OW':
						_, kfAsstList, self.kfAsstCycle = GenButtonLines(self.s_rulename.get()+'/DeathAssist.txt')
						iterlist.append(kfAsstList)
						self.KillfeedCycleDict['Assist'] = self.kfAsstCycle
						_, kfDomsList, self.kfDomsCycle = GenButtonLines(self.s_rulename.get()+'/DeathDom.txt')	
						iterlist.append(kfDomsList)
						self.KillfeedCycleDict['DomDeath'] = self.kfDomsCycle
						_, kfKillList, self.kfKillCycle = GenButtonLines(self.s_rulename.get()+'/DeathKill.txt')	
						iterlist.append(kfKillList)
						self.KillfeedCycleDict['Kill'] = self.kfKillCycle
						_, kfSubsList, self.kfSubsCycle = GenButtonLines(self.s_rulename.get()+'/DeathSub.txt')	
						iterlist.append(kfSubsList)
						self.KillfeedCycleDict['SubDeath'] = self.kfSubsCycle
						_, kfTeamList, self.kfTeamCycle = GenButtonLines(self.s_rulename.get()+'/DeathTeam.txt')	
						iterlist.append(kfTeamList)
						self.KillfeedCycleDict['TeamDeath'] = self.kfTeamCycle
					elif self.hyp_game.get() == 'LoL':
						_, kfSubsList, self.kfSubsCycle = GenButtonLines(self.s_rulename.get()+'/DeathSub.txt')	
						iterlist.append(kfSubsList)	
						self.KillfeedCycleDict['SubDeath'] = self.kfSubsCycle
				except IndexError:
					pass
				except FileNotFoundError:
					pass
				if self.UseActionMenu.get() == 1:
					try:
						FirstIconFound = False
						self.IconA, ActionListA, self.ActionCycleA = GenButtonLines(self.s_rulename.get()+'/ButtonA.txt')
						FirstIconFound = True
						iterlist.append(ActionListA)
						self.IconB, ActionListB, self.ActionCycleB = GenButtonLines(self.s_rulename.get()+'/ButtonB.txt')
						iterlist.append(ActionListB)
						self.IconC, ActionListC, self.ActionCycleC = GenButtonLines(self.s_rulename.get()+'/ButtonC.txt')
						iterlist.append(ActionListC)
						self.IconD, ActionListD, self.ActionCycleD = GenButtonLines(self.s_rulename.get()+'/ButtonD.txt')
						iterlist.append(ActionListD)
						self.IconE, ActionListE, self.ActionCycleE = GenButtonLines(self.s_rulename.get()+'/ButtonE.txt')
						iterlist.append(ActionListE)
						self.IconF, ActionListF, self.ActionCycleF = GenButtonLines(self.s_rulename.get()+'/ButtonF.txt')
						iterlist.append(ActionListF)
						self.IconG, ActionListG, self.ActionCycleG = GenButtonLines(self.s_rulename.get()+'/ButtonG.txt')
						iterlist.append(ActionListG)
						self.IconH, ActionListH, self.ActionCycleH = GenButtonLines(self.s_rulename.get()+'/ButtonH.txt')
						iterlist.append(ActionListH)
						self.IconI, ActionListI, self.ActionCycleI = GenButtonLines(self.s_rulename.get()+'/ButtonI.txt')
						iterlist.append(ActionListI)
						self.IconJ, ActionListJ, self.ActionCycleJ = GenButtonLines(self.s_rulename.get()+'/ButtonJ.txt')
						iterlist.append(ActionListJ)
					except FileNotFoundError as e:
						pass
					except Exception as e:
						print(e)
				for list in iterlist:
					for line in list:
						self.CheckForPictue(line)
				self.RulesOkay = True
				self.BuildActionMenu()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'EstablishRules', subj='')
			
	def EditHypno(self):
		def UpdateEditMenu():
			try:
				if self.Editting == True:
					if self.gifcanvas:
						self.gifcanvas.itemconfig(self.gifpreview, image=next(self.GifCycle))
					if self.hyp_able.get() == 2:
						self.hyp_pinup.set(0)
						self.EnablePinups.configure(state=DISABLED)
					else:
						self.EnablePinups.configure(state=NORMAL)
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
				if self.c_hypno.poll() == True:
					self.c_hypno.recv()
					
				self.EditMenu = Toplevel()
				self.EditMenu.title("HypnoTherapy Settings")
				self.EditMenu.overrideredirect(True)
				width, height = 1200,415
				x = (self.screenwidth  / 2) - (width  / 2)
				y = (self.screenheight / 2) - (height / 2)
				self.EditMenu.geometry('%dx%d+%d+%d'%(width, height, x, y))
				
				self.note = Notebook(self.EditMenu)
				
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

					# Paypal box
				self.bgPaypal = Label(self.EditMenu, bg='gray75')
				self.bgPaypal.place(x=10,y=height-65)
				msg = Label(self.bgPaypal, width=22, text='Play Support on Paypal')
				msg.grid(row=0, column=0, columnspan=2, sticky=E+W)
				w = Text(self.bgPaypal, height=1, width=22, borderwidth=0, font=('Times', 14))
				w.insert(1.0, 'ugraveknight@gmail.com')
				w.grid(row=1, columnspan=2)
				w.configure(state=DISABLED)
				
					# Exit button
				Button(self.EditMenu, text="Dismiss", command=CloseEditMenu).place(x=width-115,y=height-65)
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
			folder = self.convfolder.get()
			if folder == 'All':
				for folder in self.hyp_folders:
					if not folder == 'All':
						HP.ConvertImg(folder,self.delold.get(),
							self.screenwidth,self.screenheight)
			else:
				HP.ConvertImg(folder,self.delold.get(),
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
			# #Handle Gif# #
		self.handlegif = Canvas(self.tab1, bg='gray50',width=250, height=300)
		self.handlegif.place(x=15,y=5)
		OptionMenu(self.handlegif, self.background_select, *self.background_list,command=GenGifCycle).place(x=15,y=7)
		self.gifcanvas = Canvas(self.handlegif, width=250, height=250, bg='gray75')
		self.gifcanvas.place(x=0,y=50)
		GenGifCycle()
		try:
			self.gifpreview = self.gifcanvas.create_image(1,1,image=next(self.GifCycle), anchor=NW)
		except StopIteration:
			Label(self.gifcanvas,width=25,font=('Times',12),text='!Format Gif Before Running',anchor=W,bg='gray75').place(x=0,y=0)
			# #Format gif# #
		self.bggif = Label(self.tab1, bg='gray50',width=300)
		self.bggif.place(x=870,y=240)
		Label(self.bggif, width=6, font=('Times', 12),text='Width', anchor=W).grid(row=0,column=0, pady=2)
		Label(self.bggif, width=6, font=('Times', 12),text='Height', anchor=W).grid(row=1,column=0, pady=2)
		Entry(self.bggif, width=5, borderwidth=0, font=('Times', 14), textvariable=self.textwdith).grid(row=0,column=1)
		Entry(self.bggif, width=5, borderwidth=0, font=('Times', 14), textvariable=self.textheight).grid(row=1,column=1)
		Button(self.bggif, text="Format Gifs", command=FormatGifs).grid(row=1,column=2)
			#  Convert png #
		self.bgConvert = Label(self.tab1, bg='gray50',width=30,height=4)
		self.bgConvert.place(x=500,y=240)
		Button(self.bgConvert, text="Convert jpg to png", command=HandleImgConvert).place(x=1,y=1)
		Checkbutton(self.bgConvert, text="Delete jpgs", variable=self.delold).place(x=138,y=2)
		OptionMenu(self.bgConvert, self.convfolder, *self.conv_hyp_folders).place(x=1,y=35)
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
		self.EnablePinups = Checkbutton(self.tab1, text="Enable Pinups", variable=self.hyp_pinup)
		self.EnablePinups.place(x=300,y=275)	# has to be an object
		Checkbutton(self.tab1, text="Healslut Desktop Background", variable=self.UseHSBackground).place(x=800,y=50)
	
	def SetupTab2(self):
		def GenKillfeedList():
			AllCharList = []
			for i in glob(self.KillFeedPath+'*.png'):
				if not 'Assist' in i:
					AllCharList.append(i.replace(self.KillFeedPath,'').replace('.png',''))
			if not AllCharList == []:
				self.AllCharList = AllCharList
		# ############################# #
		owlvl = 250
		Message(self.tab2, text='Rule set').place(x=25,y=20)
		Message(self.tab2, text='Rule Font Size').place(x=25,y=120)
		Message(self.tab2, text='Game',aspect=200).place(x=25,y=170)
		Button(self.tab2, text="Load Premade Rules", command=self.LoadPreDict).place(x=40,y=70)
		OptionMenu(self.tab2, self.s_rulename, *self.rulesets).place(x=125,y=20)
		OptionMenu(self.tab2, self.fontsize, '12', '18', '20', '24', '30').place(x=125,y=120)
		OptionMenu(self.tab2, self.hyp_game, 'None', 'OW', 'LoL').place(x=125,y=170)
		GenKillfeedList()
		Message(self.tab2, text='Sub Character').place(x=25,y=owlvl)
		Message(self.tab2, text='Dom Character').place(x=300,y=owlvl)
		self.optSub = OptionMenu(self.tab2, self.HSSub, *self.AllCharList)
		self.optDom = OptionMenu(self.tab2, self.HSDom, *self.AllCharList)
		self.chkFP = Checkbutton(self.tab2, text="Freeplay", variable=self.Freeplay)
		self.optSub.place(x=125,y=owlvl)
		self.optDom.place(x=400,y=owlvl)
		self.chkFP.place(x=550,y=owlvl+5)
		Radiobutton(self.tab2, text="No Rules", variable=self.display_rules,value=0).place(x=300,y=75)
		Radiobutton(self.tab2, text="Transparent Rules", variable=self.display_rules,value=1).place(x=300,y=100)
		Radiobutton(self.tab2, text="Opaque Rules", variable=self.display_rules,value=2).place(x=300,y=125)
		Checkbutton(self.tab2, text="Use ActionMenu", variable=self.UseActionMenu).place(x=300,y=150)
				
	def SetupTab3(self):
		Message(self.tab3, text='Dom Gender'			).place(x=25, y=20)
		Message(self.tab3, text='Self Gender'			).place(x=25, y=70)
		Message(self.tab3, text='Sex'					).place(x=25, y=120)
		Message(self.tab3, text='Write For Me'			).place(x=300, y=20)
		Message(self.tab3, text='Word Count'			).place(x=300, y=70)
		Message(self.tab3, text='Looping Audio'			).place(x=575, y=20)
		Message(self.tab3, text='Track Type'			).place(x=575, y=70)
		Message(self.tab3, text='Speed Decay Timer'		).place(x=800,y=20)
		Message(self.tab3, text='Speed Decay Strengh'	).place(x=800,y=70)
		OptionMenu( self.tab3, self.hyp_dom, "None", "Male", "Female").place(x=125,y=20)
		OptionMenu( self.tab3, self.hyp_sub, "Sub", "Boy", "Girl").place(x=125,y=70)
		OptionMenu( self.tab3, self.FemSex, "None", "Bimbo", "Sissy").place(x=125,y=120)
		OptionMenu( self.tab3, self.hyp_homework, "Never", "Not Often", "Often", "Very Often", "Always", "Banner").place(x=400,y=20)
		OptionMenu( self.tab3, self.hyp_words, "None", "Low", "Medium", "High", "Very High", "Max", "Unlimited").place(x=400,y=70)
		OptionMenu( self.tab3, self.loopingAudio, "None", "List", "Shuffle").place(x=675,y=20)
		OptionMenu( self.tab3, self.AudioType, "Either", "Music", "Spoken").place(x=675,y=70)
		OptionMenu( self.tab3, self.s_decay, '0', '3', '10', '30', '45', '60', '75', '90').place(x=900,y=20)
		OptionMenu( self.tab3, self.s_decay_pow, '0', '-1', '-3', '-10', '-20', '3/4', '1/2', '1/4').place(x=900,y=70)
		Checkbutton(self.tab3, text="Transparent Banner", variable=self.hyp_tranbanr).place(x=350,y=150)
		Checkbutton(self.tab3, text="Transparent Words",  variable=self.hyp_banword).place(x=350,y=175)
		
	#########################
	# Begin Buttons Manager #
	#########################
	
	def BuildActionMenu(self):
		def GenButtonImage(filename):
			Filepath = path.abspath('Resources\\Buttonlabels\\'+filename)
			tempphoto = Image.open(Filepath)
			tempphoto = tempphoto.resize((50, 50), Image.LANCZOS)
			return ImageTk.PhotoImage(tempphoto)
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
					self.imageRwd = GenButtonImage(self.rwdicon)
					self.BtnRwrd.config(image=self.imageRwd,bd=0,highlightthickness=0)
				if not self.punicon == '':
					self.imagePun = GenButtonImage(self.punicon)
					self.BtnRwrd.config(image=self.imageRwd,bd=0,highlightthickness=0)
				self.BtnRwrd.config(command=partial(self.HandleCycles,self.rewardcycle))
				self.BtnPnsh.config(command=partial(self.HandleCycles,self.punishcycle))
		
				try:
				
					self.imageA = GenButtonImage(self.IconA)
					self.ButtonA = Button(self.ActionFrame, image=self.imageA, text="A",
						command=partial(self.HandleCycles,self.ActionCycleA)).grid(row=1,column=0,sticky=W+E+N+S)
					self.imageB = GenButtonImage(self.IconB)
					self.ButtonB = Button(self.ActionFrame, image=self.imageB, text="A",
						command=partial(self.HandleCycles,self.ActionCycleB)).grid(row=1,column=1,sticky=W+E+N+S)
					self.imageC = GenButtonImage(self.IconC)
					self.ButtonC = Button(self.ActionFrame, image=self.imageC, text="A",
						command=partial(self.HandleCycles,self.ActionCycleC)).grid(row=2,column=0,sticky=W+E+N+S)
					self.imageD = GenButtonImage(self.IconD)
					self.ButtonD = Button(self.ActionFrame, image=self.imageD, text="A",
						command=partial(self.HandleCycles,self.ActionCycleD)).grid(row=2,column=1,sticky=W+E+N+S)
					self.imageE = GenButtonImage(self.IconE)
					self.ButtonE = Button(self.ActionFrame, image=self.imageE, text="A",
						command=partial(self.HandleCycles,self.ActionCycleE)).grid(row=3,column=0,sticky=W+E+N+S)
					self.imageF = GenButtonImage(self.IconF)
					self.ButtonF = Button(self.ActionFrame, image=self.imageF, text="A",
						command=partial(self.HandleCycles,self.ActionCycleF)).grid(row=3,column=1,sticky=W+E+N+S)
					self.imageG = GenButtonImage(self.IconG)
					self.ButtonG = Button(self.ActionFrame, image=self.imageG, text="A",
						command=partial(self.HandleCycles,self.ActionCycleG)).grid(row=4,column=0,sticky=W+E+N+S)
					self.imageH = GenButtonImage(self.IconH)
					self.ButtonH = Button(self.ActionFrame, image=self.imageH, text="A",
						command=partial(self.HandleCycles,self.ActionCycleH)).grid(row=4,column=1,sticky=W+E+N+S)
					self.imageI = GenButtonImage(self.IconI)
					self.ButtonI = Button(self.ActionFrame, image=self.imageI, text="A",
						command=partial(self.HandleCycles,self.ActionCycleI)).grid(row=5,column=0,sticky=W+E+N+S)
					self.imageJ = GenButtonImage(self.IconJ)
					self.ButtonJ = Button(self.ActionFrame, image=self.imageJ, text="A",
						command=partial(self.HandleCycles,self.ActionCycleJ)).grid(row=5,column=1,sticky=W+E+N+S)
				except Exception as e:
					pass
				
	def CheckForPictue(self,line):
		def ConfigCamInfo():
			Filepath = path.abspath('Resources\\Cam Info.txt')
			with open(Filepath, 'r') as f:
				Lines = f.read().split('\n')
			with open(Filepath, 'w') as f:
				for line in Lines:
					if not line == '0':
						f.write(line+'\n')
					else:
						f.write('1''\n')
			self.usersecure = '1'
			self.win.destroy()
		def EmailWarning():
			try:
				self.win = Toplevel()
				self.win.wm_title("Picture Email Enabler")
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
				w.configure(state=DISABLED)
				Button(self.win, text="I've done it, please dont show this again.", command=ConfigCamInfo).pack()
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'popup_bonus', subj='')
		# ################################### #
		if '$picture' in line:
			if not self.usersecure == '1':
				if self.ActiveEmailWarning == False:
					self.ActiveEmailWarning = True
					EmailWarning()

	def WordSearchFrame(self):
		def ScrambleGrid():
			grid=self.WordSearchGrid
			SavedCords=self.WordSearchSavedCords
			if self.WSActive == True:
				width, height = WordSearch.GenDimensions(self.WordList,self.Difficulty)
				grid = WordSearch.GenBlankGrid(self.Difficulty,width,height,SavedCords)
				self.WSFrame.bg.itemconfig(self.WordSearchBG, text="\n".join(map(lambda row: " ".join(row), grid)))
				self.after(30000, ScrambleGrid)
		def StartMoveWS(event):
			self.WSx, self.WSy = event.x, event.y
		def StopMoveWS(event):
			self.WSx,self.WSy = None, None
		def WordSearchOnMotion(event):
			x = self.WSFrame.winfo_x() + event.x - self.WSx
			y = self.WSFrame.winfo_y() + event.y - self.WSy
			self.WSFrame.geometry("+%s+%s" % (x, y))
		# ####################### #
		while True:
			try:
				width, height = 800,738
				WordList = HP.GenWordSearchList(self.Difficulty)
				grid,SavedCords = WordSearch.Main(WordList,self.Difficulty)
				self.WSFrame = Toplevel(self, bg=HP.TRANS_CLR(), highlightthickness=0)
				self.WSFrame.wm_title("Word Search")
				self.WSFrame.overrideredirect(True)
				self.WSFrame.wm_attributes("-topmost", 1)
				self.WSFrame.wm_attributes("-transparentcolor", HP.TRANS_CLR())
				x = (self.screenwidth  / 2) - (width  / 2)
				y = (self.screenheight / 2) - (height / 2)
				self.WSFrame.geometry('%dx%d+%d+%d' % (width, height, x, y))
				
					# MOVING GRIP 
				self.grip = Label(self.WSFrame, height=1, bg='Gray50', text="< Hold to Move >", font=('Times', 8))
				self.grip.pack(fill=X)
				self.grip.bind("<ButtonPress-1>", StartMoveWS)
				self.grip.bind("<ButtonRelease-1>", StopMoveWS)
				self.grip.bind("<B1-Motion>", WordSearchOnMotion)
				
				FontColor = 'pink'
				self.WSFrame.bg = Canvas(self.WSFrame, bg='light blue', width=300, height=height*2)
				self.WSFrame.bg.pack(fill=X)
				WordListStr1 = '\n\n\n'
				WordListStr2 = ''
				Filepath = path.abspath('Resources/ButtonLabels/Misc/WordSearchBackgroundDark.png')
				image = Image.open(Filepath)
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
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'WordSearchFrame', subj='')
		self.after(15000, ScrambleGrid)

	def HandleCycles(self,mycycle):
		def do_macro(macro):
			if '$playsound' in macro:
				file = macro.replace('$playsound ','')
				try:
					Filepath = path.abspath('Resources\\Audio\\'+file)
					playsound(Filepath, False)
				except PlaysoundException:
					print(file, 'not found in Resources\\Audio\\')
			if '$playvideo' in macro:
				file = macro.replace('$playvideo ','')
				Filepath = path.abspath('Resources\\Video\\'+file)
				self.p_vid.send(Filepath)
			if '$text' in macro:
				macro=macro+' '
				text = macro.replace('$text','').upper()
				self.p_txt.send(text)
			if '$RandText' in macro:
				text = macro.replace('$RandText-','').upper()
				if 'INSULT' in text:
					line = HP.SetWrittenLine(self.Insults,self.hyp_dom.get(),self.hyp_sub.get(),self.FemSex.get())
					text = text.replace('INSULT','')+' '+line
				elif 'PRAISE' in text:
					line = HP.SetWrittenLine(self.Praise,self.hyp_dom.get(),self.hyp_sub.get(),self.FemSex.get())
					text = text.replace('PRAISE','')+' '+line
				self.p_txt.send(text)
			if '$+vibe' in macro:
				self.VibeSpeed += int(macro.replace('$+vibe',''))
			if '$-vibe' in macro:
				self.VibeSpeed -= int(macro.replace('$-vibe',''))
			if '$+rotate' in macro:
				self.RotrSpeed += int(macro.replace('$+rotate',''))
			if '$-rotate' in macro:
				self.RotrSpeed -= int(macro.replace('$-rotate',''))
			if '$+air' in macro:
				self.AirSpeed += int(macro.replace('$+air',''))
			if '$-air' in macro:
				self.AirSpeed -= int(macro.replace('$-air',''))
			if '$pinup' in macro:
				Filepath = path.abspath('Resources\\Images\\'+macro.replace('$pinup ',''))+'\\'
				self.p_pinup.send(Filepath)
			if '$picture' in macro:
				Thread(target=HP.TakePic, args=(self.usermail, self.userpass, self.ToEmail)).start()
			if '$writeforme' in macro:
				homeworkcount = int(macro.replace('$writeforme',''))
				print(homeworkcount)
				self.p_homework.send(homeworkcount)
			if '$wordsearch' in macro:
				self.Difficulty = macro.replace('$wordsearch ','').upper()
				if self.WSActive == True:
					self.WSActive = False
					try:
						self.WSFrame.destroy()
					except AttributeError:
						pass
				else:
					self.WSActive = True
					self.WordSearchFrame()
			if '$diceroll' in macro:
				Dice = macro.replace('$diceroll','').upper()
				text,sep,tail = Dice.partition(' ')
				count,sep,die = tail.partition('D')
				for i in range(int(count)):
					text = text+' '+str(self.Alphabet[-i+1])+':'+str(randint(1,int(die)))
				self.p_txt.send(text)
		# ########################################## #
		try:
			cyc = next(mycycle)
			line = str(cyc).split(',')
			for macro in line:
				do_macro(macro.replace('\n',''))
		except Exception as e:
			try:
				HP.HandleError(format_exc(2), e, 'HandleCycles', subj=[k for k,v in locals().items() if v == mycycle][0])
			except Exception as e:
				HP.HandleError(format_exc(2), e, 'DumbCyclesString', subj='Failed to iterate locals')

	def DestroyActions(self,Exit=False):
		if self.Editting or self.OverlayActive or Exit:
			self.Editting = False
			self.ActionMenuOpen = False
			self.WSActive = False
			self.OverlayActive = False
			self.BtnHypno.config(text='Start\nHypno')
			if self.c_Vibe.poll() == False:
				self.p_Vibe.send(True)
			if self.c_hypno.poll() == False:
				self.p_hypno.send(True)
			try:
				self.ActionMenu.destroy()
			except AttributeError:
				pass
			try:
				self.WSFrame.destroy()
			except AttributeError:
				pass
			try:
				self.EditMenu.destroy()
			except AttributeError:
				pass
				
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
			'FemSex:'+str(self.FemSex.get()),
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
				
	def Shutdown(self):				
		try:
			self.SavePref()
			if self.Old_UseHSBackground == 1 or self.UseHSBackground.get() == 1:
				HP.HandleOSBackground('Exit')
			self.DestroyActions(True)
			self.master.quit()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'Shutdown', subj='')

class StartHypnoProcess(Process):
	def __init__(self, delay,opacity,game,
						homework,wordcount,hypno,dom,sub,pinup,banwords,tranbanr,
						globfile,s_rulename,fontsize,display_rules,loopingAudio,AudioType,
						gifset,FemSex,c_vid,c_txt,c_pinup,c_homework,c_wordknt,c_CharSelect,
						c_hypno):
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
			self.c_vid = c_vid
			self.c_txt = c_txt
			self.c_pinup = c_pinup
			self.c_homework = c_homework
			self.c_wordknt = c_wordknt
			self.c_CharSelect = c_CharSelect
			self.c_hypno = c_hypno	

			Process.__init__(self)
			self.start()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'StartHypnoProcess.init', subj='')
			
	def run(self):
		try:
			print('Launching HypnoTherapy Layer...')
			HypnoTherapy.launch(self.delay,self.opacity,self.game,
				self.homework,self.wordcount,self.OverlayActive,self.dom,self.sub,self.pinup,self.banwords,self.tranbanr,
				self.globfile,self.s_rulename,self.fontsize,self.display_rules,self.loopingAudio,self.AudioType,self.gifset,
				self.FemSex,self.c_vid,self.c_txt,self.c_pinup,self.c_homework,self.c_wordknt,self.c_CharSelect,self.c_hypno)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'StartHypnoProcess.run', subj='')

# ##################################
## ##################################
# ##################################

def go():
	try:
		HP.VersionCheck()
		ShowWindow(GetForegroundWindow(), SW_MINIMIZE)
		root = Tk()
		root.geometry('%dx%d+%d+%d' % HP.CenterWindow(root, 50, 275))
		root.wm_attributes("-topmost", 1)
		Insults,Praise = HP.GenInsultsNPraise()
		e = HealslutMaster(root,  HP.GenFolders(), HP.GenUserInfo(), 
			HP.GenBackgroundList(), HP.GenUserPref(), Insults, Praise)
		print('Healslut Master is now live \n')
		root.mainloop()
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'healslutmaster.go', subj='')


#def PrepChecklist(self):
#	self.Checklist = Toplevel(self.master)

#	self.lbl2 = Label(self.Checklist, text='Healslut Checklist')
#	self.lbl2.place(x=25,y=25)
#	self.lbl3 = Label(self.Checklist, text='\N{check mark}Mercy Skin Set to Imp')
#	self.lbl3.place(x=25,y=50)
#	self.lbl3 = Label(self.Checklist, text='\N{check mark}Mercy Emote Set to Relax')
#	self.lbl3.place(x=25,y=75)
#	self.lbl3 = Label(self.Checklist, text='\N{check mark}Mercy Spray Set to Arrow')
#	self.lbl3.place(x=25,y=100)
#	self.lbl3 = Label(self.Checklist, text='\N{check mark}Melee and Weapon Switch Buttons Unbinded')
#	self.lbl3.place(x=25,y=125)
		
if __name__ == '__main__':
	freeze_support()
	go()
	

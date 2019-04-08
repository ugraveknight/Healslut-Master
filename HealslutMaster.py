Version='v1.3'
if __name__ == '__main__':
	print('if you believe this program has frozen, press ctrl + c, then check the Errors folder for details')
	print('Version number:',Version)

import HypnoTherapy
import OverwatchVibe

from tkinter import *
from win32gui import FindWindow, GetForegroundWindow, ShowWindow, SetWindowLong
from win32con import SW_MINIMIZE
from PIL import Image, ImageTk
from itertools import cycle
from time import time
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




	
	###########################  Info  ##############################
	#																#
	# 					Created by u/Graveknight1					#
	#																#
	# Please contact me via reddit for questions or requests if you	#
	# would like to donate to my work, checkout my paypal.			#										#
	#																#
	# This program is not for sale, if someone charged you for it,  #
	# you've been ripped off.										#
	#																#
	# This code was written for the Healsluts community. If you		#
	# like what you see, check them out at r/healsluts				#										#
	#																#
	#################################################################
	#				use this line to compile the .exe				#
	#																#
	#pyinstaller -f --icon=Developer\hs.ico HealslutMaster.py		#
	#																#
	#																#
	#################################################################
	#																#
	# https://lovense.com/developer/docs/session-control			#
	# https://lovense.com/developer/docs/lan-connect-pc				#
	#																#
	#################################################################
	
#thanks to https://www.reddit.com/r/iateacrayon/wiki/list for the images


class HealslutMaster(Frame):
	def __init__(self, master, hyp_folders, userinfo, background_list, prefdict,
								p_ow, c_ow,	
								p_hypno, c_hypno, 
								p_vid, c_vid, 
								p_txt, c_txt,
								p_rules, c_rules,
								p_homework, c_homework,
								*pargs):
		Frame.__init__(self, master, *pargs)
		try:
			self.master = master
			self.master.overrideredirect(1)
			self.c_hypno, self.p_hypno = c_hypno, p_hypno
			self.c_ow, self.p_ow = c_ow, p_ow
			self.p_vid, self.c_vid = p_vid, c_vid
			self.p_txt, self.c_txt = p_txt, c_txt
			self.p_rules, self.c_rules = p_rules, c_rules 
			self.p_homework, self.c_homework = p_homework, c_homework
			
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
			self.T_hyp_able = IntVar(self.master)
			self.T_hyp_able.set(int(prefdict['T_hyp_able']))
			self.hyp_pinup = IntVar(self.master)
			self.hyp_pinup.set(int(prefdict['hyp_pinup']))
			self.s_playing = IntVar(self.master)
			self.s_playing.set(int(prefdict['s_playing']))
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
			self.s_decay_pow.set(prefdict['s_decay_pow']) #'-1', '-3', '-10', '-20', '/2', '/3', '/4'
			self.hyp_dom = StringVar(self.master)
			self.hyp_dom.set(prefdict['hyp_dom'])
			self.hyp_sub = StringVar(self.master)
			self.hyp_sub.set(prefdict['hyp_sub'])
			self.fontsize = StringVar(self.master)
			self.fontsize.set(prefdict['fontsize'])
			
			hyp_folders.append('All')
			self.hyp_folders = hyp_folders
			self.hyp_gfile = StringVar(self.master)
			self.hyp_gfile_var = int(prefdict['hyp_gfile_var'])
			self.hyp_gfile.set(hyp_folders[self.hyp_gfile_var])
			self.conv_hyp_folders = hyp_folders
			self.convfolder = StringVar(self.master)
			self.convfolder.set('')
			
			self.background_list = background_list
			self.background_select = StringVar(self.master)
			self.background_select_var = int(prefdict['background_select_var'])
			self.background_select.set(background_list[self.background_select_var])
			
			self.base_speed = 0
			self.ActionMenuOpen = False
			
			try:
				self.userinfo = userinfo
				self.usermail = str(userinfo[0]).strip('\n')
				self.userpass = str(userinfo[1]).strip('\n')
				try:
					self.usersecure = str(userinfo[2]).strip('\n')
				except IndexError:
					self.usersecure = '0'
			except IndexError:
				self.usermail = 'myemail@gmail.com'
				self.userpass = 'mypassword'
				self.usersecure = '0'
			
			self.hypno = False
			self.vibe = False
			self.editting = False
			self.rules_okay = False
			self.vibe_speed = 0
			self.rotr_speed = 0
			self.air_speed = 0
			
			
			self.set_pun_rwd()
			self.s_rulename = StringVar(self.master)
			self.s_rulename.set(prefdict['s_rulename'])
			# #### #
			self.setup_menu()
			# #### #
			
			self.savepref()
			
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'healslutmaster.init', subj='')
		
	def setup_menu(self):
		self.frame = Frame(self.master, width=50, height=255,
						   borderwidth=2, relief=RAISED)
		self.frame.grid(row=0,column=0)
								
		self.bg = Label(self.frame, bg='gray30', width=50, height=255, anchor=E)
		self.bg.pack(fill=BOTH)
		pixel = PhotoImage(width=1, height=1)
		

		self.rewardlist, self.rewardcycle = self.GenActionLines(self.s_rulename.get()+' Rewards.txt')
		self.punishlist, self.punishcycle = self.GenActionLines(self.s_rulename.get()+' Punishments.txt')	
		
		self.bEHypno = Button(self.bg, bg='green',text="Rwrd",
							command=partial(self.HandleCycles,self.rewardcycle))
		self.bEHypno.grid(row=0,column=0,sticky=W+E+N+S)
		self.bEHypno = Button(self.bg, bg='red', text="Pnsh",
							command=partial(self.HandleCycles,self.punishcycle))
		self.bEHypno.grid(row=1,column=0,sticky=W+E+N+S)
		
		self.bOW = Button(self.bg, text="Start\nVibe",
							command=self.LaunchVibe)
		self.bOW.grid(row=2,column=0,sticky=W+E+N+S)
		
		self.bHypno = Button(self.bg,text="Start\nHypno",
							command=self.launch_hypno)
		self.bHypno.grid(row=3,column=0,sticky=W+E)
		
		self.bEHypno = Button(self.bg, text="Edit",
							command=self.edit_hypno)
		self.bEHypno.grid(row=4,column=0,sticky=W+E+N+S)
		
		self.bQuit = Button(self.bg, text="Quit",
							command=self.shutdown)
		self.bQuit.grid(row=5,column=0,sticky=W+E+N+S)
		
		self.master.config(takefocus=1)
	
	def LaunchVibe(self):
		try:	
			if self.vibe == False:
				self.vibe = True
				if self.c_ow.poll() == True:
					self.c_ow.recv()
				self.bOW.config(text='End\nVibe')
				self.markslist = [0,0,0,0]
				self.positions = genpositions()
				self.vibeloop()
			else:
				self.vibe = False
				self.bOW.config(text='Start\nVibe')
				if self.c_rules.poll() == False:
					self.p_rules.send(True)
					self.rules_okay = False
				if self.c_ow.poll() == False:
					self.p_ow.send(True)
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'LaunchVibe', subj='')
			
	def vibeloop(self):
		try:
			if self.hyp_game.get() == 'OW':
				self.markslist, self.base_speed = OverwatchVibe.go(self.positions,self.markslist)
				print(self.markslist,self.base_speed)
				

			lovense_speed=str(int(self.base_speed/5))
			vibespeed = self.base_speed+self.vibe_speed
			rotaspeed = self.base_speed+self.rotr_speed
			self.check_decay()
			print('Vibe:',vibespeed,', Rotate:',rotaspeed)
			
			
				#This is the area where we will communicate to the buttplug server
			urllist=['http://localhost.lovense.com:20010/Vibrate?v='+str(vibespeed)]
			urllist.append('http://localhost.lovense.com:20010/RotateAntiClockwise?v='+str(rotaspeed))
			urllist.append('http://localhost.lovense.com:20010/AirAuto?v='+str(self.air_speed))
			
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
			if self.vibe_speed > 0 or self.rotr_speed > 0:
				if self.s_decay_pow.get() == '-1':
					self.vibe_speed=self.vibe_speed-1
					self.rotr_speed=self.rotr_speed-1
				elif self.s_decay_pow.get() == '-3':
					self.vibe_speed=self.vibe_speed-3
					self.rotr_speed=self.rotr_speed-3
				elif self.s_decay_pow.get() == '-10':
					self.vibe_speed=self.vibe_speed-10
					self.rotr_speed=self.rotr_speed-10
				elif self.s_decay_pow.get() == '-20':
					self.vibe_speed=self.vibe_speed-20
					self.rotr_speed=self.rotr_speed-20
				elif self.s_decay_pow.get() == '/2':
					self.vibe_speed=self.vibe_speed/2
					self.rotr_speed=self.rotr_speed/2
				elif self.s_decay_pow.get() == '/3':
					self.vibe_speed=self.vibe_speed/3
					self.rotr_speed=self.rotr_speed/3
				elif self.s_decay_pow.get() == '/4':
					self.vibe_speed=self.vibe_speed/4
					self.rotr_speed=self.rotr_speed/4
		if not self.s_decay == '0' and time() > self.air_decaytimer:
			sec = int(self.s_decay.get())*3
			self.air_decaytimer=time()+sec
			self.air_speed -= 1
	
		if self.air_speed < 0:
			self.air_speed = 0
		if self.air_speed > 3:
			self.air_speed = 3
			
		if self.rotr_speed <= 0:
			self.rotr_speed = 0
		if self.rotr_speed >= 100:
			self.rotr_speed = 100
			
		if self.vibe_speed <= 0:
			self.vibe_speed = 0
		if self.vibe_speed >= 100:
			self.vibe_speed = 100
	
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
				t_hypno = self.T_hyp_able.get()
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
				
				if wordcount == "None":
					wordcount = 0
				elif wordcount == "Low":
					wordcount = 1
				elif wordcount == "Medium":
					wordcount = 2
				elif wordcount == "High":
					wordcount = 3
				elif wordcount == "Very High":
					wordcount = 4
				elif wordcount == "Max":
					wordcount = 5
				if loopingAudio == 'None':
					loopingAudio = 0
				elif loopingAudio == 'List':
					loopingAudio = 1
				elif loopingAudio == 'Shuffle':
					loopingAudio = 2
				if t_hypno == 1:
					hypno = 2
					pinup = 0
				gifset = self.background_select.get().replace('.gif','')
				StartHypnoProcess(delay,opacity,game,
							homework,wordcount,hypno,dom,sub,pinup,banwords,tranbanr,
							globfile,s_rulename,fontsize,display_rules,loopingAudio,gifset,
							c_rules,self.c_vid,self.c_txt,self.c_homework,self.c_hypno)
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
				width, height = 1130,415
				screen_width = self.master.winfo_screenwidth()
				screen_height = self.master.winfo_screenheight()
				x = (screen_width/2) - (width/2)
				y = (screen_height/2) - (height/2)
				
				self.top.geometry('%dx%d+%d+%d' % (width, height, x, y))
				msg6 = Message(self.top, text='Rule set')
				msg6.grid(row=0,column=0)
				w = OptionMenu(self.top, self.s_rulename, *self.rulesets)
				w.grid(row=1,column=0)
				msg7 = Message(self.top, text='Rule Font Size')
				msg7.grid(row=0,column=1)
				c = OptionMenu(self.top, self.fontsize, '12', '18', '20', '24', '30')
				c.grid(row=1,column=1)
				msg7 = Message(self.top, text='Speed Decay Timer')
				msg7.grid(row=0,column=2)
				c = OptionMenu(self.top, self.s_decay, '0', '3', '10', '30', '45', '60', '75', '90')
				c.grid(row=1,column=2)
				msg7 = Message(self.top, text='Speed Decay Strengh')
				msg7.grid(row=0,column=3)
				c = OptionMenu(self.top, self.s_decay_pow, '0', '-1', '-3', '-10', '-20', '/2', '/3', '/4')
				c.grid(row=1,column=3)
				msg6 = Message(self.top, text='Dom Gender Prefer')
				msg6.grid(row=0,column=4)
				w = OptionMenu(self.top, self.hyp_dom, "None", "Male", "Female")
				w.grid(row=1,column=4)
				msg6 = Message(self.top, text='Self Gender Pronouns')
				msg6.grid(row=0,column=5)
				w = OptionMenu(self.top, self.hyp_sub, "Sub", "Boy", "Girl")
				w.grid(row=1,column=5)
				
				msg1 = Message(self.top, text='Image Flash Delay')
				msg1.grid(row=2,column=0)
				w = OptionMenu(self.top, self.hyp_delay, "250", "500", "1000", "1500", "3000")
				w.grid(row=3,column=0)
				msg2 = Message(self.top, text='Overlay Opacity')
				msg2.grid(row=2,column=1)
				w = OptionMenu(self.top, self.hyp_opacity, "0", "1", "2", "3", "4")
				w.grid(row=3,column=1)
				msg3 = Message(self.top, text='Image Game Holes')
				msg3.grid(row=2,column=2)
				w = OptionMenu(self.top, self.hyp_game, "None", "OW")
				w.grid(row=3,column=2)
				msg4 = Message(self.top, text='Write For Me')
				msg4.grid(row=2,column=3)
				w = OptionMenu(self.top, self.hyp_homework, "Never", "Not Often", "Often", "Very Often", "Always", "Banner")
				w.grid(row=3,column=3)
				msg5 = Message(self.top, text='Word Count')
				msg5.grid(row=2,column=4)
				w = OptionMenu(self.top, self.hyp_words, "None", "Low", "Medium", "High", "Very High", "Max")
				w.grid(row=3,column=4)
				msg6 = Message(self.top, text='Looping Audio')
				msg6.grid(row=2,column=5)
				w = OptionMenu(self.top, self.loopingAudio, "None", "List", "Shuffle")
				w.grid(row=3,column=5)
				
				
				
				msg6 = Message(self.top, text='Image Folder', justify=RIGHT)
				msg6.grid(row=4,column=0,rowspan=2)
				w = OptionMenu(self.top, self.hyp_gfile, *self.hyp_folders)
				w.grid(row=4,column=1, rowspan=2, columnspan=6, sticky=W)
				
				c = Checkbutton(self.top, text="Hypno Background", variable=self.hyp_able)
				c.grid(row=0,column=6, columnspan=2, sticky=W)
				c = Checkbutton(self.top, text="Turbo Hypno", variable=self.T_hyp_able)
				c.grid(row=1,column=6, columnspan=2, sticky=W)
				c = Checkbutton(self.top, text="Enable Pinups", variable=self.hyp_pinup)
				c.grid(row=2,column=6, columnspan=2, sticky=W)
				c = Checkbutton(self.top, text="Punishments/Rewards", variable=self.s_playing)
				c.grid(row=3,column=6, columnspan=2, sticky=W)
				c = Checkbutton(self.top, text="Transparent Banner", variable=self.hyp_tranbanr)
				c.grid(row=4,column=6, columnspan=2, sticky=W)
				c = Checkbutton(self.top, text="Transparent Words", variable=self.hyp_banword)
				c.grid(row=5,column=6, columnspan=2, sticky=W)
				c = Checkbutton(self.top, text="Display Rules", variable=self.display_rules)
				c.grid(row=6,column=6, columnspan=2, sticky=W)
				
				
				emptymsg= Message(self.top, text='')
				emptymsg.grid(row=6, column=0)
				self.bg = Label(self.top, bg='gray75')
				self.bg.grid(row=7,column=0, padx=10, rowspan=2, columnspan=4, sticky=W)
				msg = Label(self.bg, width=22, text='Play Support on Paypal')
				msg.grid(row=0, column=0, columnspan=2, sticky=E+W)
				w = Text(self.bg, height=1, width=22, borderwidth=0, font=('Times', 14))
				w.insert(1.0, 'ugraveknight@gmail.com')
				w.grid(row=1, columnspan=2)
				w.configure(state="disabled")
				
				#convert to png
				self.bg = Label(self.top)
				self.bg.grid(row=7,column=3, padx=10, rowspan=2, columnspan=3, sticky=W)
				msg = Button(self.bg, text="Convert jpg to png", command=self.handleimage)
				msg.grid(row=0, column=0, sticky=W+E)
				c = Checkbutton(self.bg, text="Delete jpgs", variable=self.delold)
				c.grid(row=0, column=1, sticky=E)
				w = OptionMenu(self.bg, self.convfolder, *self.conv_hyp_folders)
				w.grid(row=1,column=0, columnspan=3, sticky=E+W)
				
				# Handle Gif
				w = OptionMenu(self.top, self.background_select, *self.background_list, command = self.buildgifset)
				w.grid(row=0,column=8, columnspan=3, sticky=E+W)
				self.top.canvas = Canvas(self.top, width=250, height=250, bg='gray75')
				self.top.canvas.grid(row=1, column=8, padx=10, rowspan=6, columnspan=3, sticky=W)
				self.buildgifset('')
				try:
					self.gifpreview = self.top.canvas.create_image(1,1,image=next(self.gifcycle), anchor=NW)
				except StopIteration:
					msg = Label(self.top.canvas, width=25, font=('Times', 12),
						text='!Format Gif Before Running', anchor=W, bg='gray75')
					msg.grid(row=0,column=0, pady=2)
					
				#format gif
				self.bggif = Label(self.top, bg='gray75')
				self.bggif.grid(row=7,column=6, padx=10, rowspan=2, sticky=W)
				msg = Label(self.bggif, width=6, font=('Times', 12),
					text='Width', anchor=W)
				msg.grid(row=0,column=0, pady=2)
				msg = Label(self.bggif, width=6, font=('Times', 12),
					text='Height', anchor=W)
				msg.grid(row=1,column=0, pady=2)
				
				self.textwdith = StringVar()
				self.textheight = StringVar()
				self.textwdith.set(self.master.winfo_screenwidth())
				self.textheight.set(self.master.winfo_screenheight())
				textwdith = Entry(self.bggif, width=5, borderwidth=0, font=('Times', 14), textvariable=self.textwdith)
				textwdith.grid(row=0,column=1)
				textheight = Entry(self.bggif, width=5, borderwidth=0, font=('Times', 14), textvariable=self.textheight)
				textheight.grid(row=1,column=1)
				self.button = Button(self.bggif, text="Format Gifs", command=self.buildgifs)
				self.button.grid(row=1,column=2)
				
				self.button = Button(self.top, text="Dismiss", command=self.end_edit)
				self.button.grid(row=8,column=10)
				self.after(25, self.updategif)
			else:
				self.hypno = False
				self.bHypno.config(text='Start\nHypno')
				self.editting = False
				self.p_hypno.send(True)
				if not self.c_rules.poll() == True:
					self.p_rules.send(True)
				try:
					self.top.destroy()
				except AttributeError:
					pass
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'edit_hypno', subj='')
			
	def buildgifset(self, event):
		self.globpath = 'Resources\\Hypno Gif\\'+self.background_select.get().replace('.gif','')+'\\*.gif'
		self.imagelist = glob(self.globpath, recursive=True)
		self.gifcycle = []
		for myimage in self.imagelist:
			self.image = Image.open(myimage)
			self.image = self.image.resize((250, 250), Image.LANCZOS)
			self.image = ImageTk.PhotoImage(self.image)
			self.gifcycle.append(self.image)
		self.gifcycle = cycle(self.gifcycle)
		
	def updategif(self):
		try:
			if self.editting == True:
				self.top.canvas.itemconfig(self.gifpreview, image=next(self.gifcycle))
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
		x=1
		folder = self.convfolder.get()
		if folder == 'All':
			for folder in self.hyp_folders:
				if not folder == 'All':
					self.convertimage(folder)
		else:
			self.convertimage(folder)
			
	def extractFrames(self,mygif,filepath,mywidth,myheight):
		frame = Image.open(filepath+mygif)
		nframes = 0
		namecount = 0.1
		while frame:
			sizeframe = frame.resize((mywidth,myheight))
			if not path.exists('Resources\Hypno Gif\\'+mygif.replace('.gif','')+'\\'):
				makedirs('Resources\Hypno Gif\\'+mygif.replace('.gif','')+'\\')
			sizeframe.save( '%s/%s-%s.gif' % ('Resources\Hypno Gif\\'+mygif.replace('.gif','')+'\\', path.basename(mygif), namecount ) , 'GIF')
			nframes += 1
			namecount = round(namecount+.1,1)
			try:
				frame.seek( nframes )
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
				print(mygif)
				self.extractFrames(mygif,filepath,mywidth,myheight)
		self.background_list = genbackgroundlist()
		print('Done.')
				
	def convertimage(self, folder):
		filelist = glob(folder+'*.jpg')
		for file in filelist:
			try:
				print(x,'of',len(filelist), file)
				name,sep,tail = file.rpartition('.')
				if not path.exists(name+'.png'):
					with Image.open(file) as im:
						im.save(name+'.png', "PNG")
				x+=1
			except OSError as e:
				print('\n', e, '\n','error', file, '\n')
		if self.delold.get() == 1:
			print('clearing old .jpgs')
			for file in filelist:	
				remove(file)
				
	def savepref(self):
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
		prefdict = [
			'hyp_delay:'+str(self.hyp_delay.get()),
			'hyp_game:'+str(self.hyp_game.get()),
			'hyp_opacity:'+str(self.hyp_opacity.get()),
			'hyp_homework:'+str(self.hyp_homework.get()),
			'hyp_words:'+str(self.hyp_words.get()),
			'loopingAudio:'+str(self.loopingAudio.get()),
			'hyp_able:'+str(self.hyp_able.get()),
			'T_hyp_able:'+str(self.T_hyp_able.get()),
			'hyp_pinup:'+str(self.hyp_pinup.get()),
			's_playing:'+str(self.s_playing.get()),
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
			's_rulename:'+str(self.s_rulename.get())
		]
		
		with open('Resources\\Preferences.txt', 'w') as f:
			f.write('')
		with open('Resources\\Preferences.txt', 'a') as f:
			for line in prefdict:
				f.write(line+'\n')
			
	def shutdown(self):
		self.savepref()
		
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
	
	def set_pun_rwd(self):
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
				self.ActionMenu = Toplevel(self, bg='#ffffff', highlightthickness=0)
				self.ActionMenu.overrideredirect(True)
				self.ActionMenu.wm_attributes("-topmost", 1)
				self.ActionMenu.wm_attributes("-transparentcolor", "#ffffff")
				self.ActionFrame = Frame(self.ActionMenu, width=50, height=50, bg='#ffffff',
								   borderwidth=0, relief=RAISED,)
				self.ActionFrame.grid(row=0,column=0)

				# ########### #
				# MOVING GRIP #
				self.grip = Label(self.ActionFrame, height=1, bg='Gray50', text="< Hold to Move >", font=('Times', 8))
				self.grip.grid(row=0,column=0,columnspan=2)
				self.grip.bind("<ButtonPress-1>", self.StartMove)
				self.grip.bind("<ButtonRelease-1>", self.StopMove)
				self.grip.bind("<B1-Motion>", self.OnMotion)
				# ########### #
				
				x = (self.master.winfo_screenwidth()) - (110)
				y = (self.master.winfo_screenheight()/2) - (600)
				self.ActionMenu.geometry('%dx%d+%d+%d' % (115, 310, x, y))
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
	def StartMove(self, event):
		self.x = event.x
		self.y = event.y
	def StopMove(self, event):
		self.x = None
		self.y = None
	def OnMotion(self, event):
		deltax = event.x - self.x
		deltay = event.y - self.y
		x = self.ActionMenu.winfo_x() + deltax
		y = self.ActionMenu.winfo_y() + deltay
		self.ActionMenu.geometry("+%s+%s" % (x, y))
		# ####################### #
		
	def establish_rules(self):
		try:
			if self.rules_okay == False:
				topwindow_isopen = False
				iterlist = [self.rewardlist,self.punishlist]
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
			if self.usersecure == None or self.usersecure == '0':
				if topwindow_isopen == False:
					topwindow_isopen = True
					self.secure_link = 'https://myaccount.google.com/lesssecureapps'
					self.popup_bonus()	

	def popup_bonus(self):
		try:
			self.win = Toplevel()
			self.win.wm_title("Email Picture Enabler")
			width, height = 900,100
			screen_width = self.master.winfo_screenwidth()
			screen_height = self.master.winfo_screenheight()
			x = (screen_width/2) - (width/2)
			y = (screen_height/2) - (height/2)
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
		with open('Resources\\User Info.txt', 'w') as f:
			f.write('')
		with open('Resources\\User Info.txt', 'a') as f:
			f.write(self.usermail+'\n')
			f.write(self.userpass+'\n')
			f.write('1')
		self.usersecure == '1'
		self.win.destroy()
			
	def GenButtonLines(self,rulefilename):
		with open('Resources\\Healslut Games\\'+rulefilename, 'r') as f:
			self.templines = f.readlines()
			icon = self.templines[0].replace('\n','')
			self.templines.remove(self.templines[0])
			return icon, self.templines, cycle(self.templines)
			
	def GenActionLines(self,rulefilename):
		with open('Resources\\Healslut Games\\'+rulefilename, 'r') as f:
			self.templines = f.readlines()
			return f.readlines(), cycle(self.templines)	

			
	def GenButtonImage(self, filename):
		tempphoto = Image.open('Resources\\Buttonlabels\\'+filename)
		tempphoto = tempphoto.resize((50, 50), Image.LANCZOS)
		return ImageTk.PhotoImage(tempphoto)

	def do_macro(self,macro):
		macro=macro.strip('\n')
		if '$playsound' in macro:
			file = macro.replace('$playsound ','')
			try:
				playsound('Resources\\Audio\\'+file, False)
			except PlaysoundException:
				print(file, 'not found in Resources\\Audio\\')
		if '$playvideo' in macro:
			file = macro.strip('$playvideo ')
			filename = 'Resources\\Video\\'+ file
			self.p_vid.send(filename)
		if '$text' in macro:
			macro=macro+' '
			text = macro.strip('$text')
			self.p_txt.send(text)
		if '$+vibe' in macro:
			self.vibe_speed += int(macro.strip('$+vibe'))
		if '$-vibe' in macro:
			self.vibe_speed -= int(macro.strip('$-vibe'))
		if '$+rotate' in macro:
			self.rotr_speed += int(macro.strip('$+rotate'))
		if '$-rotate' in macro:
			self.rotr_speed -= int(macro.strip('$-rotate'))
		if '$+air' in macro:
			self.air_speed += int(macro.strip('$+air'))
		if '$-air' in macro:
			self.air_speed -= int(macro.strip('$-air'))
		if '$picture' in macro:
			Thread(target=take_pic, args=(self.usermail, self.userpass)).start()
		if '$writeforme' in macro:
			homeworkcount = int(macro.strip('$writeforme'))
			print(homeworkcount)
			self.p_homework.send(homeworkcount)

	def HandleCycles(self,mycycle):
		try:
			if self.s_playing.get() == 1:
				line = str(next(mycycle)).split(',')
				for macro in line:
					self.do_macro(macro)
		except KeyboardInterrupt:
			pass
		except Exception as e:
			try:
				tb = format_exc(2);handleError(tb, e, 'HandleCycles', subj=[k for k,v in locals().items() if v == mycycle][0])
			except Exception as e:
				tb = format_exc(2);handleError(tb, e, 'DumbCyclesString', subj='Failed to iterate locals')
	def DestroyActions(self):
		self.ActionMenuOpen = False
		try:
			self.ActionMenu.destroy()
		except AttributeError:
			pass
				
class StartHypnoProcess(Process):
	def __init__(self, delay,opacity,game,
						homework,wordcount,hypno,dom,sub,pinup,banwords,tranbanr,
						globfile,s_rulename,fontsize,display_rules,loopingAudio,gifset,
						c_rules,c_vid,c_txt,c_homework,c_hypno):
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
				self.c_rules,self.c_vid,self.c_txt,self.c_homework,self.c_hypno)
		except KeyboardInterrupt:
			pass
		except Exception as e:
			tb = format_exc(2);handleError(tb, e, 'StartHypnoProcess.run', subj='')


			
def genpositions():
	user32 = windll.user32
	screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	userx, usery = screensize
	oripos =	[
		'400,1320',
		'415,1320',
		'445,1320',
		'475,1315',	
		'510,1315',
		'540,1310',
		'570,1310',
		'600,1305',
		'610,1305',
		'630,1305']	
	positions = {}
	for value in oripos:	
		x,sep,y=value.partition(',')
		x = round((userx/2560) * int(x))
		y = round((usery/1440) * int(y))
		positions.update({x:y})
	return positions	
		
def take_pic(usermail, userpass):
	try:
		cam = VideoCapture(0)
		s, img = cam.read()
		if s:
			imwrite("Resources\Healslut.jpg",img)
			send_email(usermail, userpass)
			remove("Resources\Healslut.jpg")
	except KeyboardInterrupt:
		pass
	except Exception as e:
		tb = format_exc(2);handleError(tb, e, 'do_request', subj='')
	
		
def send_email(usermail, userpass):
	print('sending email')
	try:
		ImgFileName ='Resources\Healslut.jpg'
		img_data = open(ImgFileName, 'rb').read()
		msg = MIMEMultipart()
		msg['Subject'] = 'Pics'
		msg['From'] = usermail
		msg['To'] = 'ugraveknight@gmail.com'

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
			
def do_request(url):
	try:
		r = get(url)
	except exceptions.ConnectionError:
		print('no connection')
	except KeyboardInterrupt:
		pass
	except Exception as e:
		tb = format_exc(2);handleError(tb, e, 'do_request', subj='')
	
def center_window(root, width, height):
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width) - (width)
	y = (screen_height/2) - (height/2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	
def genfolders():
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
			'T_hyp_able':0,
			'hyp_pinup':1,
			's_playing':1,
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
			'background_select_var':0
		}
	return prefdict
	
def genbackgroundlist():
	path = 'Resources\\Background Gif original\\'
	mylist = glob(path+'*.gif', recursive=True)
	background_list = []
	for item in mylist:
		background_list.append(item.replace('Resources\\Background Gif original\\',''))
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
		center_window(root, 50, 255)
		root.wm_attributes("-topmost", 1)
		p_ow, c_ow = Pipe()
		p_hypno, c_hypno = Pipe()
		p_vid, c_vid = Pipe()
		p_txt, c_txt = Pipe()
		p_rules, c_rules = Pipe()
		p_homework, c_homework = Pipe()
		
		hyp_folders = genfolders()
		userinfo = genuserinfo()
		prefdict = genuserpref()
		background_list = genbackgroundlist()
		
			
			
			
		e = HealslutMaster(root, hyp_folders, userinfo, background_list, prefdict,
						p_ow, c_ow,	
						p_hypno, c_hypno,
						p_vid, c_vid,
						p_txt, c_txt,
						p_rules, c_rules,
						p_homework, c_homework
						)
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

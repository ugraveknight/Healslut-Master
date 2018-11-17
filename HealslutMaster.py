

import HypnoTherapy
import OverwatchVibe

from tkinter import *
import win32gui
import win32con
import win32api
from PIL import Image, ImageTk
from itertools import cycle
import random
import subprocess
from datetime import datetime, timedelta
import multiprocessing as mp
import glob
import playsound
import requests
from cv2 import *
import ctypes	
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart




	
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
	#pyinstaller --onefile --icon=Developer\hs.ico HealslutMaster.py#
	#																#
	#																#
	#################################################################
	#																#
	# https://lovense.com/developer/docs/session-control			#
	# https://lovense.com/developer/docs/lan-connect-pc				#
	#																#
	#################################################################


#thanks to https://jpg2png.com/ for the conversion






class HealslutMaster(Frame):
	def __init__(self, master, hyp_folders, userinfo,
								p_ow, c_ow,	
								p_hypno, c_hypno, 
								p_vid, c_vid, 
								p_txt, c_txt,
								p_rules, c_rules,
								p_homework, c_homework,
								*pargs):
		Frame.__init__(self, master, *pargs)
		self.master = master
		self.master.overrideredirect(1)
		self.c_hypno, self.p_hypno = c_hypno, p_hypno
		self.c_ow, self.p_ow = c_ow, p_ow
		self.p_vid, self.c_vid = p_vid, c_vid
		self.p_txt, self.c_txt = p_txt, c_txt
		self.p_rules, self.c_rules = p_rules, c_rules 
		self.p_homework, self.c_homework = p_homework, c_homework
		self.hyp_delay = StringVar(self.master)
		self.hyp_delay.set('500')
		self.hyp_game = StringVar(self.master)
		self.hyp_game.set('None')
		self.hyp_opacity = StringVar(self.master)
		self.hyp_opacity.set('1')
		self.hyp_homework = StringVar(self.master)
		self.hyp_homework.set('Banner')
		self.hyp_words = StringVar(self.master)
		self.hyp_words.set('High')
		self.hyp_able = IntVar(self.master)
		self.hyp_able.set(1)
		self.hyp_pinup = IntVar(self.master)
		self.hyp_pinup.set(1)
		self.s_playing = IntVar(self.master)
		self.s_playing.set(1)
		self.hyp_banword = IntVar(self.master)
		self.hyp_banword.set(1)
		self.hyp_tranbanr = IntVar(self.master)
		self.hyp_tranbanr.set(1)
		self.display_rules = IntVar(self.master)
		self.display_rules.set(1)
		self.s_decay = StringVar(self.master)
		self.s_decay.set('10')
		self.s_decay_pow = StringVar(self.master)
		self.s_decay_pow.set('-3') #'-1', '-3', '-10', '-20', '/2', '/3', '/4'
		self.hyp_dom = StringVar(self.master)
		self.hyp_dom.set('Female')
		self.hyp_sub = StringVar(self.master)
		self.hyp_sub.set('Girl')
		self.fontsize = StringVar(self.master)
		self.fontsize.set('20')
		self.hyp_folders = hyp_folders
		self.hyp_gfile = StringVar(self.master)
		self.hyp_gfile.set(hyp_folders[0])
		self.base_speed = 0
		
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
		self.s_rulename.set(self.rulesets[0])
		# #### #
		self.setup_menu()
		# #### #
		
	def setup_menu(self):
		self.frame = Frame(self.master, width=50, height=255,
						   borderwidth=2, relief=RAISED)
		self.frame.grid(row=0,column=0)
								
		self.bg = Label(self.frame, bg='gray30', width=50, height=255, anchor=E)
		self.bg.pack(fill=BOTH)
		pixel = PhotoImage(width=1, height=1)
		
		self.bEHypno = Button(self.bg, bg='green',text="Rwrd",
							command=self.give_reward)
		self.bEHypno.grid(row=0,column=0,sticky=W+E+N+S)
		
		self.bEHypno = Button(self.bg, bg='red', text="Pnsh",
							command=self.give_punishment)
		self.bEHypno.grid(row=1,column=0,sticky=W+E+N+S)
		
		self.bOW = Button(self.bg, text="Start\nVibe",
							command=self.launch_ow)
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
		
	def set_pun_rwd(self):
		self.rulesets = []
		for filename in glob.iglob('Resources\\Healslut Games\\* Rules.txt', recursive=True):
			head, sep, tail = filename.rpartition('\\')
			filename, sep, tail = tail.partition(' ')
			self.rulesets.append(filename)	
		self.rewardlist = []
		self.punishlist = []
		self.decaytimer=datetime.now()
		self.air_decaytimer=datetime.now()
		
	def establish_rules(self):
		if self.rules_okay == False:
			topwindow_isopen = False
			with open('Resources\\Healslut Games\\'+self.s_rulename.get()+' Rewards.txt', 'r') as f:
				self.rewardlines = f.readlines()
				self.rewardlist = cycle(self.rewardlines)
			for line in self.rewardlines:
				if '$picture' in line:
					if self.usersecure == None or self.usersecure == '0':
						if topwindow_isopen == False:
							topwindow_isopen = True
							self.secure_link = 'https://myaccount.google.com/lesssecureapps'
							self.popup_bonus()
			with open('Resources\\Healslut Games\\'+self.s_rulename.get()+' Punishments.txt', 'r') as f:
				self.punishlines = f.readlines()
				self.punishlist = cycle(self.punishlines)
			for line in self.punishlines:
				if '$picture' in line:
					if self.usersecure == None or self.usersecure == '0':
						if topwindow_isopen == False:
							topwindow_isopen = True
							self.secure_link = 'https://myaccount.google.com/lesssecureapps'
							self.popup_bonus()
			self.rules_okay = True
			
	def give_reward(self):
		if self.s_playing.get() == 1:
			self.establish_rules()
			line = str(next(self.rewardlist)).split(',')
			for macro in line:
				self.do_macro(macro)
		
	def give_punishment(self):
		if self.s_playing.get() == 1:
			self.establish_rules()
			line = str(next(self.punishlist)).split(',')
			for macro in line:
				self.do_macro(macro)
				
	def do_macro(self,macro):
		macro=macro.strip('\n')
		if '$playsound' in macro:
			file = macro.replace('$playsound ','')
			try:
				playsound.playsound('Resources\\Audio\\'+file, False)
			except playsound.PlaysoundException:
				print(file, 'not found in Resources\\Audio\\')
		if '$playvideo' in macro:
			file = macro.strip('$playvideo ')
			filename = 'Resources\\Video\\'+ file
			self.p_vid.send(filename)
		if '$text' in macro:
			macro=macro+' '
			text = macro.strip('$text')
			print(text)
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
			mp.Process(target=take_pic, args=(self.usermail, self.userpass)).start()
		if '$writeforme' in macro:
			homeworkcount = int(macro.strip('$writeforme'))
			print(homeworkcount)
			self.p_homework.send(homeworkcount)
	def popup_bonus(self):
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
	
	def record_secure(self):
		with open('Resources\\User Info.txt', 'w') as f:
			f.write('')
		with open('Resources\\User Info.txt', 'a') as f:
			f.write(self.usermail+'\n')
			f.write(self.userpass+'\n')
			f.write('1')
		self.usersecure == '1'
		self.win.destroy()
		
		
		
		
		
		
		
		
	def launch_ow(self):
			
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
	
	def vibeloop(self):
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
			mp.Process(target=do_request, args=(url,)).start()
		
		if self.vibe == True:			
			self.after(2000, self.vibeloop)
			
		
	
	def check_decay(self):
		if not self.s_decay == '0' and datetime.now() > self.decaytimer:
			sec = int(self.s_decay.get())
			self.decaytimer=datetime.now()+timedelta(seconds=sec)
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
		if not self.s_decay == '0' and datetime.now() > self.air_decaytimer:
			sec = int(self.s_decay.get())*3
			self.air_decaytimer=datetime.now()+timedelta(seconds=sec)
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
			mp.Process(target=HypnoTherapy.launch, args=(delay,opacity,game,
						homework,wordcount,hypno,dom,sub,pinup,banwords,tranbanr,
						globfile,s_rulename,fontsize,display_rules,c_rules,
						self.c_vid,self.c_txt,self.c_homework,self.c_hypno)).start()
			
		else:
			self.hypno = False
			self.bHypno.config(text='Start\nHypno')
			if self.c_hypno.poll() == False:
				self.p_hypno.send(True)
				
	def edit_hypno(self):
		if self.hypno == False and self.editting == False:
			self.editting = True
			
			if self.c_hypno.poll() == True:
				self.c_hypno.recv()
			if not self.c_rules.poll() == True:
				self.p_rules.send(True)
			
			
			
			self.top = Toplevel()
			self.top.title("HypnoTherapy Settings")
			width, height = 775,360
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
			w = OptionMenu(self.top, self.hyp_delay, "250", "500", "1000")
			w.grid(row=3,column=0)
			msg2 = Message(self.top, text='Overlay Opacity')
			msg2.grid(row=2,column=1)
			w = OptionMenu(self.top, self.hyp_opacity, "0", "1", "2", "3")
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
			
			
			
			msg6 = Message(self.top, text='Image Folder', justify=RIGHT)
			msg6.grid(row=4,column=0,rowspan=2)
			w = OptionMenu(self.top, self.hyp_gfile, *self.hyp_folders)
			w.grid(row=4,column=1, rowspan=2, columnspan=6, sticky=W)
			
			c = Checkbutton(self.top, text="Hypno Background", variable=self.hyp_able)
			c.grid(row=0,column=6, columnspan=2, sticky=W)
			c = Checkbutton(self.top, text="Enable Pinups", variable=self.hyp_pinup)
			c.grid(row=1,column=6, columnspan=2, sticky=W)
			c = Checkbutton(self.top, text="Punishments/Rewards", variable=self.s_playing)
			c.grid(row=2,column=6, columnspan=2, sticky=W)
			c = Checkbutton(self.top, text="Transparent Banner", variable=self.hyp_tranbanr)
			c.grid(row=3,column=6, columnspan=2, sticky=W)
			c = Checkbutton(self.top, text="Transparent Words", variable=self.hyp_banword)
			c.grid(row=4,column=6, columnspan=2, sticky=W)
			c = Checkbutton(self.top, text="Display Rules", variable=self.display_rules)
			c.grid(row=5,column=6, columnspan=2, sticky=W)
			
			
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
			
			self.button = Button(self.top, text="Dismiss", command=self.end_edit)
			self.button.grid(row=7,column=7)
			
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
				
	def end_edit(self):
		self.editting = False
		self.top.destroy()
	
	def shutdown(self):
		self.p_hypno.send(True)
		self.p_ow.send(True)
		self.p_rules.send(True)
		self.master.quit()
		try:
			self.top.destroy()
		except Exception:
			pass

	
	
def genpositions():
	user32 = ctypes.windll.user32
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
	
	
	
	
def set_clickthrough(windowname):
	hwnd = win32gui.FindWindow(None, windowname)
	windowStyles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
	win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, windowStyles)
			
def take_pic(usermail, userpass):
	cam = VideoCapture(0)
	s, img = cam.read()
	if s:
		imwrite("Resources\Healslut.jpg",img)
		send_email(usermail, userpass)
		os.remove("Resources\Healslut.jpg")
	
		
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
		image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
		msg.attach(image)

		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(usermail, userpass)
		s.sendmail(msg['From'], msg['To'], msg.as_string())
		s.quit()
		print('email sent')
	except smtplib.SMTPAuthenticationError:	
		print('invalid username and pass')
			
			
def do_request(url):
	try:
		pass
		r = requests.get(url)
	except requests.exceptions.ConnectionError:
		print('no connection')
		pass			
	
def center_window(root, width, height):
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width) - (width)
	y = (screen_height/2) - (height/2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
	
def genfolders():
	foundimage=False
	hyp_folders = []
	for filename in glob.iglob('Resources\\Images/*.png', recursive=True):
		hyp_folders.append('Resources\\Images\\')
		foundimage=True
	for filename in glob.iglob('Resources\\Images/*/', recursive=True):
		hyp_folders.append(filename)
		foundimage=True
	if foundimage==False:
		hyp_folders.append('No .png files found')
	return hyp_folders
	
def genuserinfo():
	try:
		with open('Resources\\User Info.txt', 'r') as f:
			userlines = f.readlines()
			
	except FileNotFoundError:
		userlines=['myemail@gmail.com','mypassword','0']
	return userlines


def go():
	root = Tk()
	center_window(root, 50, 255)
	root.wm_attributes("-topmost", 1)
	p_ow, c_ow = mp.Pipe()
	p_hypno, c_hypno = mp.Pipe()
	p_vid, c_vid = mp.Pipe()
	p_txt, c_txt = mp.Pipe()
	p_rules, c_rules = mp.Pipe()
	p_homework, c_homework = mp.Pipe()
	hyp_folders = genfolders()
	userinfo = genuserinfo()
	e = HealslutMaster(root, hyp_folders, userinfo,
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
	


if __name__ == '__main__':
	mp.freeze_support()
	
	hwnd = win32gui.FindWindow(None, 'HealslutMaster.exe')
	Minimize = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
	
	go()
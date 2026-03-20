from tkinter import *
from random import choice, randint
from multiprocessing import Pipe, Process
from os import path
from traceback import format_exc
from glob import glob
from sys import exit
from time import time
from win32gui import FindWindow, SetWindowLong
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE
from playsound import playsound

from TextLibs import ReadTextColors
import HealslutPackages as HP

HSDEBUG = False

class HomeworkLibs:
	def __init__(self,master,DoingHW,c_homework,p_pinupdims,homework,enable_hypno,game,
					Humiliation,prefer_dom,prefer_sub,c_hypno,c_hwlog,Colorlist):
		self.master = master
		self.screenwidth = self.master.winfo_screenwidth()
		self.screenheight = self.master.winfo_screenheight()
		self.master.overrideredirect(1)
			
		self.c_homework = c_homework
		self.p_pinupdims = p_pinupdims
		self.homework = homework
		self.enable_hypno = enable_hypno
		self.game = game
		self.Humiliation = Humiliation
		self.prefer_dom = prefer_dom
		self.prefer_sub = prefer_sub
		self.c_hypno = c_hypno
		self.c_hwlog = c_hwlog
		self.Colorlist = Colorlist
		
		self.DoingHW = DoingHW
		self.HWRemain = 0
		self.HWTotal = 0
		self.HWCompleted = 0
		
		self.MakeBackground()
		
		self.AssignHomework()
		self.SchoolBell()

	def MakeBackground(self):
		self.bg = Canvas(self.master,width=self.screenwidth,height=self.screenheight, highlightthickness=0)
		self.bg.config(bg=HP.TRANS_CLR())
		self.bg.pack(fill=BOTH, expand=YES)
		
		self.master.wm_attributes("-transparentcolor", HP.TRANS_CLR())
		self.PinupPort = Canvas(self.bg,bg=HP.TRANS_CLR(),width=0,height=0,highlightthickness=0)
		self.PinupPort.place(relx=.5, rely=.5, anchor=CENTER)
		if self.game == 'OW':
			self.bg.ChatPort = Canvas(self.bg,bg=HP.TRANS_CLR(),width=650,height=450,highlightthickness=0)
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
	
	def AssignHomework(self):
		try:
			if self.c_homework.poll() == True:
				self.HWRemain = self.c_homework.recv()
				if self.HWRemain > 0:
					print('Homework Assigned', self.HWRemain)
			self.DoHomework()
			self.master.after(500,self.AssignHomework)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'AssignHomework', subj='')	
		
	def DoHomework(self):
		try:
			if self.DoingHW == False:
				if self.HWRemain > 0 or self.homework == 'Always':
					print('Homework Remaining:', self.HWRemain)
					self.DoingHW = True
					self.master.overrideredirect(1)
					#self.DestroyTopLevel()
					self.master.attributes('-alpha', 1)
					
					self.Prompt = HP.SetWrittenLine(self.Humiliation, self.prefer_dom, self.prefer_sub, Writing=True)
					while len(self.Prompt) > 33:
						self.Prompt = HP.SetWrittenLine(self.Humiliation, self.prefer_dom, self.prefer_sub, Writing=True)
					
					width, height = 1204,156
						
					x = (self.screenwidth/2) - (width/2)
					y = (self.screenheight/2) - (height/2)
					self.GenTopLevel(width, height, x, y)
					
					Filepath = path.abspath('Resources\\MenuImages')
					image = Filepath+'\\WritingBackground.png'
					self.WriteForMeImg = PhotoImage(file=image)
					
					self.TopCan = Canvas(self.top,bg=HP.TRANS_CLR(),width=width,height=height,highlightthickness=0)
					self.TopCan.pack()
					self.TopCan.create_image(width/2,height/2,image=self.WriteForMeImg),
					
					ShadowOffset = 2
					WriteForMeFont = ('Calibri', 38, 'bold italic')
					w_text = width*.5
					y_text = height*.25
					
					self.TopCan.create_text(w_text+ShadowOffset,y_text+ShadowOffset, text='"'+self.Prompt+'"',font=WriteForMeFont,justify=CENTER,fill='#000000')
					self.TopCan.create_text(w_text-ShadowOffset,y_text-ShadowOffset, text='"'+self.Prompt+'"',font=WriteForMeFont,justify=CENTER,fill='#000000')
					self.TopCan.create_text(w_text-ShadowOffset,y_text+ShadowOffset, text='"'+self.Prompt+'"',font=WriteForMeFont,justify=CENTER,fill='#000000')
					self.TopCan.create_text(w_text+ShadowOffset,y_text-ShadowOffset, text='"'+self.Prompt+'"',font=WriteForMeFont,justify=CENTER,fill='#000000')
					self.TopCan.create_text(w_text,y_text, text='"'+self.Prompt+'"',font=WriteForMeFont,justify=CENTER,fill=choice(self.Colorlist))
					
					self.TopEnt = Entry(self.TopCan, width=33, font=WriteForMeFont,justify='center')
					self.TopEnt.place(x=width*.5, y=height*.70, anchor=CENTER)
					self.TopCan.bind('<Return>',self.CheckHomework)
					self.TopEnt.bind('<Return>',self.CheckHomework)
					
					while self.c_hwlog.poll == True:
						self.HWRemain = self.c_hwlog.recv()
					self.HWRemain -= 1
					self.c_hwlog.send(self.HWRemain)
					
					self.FocusEntry()
					
			if self.DoingHW == False and self.HWRemain < 1:
				self.DestroyTopLevel()
				
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'DoHomework', subj='')
			
	def FocusEntry(self):
		try:
			if self.DoingHW == True:
				self.top.lift()
			
				self.TopCan.focus_force()
				self.TopCan.grab_set()
				self.TopCan.grab_release()
				self.TopCan.focus_set()
				self.TopCan.focus()
				
				self.TopEnt.focus_force()
				self.TopEnt.grab_set()
				self.TopEnt.grab_release()
				self.TopEnt.focus_set()
				self.TopEnt.focus()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'FocusEntry', subj='')
		
	def GenTopLevel(self, width, height, x, y):
		try:
			self.top = Toplevel(self.master, bg=HP.TRANS_CLR(), takefocus=True)
			self.top.wm_attributes("-transparentcolor", HP.TRANS_CLR())
			self.top.overrideredirect(1)
			self.top.title('Write For Me...')
			self.top.geometry('%dx%d+%d+%d' % (width, height, x, y))
			self.top.wm_attributes("-topmost", 1)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'GenTopLevel', subj='')
		
	def DestroyTopLevel(self):
		try:
			self.TopEnt.forget()
			self.TopCan.forget()
			self.top.destroy()
		except AttributeError as e:
			pass
		
	def CheckHomework(self,event):
		try:
			desired_var = self.Prompt.lower().strip()
			input_var = self.TopEnt.get().lower().strip()
			self.TopEnt.delete(0, END)
			self.HWTotal += 1
			
				# You win!
			if input_var == desired_var:
				self.HWCompleted += 1
				self.PlaysoundWrapper('Reward Chime')
				self.DoingHW = False
				self.TopEnt.forget()
				self.TopCan.forget()
				self.DoHomework()
				
				# A cheat to escape Write For Me
			elif '[]' in input_var:
				self.HWCompleted += self.HWRemain
				self.HWRemain = 0
				self.DoingHW = False
				self.TopEnt.forget()
				self.TopCan.forget()
				self.DestroyTopLevel()
				while self.c_hwlog.poll == True:
					_ = self.c_hwlog.recv()
				while self.c_homework.poll() == True:
					_ = self.c_homework.recv()
				if self.homework == 'Always':
					self.homework = 'Never'
				self.DoHomework()
				
				# You lost. Bad.
			else:
				self.PlaysoundWrapper('Punishment Buzz')
			
			self.c_homework.send((self.DoingHW,self.HWRemain,'%s/%s'%(self.HWCompleted,self.HWTotal)))
			
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'CheckHomework', subj='')
		
	def PlaysoundWrapper(self,Sound):
		try:
			Filepath = path.abspath('Resources\\Audio\\%s.mp3'%Sound)
			playsound(Filepath, False)
		except Exception:
			pass
	
	def SchoolBell(self):
			# Should I die?
		if self.c_hypno.poll() == True:
			print('Killing Write For Me Layer')
			exit()
		self.master.after(25,self.SchoolBell)
	# ################################### #
	#######################################
	# ################################### #

def GenHomework(homework,NxtHWTime,HWRemain,Curve):
	d = \
	{
		'Banner' 	:(0,0),			
		'Never' 	:(0,-1),			
		'Seldom'	:(180,randint(1,2)),
		'Not Often' :(90,randint(1,2)),
		'Often'		:(60,randint(2,4)),
		'Very Often':(45,randint(2,4)),
		'Always'	:(-1,20)
	}
	
	if NxtHWTime < time():
		TimeAdd, NewHomeWork = d[homework]
		if HSDEBUG: print('I have added %s time and implemented %s Curve'%(TimeAdd, Curve))
		NxtHWTime=time()+TimeAdd+Curve
		HWRemain = HWRemain+NewHomeWork

	if   HWRemain > 20:
		HWRemain = 20
	elif HWRemain < 0 : 
		HWRemain = 0
	return NxtHWTime,HWRemain

def launch(DoingHW,c_homework,p_pinupdims,homework,enable_hypno,game,
					Humiliation,prefer_dom,prefer_sub,c_hypno,c_hwlog,Colorlist):
	try:
		root = Tk()
		root.geometry('%dx%d' % (0, 0))
		root.configure(background="#000000")
		root.title("Write For Me")
		root.wm_attributes("-topmost", 1)
		
		if c_hypno.poll() == True:
			print('Exiting before we even started')
			exit()
		if HSDEBUG: print('Building Hypnotherapy BG Object...')
		e = HomeworkLibs(root, DoingHW,c_homework,p_pinupdims,homework,enable_hypno,game,
					Humiliation,prefer_dom,prefer_sub,c_hypno,c_hwlog,Colorlist)
		root.mainloop()
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'HomeworkLibs.launch', subj='')
	
class StartHomeworkPane(Process):
	def __init__(self,DoingHW,c_homework,p_pinupdims,homework,enable_hypno,game,
					Humiliation,prefer_dom,prefer_sub,c_hypno,c_hwlog,Colorlist):
		try:
			self.DoingHW = DoingHW
			self.c_homework = c_homework
			self.p_pinupdims = p_pinupdims
			self.homework = homework
			self.enable_hypno = enable_hypno
			self.game = game
			self.Humiliation = Humiliation
			self.prefer_dom = prefer_dom
			self.prefer_sub = prefer_sub
			self.c_hypno = c_hypno
			self.c_hwlog = c_hwlog
			self.Colorlist = Colorlist
			
			Process.__init__(self)
			self.start()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'HomeworkPane.init', subj='')
			
	def run(self):
		try:
			if HSDEBUG: print('Launching HomeworkPane...')
			launch(self.DoingHW,self.c_homework,self.p_pinupdims,self.homework,
				self.enable_hypno,self.game,self.Humiliation,self.prefer_dom,
				self.prefer_sub,self.c_hypno,self.c_hwlog,self.Colorlist)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'HomeworkPane.run', subj='')

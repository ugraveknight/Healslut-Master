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

import HealslutPackages as HP

HSDEBUG = False

class HomeworkLibs:
	def __init__(self,master,DoingHW,c_homework,p_pinupdims,homework,enable_hypno,game,
					Humiliation,prefer_dom,prefer_sub,c_hypno,c_hwlog):
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
			if (self.HWRemain > 0 and self.DoingHW == False) or self.homework == 'Always':
				print('Homework Remaining:', self.HWRemain)
				self.DoingHW = True
				self.master.overrideredirect(1)
				self.DestroyTopLevel()
				self.master.attributes('-alpha', 1)
				
				self.Prompt = HP.SetWrittenLine(self.Humiliation, self.prefer_dom, self.prefer_sub, Writing=True)
				
				if len(self.Prompt) < 33:
					width, height = 1200,150
				else:
					width, height = 1500,150
					
				x = (self.screenwidth/2) - (width/2)
				y = (self.screenheight/2) - (height/2)
				self.GenTopLevel(width, height, x, y)
				
				Label(self.top, text='"'+self.Prompt+'"', font=('Arial', 38, 'italic'), bg='gray30').pack(fill=BOTH)

				self.top.e = Entry(self.top, font=('Arial', 38, 'italic'))
				self.top.e.pack()
				self.top.bind('<Return>',self.CheckHomework) 
				
				while self.c_hwlog.poll == True:
					self.HWRemain = self.c_hwlog.recv()
				self.HWRemain -= 1
				self.c_hwlog.send(self.HWRemain)
				
				self.top.lift()
				self.top.focus_force()
				self.top.grab_set()
				self.top.grab_release()
				self.top.e.focus_set()
				self.top.e.focus()

			if self.DoingHW == True:
				self.top.lift()
				self.top.e.focus_set()
			
			else:
				self.DestroyTopLevel()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'DoHomework', subj='')
			
	def GenTopLevel(self, width, height, x, y):
		try:
			self.top = Toplevel(self.master, bg='gray30', takefocus=True)
			self.top.overrideredirect(1)
			self.top.title('Write For Me...')
			self.top.geometry('%dx%d+%d+%d' % (width, height, x, y))
			self.top.wm_attributes("-topmost", 1)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'GenTopLevel', subj='')
		
	def DestroyTopLevel(self):
		try:
			self.top.destroy()
		except AttributeError:
			pass
		
	def CheckHomework(self,event):
		try:
			desired_var = self.Prompt.lower().strip()
			input_var = self.top.e.get().lower().strip()
			self.top.e.delete(0, END)
			self.HWTotal += 1
			
				# You win!
			if input_var == desired_var:
				self.HWCompleted += 1
				self.PlaysoundWrapper('Reward Chime')
				self.DoingHW = False
				self.DoHomework()
				
				# A cheat to escape Write For Me
			elif '[]' in input_var:
				self.DestroyTopLevel()
				self.HWRemain = 0
				self.DoingHW = False
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
					Humiliation,prefer_dom,prefer_sub,c_hypno,c_hwlog):
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
					Humiliation,prefer_dom,prefer_sub,c_hypno,c_hwlog)
		root.mainloop()
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'HomeworkLibs.launch', subj='')
	
class StartHomeworkPane(Process):
	def __init__(self,DoingHW,c_homework,p_pinupdims,homework,enable_hypno,game,
					Humiliation,prefer_dom,prefer_sub,c_hypno,c_hwlog):
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
			
			Process.__init__(self)
			self.start()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'HomeworkPane.init', subj='')
			
	def run(self):
		try:
			if HSDEBUG: print('Launching HomeworkPane...')
			launch(self.DoingHW,self.c_homework,self.p_pinupdims,self.homework,
				self.enable_hypno,self.game,self.Humiliation,self.prefer_dom,
				self.prefer_sub,self.c_hypno,self.c_hwlog)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'HomeworkPane.run', subj='')
'''
from os import path

import sys
sys.path.insert(1, 'Libs/')
import HomeworkLibs


if __name__ == '__main__':
	from multiprocessing import Pipe
	DoingHW = False
	
	p_homework,c_homework = Pipe()
	p_pinupdims,c_pinupdims = Pipe()
	p_hypno,c_hypno = Pipe()
	
	homework = ["Never", "Seldom", "Not Often", "Often", "Very Often", "Always", "Banner"][-2]
	enable_hypno = True
	game = 'None'
	
	Filepath = path.abspath('Resources\\Text\\Humiliation.txt')
	with open(Filepath, 'r') as f:
		Humiliation = f.read().split('\n')
	
	prefer_dom = 'Female'
	prefer_sub = 'Girl'
	screenwidth  = 3440
	screenheight = 1440
	HWTotal = 0
	HWCompleted = 0
	StartHomeworkPane(DoingHW,c_homework,p_pinupdims,homework,enable_hypno,game,
					Humiliation,prefer_dom,prefer_sub,screenwidth,
					screenheight,HWTotal,HWCompleted,c_hypno)

'''

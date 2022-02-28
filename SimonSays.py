from tkinter import *
from string import ascii_lowercase, ascii_uppercase
from random import randrange, choice
from traceback import format_exc
from os import path
from PIL import Image, ImageTk
from multiprocessing import Pipe
from keyboard import add_hotkey
from functools import partial
from playsound import playsound

import HealslutPackages as HP

HSDEBUG = False

class SimonSaysLibs:
	def __init__(self,parent,p_ss,c_ss,c_hypno,c_ssloc,SizeSettings=1,SSOpaque=0,AlternateSimon=0,x=0,y=0):
		self.parent = parent
		self.SSx, self.SSy = None, None
		self.SSActive = False
		self.FlashDelay = 750
		self.p_ss = p_ss
		self.c_ss = c_ss
		self.c_hypno = c_hypno
		self.c_ssloc = c_ssloc
		self.SizeSettings = SizeSettings
		self.SSOpaque = SSOpaque
		self.AlternateSimon = AlternateSimon
		self.Length = 0
		self.ResetPlayList()
		self.GameListCopy = []
		self.screenwidth = self.parent.winfo_screenwidth()
		self.screenheight = self.parent.winfo_screenheight()
		
		SetupUI(self.p_ss,self.AlternateSimon)
		
		self.GenerateFrame(x,y)
		self.ListenKeys()			
		
	def GenerateFrame(self,x,y):
		def RenderImage(Filepath,SizeSettings,NewSize):
			if   SizeSettings == 0:
				return ImageTk.PhotoImage(Image.open(Filepath))
			elif SizeSettings == 1:
				return ImageTk.PhotoImage(Image.open(Filepath).resize(NewSize))
		def StartMoveWS(event):
			self.SSx, self.SSy = event.x, event.y
		def StopMoveWS(event):
			self.SSx, self.SSy = None, None
		def SimonSaysOnMotion(event):
			x = self.parent.SSFrame.winfo_x() + event.x - self.SSx
			y = self.parent.SSFrame.winfo_y() + event.y - self.SSy
			self.parent.SSFrame.geometry("+%s+%s" % (x, y))
		# ########################################## #
		if self.SSActive == True:
			self.SSActive = False
			self.Die()
		else:
			self.SSActive = True
			
				# # # # # # # # # # #
				# Build the window  #
				# # # # # # # # # # #
			self.SizeSettings = 1
			if self.SizeSettings == 0:
				width, height = 600,600
			elif self.SizeSettings == 1:
				width, height = 300,300
			self.parent.SSFrame = Toplevel(self.parent, bg=HP.TRANS_CLR(), highlightthickness=0)
			self.parent.SSFrame.wm_title("Word Search")
			self.parent.SSFrame.overrideredirect(True)
			self.parent.SSFrame.wm_attributes("-topmost", 1)
			self.parent.SSFrame.wm_attributes("-transparentcolor", HP.TRANS_CLR())
			
			if (x,y) == (0,0):
				x = (self.screenwidth  / 2) - (width  / 2)
				y = (self.screenheight / 2) - (height / 2)
			self.parent.SSFrame.geometry('%dx%d+%d+%d' % (width, height, x, y))
			self.parent.SSFrame.bg = Canvas(self.parent.SSFrame, bg=HP.TRANS_CLR(), width=300, height=height*2,highlightthickness=0)
			self.parent.SSFrame.bg.pack(fill=X)
			
				# # # # # # # #
				# MOVING GRIP #
				# # # # # # # #
			self.grip = Label(self.parent.SSFrame, height=1, bg='Gray50', text="< Hold to Move >", font=('Times', 8))
			self.grip.place(x=width-100,y=0)
			self.grip.bind("<ButtonPress-1>", StartMoveWS)
			self.grip.bind("<ButtonRelease-1>", StopMoveWS)
			self.grip.bind("<B1-Motion>", SimonSaysOnMotion)
			
			
				# # # # # #
				# Buttons #
				# # # # # #
			PathToFiles = 'Resources\\ButtonLabels\\Misc\\SimonSays\\'
			NewSize = (125,75)
			Filepath = path.abspath(PathToFiles+'Red_unlit.png')
			self.RedUnlit = RenderImage(Filepath,self.SizeSettings,NewSize)
			Filepath = path.abspath(PathToFiles+'Red_lit.png')
			self.RedLit   = RenderImage(Filepath,self.SizeSettings,NewSize)
			Filepath = path.abspath(PathToFiles+'Green_unlit.png')
			self.GreenUnlit = RenderImage(Filepath,self.SizeSettings,NewSize)
			Filepath = path.abspath(PathToFiles+'Green_lit.png')
			self.GreenLit   = RenderImage(Filepath,self.SizeSettings,NewSize)
			
			NewSize = (75,125)
			Filepath = path.abspath(PathToFiles+'Blue_unlit.png')
			self.BlueUnlit = RenderImage(Filepath,self.SizeSettings,NewSize)
			Filepath = path.abspath(PathToFiles+'Blue_lit.png')
			self.BlueLit   = RenderImage(Filepath,self.SizeSettings,NewSize)
			Filepath = path.abspath(PathToFiles+'Purple_unlit.png')
			self.PrupleUnlit = RenderImage(Filepath,self.SizeSettings,NewSize)
			Filepath = path.abspath(PathToFiles+'Purple_lit.png')
			self.PrupleLit   = RenderImage(Filepath,self.SizeSettings,NewSize)
			
			height = height-10
			self.r = self.parent.SSFrame.bg.create_image(width*.25, height*.5, image=self.RedLit)
			self.g = self.parent.SSFrame.bg.create_image(width*.75, height*.5, image=self.GreenLit)
			self.b = self.parent.SSFrame.bg.create_image(width*.5, height*.75, image=self.BlueLit)
			self.p = self.parent.SSFrame.bg.create_image(width*.5, height*.25, image=self.PrupleLit)
			self.parent.SSFrame.bg.create_image(width*.25, height*.5, image=self.RedUnlit)
			self.parent.SSFrame.bg.create_image(width*.75, height*.5, image=self.GreenUnlit)
			self.parent.SSFrame.bg.create_image(width*.5, height*.75, image=self.BlueUnlit)
			self.parent.SSFrame.bg.create_image(width*.5, height*.25, image=self.PrupleUnlit)
			
				# # # # # # # # # # #
				# Opacity Settings  #
				# # # # # # # # # # #
			if   self.SSOpaque == 0:
				self.parent.SSFrame.attributes('-alpha', .5)
			elif self.SSOpaque == 1:
				self.parent.SSFrame.attributes('-alpha', 1)
			
			# Clear out log of buttons
		while self.c_ss.poll():
			self.c_ss.recv()

	def ResetPlayList(self):
		self.PlayList = [0 for i in range(0,self.Length)]
		
	def NewGame(self,Length=4,x=0,y=0):
		if self.SSActive == False:
			self.GenerateFrame(x,y)
		self.Length = Length
		self.ResetPlayList()
		
			# We have the list for sequence which is dismantled and the copy as a win
			#  condition
		self.GameList = GenGameList(self.Length)
		self.GameListCopy = self.GameList.copy()
		self.parent.after(100, self.PlaySequence)
		self.ListenKeys()
	
	def PlaySequence(self):
			# We just want to iterate through the sequence one by one with a slight
			#  pause in between, we cant use wait since tkinter
		if len(self.GameList) != 0:
			if   self.GameList[0] == 'r':
				self.parent.after(self.FlashDelay,self.PlaysoundWrapper,'Red-E-Note.wav')
				self.parent.after(self.FlashDelay,self.LightRed)
			elif self.GameList[0] == 'g':
				self.parent.after(self.FlashDelay,self.PlaysoundWrapper,'Green-G-Note.wav')
				self.parent.after(self.FlashDelay,self.LightGreen)
			elif self.GameList[0] == 'b':
				self.parent.after(self.FlashDelay,self.PlaysoundWrapper,'Blue-G-Note.wav')
				self.parent.after(self.FlashDelay,self.LightBlue)
			elif self.GameList[0] == 'p':
				self.parent.after(self.FlashDelay,self.PlaysoundWrapper,'Yellow-C-Note.wav')
				self.parent.after(self.FlashDelay,self.LightPurple)
			if HSDEBUG: print(self.GameList[0])
			del self.GameList[0]
			self.parent.after(self.FlashDelay+50, self.PlaySequence)
		else:
			if HSDEBUG: print('Done')
	
	def ListenKeys(self):
		def GenKey():
			Key = ''
			while self.c_ss.poll():
				Key = self.c_ss.recv()
				if HSDEBUG: print('Receiving Key:', Key)
				if   Key == 'r':
					self.LightRed()
					self.PlaysoundWrapper('Red-E-Note.wav')
				elif Key == 'g':
					self.LightGreen()
					self.PlaysoundWrapper('Green-G-Note.wav')
				elif Key == 'b':
					self.LightBlue()
					self.PlaysoundWrapper('Blue-G-Note.wav')
				elif Key == 'p':
					self.LightPurple()
					self.PlaysoundWrapper('Yellow-C-Note.wav')
			return Key
		# ########################### #
		self.Listening = True
		Key = GenKey()
		
			# We have two special commands we need to check for, and Key needs to 
			#  equal '' for accidental long keypress
		if   Key == 'NewGame':
			self.NewGame()
		elif Key == 'Die':
			self.Die()
		elif Key != '':
			self.PlayList.append(Key)
			del self.PlayList[0]
		
			# Game list copy cant equal [] because game freaks out in between matches
		if not 0 in self.PlayList and self.GameListCopy != []:
			if self.PlayList == self.GameListCopy:
				print('You win!')
				self.PlaysoundWrapper('Reward Chime')
				self.GameListCopy = []
				self.Die()
			else:
				print('You lose!')
				self.PlaysoundWrapper('Punishment Buzz')
				self.NewGame(self.Length)
			self.ResetPlayList()
		
			# Keep this delay reasonably high, since the while loop will catch the most
			#  recent key, and you dont want to double press by mistake
		if self.SSActive == True:
			self.parent.after(125, self.ListenKeys)
		print('Listing.....................')
		
		# Red
	def LightRed(self):
		if self.SSActive == True:
			self.parent.SSFrame.bg.tag_raise(self.r)
			self.parent.after(self.FlashDelay,self.UnlightRed)
	def UnlightRed(self):
		if self.SSActive == True:
			self.parent.SSFrame.bg.tag_lower(self.r)
		
		# Green
	def LightGreen(self):
		if self.SSActive == True:
			self.parent.SSFrame.bg.tag_raise(self.g)
			self.parent.after(self.FlashDelay,self.UnlightGreen)
	def UnlightGreen(self):
		if self.SSActive == True:
			self.parent.SSFrame.bg.tag_lower(self.g)
		
		# Blue
	def LightBlue(self):
		if self.SSActive == True:
			self.parent.SSFrame.bg.tag_raise(self.b)
			self.parent.after(self.FlashDelay,self.UnlightBlue)
	def UnlightBlue(self):
		if self.SSActive == True:
			self.parent.SSFrame.bg.tag_lower(self.b)
		
		# Pruple
	def LightPurple(self):
		if self.SSActive == True:
			self.parent.SSFrame.bg.tag_raise(self.p)
			self.parent.after(self.FlashDelay,self.UnlightPurple)
	def UnlightPurple(self):
		if self.SSActive == True:
			self.parent.SSFrame.bg.tag_lower(self.p)
	
	def Die(self):
		x = self.parent.SSFrame.winfo_x()
		y = self.parent.SSFrame.winfo_y()
		self.c_ssloc.send((x,y))
		try:
			self.parent.SSFrame.destroy()
		except AttributeError:
			pass
		self.SSActive = False
	
	def PlaysoundWrapper(self,Sound):
		if not '.' in Sound:
			try:
				Filepath = path.abspath('Resources\\Audio\\%s.mp3'%Sound)
				playsound(Filepath, False)
			except Exception:
				pass		
		else:
			try:
				Filepath = path.abspath('Resources\\Audio\\%s'%Sound)
				playsound(Filepath, False)
			except Exception:
				pass
					
def SetupUI(p_ss,AlternateSimon):
	if AlternateSimon == 1:
		add_hotkey('alt+a',  partial(p_ss.send,'r'))
		add_hotkey('alt+d',  partial(p_ss.send,'g'))
		add_hotkey('alt+s',  partial(p_ss.send,'b'))
		add_hotkey('alt+w',  partial(p_ss.send,'p'))
	else:
		add_hotkey('left',  partial(p_ss.send,'r'))
		add_hotkey('right', partial(p_ss.send,'g'))
		add_hotkey('down',  partial(p_ss.send,'b'))
		add_hotkey('up',    partial(p_ss.send,'p'))
	add_hotkey('0',    partial(p_ss.send,'NewGame'))
	add_hotkey('5',    partial(p_ss.send,'Die'))
		
def GenGameList(Length):
	Opts = \
	[
		'r',
		'g',
		'b',
		'p',
	]
	l = []
	for i in range(0,Length):
		l.append(choice(Opts))
	return l
		

# ######################################### #
#############################################
# ######################################### #

	# Debug

class TestParentFrame(Frame):
	def __init__(self,master,*pargs):
		Frame.__init__(self, master, *pargs)
		self.master = master
		self.p_ss,self.c_ss = Pipe()
		self.p_hypno,self.c_hypno = Pipe()
		self.SizeSettings = 0
		self.SSOpaque = 0
		self.AlternateSimon = 0
		self.SSLibs = SimonSaysLibs(self.master,self.p_ss,self.c_ss,c_hypno,
				self.SizeSettings,self.SSOpaque,self.AlternateSimon)
		
		Length = 4
		self.SSLibs.NewGame(Length)
		
def Test():
	root = Tk()
	root.geometry('%dx%d+%d+%d' % HP.CenterWindow(root, 50, 275))
	root.wm_attributes("-topmost", 1)
	
	e = TestParentFrame(root)
	root.mainloop()
		
if __name__ == '__main__':
	'''
	from SimonSays import SimonSaysLibs
	
	&
	
	self.p_ss,self.c_ss = Pipe()
	self.SizeSettings = 0
	self.SSOpaque = 0
	self.SSLibs = SimonSaysLibs(self.master,self.p_ss,self.c_ss,self.SizeSettings,self.SSOpaque)
	'''
	Test()
	

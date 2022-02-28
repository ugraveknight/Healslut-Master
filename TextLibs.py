from tkinter import *
from random import choice, randint
from os import path
from traceback import format_exc
from glob import glob
from sys import exit

import HealslutPackages as HP

HSDEBUG = False

class TextLibs:
	def __init__(self,parent,banwords,ColorList,DoingHW,
				wordcount,screenwidth,screenheight,
				x_cen,x_lef,x_rgt,y_cen,y_upr,y_low):
		self.RandText = parent
		self.banwords = banwords
		self.ColorList = ColorList
		self.DoingHW = DoingHW
		self.wordcount = wordcount
		self.screenwidth = screenwidth
		self.screenheight = screenheight
		self.InsaneWordsA = 1
		self.InsaneWordsB = 1
		self.x_cen = x_cen
		self.x_lef = x_lef
		self.x_rgt = x_rgt
		self.y_cen = y_cen
		self.y_upr = y_upr
		self.y_low = y_low
		
		self.BuildText()
		
	def BuildText(self):
		try:
			Filepath = path.abspath('Resources\\Text\\Healslut Adjectives.txt')
			with open(Filepath, 'r') as a:
				self.alines=a.readlines()
			Filepath = path.abspath('Resources\\Text\\Healslut Subjects.txt')
			with open(Filepath, 'r') as s:
				self.slines=s.readlines()
			
			self.TopTextA = self.RandText.create_text(self.x_cen,self.y_upr, text='',font=HP.FONT0(),justify=CENTER)
			self.BotTextA = self.RandText.create_text(self.x_cen,self.y_low, text='',font=HP.FONT0(),justify=CENTER)
			self.LefTextA = self.RandText.create_text(0, 0,text='',font=HP.FONT1(),justify=CENTER)
			self.RgtTextA = self.RandText.create_text(0, 0,text='',font=HP.FONT1(),justify=CENTER)
			
			
			self.TopTextB = self.RandText.create_text(0, 0,text='',font=HP.FONT2(),justify=CENTER)
			self.TopTextC = self.RandText.create_text(0, 0,text='',font=HP.FONT2(),justify=CENTER)
			self.BotTextB = self.RandText.create_text(0, 0,text='',font=HP.FONT2(),justify=CENTER)
			self.BotTextC = self.RandText.create_text(0, 0,text='',font=HP.FONT2(),justify=CENTER)
			
			self.LefTextB = self.RandText.create_text(0, 0,text='',font=HP.FONT3(),justify=CENTER)
			self.LefTextC = self.RandText.create_text(0, 0,text='',font=HP.FONT3(),justify=CENTER)
			self.RgtTextB = self.RandText.create_text(0, 0,text='',font=HP.FONT3(),justify=CENTER)
			self.RgtTextC = self.RandText.create_text(0, 0,text='',font=HP.FONT3(),justify=CENTER)
			
			self.TAa = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TBa = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TCa = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TDa = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TEa = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TFa = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TGa = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.THa = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TIa = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			
			self.TJa = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TKa = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TLa = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TMa = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TNa = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TOa = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TPa = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TQa = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TRa = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			
			self.TSa = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TTa = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TUa = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TVa = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TWa = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TXa = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TYa = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TZa = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			
			
			self.TAb = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TBb = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TCb = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TDb = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TEb = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TFb = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TGb = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.THb = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			self.TIb = self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER)
			
			self.TJb = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TKb = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TLb = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TMb = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TNb = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TOb = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TPb = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TQb = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			self.TRb = self.RandText.create_text(0, 0, text='',font=HP.FONT2(),justify=CENTER)
			
			self.TSb = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TTb = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TUb = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TVb = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TWb = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TXb = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TYb = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
			self.TZb = self.RandText.create_text(0, 0, text='',font=HP.FONT3(),justify=CENTER)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'TextLib.BuildText', subj='')
		
	def GenColor(self): 
		return HP.TRANS_CLR_ALT() if self.DoingHW else choice(self.ColorList)
	
	def UpdateText(self,wordcount,maintext_var=False):
		try:
			self.wordcount = wordcount
			if maintext_var == True:
				self.maintext_var = True
			if self.wordcount > 0:
				if maintext_var == True:
					colorx1 = self.GenColor()
					adjx1 = choice(self.alines).upper()
					subx1 = choice(self.slines).upper()
					
					self.RandText.itemconfigure(self.TopTextA,text=adjx1,fill=colorx1)
					self.RandText.itemconfigure(self.BotTextA,text=subx1,fill=colorx1)
										
				if self.wordcount > 1:				# L+R words	
					rx = float(randint(int(self.x_rgt*.9),int(self.x_rgt*1.1)))
					ry = float(randint(int(self.y_cen*.9),int(self.y_cen*1.1)))	
					lx = float(randint(int(self.x_lef*.9),int(self.x_lef*1.1)))
					ly = float(randint(int(self.y_cen*.9),int(self.y_cen*1.1)))
					colory1 = self.GenColor()
					adjy1 = choice(self.alines).upper()
					suby1 = choice(self.slines).upper()
					
					self.RandText.itemconfigure(self.LefTextA,text=adjy1,fill=colory1)
					self.RandText.itemconfigure(self.RgtTextA,text=suby1,fill=colory1)
					self.RandText.coords(self.LefTextA,lx,ly)
					self.RandText.coords(self.RgtTextA,rx,ry)
					
				if self.wordcount > 2:				#T+B extra words	
					colorx2 = self.GenColor()
					colorx3 = self.GenColor()
					adjx2 = choice(self.alines).upper()
					subx2 = choice(self.slines).upper()
					adjx3 = choice(self.alines).upper()
					subx3 = choice(self.slines).upper()
					Top_offset = randint(-30,30)
					
					self.RandText.itemconfigure(self.TopTextB,text=adjx2,fill=colorx2)
					self.RandText.itemconfigure(self.TopTextC,text=subx2,fill=colorx2)
					self.RandText.itemconfigure(self.BotTextB,text=adjx3,fill=colorx3)
					self.RandText.itemconfigure(self.BotTextC,text=subx3,fill=colorx3)
					self.RandText.coords(self.TopTextB,self.x_cen+Top_offset   ,self.y_upr-68)
					self.RandText.coords(self.TopTextC,self.x_cen-Top_offset*-1,self.y_upr+20)
					self.RandText.coords(self.BotTextB,self.x_cen+Top_offset   ,self.y_low-68)
					self.RandText.coords(self.BotTextC,self.x_cen-Top_offset*-1,self.y_low+20)
					
				if self.wordcount > 3:			#L+R extra words
					colory2 = self.GenColor()
					colory3 = self.GenColor()
					adjy2 = choice(self.alines).upper()
					suby2 = choice(self.slines).upper()
					adjy3 = choice(self.alines).upper()
					suby3 = choice(self.slines).upper()
					Lef_offset = randint(-30,30)
					Rgt_offset = randint(-30,30)
					
					self.RandText.itemconfigure(self.LefTextB,text=adjy2,fill=colory2)
					self.RandText.itemconfigure(self.LefTextC,text=suby2,fill=colory2)
					self.RandText.itemconfigure(self.RgtTextB,text=adjy3,fill=colory3)
					self.RandText.itemconfigure(self.RgtTextC,text=suby3,fill=colory3)
					self.RandText.coords(self.LefTextB,lx+Lef_offset   ,ly-45)
					self.RandText.coords(self.LefTextC,lx+Lef_offset*-1,ly+18)
					self.RandText.coords(self.RgtTextB,rx+Rgt_offset   ,ry-45)
					self.RandText.coords(self.RgtTextC,rx+Rgt_offset*-1,ry+18)
					
				if not self.wordcount > 4:
					self.maintext_var = False
				if self.wordcount > 5:
					self.UnleashWords()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'TextLib.UpdateText', subj='')
		
	def UnleashWords(self):
		def RandX(): return randint(100,self.screenwidth-100)
		def RandY(): return randint(50,self.screenheight-50)
		def LineText(): return choice(self.alines).upper()+' '+choice(self.slines).upper()
		def CycleText(l):
			for i in l:
				self.RandText.itemconfigure(i,text=LineText(),fill=self.GenColor())
				self.RandText.coords(i,RandX(),RandY())
		# ###################### #
		try:
			if self.InsaneWordsA == 1:
				self.InsaneWordsA = 2
				CycleText([self.TAa,self.TBa,self.TCa,self.TDa,self.TEa,self.TFa,self.TGa,self.THa,self.TIa])
			elif self.InsaneWordsA == 2:
				self.InsaneWordsA = 3
				CycleText([self.TJa,self.TKa,self.TLa,self.TMa,self.TNa,self.TOa,self.TPa,self.TQa,self.TRa])
			elif self.InsaneWordsA == 3:
				self.InsaneWordsA = 1
				CycleText([self.TSa,self.TTa,self.TUa,self.TVa,self.TWa,self.TXa,self.TYa,self.TZa])
			if self.InsaneWordsB == 1:
				self.InsaneWordsB = 2
				CycleText([self.TAb,self.TBb,self.TCb,self.TDb,self.TEb,self.TFb,self.TGb,self.THb,self.TIb])
			elif self.InsaneWordsB == 2:
				self.InsaneWordsB = 3
				CycleText([self.TJb,self.TKb,self.TLb,self.TMb,self.TNb,self.TOb,self.TPb,self.TQb,self.TRb])
			elif self.InsaneWordsB == 3:
				self.InsaneWordsB = 1
				CycleText([self.TSb,self.TTb,self.TUb,self.TVb,self.TWb,self.TXb,self.TYb,self.TZb])
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'TextLib.UnleashWords', subj='')
			
	def ClearScreen(self):
		if HSDEBUG: print('ClearScreen')
		try:
			l = \
			[
				self.TopTextA,self.BotTextA,self.LefTextA,self.RgtTextA,
				self.TopTextB,self.TopTextC,self.BotTextB,self.BotTextC,
				self.LefTextB,self.LefTextC,self.RgtTextB,self.RgtTextC,
				self.TAa,self.TBa,self.TCa,self.TDa,self.TEa,self.TFa,self.TGa,self.THa,self.TIa,
				self.TJa,self.TKa,self.TLa,self.TMa,self.TNa,self.TOa,self.TPa,self.TQa,self.TRa,
				self.TSa,self.TTa,self.TUa,self.TVa,self.TWa,self.TXa,self.TYa,self.TZa,
				self.TAb,self.TBb,self.TCb,self.TDb,self.TEb,self.TFb,self.TGb,self.THb,self.TIb,
				self.TJb,self.TKb,self.TLb,self.TMb,self.TNb,self.TOb,self.TPb,self.TQb,self.TRb,
				self.TSb,self.TTb,self.TUb,self.TVb,self.TWb,self.TXb,self.TYb,self.TZb
			]
			for i in l:
				self.RandText.itemconfigure(i,text='')
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'TextLib.ClearScreen', subj='')
			
	def Destroy(self):
		exit()

	# ################################### #
	#######################################
	# ################################### #

def GenColorList():
	try:
		Filepath = path.abspath('Resources\\Text\\Colors\\')+'\\'
		return [file.replace(Filepath,'') for file in glob(Filepath+'*.txt')]
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'TextLib.GenColorList', subj='')
	
def ReadTextColors(file):
	try:
		Filepath = path.abspath('Resources\\Text\\Colors\\'+file)
		with open(Filepath, 'r') as f:
			ColorList = f.read().split('\n')
		return ColorList
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'TextLib.ReadTextColors', subj='')

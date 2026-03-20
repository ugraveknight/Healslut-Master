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
		self.ShadowOffset = 2
		try:
			Filepath = path.abspath('Resources\\Text\\Healslut Adjectives.txt')
			with open(Filepath, 'r') as a:
				self.alines=a.readlines()
			Filepath = path.abspath('Resources\\Text\\Healslut Subjects.txt')
			with open(Filepath, 'r') as s:
				self.slines=s.readlines()
			
			LengthofStandardWords = 12
			LengthofUnlimitedWords = 52
			
			# # # # # # # # # # # # #
			# The Background Border #
			self.ShadowWordsList = \
			[
				[
				self.RandText.create_text(self.x_cen+self.ShadowOffset,self.y_upr+self.ShadowOffset, text='',font=HP.FONT0(),justify=CENTER,fill='#000000'),
				self.RandText.create_text(self.x_cen-self.ShadowOffset,self.y_upr-self.ShadowOffset, text='',font=HP.FONT0(),justify=CENTER,fill='#000000'),
				self.RandText.create_text(self.x_cen-self.ShadowOffset,self.y_upr+self.ShadowOffset, text='',font=HP.FONT0(),justify=CENTER,fill='#000000'),
				self.RandText.create_text(self.x_cen+self.ShadowOffset,self.y_upr-self.ShadowOffset, text='',font=HP.FONT0(),justify=CENTER,fill='#000000'),
				],
				[
				self.RandText.create_text(self.x_cen+self.ShadowOffset,self.y_low+self.ShadowOffset, text='',font=HP.FONT0(),justify=CENTER,fill='#000000'),
				self.RandText.create_text(self.x_cen-self.ShadowOffset,self.y_low-self.ShadowOffset, text='',font=HP.FONT0(),justify=CENTER,fill='#000000'),
				self.RandText.create_text(self.x_cen-self.ShadowOffset,self.y_low+self.ShadowOffset, text='',font=HP.FONT0(),justify=CENTER,fill='#000000'),
				self.RandText.create_text(self.x_cen+self.ShadowOffset,self.y_low-self.ShadowOffset, text='',font=HP.FONT0(),justify=CENTER,fill='#000000'),
				],
			]
			for i in range(LengthofStandardWords+LengthofUnlimitedWords):
				t = \
				[
				self.RandText.create_text(0,0, text='',font=HP.FONT1(),justify=CENTER,fill='#000000'),
				self.RandText.create_text(0,0, text='',font=HP.FONT1(),justify=CENTER,fill='#000000'),
				self.RandText.create_text(0,0, text='',font=HP.FONT1(),justify=CENTER,fill='#000000'),
				self.RandText.create_text(0,0, text='',font=HP.FONT1(),justify=CENTER,fill='#000000'),
				]
				self.ShadowWordsList.append(t)
			
			# # # # # # # # # # #
			#  Low to Max words #
			self.StandardWordsList = \
			[
				self.RandText.create_text(self.x_cen,self.y_upr, text='',font=HP.FONT0(),justify=CENTER),
				self.RandText.create_text(self.x_cen,self.y_low, text='',font=HP.FONT0(),justify=CENTER)
			]
			self.StandardWordsList += [self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER) for i in range(LengthofStandardWords-2)]
			
			# # # # # # # # # # #
			#  Unlimited words  #
			self.UnlimitedWordsList = [self.RandText.create_text(0, 0, text='',font=HP.FONT1(),justify=CENTER) for i in range(LengthofUnlimitedWords)]
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
					
					self.ManageShadowWords(0,adjx1,self.x_cen,self.y_upr)
					self.ManageShadowWords(1,subx1,self.x_cen,self.y_low)
					
					self.RandText.itemconfigure(self.StandardWordsList[0],text=adjx1,fill=colorx1)
					self.RandText.itemconfigure(self.StandardWordsList[1],text=subx1,fill=colorx1)
					self.RandText.coords(self.StandardWordsList[0],self.x_cen,self.y_upr)
					self.RandText.coords(self.StandardWordsList[1],self.x_cen,self.y_low)
					self.RandText.tag_raise(self.StandardWordsList[0])
					self.RandText.tag_raise(self.StandardWordsList[1])
					
					
										
				if self.wordcount > 1:				# L+R words	
					rx = float(randint(int(self.x_rgt*.9),int(self.x_rgt*1.1)))
					ry = float(randint(int(self.y_cen*.9),int(self.y_cen*1.1)))	
					lx = float(randint(int(self.x_lef*.9),int(self.x_lef*1.1)))
					ly = float(randint(int(self.y_cen*.9),int(self.y_cen*1.1)))
					colory1 = self.GenColor()
					adjy1 = choice(self.alines).upper()
					suby1 = choice(self.slines).upper()
					
					self.ManageShadowWords(2,adjy1,lx,ly)
					self.ManageShadowWords(3,suby1,rx,ry)
					
					self.RandText.itemconfigure(self.StandardWordsList[2],text=adjy1,fill=colory1)
					self.RandText.itemconfigure(self.StandardWordsList[3],text=suby1,fill=colory1)
					self.RandText.coords(self.StandardWordsList[2],lx,ly)
					self.RandText.coords(self.StandardWordsList[3],rx,ry)
					self.RandText.tag_raise(self.StandardWordsList[2])
					self.RandText.tag_raise(self.StandardWordsList[3])
					
										
				if self.wordcount > 2:				#T+B extra words	
					colorx2 = self.GenColor()
					colorx3 = self.GenColor()
					adjx2 = choice(self.alines).upper()
					subx2 = choice(self.slines).upper()
					adjx3 = choice(self.alines).upper()
					subx3 = choice(self.slines).upper()
					Top_offset = randint(-30,30)
					
					self.ManageShadowWords(4,adjx2,self.x_cen+Top_offset   ,self.y_upr-68)
					self.ManageShadowWords(5,subx2,self.x_cen-Top_offset*-1,self.y_upr+20)
					self.ManageShadowWords(6,adjx3,self.x_cen+Top_offset   ,self.y_low-68)
					self.ManageShadowWords(7,subx3,self.x_cen-Top_offset*-1,self.y_low+20)
					
					self.RandText.itemconfigure(self.StandardWordsList[4],text=adjx2,fill=colorx2)
					self.RandText.itemconfigure(self.StandardWordsList[5],text=subx2,fill=colorx2)
					self.RandText.itemconfigure(self.StandardWordsList[6],text=adjx3,fill=colorx3)
					self.RandText.itemconfigure(self.StandardWordsList[7],text=subx3,fill=colorx3)
					self.RandText.coords(self.StandardWordsList[4],self.x_cen+Top_offset   ,self.y_upr-68)
					self.RandText.coords(self.StandardWordsList[5],self.x_cen-Top_offset*-1,self.y_upr+20)
					self.RandText.coords(self.StandardWordsList[6],self.x_cen+Top_offset   ,self.y_low-68)
					self.RandText.coords(self.StandardWordsList[7],self.x_cen-Top_offset*-1,self.y_low+20)
					self.RandText.tag_raise(self.StandardWordsList[4])
					self.RandText.tag_raise(self.StandardWordsList[5])
					self.RandText.tag_raise(self.StandardWordsList[6])
					self.RandText.tag_raise(self.StandardWordsList[7])
					
					
				if self.wordcount > 3:			#L+R extra words
					colory2 = self.GenColor()
					colory3 = self.GenColor()
					adjy2 = choice(self.alines).upper()
					suby2 = choice(self.slines).upper()
					adjy3 = choice(self.alines).upper()
					suby3 = choice(self.slines).upper()
					Lef_offset = randint(-30,30)
					Rgt_offset = randint(-30,30)
					
					self.ManageShadowWords(8,adjy2,lx+Lef_offset   ,ly-45)
					self.ManageShadowWords(9,suby2,lx+Lef_offset*-1,ly+18)
					self.ManageShadowWords(10,adjy3,rx+Rgt_offset   ,ry-45)
					self.ManageShadowWords(11,suby3,rx+Rgt_offset*-1,ry+18)
					
					self.RandText.itemconfigure(self.StandardWordsList[8],text=adjy2,fill=colory2)
					self.RandText.itemconfigure(self.StandardWordsList[9],text=suby2,fill=colory2)
					self.RandText.itemconfigure(self.StandardWordsList[10],text=adjy3,fill=colory3)
					self.RandText.itemconfigure(self.StandardWordsList[11],text=suby3,fill=colory3)
					self.RandText.coords(self.StandardWordsList[8],lx+Lef_offset   ,ly-45)
					self.RandText.coords(self.StandardWordsList[9],lx+Lef_offset*-1,ly+18)
					self.RandText.coords(self.StandardWordsList[10],rx+Rgt_offset   ,ry-45)
					self.RandText.coords(self.StandardWordsList[11],rx+Rgt_offset*-1,ry+18)
					self.RandText.tag_raise(self.StandardWordsList[8])
					self.RandText.tag_raise(self.StandardWordsList[9])
					self.RandText.tag_raise(self.StandardWordsList[10])
					self.RandText.tag_raise(self.StandardWordsList[11])
					
				if not self.wordcount > 4:
					self.maintext_var = False
				if self.wordcount > 5:
					self.UnleashWords()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'TextLib.UpdateText', subj='')
	
	def ManageShadowWords(self,i,LineText,X,Y):
		self.RandText.itemconfigure(self.ShadowWordsList[i][0],text=LineText)
		self.RandText.itemconfigure(self.ShadowWordsList[i][1],text=LineText)
		self.RandText.itemconfigure(self.ShadowWordsList[i][2],text=LineText)
		self.RandText.itemconfigure(self.ShadowWordsList[i][3],text=LineText)
		self.RandText.coords(self.ShadowWordsList[i][0],X-self.ShadowOffset,Y-self.ShadowOffset)
		self.RandText.coords(self.ShadowWordsList[i][1],X-self.ShadowOffset,Y+self.ShadowOffset)
		self.RandText.coords(self.ShadowWordsList[i][2],X+self.ShadowOffset,Y-self.ShadowOffset)
		self.RandText.coords(self.ShadowWordsList[i][3],X+self.ShadowOffset,Y+self.ShadowOffset)
		self.RandText.tag_raise(self.ShadowWordsList[i][0])
		self.RandText.tag_raise(self.ShadowWordsList[i][1])
		self.RandText.tag_raise(self.ShadowWordsList[i][2])
		self.RandText.tag_raise(self.ShadowWordsList[i][3])
		
	def UnleashWords(self):
		def RandX(): return randint(100,self.screenwidth-100)
		def RandY(): return randint(50,self.screenheight-50)
		def RandLineText(): return choice(self.alines).upper()+' '+choice(self.slines).upper()
		def CycleText(Bottom,Top):
			for tag in self.UnlimitedWordsList[Bottom:Top]:
				LineText = RandLineText()
				RandomX = RandX()
				RandomY = RandY()
				
				self.ManageShadowWords(self.UnlimitedWordsList.index(tag),LineText,RandomX,RandomY)
				
				self.RandText.itemconfigure(tag,text=LineText,fill=self.GenColor())
				self.RandText.coords(tag,RandomX,RandomY)
				self.RandText.tag_raise(tag)
				
		# ###################### #
		try:
			if self.InsaneWordsA == 1:
				self.InsaneWordsA = 2
				CycleText(12,18)
			elif self.InsaneWordsA == 2:
				self.InsaneWordsA = 3
				CycleText(18,24)
			elif self.InsaneWordsA == 3:
				self.InsaneWordsA = 4
				CycleText(24,30)
			elif self.InsaneWordsA == 4:
				self.InsaneWordsA = 1
				CycleText(30,36)
				
			if self.InsaneWordsB == 1:
				self.InsaneWordsB = 2
				CycleText(36,42)
			elif self.InsaneWordsB == 2:
				self.InsaneWordsB = 3
				CycleText(42,48)
			elif self.InsaneWordsB == 3:
				self.InsaneWordsB = 4
				CycleText(48,54)
			elif self.InsaneWordsB == 4:
				self.InsaneWordsB = 1
				CycleText(54,60)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'TextLib.UnleashWords', subj='')
			
	def ClearScreen(self):
		if HSDEBUG: print('ClearScreen')
		try:
			l = self.StandardWordsList + self.UnlimitedWordsList
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
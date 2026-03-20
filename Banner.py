from tkinter import *
from random import choice, randint
from time import time
from os import path
from PIL import Image, ImageTk
from traceback import format_exc
from win32gui import FindWindow, SetWindowLong
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE
import sys

import HealslutPackages as HP
from TextLibs import TextLibs

HSDEBUG = False

class Banner(Frame):
	def __init__(self, master, delay, dom, sub, humiliation, ColorList, 
					banwords, wordcount, tranbanr, homework, output, 
					display_rules, fontsize, c_images, c_txt, c_wordknt,
					c_CharSelect, c_hypno, *pargs):
		try:
			self.master = master
			self.screenwidth = self.master.winfo_screenwidth()
			self.screenheight = self.master.winfo_screenheight()
			self.delay = delay
			self.dom = dom
			self.sub = sub
			self.humiliation = humiliation
			self.ColorList = ColorList
			self.banwords = banwords
			self.wordcount = wordcount
			self.tranbanr = tranbanr
			self.homework = homework
			self.output = output
			self.display_rules = display_rules
			self.fontsize = fontsize
			self.c_images = c_images
			self.c_txt = c_txt
			self.c_wordknt = c_wordknt
			self.c_CharSelect = c_CharSelect
			self.c_hypno = c_hypno
			self.banner_var = 4		
			self.freshtext = False
			self.endtime = time()
			
			self.master.wm_attributes("-topmost", 1)
			self.master.wm_attributes("-transparentcolor", HP.TRANS_CLR())
			self.screen_width = self.screenwidth
			self.screen_height = self.screenheight
			
			self.x_cen = int(self.screenwidth  * .5)
			self.x_lef = int(self.screenwidth  * .4)
			self.x_rgt = int(self.screenwidth  * .6)
			self.y_cen = int(self.screenheight * .5)
			self.y_upr = int(self.screenheight * .33)
			self.y_low = int(self.screenheight * .66)
			
			self.master.geometry('%dx%d+%d+%d' % (self.screen_width, self.screen_height, 0, 0))
			self.TextWidth = self.screen_width-300
			self.master.overrideredirect(1)
			self.banner = Canvas(self.master, bg=HP.TRANS_CLR(), width=495, height=200,highlightthickness=0)
			self.banner.pack(fill=BOTH, expand=YES)
			
			shdow = 2
			self.BannerTexta = self.banner.create_text(self.screen_width/2+shdow, self.screen_height/1.3+shdow, text='', anchor=CENTER,font=HP.FONT0(),fill='#000000')
			self.BannerTextb = self.banner.create_text(self.screen_width/2-shdow, self.screen_height/1.3-shdow, text='', anchor=CENTER,font=HP.FONT0(),fill='#000000')
			self.BannerTextc = self.banner.create_text(self.screen_width/2+shdow, self.screen_height/1.3-shdow, text='', anchor=CENTER,font=HP.FONT0(),fill='#000000')
			self.BannerTextd = self.banner.create_text(self.screen_width/2-shdow, self.screen_height/1.3+shdow, text='', anchor=CENTER,font=HP.FONT0(),fill='#000000')
			self.BannerText = self.banner.create_text(self.screen_width/2, self.screen_height/1.3,anchor=CENTER, text='', font=HP.FONT0())
			
			self.maintexta = self.banner.create_text(self.screen_width*.5+shdow, self.screen_height*.4+shdow, text='', anchor=CENTER,font=HP.FONT4(),fill='#000000')
			self.maintextb = self.banner.create_text(self.screen_width*.5-shdow, self.screen_height*.4-shdow, text='', anchor=CENTER,font=HP.FONT4(),fill='#000000')
			self.maintextc = self.banner.create_text(self.screen_width*.5+shdow, self.screen_height*.4-shdow, text='', anchor=CENTER,font=HP.FONT4(),fill='#000000')
			self.maintextd = self.banner.create_text(self.screen_width*.5-shdow, self.screen_height*.4+shdow, text='', anchor=CENTER,font=HP.FONT4(),fill='#000000')
			self.maintext = self.banner.create_text(self.screen_width*.5, self.screen_height*.4, text='', anchor=CENTER,font=HP.FONT4())
			
			if self.display_rules == 2:
				self.banner.create_text(0-2,self.y_cen-2,text=self.output,font=(HP.GlobalFont(),self.fontsize),fill='Black',   justify=LEFT,anchor=W)
				self.banner.create_text(0+2,self.y_cen+2,text=self.output,font=(HP.GlobalFont(),self.fontsize),fill='Black',   justify=LEFT,anchor=W)
				self.banner.create_text(0-2,self.y_cen+2,text=self.output,font=(HP.GlobalFont(),self.fontsize),fill='Black',   justify=LEFT,anchor=W)
				self.banner.create_text(0+2,self.y_cen-2,text=self.output,font=(HP.GlobalFont(),self.fontsize),fill='Black',   justify=LEFT,anchor=W)
				self.banner.create_text(0,  self.y_cen,  text=self.output,font=(HP.GlobalFont(),self.fontsize),fill='hot pink',justify=LEFT,anchor=W)
			
			self.TextLibWrapper()
			self.RunOpaqBanner()
			self.master.after(1000,SetClickthrough)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'Banner', subj='')
	
	def TextLibWrapper(self):
		self.TL = TextLibs(self.banner,self.banwords,self.ColorList,False,
			self.wordcount,self.screenwidth,self.screenheight,
			self.x_cen,self.x_lef,self.x_rgt,self.y_cen,self.y_upr,self.y_low)
	
	def RunOpaqBanner(self):
			
			# The transparent Banner is definitely run at the Hypnotherapy layer...
			# So I am eventually going to have to figure out what all of this code 
			# does and destroy some of it? at least document it jesus what was I thinking...
			
			# in hindsight, Banner.py is a misnomer. This file should be called Opaque Layer.
	
		try:
			# exit condition
			if self.c_hypno.poll() == True:
				self.master.quit()
			
			if self.tranbanr == 0 and self.homework == 'Banner':
				self.banner_var+=1
				if self.banner_var >= 4:
					self.written_line = HP.SetWrittenLine(self.humiliation, self.dom, self.sub)
					self.banner_var = 0
					self.linecolor = choice(self.ColorList)
				
				self.banner.itemconfigure(self.BannerText,text=self.written_line.upper(),width=self.TextWidth,fill=self.linecolor)
				self.banner.itemconfigure(self.BannerTexta,text=self.written_line.upper(),width=self.TextWidth)
				self.banner.itemconfigure(self.BannerTextb,text=self.written_line.upper(),width=self.TextWidth)
				self.banner.itemconfigure(self.BannerTextc,text=self.written_line.upper(),width=self.TextWidth)
				self.banner.itemconfigure(self.BannerTextd,text=self.written_line.upper(),width=self.TextWidth)
			
			# this manages the wordknt macro, and on screen words when opaque
			if self.banwords == 0:
				self.TL.UpdateText(self.wordcount,True)
				if self.c_wordknt.poll() == True:
					while self.c_wordknt.poll():
						newcount = self.c_wordknt.recv()
					if self.wordcount != newcount:
						self.TL.ClearScreen()
						self.wordcount = newcount
				self.master.after(int(self.delay/2), self.TL.UpdateText(self.wordcount))
			
			'''
			# this is currently unused, pending the character selection functionality
			if self.c_CharSelect.poll() == True:
				self.c_CharSelect.recv()
				self.i = ImageTk.PhotoImage(Image.open('CharacterSelect.png'))
				self.CharSelect = self.banner.create_image(0,0, image=self.i)
			'''
			
			# # # # # # # # # # # # # # # # # # # # # #
			# This section plays to the $Text option. #
			
			# Check $Text Poll
			if self.c_txt.poll() == True:
				pipetext = self.c_txt.recv()
				text_count, sep, self.mytext = pipetext.partition(' ')
				self.endtime = time()+int(text_count)
				self.freshtext = True
			
			# Initalize and recolor
			if time() < self.endtime:
				self.linecolor = choice(self.ColorList)
				self.banner.itemconfigure(self.maintext, text=self.mytext,width=self.TextWidth,fill=self.linecolor)
				self.banner.itemconfigure(self.maintexta,text=self.mytext,width=self.TextWidth)
				self.banner.itemconfigure(self.maintextb,text=self.mytext,width=self.TextWidth)
				self.banner.itemconfigure(self.maintextc,text=self.mytext,width=self.TextWidth)
				self.banner.itemconfigure(self.maintextd,text=self.mytext,width=self.TextWidth)
			# Else, we remove the text
			elif self.freshtext == True:
				self.freshtext = False
				self.banner.itemconfigure(self.maintext, text='',width=self.TextWidth,fill=self.linecolor)
				self.banner.itemconfigure(self.maintexta,text='',width=self.TextWidth)
				self.banner.itemconfigure(self.maintextb,text='',width=self.TextWidth)
				self.banner.itemconfigure(self.maintextc,text='',width=self.TextWidth)
				self.banner.itemconfigure(self.maintextd,text='',width=self.TextWidth)
			
			self.master.lift()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'RunOpaqBanner', subj='')
		self.master.after(self.delay, self.RunOpaqBanner)
		
def create_banner(delay,dom,sub,humiliation,ColorList,banwords,
						wordcount,tranbanr,homework,output,
						display_rules,fontsize,c_images,c_txt,
						c_wordknt,c_CharSelect,c_hypno):
	try:
		root = Tk()
		root.geometry('%dx%d' % (root.winfo_screenwidth(), root.winfo_screenheight()))
		root.configure(background=HP.TRANS_CLR())
		root.title("Healslut Banner")
		e = Banner(root,delay,dom,sub,humiliation,ColorList,banwords,wordcount,tranbanr,
							homework,output,display_rules,fontsize,c_images,c_txt,c_wordknt,
							c_CharSelect,c_hypno)
		root.mainloop()
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'create_banner', subj='')

def SetClickthrough(windowname="Healslut Banner"):	#I want this to be in HP, but doesnt work when imported
	try:
		hwnd = FindWindow(None, windowname)
		if HSDEBUG: print('Cloaking Banner...', windowname, hwnd)
		windowStyles = WS_EX_LAYERED | WS_EX_TRANSPARENT
		SetWindowLong(hwnd, GWL_EXSTYLE, windowStyles)
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'Banner_SetClickthrough', subj='')
		
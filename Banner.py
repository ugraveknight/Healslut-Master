from tkinter import *
from random import choice, randint
from time import time
from os import path
from PIL import Image, ImageTk
from traceback import format_exc
from win32gui import FindWindow, SetWindowLong
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE

import HealslutPackages as HP

class Banner(Frame):
	def __init__(self, master, delay, dom, sub, humiliation, color_list, 
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
			self.color_list = color_list
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
			self.InsaneWordsA = 1
			self.InsaneWordsB = 1
			self.master.wm_attributes("-topmost", 1)
			self.master.wm_attributes("-transparentcolor", HP.TRANS_CLR_ALT())
			self.screen_width = self.screenwidth
			self.screen_height = self.screenheight
			self.master.geometry('%dx%d+%d+%d' % (self.screen_width, self.screen_height, 0, 0))
			self.TextWidth = self.screen_width-300
			self.master.overrideredirect(1)
			self.banner = Canvas(self.master, bg=HP.TRANS_CLR_ALT(), width=495, height=200,highlightthickness=0)
			self.banner.pack(fill=BOTH, expand=YES)
			self.tmp_banner = self.banner.create_text(0, 0, text='')
			self.maintext = self.banner.create_text(0, 0, text='')
			if self.display_rules == 2:
				self.banner.create_text(0, self.screen_height/2, text=self.output, font=("Impact", self.fontsize), 
							fill='hot pink',justify=LEFT, anchor=W)
			self.BuildText()
			self.RunOpaqBanner()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'Banner', subj='')
	
	def BuildText(self):
		if self.banwords == 0:
			Filepath = path.abspath('Resources\\Text\\Healslut Adjectives.txt')
			with open(Filepath, 'r') as a:
				self.alines=a.readlines()
			Filepath = path.abspath('Resources\\Text\\Healslut Subjects.txt')
			with open(Filepath, 'r') as s:
				self.slines=s.readlines()
				
			self.TopTextA = self.banner.create_text(0, 0, text='')
			self.TopTextB = self.banner.create_text(0, 0, text='')
			self.TopTextC = self.banner.create_text(0, 0, text='')
			self.BotTextA = self.banner.create_text(0, 0, text='')
			self.BotTextB = self.banner.create_text(0, 0, text='')
			self.BotTextC = self.banner.create_text(0, 0, text='')
			self.LefTextA = self.banner.create_text(0, 0, text='')
			self.LefTextB = self.banner.create_text(0, 0, text='')
			self.LefTextC = self.banner.create_text(0, 0, text='')
			self.RgtTextA = self.banner.create_text(0, 0, text='')
			self.RgtTextB = self.banner.create_text(0, 0, text='')
			self.RgtTextC = self.banner.create_text(0, 0, text='')
			
			self.TAa = self.banner.create_text(0, 0, text='')
			self.TBa = self.banner.create_text(0, 0, text='')
			self.TCa = self.banner.create_text(0, 0, text='')
			self.TDa = self.banner.create_text(0, 0, text='')
			self.TEa = self.banner.create_text(0, 0, text='')
			self.TFa = self.banner.create_text(0, 0, text='')
			self.TGa = self.banner.create_text(0, 0, text='')
			self.THa = self.banner.create_text(0, 0, text='')
			self.TIa = self.banner.create_text(0, 0, text='')
			self.TJa = self.banner.create_text(0, 0, text='')
			self.TKa = self.banner.create_text(0, 0, text='')
			self.TLa = self.banner.create_text(0, 0, text='')
			self.TMa = self.banner.create_text(0, 0, text='')
			self.TNa = self.banner.create_text(0, 0, text='')
			self.TOa = self.banner.create_text(0, 0, text='')
			self.TPa = self.banner.create_text(0, 0, text='')
			self.TQa = self.banner.create_text(0, 0, text='')
			self.TRa = self.banner.create_text(0, 0, text='')
			self.TSa = self.banner.create_text(0, 0, text='')
			self.TTa = self.banner.create_text(0, 0, text='')
			self.TUa = self.banner.create_text(0, 0, text='')
			self.TVa = self.banner.create_text(0, 0, text='')
			self.TWa = self.banner.create_text(0, 0, text='')
			self.TXa = self.banner.create_text(0, 0, text='')
			self.TYa = self.banner.create_text(0, 0, text='')
			self.TZa = self.banner.create_text(0, 0, text='')
			self.TAb = self.banner.create_text(0, 0, text='')
			self.TBb = self.banner.create_text(0, 0, text='')
			self.TCb = self.banner.create_text(0, 0, text='')
			self.TDb = self.banner.create_text(0, 0, text='')
			self.TEb = self.banner.create_text(0, 0, text='')
			self.TFb = self.banner.create_text(0, 0, text='')
			self.TGb = self.banner.create_text(0, 0, text='')
			self.THb = self.banner.create_text(0, 0, text='')
			self.TIb = self.banner.create_text(0, 0, text='')
			self.TJb = self.banner.create_text(0, 0, text='')
			self.TKb = self.banner.create_text(0, 0, text='')
			self.TLb = self.banner.create_text(0, 0, text='')
			self.TMb = self.banner.create_text(0, 0, text='')
			self.TNb = self.banner.create_text(0, 0, text='')
			self.TOb = self.banner.create_text(0, 0, text='')
			self.TPb = self.banner.create_text(0, 0, text='')
			self.TQb = self.banner.create_text(0, 0, text='')
			self.TRb = self.banner.create_text(0, 0, text='')
			self.TSb = self.banner.create_text(0, 0, text='')
			self.TTb = self.banner.create_text(0, 0, text='')
			self.TUb = self.banner.create_text(0, 0, text='')
			self.TVb = self.banner.create_text(0, 0, text='')
			self.TWb = self.banner.create_text(0, 0, text='')
			self.TXb = self.banner.create_text(0, 0, text='')
			self.TYb = self.banner.create_text(0, 0, text='')
			self.TZb = self.banner.create_text(0, 0, text='')
		
			self.x_cen = int(self.screenwidth*.5)
			self.x_lef = int(self.screenwidth*.4)
			self.x_rgt = int(self.screenwidth*.6)
			self.y_cen = int(self.screenheight*.5)
			self.y_upr = int(self.screenheight*.33)
			self.y_low = int(self.screenheight*.66)	
			
	def RunOpaqBanner(self):
		try:
			if self.c_hypno.poll() == True:
				self.master.quit()
			if self.tranbanr == 0 and self.homework == 'Banner':
				self.banner_var+=1
				if self.banner_var >= 4:
					self.written_line = HP.SetWrittenLine(self.humiliation, self.dom, self.sub)
					self.banner_var = 0
					self.linecolor = choice(self.color_list)
				self.banner.delete(self.tmp_banner)
				self.tmp_banner = self.banner.create_text(self.screen_width/2, self.screen_height/1.3, 
													text=self.written_line.upper(),width=self.TextWidth,anchor=CENTER,
													font=("Impact", 44), fill=self.linecolor)
			if self.banwords == 0:
				self.maintext_var = True
				self.update_text()
				if self.c_wordknt.poll() == True:
					self.wordcount = self.c_wordknt.recv()
					if not self.wordcount == 6:
						self.clear_screen()
				self.master.after(int(self.delay/2), self.update_text)
			if self.c_CharSelect.poll() == True:
				self.c_CharSelect.recv()
				self.i = ImageTk.PhotoImage(Image.open('CharacterSelect.png'))
				self.CharSelect = self.banner.create_image(0,0, image=self.i)
			if self.c_txt.poll() == True:
				pipetext = self.c_txt.recv()
				text_count, sep, self.mytext = pipetext.partition(' ')
				self.endtime = time()+int(text_count)
				self.freshtext = True
			if time() < self.endtime:
				self.linecolor = choice(self.color_list)
				self.banner.delete(self.maintext)
				self.maintext = self.banner.create_text(self.screen_width*.5, self.screen_height*.4, 
													text=self.mytext,width=self.TextWidth,anchor=CENTER,
													font=("Impact", 50), fill=self.linecolor)
			elif self.freshtext == True:
				self.freshtext = False
				self.banner.delete(self.maintext)
				self.maintext = self.banner.create_text(self.screen_width*.5, self.screen_height*.4, 
													text=' ')
			self.master.lift()
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'RunOpaqBanner', subj='')
		self.master.after(self.delay, self.RunOpaqBanner)
		
	def GenColor(self): return choice(self.color_list)
	def update_text(self):
		try:
			if self.wordcount > 0:
				if self.maintext_var == True:
					colorx1 = self.GenColor()
					adjx1 = choice(self.alines).upper()
					subx1 = choice(self.slines).upper()	
					self.banner.delete(self.TopTextA)
					self.banner.delete(self.BotTextA)
					self.TopTextA = self.banner.create_text(self.x_cen,self.y_upr,text=adjx1,font=HP.FONT0(),fill=colorx1,justify=CENTER)
					self.BotTextA = self.banner.create_text(self.x_cen,self.y_low,text=subx1,font=HP.FONT0(),fill=colorx1,justify=CENTER)
				if self.wordcount > 1:				# L+R words	
					lx = float(randint(int(self.x_lef*.9),int(self.x_lef*1.1)))
					ly = float(randint(int(self.y_cen*.9),int(self.y_cen*1.1)))
					rx = float(randint(int(self.x_rgt*.9),int(self.x_rgt*1.1)))
					ry = float(randint(int(self.y_cen*.9),int(self.y_cen*1.1)))
					colory1 = self.GenColor()	
					adjy1 = choice(self.alines).upper()
					suby1 = choice(self.slines).upper()
					
					self.banner.delete(self.RgtTextA)
					self.banner.delete(self.LefTextA)
					self.LefTextA = self.banner.create_text(lx, ly,text=adjy1,font=HP.FONT1(),fill=colory1,justify=CENTER)
					self.RgtTextA = self.banner.create_text(rx, ry,text=suby1,font=HP.FONT1(),fill=colory1,justify=CENTER)
				if self.wordcount > 2:				#T+B extra words	
					colorx2 = self.GenColor()
					colorx3 = self.GenColor()
					adjx2 = choice(self.alines).upper()
					subx2 = choice(self.slines).upper()
					adjx3 = choice(self.alines).upper()
					subx3 = choice(self.slines).upper()
					
					self.banner.delete(self.TopTextB)
					self.banner.delete(self.TopTextC)
					self.banner.delete(self.BotTextB)
					self.banner.delete(self.BotTextC)						
					Top_offset = self.x_cen+randint(-30,30)
					self.TopTextB = self.banner.create_text(Top_offset   ,self.y_upr-68,text=adjx2,font=HP.FONT2(),fill=colorx2,justify=CENTER)
					self.TopTextC = self.banner.create_text(Top_offset*-1,self.y_upr+20,text=subx2,font=HP.FONT2(),fill=colorx2,justify=CENTER)
					self.BotTextB = self.banner.create_text(Top_offset   ,self.y_low+-68,text=adjx3,font=HP.FONT2(),fill=colorx3,justify=CENTER)
					self.BotTextC = self.banner.create_text(Top_offset*-1,self.y_low+20,text=subx3,font=HP.FONT2(),fill=colorx3,justify=CENTER)	
				if self.wordcount > 3:			#L+R extra words
					colory2 = self.GenColor()
					colory3 = self.GenColor()
					adjy2 = choice(self.alines).upper()
					suby2 = choice(self.slines).upper()
					adjy3 = choice(self.alines).upper()
					suby3 = choice(self.slines).upper()
					
					self.banner.delete(self.RgtTextB)
					self.banner.delete(self.RgtTextC)
					self.banner.delete(self.LefTextB)
					self.banner.delete(self.LefTextC)
					Lef_offset = lx+randint(-30,30)
					Rgt_offset = rx+randint(-30,30)
					self.RgtTextB = self.banner.create_text(Rgt_offset   ,ry-45,text=adjy3,font=HP.FONT3(),fill=colory3,justify=CENTER)
					self.RgtTextC = self.banner.create_text(Rgt_offset*-1,ry+18,text=suby3,font=HP.FONT3(),fill=colory3,justify=CENTER)
					self.LefTextB = self.banner.create_text(Lef_offset   ,ly-45,text=adjy2,font=HP.FONT3(),fill=colory2,justify=CENTER)
					self.LefTextC = self.banner.create_text(Lef_offset*-1,ly+18,text=suby2,font=HP.FONT3(),fill=colory2,justify=CENTER)
				if not self.wordcount > 4:
					self.maintext_var = False
				if self.wordcount > 5:
					self.UnleashWords()	
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'banner.update_text', subj='')
	
	def UnleashWords(self):
		def RandX(): return randint(100,self.screenwidth-100)
		def RandY(): return randint(50,self.screenheight-50)
		def LineText(): return choice(self.alines).upper()+' '+choice(self.slines).upper()
		# ###################### #
		try:
			if self.InsaneWordsA == 1:
				self.InsaneWordsA = 2
				self.banner.delete(self.TAa)
				self.banner.delete(self.TBa)
				self.banner.delete(self.TCa)
				self.banner.delete(self.TDa)
				self.banner.delete(self.TEa)
				self.banner.delete(self.TFa)
				self.banner.delete(self.TGa)
				self.banner.delete(self.THa)
				self.banner.delete(self.TIa)
				self.TAa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TBa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TCa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TDa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TEa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TFa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TGa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.THa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TIa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)

			elif self.InsaneWordsA == 2:
				self.InsaneWordsA = 3
				self.banner.delete(self.TJa)
				self.banner.delete(self.TKa)
				self.banner.delete(self.TLa)
				self.banner.delete(self.TMa)
				self.banner.delete(self.TNa)
				self.banner.delete(self.TOa)
				self.banner.delete(self.TPa)
				self.banner.delete(self.TQa)
				self.banner.delete(self.TRa)
				self.TJa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TKa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TLa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TMa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TNa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TOa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TPa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TQa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TRa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)

			elif self.InsaneWordsA == 3:
				self.InsaneWordsA = 1
				self.banner.delete(self.TSa)
				self.banner.delete(self.TTa)
				self.banner.delete(self.TUa)
				self.banner.delete(self.TVa)
				self.banner.delete(self.TWa)
				self.banner.delete(self.TXa)
				self.banner.delete(self.TYa)
				self.banner.delete(self.TZa)
				self.TSa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TTa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TUa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TVa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TWa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TXa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TYa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TZa = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
			
			if self.InsaneWordsB == 1:
				self.InsaneWordsB = 2
				self.banner.delete(self.TAb)
				self.banner.delete(self.TBb)
				self.banner.delete(self.TCb)
				self.banner.delete(self.TDb)
				self.banner.delete(self.TEb)
				self.banner.delete(self.TFb)
				self.banner.delete(self.TGb)
				self.banner.delete(self.THb)
				self.banner.delete(self.TIb)
				self.TAb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TBb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TCb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TDb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TEb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TFb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TGb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.THb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)
				self.TIb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT1(),fill=self.GenColor(),justify=CENTER)

			elif self.InsaneWordsB == 2:
				self.InsaneWordsB = 3
				self.banner.delete(self.TJb)
				self.banner.delete(self.TKb)
				self.banner.delete(self.TLb)
				self.banner.delete(self.TMb)
				self.banner.delete(self.TNb)
				self.banner.delete(self.TOb)
				self.banner.delete(self.TPb)
				self.banner.delete(self.TQb)
				self.banner.delete(self.TRb)
				self.TJb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TKb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TLb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TMb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TNb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TOb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TPb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TQb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)
				self.TRb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT2(),fill=self.GenColor(),justify=CENTER)

			elif self.InsaneWordsB == 3:
				self.InsaneWordsB = 1
				self.banner.delete(self.TSb)
				self.banner.delete(self.TTb)
				self.banner.delete(self.TUb)
				self.banner.delete(self.TVb)
				self.banner.delete(self.TWb)
				self.banner.delete(self.TXb)
				self.banner.delete(self.TYb)
				self.banner.delete(self.TZb)
				self.TSb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TTb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TUb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TVb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TWb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TXb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TYb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
				self.TZb = self.banner.create_text(RandX(),RandY(),text=LineText(),font=HP.FONT3(),fill=self.GenColor(),justify=CENTER)
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'banner.UnleashWords', subj='')
			
	def clear_screen(self):
		if self.banwords == 0:
			self.banner.delete(self.TAa)
			self.banner.delete(self.TBa)
			self.banner.delete(self.TCa)
			self.banner.delete(self.TDa)
			self.banner.delete(self.TEa)
			self.banner.delete(self.TFa)
			self.banner.delete(self.TGa)
			self.banner.delete(self.THa)
			self.banner.delete(self.TIa)
			self.banner.delete(self.TJa)
			self.banner.delete(self.TKa)
			self.banner.delete(self.TLa)
			self.banner.delete(self.TMa)
			self.banner.delete(self.TNa)
			self.banner.delete(self.TOa)
			self.banner.delete(self.TPa)
			self.banner.delete(self.TQa)
			self.banner.delete(self.TRa)
			self.banner.delete(self.TSa)
			self.banner.delete(self.TTa)
			self.banner.delete(self.TUa)
			self.banner.delete(self.TVa)
			self.banner.delete(self.TWa)
			self.banner.delete(self.TXa)
			self.banner.delete(self.TYa)
			self.banner.delete(self.TZa)
			self.banner.delete(self.TAb)
			self.banner.delete(self.TBb)
			self.banner.delete(self.TCb)
			self.banner.delete(self.TDb)
			self.banner.delete(self.TEb)
			self.banner.delete(self.TFb)
			self.banner.delete(self.TGb)
			self.banner.delete(self.THb)
			self.banner.delete(self.TIb)
			self.banner.delete(self.TJb)
			self.banner.delete(self.TKb)
			self.banner.delete(self.TLb)
			self.banner.delete(self.TMb)
			self.banner.delete(self.TNb)
			self.banner.delete(self.TOb)
			self.banner.delete(self.TPb)
			self.banner.delete(self.TQb)
			self.banner.delete(self.TRb)
			self.banner.delete(self.TSb)
			self.banner.delete(self.TTb)
			self.banner.delete(self.TUb)
			self.banner.delete(self.TVb)
			self.banner.delete(self.TWb)
			self.banner.delete(self.TXb)
			self.banner.delete(self.TYb)
			self.banner.delete(self.TZb)
			self.TAa = self.banner.create_text(0, 0, text='')
			self.TBa = self.banner.create_text(0, 0, text='')
			self.TCa = self.banner.create_text(0, 0, text='')
			self.TDa = self.banner.create_text(0, 0, text='')
			self.TEa = self.banner.create_text(0, 0, text='')
			self.TFa = self.banner.create_text(0, 0, text='')
			self.TGa = self.banner.create_text(0, 0, text='')
			self.THa = self.banner.create_text(0, 0, text='')
			self.TIa = self.banner.create_text(0, 0, text='')
			self.TJa = self.banner.create_text(0, 0, text='')
			self.TKa = self.banner.create_text(0, 0, text='')
			self.TLa = self.banner.create_text(0, 0, text='')
			self.TMa = self.banner.create_text(0, 0, text='')
			self.TNa = self.banner.create_text(0, 0, text='')
			self.TOa = self.banner.create_text(0, 0, text='')
			self.TPa = self.banner.create_text(0, 0, text='')
			self.TQa = self.banner.create_text(0, 0, text='')
			self.TRa = self.banner.create_text(0, 0, text='')
			self.TSa = self.banner.create_text(0, 0, text='')
			self.TTa = self.banner.create_text(0, 0, text='')
			self.TUa = self.banner.create_text(0, 0, text='')
			self.TVa = self.banner.create_text(0, 0, text='')
			self.TWa = self.banner.create_text(0, 0, text='')
			self.TXa = self.banner.create_text(0, 0, text='')
			self.TYa = self.banner.create_text(0, 0, text='')
			self.TZa = self.banner.create_text(0, 0, text='')
			self.TAb = self.banner.create_text(0, 0, text='')
			self.TBb = self.banner.create_text(0, 0, text='')
			self.TCb = self.banner.create_text(0, 0, text='')
			self.TDb = self.banner.create_text(0, 0, text='')
			self.TEb = self.banner.create_text(0, 0, text='')
			self.TFb = self.banner.create_text(0, 0, text='')
			self.TGb = self.banner.create_text(0, 0, text='')
			self.THb = self.banner.create_text(0, 0, text='')
			self.TIb = self.banner.create_text(0, 0, text='')
			self.TJb = self.banner.create_text(0, 0, text='')
			self.TKb = self.banner.create_text(0, 0, text='')
			self.TLb = self.banner.create_text(0, 0, text='')
			self.TMb = self.banner.create_text(0, 0, text='')
			self.TNb = self.banner.create_text(0, 0, text='')
			self.TOb = self.banner.create_text(0, 0, text='')
			self.TPb = self.banner.create_text(0, 0, text='')
			self.TQb = self.banner.create_text(0, 0, text='')
			self.TRb = self.banner.create_text(0, 0, text='')
			self.TSb = self.banner.create_text(0, 0, text='')
			self.TTb = self.banner.create_text(0, 0, text='')
			self.TUb = self.banner.create_text(0, 0, text='')
			self.TVb = self.banner.create_text(0, 0, text='')
			self.TWb = self.banner.create_text(0, 0, text='')
			self.TXb = self.banner.create_text(0, 0, text='')
			self.TYb = self.banner.create_text(0, 0, text='')
			self.TZb = self.banner.create_text(0, 0, text='')
			
def create_banner(delay,dom,sub,humiliation,color_list,banwords,
						wordcount,tranbanr,homework,output,
						display_rules,fontsize,c_images,c_txt,
						c_wordknt,c_CharSelect,c_hypno):
	try:
		root = Tk()
		root.geometry('%dx%d' % (root.winfo_screenwidth(), root.winfo_screenheight()))
		root.configure(background=HP.TRANS_CLR_ALT())
		root.title("Healslut Banner")
		SetClickthrough()
		e = Banner(root,delay,dom,sub,humiliation,color_list,banwords,wordcount,tranbanr,
							homework,output,display_rules,fontsize,c_images,c_txt,c_wordknt,
							c_CharSelect,c_hypno)
		root.mainloop()
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'create_banner', subj='')

def SetClickthrough(windowname="Healslut Banner"):	#I want this to be in HP, but doesnt work when imported
	try:
		hwnd = FindWindow(None, windowname)
		windowStyles = WS_EX_LAYERED | WS_EX_TRANSPARENT
		SetWindowLong(hwnd, GWL_EXSTYLE, windowStyles)
	except Exception as e:
		HP.HandleError(format_exc(2), e, 'Banner_SetClickthrough', subj='')		

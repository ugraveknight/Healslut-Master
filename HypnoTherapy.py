from tkinter import *
import win32gui, win32con, win32api

from PIL import Image, ImageTk
from itertools import cycle
import glob
import random
import atexit
import subprocess
from datetime import datetime, timedelta
import time
from functools import partial
import pywintypes
import playsound
import multiprocessing as mp
import cv2



class Hypnotherapy(Frame):
	def __init__(self, master, image_files, delay, opacity, game, 
				homework, wordcount, hypno, dom, sub, pinup, banwords,
				tranbanr, s_rulename, fontsize, display_rules, c_rules,
				c_vid, c_txt, c_homework, c_hypno, *pargs):
		Frame.__init__(self, master, *pargs)
		self.master = master
		self.delay = delay
		self.opacity = opacity
		self.game = game
		self.homework = homework
		self.wordcount = wordcount
		self.remaining_work = 0
		self.user_line = ''
		self.doing_homework=False
		self.playingvideo = False
		self.vs = None
		self.nexthomework_time=datetime.now()+timedelta(seconds=5)
		self.c_hypno = c_hypno
		self.enable_hypno = hypno
		self.prefer_dom = dom
		self.prefer_sub = sub
		self.pinupvar = pinup
		self.banwords = banwords
		self.tranbanr = tranbanr
		self.c_vid = c_vid
		self.c_txt = c_txt
		self.c_homework = c_homework
		
		self.s_rulename = s_rulename
		self.fontsize = fontsize
		self.display_rules = display_rules
		self.c_rules = c_rules
		
		self.master.overrideredirect(1)
		self.make_background()
		self.formatgif()
		self.build_ports()
		
		self.build_rules()
		self.pinup(image_files)
		self.setup_text()
		self.updategif()
		
	def make_background(self):
		self.x_center = int(self.master.winfo_screenwidth()*.5)
		self.x_left = int(self.master.winfo_screenwidth()*.4)
		self.x_right = int(self.master.winfo_screenwidth()*.6)
		self.y_center = int(self.master.winfo_screenheight()*.5)
		self.y_upper = int(self.master.winfo_screenheight()*.33)
		self.y_lower = int(self.master.winfo_screenheight()*.66)
		
		self.bg = Canvas(self, highlightthickness=0)
		self.fg_x = self.master.winfo_screenwidth()/2
		self.fg_y = self.master.winfo_screenheight()/2
		
		if self.enable_hypno == 1:
			self.image = Image.open('Resources\\Hypno Gif\\hypno1.gif')
			self.img_copy = self.image.copy()
			self.bg_image = ImageTk.PhotoImage(self.image)
			self.bg.gif_create = self.bg.create_image(self.fg_x, self.fg_y, image=self.bg_image)
		else:
			self.bg.config(bg='#000001')
		self.bg.pack(fill=BOTH, expand=YES)
		
	def formatgif(self):
		imagelist = [
					'hypno1.gif', 'hypno2.gif', 'hypno3.gif', 'hypno4.gif', 'hypno5.gif',
					'hypno6.gif', 'hypno7.gif', 'hypno8.gif', 'hypno9.gif', 'hypno10.gif'
					]
		self.gifcycle = cycle(imagelist)
		
	def build_ports(self):
		self.master.wm_attributes("-transparentcolor", "#000001")
		if self.game == 'OW':
			self.bg.left_port = Canvas(self.bg, bg='#000001', width=495, height=200,
								highlightthickness=0)
			self.bg.left_port.pack()
			self.bg.left_port.place(relx=0, rely=1, anchor=SW)
		self.bg.right_port = Canvas(self.bg, bg='#000001', width=50, height=255,
								highlightthickness=0)
		self.bg.right_port.place(relx=1, rely=.5, anchor=E)	

	def build_rules(self):
		self.output = ''
		with open('Resources\\Healslut Games\\'+self.s_rulename+' Rules.txt', 'r') as f:
			lines = f.readlines()
			for line in lines:
				self.output = self.output+line
	
	def setup_text(self):
		with open('Resources\\Text\\Healslut Adjectives.txt', 'r') as a:
			self.alines=a.readlines()
		with open('Resources\\Text\\Healslut Subjects.txt', 'r') as s:
			self.slines=s.readlines()
		
		self.tmp_top_text = self.bg.create_text(self.x_center, self.y_upper,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
		self.tmp_top_texta = self.bg.create_text(self.x_center, self.y_upper,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
		self.tmp_top_textb = self.bg.create_text(self.x_center, self.y_upper,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
				
		self.tmp_bot_text = self.bg.create_text(self.x_center, self.y_lower,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
		self.tmp_bot_texta = self.bg.create_text(self.x_center, self.y_lower,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
		self.tmp_bot_textb = self.bg.create_text(self.x_center, self.y_lower,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
				
		self.tmp_left_text = self.bg.create_text(self.x_center, self.y_center,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
		self.tmp_left_texta = self.bg.create_text(self.x_center, self.y_center,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
		self.tmp_left_textb = self.bg.create_text(self.x_center, self.y_center,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
				
		self.tmp_right_text = self.bg.create_text(self.x_center, self.y_center,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
		self.tmp_right_texta = self.bg.create_text(self.x_center, self.y_center,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
		self.tmp_right_textb = self.bg.create_text(self.x_center, self.y_center,
				text='', font=("Impact", 44), anchor=CENTER, justify=CENTER)
				
		if self.display_rules == 1:
			self.bg.create_text(0, self.y_center, text=self.output, font=("Impact", self.fontsize), fill='hot pink',
						justify=LEFT, anchor=W)
		
		
		
		self.slides()
		
		
	def pinup(self,image_files):
		with open('Resources\\Text\\Humiliation.txt', 'r') as f:
			self.humiliation = f.readlines()
		self.color_list = []
		with open('Resources\\Text\\Text Colors.txt', 'r') as f:
			colors = f.readlines()
			for line in colors:
				self.color_list.append(line.strip('\n'))
		dom = self.prefer_dom
		sub = self.prefer_sub
		delay = self.delay
		humiliation = self.humiliation
		banwords = self.banwords
		color_list = self.color_list
		wordcount = self.wordcount
		tranbanr = self.tranbanr
		homework = self.homework
		c_images, self.p_images = mp.Pipe()
		c_hypno = self.c_hypno
		mp.Process(target=create_banner, args=(delay,dom,sub,humiliation,
							color_list,banwords,wordcount,tranbanr,homework,
							c_images,self.c_txt,c_hypno)).start()
		if self.pinupvar == 1:
			self.pinups = [(PhotoImage(file=image))
							  for image in image_files]
			img_object = random.choice(self.pinups)
			self.bg.fg = self.bg.create_image(self.x_center, self.y_center, image=img_object)
		else:
			self.bg.fg = self.bg.create_image(self.x_center, self.y_center, image='')
		
		if self.homework == 'Banner':
			self.p_images.send(True)
	
	def slides(self):
		if self.pinupvar == 1 and not self.playingvideo == True:
			img_object = random.choice(self.pinups)
			self.bg.itemconfig(self.bg.fg, image=img_object)
		if self.c_vid.poll() == True or self.playingvideo == True:
			if self.c_vid.poll() == True:
				self.video_filename = self.c_vid.recv()
				self.videostarttime = datetime.now()
			self.playingvideo = True
			self.clear_screen()
			self.set_video()
			self.after(25, self.slides)
		else:
			self.maintext_var = True
			if self.banwords == 1:
				self.update_text()
				self.after(int(self.delay/2), self.update_text)				
			self.after(self.delay, self.slides)
		if not self.doing_homework==True:
			self.breathe_transp()
		self.assign_homework()	
		
			
	def clear_screen(self):
		self.bg.delete(self.tmp_top_text)
		self.bg.delete(self.tmp_top_texta)
		self.bg.delete(self.tmp_top_textb)
		self.bg.delete(self.tmp_bot_text)
		self.bg.delete(self.tmp_bot_texta)
		self.bg.delete(self.tmp_bot_textb)
		self.bg.delete(self.tmp_left_text)
		self.bg.delete(self.tmp_left_texta)
		self.bg.delete(self.tmp_left_textb)
		self.bg.delete(self.tmp_right_text)
		self.bg.delete(self.tmp_right_texta)
		self.bg.delete(self.tmp_right_textb)
		self.tmp_top_text = self.bg.create_text(0, 0, text='')
		self.tmp_top_texta = self.bg.create_text(0, 0, text='')
		self.tmp_top_textb = self.bg.create_text(0, 0, text='')
		self.tmp_bot_text = self.bg.create_text(0, 0, text='')
		self.tmp_bot_texta = self.bg.create_text(0, 0, text='')
		self.tmp_bot_textb = self.bg.create_text(0, 0, text='')
		self.tmp_left_text = self.bg.create_text(0, 0, text='')
		self.tmp_left_texta = self.bg.create_text(0, 0, text='')
		self.tmp_left_textb = self.bg.create_text(0, 0, text='')
		self.tmp_right_text = self.bg.create_text(0, 0, text='')
		self.tmp_right_texta = self.bg.create_text(0, 0, text='')
		self.tmp_right_textb = self.bg.create_text(0, 0, text='')
		
	def set_video(self):
		self.playingvideo = True
		if self.doing_homework == True:
			self.bg.right_port.config(bg='#000000')
		else:
			self.bg.right_port.config(bg='#000001')
		if self.vs == None:
			self.vs = cv2.VideoCapture(self.video_filename) # capture video frames, 0 is your default video camera
			self.current_image = None  # current image from the camera
		ok, frame = self.vs.read()  # read frame from video stream
		if ok:
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
			self.current_image = Image.fromarray(cv2image)  # convert image for PIL
			
			self.imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter 
			self.bg.itemconfig(self.bg.fg, image=self.imgtk)
			del frame
			del cv2image
		else:
			self.clear_screen()
			del self.current_image
			del self.imgtk
			self.vs.release()
			self.vs = None
			self.playingvideo = False
			print(datetime.now()-self.videostarttime)
		
		
	def assign_homework(self):
		if self.homework == "Never":
			self.doing_homework == False
		elif self.homework == "Not Often":
			if self.nexthomework_time < datetime.now():
					self.nexthomework_time=datetime.now()+timedelta(seconds=90)
					self.remaining_work = self.remaining_work+random.randint(1,2)
				
		elif self.homework == "Often": 
			if self.nexthomework_time < datetime.now():
					self.nexthomework_time=datetime.now()+timedelta(seconds=60)
					self.remaining_work = self.remaining_work+random.randint(2,4)
		
		elif self.homework == "Very Often":
			if self.nexthomework_time < datetime.now():
					self.nexthomework_time=datetime.now()+timedelta(seconds=45)
					self.remaining_work = self.remaining_work+random.randint(2,4)
		elif self.homework == 'Always':
			self.remaining_work = 20
		if self.c_homework.poll() == True:
			self.remaining_work = self.c_homework.recv()
			print('homework recieved', self.remaining_work)
		self.do_homework()
		
	def do_homework(self):
		if self.remaining_work > 0 and self.doing_homework == False:
			print('homework=', self.remaining_work)
			self.doing_homework=True
			self.master.overrideredirect(1)
			width, height =1000,150
			screen_width = self.master.winfo_screenwidth()
			screen_height = self.master.winfo_screenheight()
			x = (screen_width/2) - (width/2)
			y = (screen_height/2) - (height/2)
			
			if self.do_homework == 'Always':
				oldtop = self.top
			self.master.wm_attributes("-transparentcolor", "#000000")
			self.master.attributes('-alpha', 1)
			self.bg.right_port.config(bg='#000000')
			self.bg.right_port.place(relx=1, rely=.5, anchor=E)	
			if self.enable_hypno == 0:
				self.bg.config(bg='#000000')
			if self.game == 'OW':
				self.bg.left_port.config(bg='#000000')	
			self.top = Toplevel(self.master, bg='gray30')
			self.top.overrideredirect(1)
			self.top.title('Write For Me...')
			self.top.geometry('%dx%d+%d+%d' % (width, height, x, y))
			self.top.wm_attributes("-topmost", 1)
			remove_clickthrough()
			
			if self.do_homework == 'Always':
				oldtop.destroy()
			
			
			self.written_line = set_written_line(self.humiliation, self.prefer_dom, self.prefer_sub)
			msg1 = Label(self.top, text='"'+self.written_line.lower()+'"', font=('Arial', 38, 'italic'), anchor=CENTER, bg='gray30')
			msg1.pack(fill=BOTH)

			self.e = Entry(self.top, font=('Arial', 38, 'italic'))
			self.e.pack()
			self.top.bind('<Return>',partial(self.getbox)) 
			self.remaining_work-=1
			
			self.top.lift()
			self.e.focus_set()
			self.e.focus()

		if self.doing_homework == False:
			self.master.wm_attributes("-transparentcolor", "#000001")
			if self.game == 'OW':
				self.bg.left_port.config(bg='#000001')
			self.bg.config(bg='#000001')
			self.bg.right_port.config(bg='#000001')
			
			set_clickthrough()
		if self.doing_homework==True:
			self.top.lift()
			self.e.focus_set()
		
	def getbox(self,event):
		self.user_line = self.e.get()
		self.e.delete(0, END)
		desired_var = self.written_line.lower().strip()
		input_var = self.user_line.lower().strip()
		if input_var == desired_var:
			self.user_line=''
			if self.homework == 'Always':
				self.do_homework()
			else:
				self.do_homework()
				self.top.destroy() 
			self.doing_homework=False
		elif '[]' in input_var:
			self.remaining_work = 0
			self.do_homework()
			self.top.destroy() 
			self.doing_homework=False
		else:
			try:
				playsound.playsound('Resources\\Audio\\Punishment Buzz.mp3', False)
			except Exception:
				pass
		
	def update_text(self):
		if self.wordcount > 0:
			if self.maintext_var == True:
				if self.doing_homework==True:
					colorx1 = '#000000'
				else:
					colorx1 = random.choice(self.color_list)
				
				adjx1 = random.choice(self.alines).upper()
				subx1 = random.choice(self.slines).upper()	
				self.bg.delete(self.tmp_top_text)
				self.bg.delete(self.tmp_bot_text)
				
				self.tmp_top_text = self.bg.create_text(self.x_center, self.y_upper, 
										text=adjx1, font=("Impact", 44), anchor=CENTER, 
										justify=CENTER, fill=colorx1)
								
				self.tmp_bot_text = self.bg.create_text(self.x_center, self.y_lower, 
										text=subx1, font=("Impact", 44), anchor=CENTER, 
										justify=CENTER, fill=colorx1)
									
			if self.wordcount > 1:				# L+R words	
				if self.doing_homework==True:
					colory1 = '#000000'
				else:
					colory1 = random.choice(self.color_list)
					
				left_x_value = float(random.randint(
								int(self.x_left*.9),
								int(self.x_left*1.1)))
				left_y_value = float(random.randint(
								int(self.y_center*.9),
								int(self.y_center*1.1)))
				right_x_value = float(random.randint(
								int(self.x_right*.9),
								int(self.x_right*1.1)))
				right_y_value = float(random.randint(
								int(self.y_center*.9),
								int(self.y_center*1.1)))
								
				adjy1 = random.choice(self.alines).upper()
				suby1 = random.choice(self.slines).upper()
				self.bg.delete(self.tmp_right_text)
				self.bg.delete(self.tmp_left_text)
				self.tmp_left_text = self.bg.create_text(left_x_value, left_y_value, 
										text=adjy1, font=("Impact", 28), anchor=CENTER, 
										justify=CENTER, fill=colory1)
									
				self.tmp_right_text = self.bg.create_text(right_x_value, right_y_value, 
										text=suby1, font=("Impact", 28), anchor=CENTER, 
										justify=CENTER, fill=colory1)
										
			if self.wordcount > 2:				#T+B extra words	
				if self.doing_homework==True:
					colorx2, colorx3 = '#000000','#000000'
				else:
					colorx2 = random.choice(self.color_list)
					colorx3 = random.choice(self.color_list)
					
				adjx2 = random.choice(self.alines).upper()
				subx2 = random.choice(self.slines).upper()
				adjx3 = random.choice(self.alines).upper()
				subx3 = random.choice(self.slines).upper()
				
				self.bg.delete(self.tmp_top_texta)
				self.bg.delete(self.tmp_top_textb)	
			
				top_offset = random.randint(-30,30)
				self.tmp_top_texta = self.bg.create_text(self.x_center+top_offset, self.y_upper-68, 
										text=adjx2, font=("Impact", 20), anchor=CENTER, 
										justify=CENTER, fill=colorx2)
				self.tmp_top_textb = self.bg.create_text(self.x_center+(top_offset)*-1, self.y_upper+20, 
										text=subx2, font=("Impact", 20), anchor=CENTER, 
										justify=CENTER, fill=colorx2)
				
				self.bg.delete(self.tmp_bot_texta)
				self.bg.delete(self.tmp_bot_textb)						
				top_offset = random.randint(-30,30)
				self.tmp_bot_texta = self.bg.create_text(self.x_center+top_offset, self.y_lower+-68, 
										text=adjx3, font=("Impact", 20), anchor=CENTER, 
										justify=CENTER, fill=colorx3)
				self.tmp_bot_textb = self.bg.create_text(self.x_center+(top_offset)*-1, self.y_lower+20, 
										text=subx3, font=("Impact", 20), anchor=CENTER, 
										justify=CENTER, fill=colorx3)	

			if self.wordcount > 3:			#L+R extra words
				if self.doing_homework==True:
					colory2, colory3 = '#000000','#000000'
				else:
					colory2 = random.choice(self.color_list)
					colory3 = random.choice(self.color_list)
			
				adjy2 = random.choice(self.alines).upper()
				suby2 = random.choice(self.slines).upper()
				adjy3 = random.choice(self.alines).upper()
				suby3 = random.choice(self.slines).upper()
				
				self.bg.delete(self.tmp_left_texta)
				self.bg.delete(self.tmp_left_textb)
				top_offset = random.randint(-30,30)
				self.tmp_left_texta = self.bg.create_text(left_x_value+top_offset, left_y_value-45, 
										text=adjy2, font=("Impact", 15), anchor=CENTER, 
										justify=CENTER, fill=colory2)
				self.tmp_left_textb = self.bg.create_text(left_x_value+(top_offset)*-1, left_y_value+18, 
										text=suby2, font=("Impact", 15), anchor=CENTER, 
										justify=CENTER, fill=colory2)
				
				self.bg.delete(self.tmp_right_texta)
				self.bg.delete(self.tmp_right_textb)
				top_offset = random.randint(-30,30)
				self.tmp_right_texta = self.bg.create_text(right_x_value+top_offset, right_y_value-45, 
										text=adjy3, font=("Impact", 15), anchor=CENTER, 
										justify=CENTER, fill=colory3)
				self.tmp_right_textb = self.bg.create_text(right_x_value+(top_offset)*-1, right_y_value+18, 
										text=suby3, font=("Impact", 15), anchor=CENTER, 
										justify=CENTER, fill=colory3)
			
			if not self.wordcount == 5:
				self.maintext_var = False	
		
	def breathe_transp(self):
		
		if self.playingvideo == True:
			self.tmp_opacity = self.opacity+1
		else:
			self.tmp_opacity = self.opacity
		
		now=int(datetime.now().strftime('%S'))
		if 0 <= now <= 15:
			now=(now-30)*-1
		elif 15 < now <= 30:
			pass
		elif 30 < now <= 45:
			now=(now-60)*-1
		elif 45 < now <= 60:
			now=now-30
		if self.tmp_opacity == 0:
			opacity = (now*.01)*1-.15
		else:
			opacity = (now*.01)*self.tmp_opacity
		self.master.overrideredirect(1)
		self.master.attributes('-alpha', opacity)	
			
	def updategif(self):
		if self.enable_hypno == 1:
			if self.playingvideo == False:
				myimage=next(self.gifcycle)
				self.image = Image.open('Resources\\Hypno Gif\\'+myimage)
				self.image = self.image.resize((self.bg.winfo_screenwidth(), self.bg.winfo_screenheight()))
				self.bg_image = ImageTk.PhotoImage(self.image)
				self.bg.itemconfig(self.bg.gif_create, image = self.bg_image)
			else:
				self.bg.itemconfig(self.bg.gif_create, image ='')
		if self.c_hypno.poll() == True:
			self.master.quit()
			
		self.after(5, self.updategif)
	
def set_clickthrough(windowname="Healslut Hypnotherapy"):
	hwnd = win32gui.FindWindow(None, windowname)
	windowStyles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
	win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, windowStyles)
	

def remove_clickthrough():
	hwnd = win32gui.FindWindow(None, "Healslut Hypnotherapy")
	windowStyles = win32con.WS_EX_LAYERED
	win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, windowStyles)

def set_written_line(humiliation, dom, sub):
		line=(random.choice(humiliation)).strip('\n')
		if line == '':
			line='i love being a healslut'
		if '99' in line:
			if dom == 'None':
				gendervar = random.randint(1,2)
			else:
				gendervar = 0
			if dom == 'Male' or gendervar == 1:
				line = line.replace('m99s', 'masters')
				line = line.replace('m99', 'master')
				line = line.replace('s99s', 'his')
				line = line.replace('s99', 'his')
				line = line.replace('n99', 'sir')
				line = line.replace('p99s', 'cocks')
				line = line.replace('p99', 'cock')
			elif dom == 'Female' or gendervar == 2:
				line = line.replace('m99s', 'mistresses')
				line = line.replace('m99', 'mistress')
				line = line.replace('s99s', 'hers')
				line = line.replace('s99', 'her')
				line = line.replace('n99', 'miss')
				line = line.replace('p99s', 'pussies')
				line = line.replace('p99', 'pussy')
		if '00' in line:
			if sub == 'Sub':
				line = line.replace('m00', 'sub')
				line = line.replace('p00s', 'parts')
				line = line.replace('p00', 'part')
			elif sub == 'Boy':
				line = line.replace('m00', 'boy')
				line = line.replace('p00s', 'balls')
				line = line.replace('p00', 'dick')
			elif sub == 'Girl':
				line = line.replace('m00', 'girl')
				line = line.replace('p00s', 'tits')
				line = line.replace('p00', 'cunt')
		return line	

			
class Banner(Frame):
	def __init__(self, master, delay, dom, sub, humiliation, color_list, 
					banwords, wordcount, tranbanr, homework, c_images, c_txt, c_hypno, *pargs):
		self.delay = delay
		self.dom = dom
		self.sub = sub
		self.humiliation = humiliation
		self.color_list = color_list
		self.banwords = banwords
		self.wordcount = wordcount
		self.tranbanr = tranbanr
		self.c_images = c_images
		self.c_txt = c_txt
		self.c_hypno = c_hypno
		self.master = master
		self.banner_var = 4		
		self.doing_homework = False
		self.freshtext = False
		self.endtime = datetime.now()
		self.master.wm_attributes("-topmost", 1)
		self.master.wm_attributes("-transparentcolor", "#000000")
		self.screen_width = self.master.winfo_screenwidth()
		self.screen_height = self.master.winfo_screenheight()
		self.master.geometry('%dx%d+%d+%d' % (self.screen_width, self.screen_height, 0, 0))
		self.master.overrideredirect(1)
		self.banner = Canvas(self.master, bg='#000000', width=495, height=200,
								highlightthickness=0)
		self.banner.pack(fill=BOTH, expand=YES)
		self.tmp_banner = self.banner.create_text(0, 0, text='')
		self.maintext = self.banner.create_text(0, 0, text='')
		if self.tranbanr == 1:
			self.master.attributes('-alpha', .5)	
		if self.banwords == 0:
			with open('Resources\\Text\\Healslut Adjectives.txt', 'r') as a:
				self.alines=a.readlines()
			with open('Resources\\Text\\Healslut Subjects.txt', 'r') as s:
				self.slines=s.readlines()
			self.tmp_top_text = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_top_texta = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_top_textb = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_bot_text = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_bot_texta = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_bot_textb = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_left_text = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_left_texta = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_left_textb = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_right_text = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_right_texta = self.banner.create_text(0, 0, text='', font=("Impact", 44))
			self.tmp_right_textb = self.banner.create_text(0, 0, text='', font=("Impact", 44))
		
			self.x_center = int(self.master.winfo_screenwidth()*.5)
			self.x_left = int(self.master.winfo_screenwidth()*.4)
			self.x_right = int(self.master.winfo_screenwidth()*.6)
			self.y_center = int(self.master.winfo_screenheight()*.5)
			self.y_upper = int(self.master.winfo_screenheight()*.33)
			self.y_lower = int(self.master.winfo_screenheight()*.66)
		
		
		self.run_banner()
		
	def run_banner(self):
		if self.c_hypno.poll() == True:
			self.master.quit()
		if self.c_images.poll() == True:
			self.master.lift()
			self.banner_var+=1
			self.maintext_var = True
			if self.banner_var >= 4:
				self.written_line = set_written_line(self.humiliation, self.dom, self.sub)
				self.banner_var = 0
				self.linecolor = random.choice(self.color_list)
			self.banner.delete(self.tmp_banner)
			self.tmp_banner = self.banner.create_text(self.screen_width/2, self.screen_height/1.3, 
												text=self.written_line.upper(),anchor=CENTER,
												font=("Impact", 44), fill=self.linecolor)
			if self.banwords == 0:
				self.master.after(int(self.delay/2), self.update_text)
		if self.c_txt.poll() == True:
			pipetext = self.c_txt.recv()
			text_count, sep, self.mytext = pipetext.partition(' ')
			self.endtime = datetime.now()+timedelta(seconds=int(text_count))
			self.master.attributes('-alpha', 1)	
			self.freshtext = True
		if datetime.now() < self.endtime:
			self.linecolor = random.choice(self.color_list)
			self.banner.delete(self.maintext)
			self.maintext = self.banner.create_text(self.screen_width*.5, self.screen_height*.4, 
												text=self.mytext,anchor=CENTER,
												font=("Impact", 50), fill=self.linecolor)
		elif self.freshtext == True:
			self.freshtext = False
			if self.tranbanr == 1:
				self.master.attributes('-alpha', .5)
			self.banner.delete(self.maintext)
			self.maintext = self.banner.create_text(self.screen_width*.5, self.screen_height*.4, 
												text=' ')
		self.master.after(self.delay, self.run_banner)
		
		
	def update_text(self):
		if self.wordcount > 0:
			if self.maintext_var == True:
				if self.doing_homework==True:
					colorx1 = '#000000'
				else:
					colorx1 = random.choice(self.color_list)
				
				adjx1 = random.choice(self.alines).upper()
				subx1 = random.choice(self.slines).upper()	
				self.banner.delete(self.tmp_top_text)
				self.banner.delete(self.tmp_bot_text)
				
				self.tmp_top_text = self.banner.create_text(self.x_center, self.y_upper, 
										text=adjx1, font=("Impact", 44), anchor=CENTER, 
										justify=CENTER, fill=colorx1)
								
				self.tmp_bot_text = self.banner.create_text(self.x_center, self.y_lower, 
										text=subx1, font=("Impact", 44), anchor=CENTER, 
										justify=CENTER, fill=colorx1)
									
			if self.wordcount > 1:				# L+R words	
				if self.doing_homework==True:
					colory1 = '#000000'
				else:
					colory1 = random.choice(self.color_list)
					
				left_x_value = float(random.randint(
								int(self.x_left*.9),
								int(self.x_left*1.1)))
				left_y_value = float(random.randint(
								int(self.y_center*.9),
								int(self.y_center*1.1)))
				right_x_value = float(random.randint(
								int(self.x_right*.9),
								int(self.x_right*1.1)))
				right_y_value = float(random.randint(
								int(self.y_center*.9),
								int(self.y_center*1.1)))
								
				adjy1 = random.choice(self.alines).upper()
				suby1 = random.choice(self.slines).upper()
				self.banner.delete(self.tmp_right_text)
				self.banner.delete(self.tmp_left_text)
				self.tmp_left_text = self.banner.create_text(left_x_value, left_y_value, 
										text=adjy1, font=("Impact", 28), anchor=CENTER, 
										justify=CENTER, fill=colory1)
									
				self.tmp_right_text = self.banner.create_text(right_x_value, right_y_value, 
										text=suby1, font=("Impact", 28), anchor=CENTER, 
										justify=CENTER, fill=colory1)
										
			if self.wordcount > 2:				#T+B extra words	
				if self.doing_homework==True:
					colorx2, colorx3 = '#000000','#000000'
				else:
					colorx2 = random.choice(self.color_list)
					colorx3 = random.choice(self.color_list)
					
				adjx2 = random.choice(self.alines).upper()
				subx2 = random.choice(self.slines).upper()
				adjx3 = random.choice(self.alines).upper()
				subx3 = random.choice(self.slines).upper()
			
				self.banner.delete(self.tmp_top_texta)
				self.banner.delete(self.tmp_top_textb)	
			
				top_offset = random.randint(-30,30)
				self.tmp_top_texta = self.banner.create_text(self.x_center+top_offset, self.y_upper-68, 
										text=adjx2, font=("Impact", 20), anchor=CENTER, 
										justify=CENTER, fill=colorx2)
				self.tmp_top_textb = self.banner.create_text(self.x_center+(top_offset)*-1, self.y_upper+20, 
										text=subx2, font=("Impact", 20), anchor=CENTER, 
										justify=CENTER, fill=colorx2)
										
				self.banner.delete(self.tmp_bot_texta)
				self.banner.delete(self.tmp_bot_textb)						
				top_offset = random.randint(-30,30)
				self.tmp_bot_texta = self.banner.create_text(self.x_center+top_offset, self.y_lower+-68, 
										text=adjx3, font=("Impact", 20), anchor=CENTER, 
										justify=CENTER, fill=colorx3)
				self.tmp_bot_textb = self.banner.create_text(self.x_center+(top_offset)*-1, self.y_lower+20, 
										text=subx3, font=("Impact", 20), anchor=CENTER, 
										justify=CENTER, fill=colorx3)	

			if self.wordcount > 3:			#L+R extra words
				if self.doing_homework==True:
					colory2, colory3 = '#000000','#000000'
				else:
					colory2 = random.choice(self.color_list)
					colory3 = random.choice(self.color_list)
			
				adjy2 = random.choice(self.alines).upper()
				suby2 = random.choice(self.slines).upper()
				adjy3 = random.choice(self.alines).upper()
				suby3 = random.choice(self.slines).upper()
				self.banner.delete(self.tmp_left_texta)
				self.banner.delete(self.tmp_left_textb)
				top_offset = random.randint(-30,30)
				self.tmp_left_texta = self.banner.create_text(left_x_value+top_offset, left_y_value-45, 
										text=adjy2, font=("Impact", 15), anchor=CENTER, 
										justify=CENTER, fill=colory2)
				self.tmp_left_textb = self.banner.create_text(left_x_value+(top_offset)*-1, left_y_value+18, 
										text=suby2, font=("Impact", 15), anchor=CENTER, 
										justify=CENTER, fill=colory2)
										
				self.banner.delete(self.tmp_right_texta)
				self.banner.delete(self.tmp_right_textb)
				top_offset = random.randint(-30,30)
				self.tmp_right_texta = self.banner.create_text(right_x_value+top_offset, right_y_value-45, 
										text=adjy3, font=("Impact", 15), anchor=CENTER, 
										justify=CENTER, fill=colory3)
				self.tmp_right_textb = self.banner.create_text(right_x_value+(top_offset)*-1, right_y_value+18, 
										text=suby3, font=("Impact", 15), anchor=CENTER, 
										justify=CENTER, fill=colory3)
			
			if not self.wordcount == 5:
				self.maintext_var = False	
				
		
def create_banner(delay,dom,sub,humiliation,color_list,banwords,
						wordcount,tranbanr,homework,c_images,c_txt,
						c_hypno):
	root = Tk()
	width = root.winfo_screenwidth()
	height = root.winfo_screenheight()
	root.geometry('%dx%d' % (width, height))
	root.configure(background="#000000")
	root.title("Healslut Banner")
	root.wm_attributes("-topmost", 1)
	set_clickthrough('Healslut Banner')
	root.attributes('-alpha', 1)
	e = Banner(root,delay,dom,sub,humiliation,color_list,
				banwords,wordcount,tranbanr,homework,c_images,c_txt,
				c_hypno)
	root.mainloop()

def launch(delay,opacity,game,homework,wordcount,hypno,
				dom,sub,pinup,banwords,tranbanr,globfile,
				s_rulename,fontsize,display_rules,c_rules,
				c_vid,c_txt,c_homework,c_hypno):
	root = Tk()
	width = root.winfo_screenwidth()
	height = root.winfo_screenheight()
	root.geometry('%dx%d' % (width, height))
	root.configure(background="#000000")
	root.attributes('-alpha', 0.3)
	root.title("Healslut Hypnotherapy")
	root.wm_attributes("-topmost", 1)
	set_clickthrough()

	if pinup == 1:
		image_files = glob.glob(globfile+'/*.png', recursive=True)
	else:
		image_files = ''
	
	if c_hypno.poll() == True:
		quit()
		
	e = Hypnotherapy(root, image_files, delay, opacity, game, 
					homework, wordcount, hypno, dom, sub, pinup, 
					banwords, tranbanr, s_rulename, fontsize, 
					display_rules, c_rules, c_vid, c_txt, c_homework,
					c_hypno)
	e.pack(fill=BOTH, expand=YES)
	root.mainloop()

from tkinter import *
from string import ascii_lowercase, ascii_uppercase
from random import randrange, choice
from traceback import format_exc
from os import path
from PIL import Image, ImageTk

import HealslutPackages as HP

	# rough verison pulled from https://github.com/chongkim/parent/blob/master/python/wordsearch_generator3.py
	# Shame I'm posting this on my nsfw account, this is actually some good code.



class WordSearchLibs:
	def __init__(self,parent,screenwidth,screenheight):
		self.parent = parent
		self.screenwidth = screenwidth
		self.screenheight = screenheight
		self.WSx, self.WSy = None, None
		self.WSActive = False
		
		#self.WordSearchFrame()

	def StartMoveWS(self,event):
		self.WSx, self.WSy = event.x, event.y
		
	def StopMoveWS(self,event):
		self.WSx, self.WSy = None, None
		
	def WordSearchOnMotion(self,event):
		x = self.parent.WSFrame.winfo_x() + event.x - self.WSx
		y = self.parent.WSFrame.winfo_y() + event.y - self.WSy
		self.parent.WSFrame.geometry("+%s+%s" % (x, y))
		
	def WordSearchFrame(self,Difficulty):
		if self.WSActive == True:
			self.WSActive = False
			self.Die()
		else:
			self.WSActive = True
			self.Difficulty = Difficulty
			while True:
				try:
						# # # # # # # # # # #
						# Build the window  #
						# # # # # # # # # # #
					width, height = 800,738
					WordList = GenWordSearchList(Difficulty)
					self.parent.WSFrame = Toplevel(self.parent, bg=HP.TRANS_CLR(), highlightthickness=0)
					self.parent.WSFrame.wm_title("Word Search")
					self.parent.WSFrame.overrideredirect(True)
					self.parent.WSFrame.wm_attributes("-topmost", 1)
					self.parent.WSFrame.wm_attributes("-transparentcolor", HP.TRANS_CLR())
					x = (self.screenwidth  / 2) - (width  / 2)
					y = (self.screenheight / 2) - (height / 2)
					self.parent.WSFrame.geometry('%dx%d+%d+%d' % (width, height, x, y))
					
						# # # # # # # #
						# MOVING GRIP #
						# # # # # # # #
					self.grip = Label(self.parent.WSFrame, height=1, bg='Gray50', text="< Hold to Move >", font=('Times', 8))
					self.grip.pack(fill=X)
					self.grip.bind("<ButtonPress-1>", self.StartMoveWS)
					self.grip.bind("<ButtonRelease-1>", self.StopMoveWS)
					self.grip.bind("<B1-Motion>", self.WordSearchOnMotion)
					
						# # # # # # # # # # #
						# Window Background #
						# # # # # # # # # # #
					self.parent.WSFrame.bg = Canvas(self.parent.WSFrame, bg='light blue', width=300, height=height*2)
					self.parent.WSFrame.bg.pack(fill=X)
					Filepath = path.abspath('Resources/ButtonLabels/Misc/WordSearchBackgroundDark.png')
					image = Image.open(Filepath)
					self.WordSearchImg = ImageTk.PhotoImage(image)
					self.parent.WSFrame.bg.create_image(width/2, height/2, image=self.WordSearchImg)
					
						# # # # # # # # # # #
						# parent Legend #
						# # # # # # # # # # #
					WordListStr1, WordListStr2 = GenWordList(WordList)
					FontColor = 'pink'
					self.parent.WSFrame.bg.create_text((5,height/2), font=('Impact', 14),
						text=WordListStr1, fill=FontColor, justify=LEFT, anchor=W)
					self.parent.WSFrame.bg.create_text((width-5,height/2), font=('Impact', 14),
						text=WordListStr2, fill=FontColor, justify=RIGHT, anchor=E)
					
						# # # # # # # # # # # # #
						# parent Play Area  #
						# # # # # # # # # # # # #
					grid,SavedCords = Main(WordList,Difficulty)
					self.WordSearchBG = self.parent.WSFrame.bg.create_text((width/2,height/2), fill='#FF7FED', font=("Courier", 16, "bold"),
						text="\n".join(map(lambda row: " ".join(row), grid)))
					
					self.WordSearchSavedCords=SavedCords
					self.WordList=WordList
					break
				except Exception as e:
					HP.HandleError(format_exc(2), e, 'WordSearchFrame', subj='')
			self.parent.after(15000, self.ScrambleGrid)

	def ScrambleGrid(self):
		try:
			#grid=self.WordSearchGrid
			if self.WSActive == True:
				width, height = GenDimensions(self.WordList,self.Difficulty)
				grid = GenBlankGrid(self.Difficulty,width,height,self.WordSearchSavedCords)
				self.parent.WSFrame.bg.itemconfig(self.WordSearchBG, text="\n".join(map(lambda row: " ".join(row), grid)))
				self.parent.after(30000, self.ScrambleGrid)
		except TclError as e:
			pass
		except Exception as e:
			HP.HandleError(format_exc(2), e, 'ScrambleGrid', subj='')
		
	def Die(self):
		try:
			self.parent.WSFrame.destroy()
		except AttributeError:
			pass

def GenWordList(WordList):
	WordListStr1 = '\n\n\n'
	WordListStr2 = ''
	
	for word in WordList[0:int(len(WordList)*.5)]:
		WordListStr1 += word+'\n'
	for word in WordList[int(len(WordList)*.5):-1]:
		WordListStr2 += word+'\n'
		
	WordListStr2+='\n\n\n'
	return WordListStr1, WordListStr2

# ######################################### #
#############################################
# ######################################### #

def GenDimensions(WordList,Difficulty,width=5,height=5):
	for word in WordList:
		if len(word) >= height or len(word) >= width:
			width = len(word)+1
			height = len(word)+5
	if len(WordList) >= width:
		width +=3
	if Difficulty == 'TEST':
		pass
	elif Difficulty == 'EASY':
		width = width+1
		height = height+1
	elif Difficulty == 'MEDIUM':
		width = width+2
		height = height+3
	elif Difficulty == 'HARD':
		width = width+4
		height = height+6
	return width, height

def GenBlankGrid(Difficulty,width,height,SavedCords,WordList=''):
	if Difficulty == 'TEST':
		grid = [[choice(['-']) for i in range(0,width)] for j in range(0,height)]
	elif Difficulty == 'EASY':
		grid = [[choice(ascii_lowercase) for i in range(0,width)] for j in range(0,height)]
	elif Difficulty == 'MEDIUM':
		grid = [[choice(ascii_uppercase) for i in range(0,width)] for j in range(0,height)]
	elif Difficulty == 'HARD':
		grid = [[choice(ascii_uppercase) for i in range(0,width)] for j in range(0,height)]
	if not SavedCords=='':
		for Cord, word in SavedCords.items():
			xrow, yrow = Cord
			grid[yrow][xrow] = word
	return grid

def GenCords(word,width,height):
	try:
		d = choice([[1,0],[0,1],[1,1]])
		xsize = width  if d[0] == 0 else width  - len(word)
		ysize = height if d[1] == 0 else height - len(word)
		x = randrange(0,xsize)
		y = randrange(0,ysize)
	except ValueError:
		raise Exception('Bad Dimensions!')
	return d,x,y
	
def CheckDict(mydict,Key,Value):
	try:
		if not mydict[Key] == Value:
			return False
		else:
			return None
	except KeyError:
		return True
		
def put_word(word,grid,Difficulty,SavedCords,width,height):
	if Difficulty == 'HARD':
		word = choice([word,word[::-1]])
	SC = dict(SavedCords)
	Loop = True
	xLoop = 0
	while Loop:
		yMemory = []
		xMemory = []
		SavedCords = dict(SC)
		d,x,y = GenCords(word,width,height)
		for i in range(0,len(word)):
			yrow = y + d[1]*i
			xrow = x + d[0]*i
			Cord = (xrow,yrow)
			GoodCord = CheckDict(SavedCords,Cord,word[i])
			if GoodCord == True:
				SavedCords[Cord] = word[i]
				yMemory.append(yrow)
				xMemory.append(xrow)
				grid[yrow][xrow] = word[i]
				if i == len(word)-1:
					Loop = False
			elif GoodCord == None:
				pass
			elif GoodCord == False:
					# There was an overlapping word
				for ii in range(0,len(yMemory)):
					if Difficulty == 'TEST':
						grid[yMemory[ii]][xMemory[ii]] = '-'
					elif Difficulty == 'EASY':
						grid[yMemory[ii]][xMemory[ii]] = choice(ascii_lowercase)
					elif Difficulty == 'MEDIUM':
						grid[yMemory[ii]][xMemory[ii]] = choice(ascii_uppercase)
					elif Difficulty == 'HARD':
						grid[yMemory[ii]][xMemory[ii]] = choice(ascii_uppercase)
				if xLoop > 100:
					return False, False
				xLoop+=1
				break
	return grid, SavedCords

def PrintSavedCords(SavedCords):	#PrintSavedCords(SavedCords)
	for Cords, Letter in SavedCords.items():
		print(Cords, Letter)
	
def GenXWord(WordList,Difficulty,width,height,SavedCords):
	try:
		grid = GenBlankGrid(Difficulty,width,height,SavedCords)
		SavedCords = {}
		for word in WordList:
			word = word.upper()
			#print(word)
			grid, SavedCords = put_word(word,grid,Difficulty,SavedCords,width,height)
			if not grid:
				return False
	except TypeError:
		GenXWord(WordList,Difficulty,width,height,SavedCords)
	return grid,SavedCords

def GenWordSearchList(Difficulty):
	try:
		if Difficulty=='MEDIUM':	WordCount = 20
		elif Difficulty=='HARD':	WordCount = 28
		else:						WordCount = 12
		Filepath = path.abspath('Resources/Text/Healslut Adjectives.txt')
		with open(Filepath,'r') as f:
			alines = f.readlines()
		Filepath = path.abspath('Resources/Text/Healslut Subjects.txt')
		with open(Filepath,'r') as f:
			blines = f.readlines()
		WordList = []
		for i in range(0,WordCount):
			while True:
				word = choice(alines+blines).replace('\n','').replace('-','').replace(' ','').upper()
				if not word == '' and not word in WordList and not len(word) > 9:
					WordList.append(word)
					break
		return WordList
	except Exception as e:
		HandleError(format_exc(2), e, 'GenWordSearchList', subj='')
	
def Main(WordList='',Difficulty='',SavedCords=''):	
	if WordList=='':
		WordList = GenWordSearchList(Difficulty)
	if Difficulty=='':
		# TEST: Random letters are replaced with null space
			# Size Modifiers: None
		# EASY: Random letters are Lowercase
			# Size Modifiers: w+1,h+1
		# MEDIUM: Random letters are Uppercase
			# Size Modifiers: w+2,h+3
		# HARD: Random letters are Uppercase, words can be backwards
			# Size Modifiers: w+4,h+6
		Difficulty = ['TEST','EASY','MEDIUM','HARD'][3]
	width, height = GenDimensions(WordList,Difficulty)
	xLoop = 0
	while True:
		xLoop+=0
		grid,SavedCords = GenXWord(WordList,Difficulty,width,height,SavedCords)
		if grid:
			break
		elif xLoop > 200:
			print('Change parameters and try again')	
	return grid,SavedCords

if __name__ == '__main__':
	grid,SavedCords = Main()
	print("\n".join(map(lambda row: " ".join(row), grid)))

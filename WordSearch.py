from string import ascii_lowercase, ascii_uppercase
from random import randrange, choice

	# rough verison pulled from https://github.com/chongkim/wordsearch/blob/master/python/wordsearch_generator3.py
	# Shame I'm posting this on my nsfw account, this is actually some good code.

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
	grid = GenBlankGrid(Difficulty,width,height,SavedCords)
	SavedCords = {}
	for word in WordList:
		word = word.upper()
		#print(word)
		grid, SavedCords = put_word(word,grid,Difficulty,SavedCords,width,height)
		if not grid:
			return False
	return grid,SavedCords
	
def GenWordSearchList(Difficulty):
	if Difficulty=='MEDIUM':
		WordCount = 20
	elif Difficulty=='HARD':
		WordCount = 28
	else:
		WordCount = 12
	with open('Resources/Text/Healslut Adjectives.txt','r') as f:
		alines = f.readlines()
	with open('Resources/Text/Healslut Subjects.txt','r') as f:
		blines = f.readlines()
	totallines = alines+blines
	WordList = []
	for i in range(0,WordCount):
		while True:
			word = choice(totallines).replace('\n','').replace('-','').replace(' ','').upper()
			if not word == '' and not word in WordList and not len(word) > 9:
				WordList.append(word)
				break
	return WordList
	
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

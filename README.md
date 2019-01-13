	#######################  Info  ###########################
	#							 #
	# 		Created by u/Graveknight1		 #
	#							 #
	# Please contact me via reddit for questions or requests #
	# If you would like to donate to my work, feel free to   #
	# reach out.						 #
	#							 #
	# This program is not for sale, if someone charged you	 #
	# for it, you've been ripped off.			 #
	#							 #
	# This code was written for the Healsluts community	 #
	# If you like what you see, check them out at 		 #
	# r/healsluts						 #
	#							 #
	##########################################################
	
	###################### Instructions #####################

I made this program so that all people could enjoy the healslut kink even when they
may not be able to coordinate with a partner. 

			#### The Program ####

This program launches a small window on the right side of your screen. Its purpose 
is to aid the user in navigating punishments, rewards, vibrator speeds and image 
overlays. I usually run this program, then start whatever game I am playing, then start
the overlay. It was my goal to make this program as customizable as possible so that
the user can enjoy an intimate experience. This program is distributed with a folder
directory consistent with the list below.

		--- Audio
			This folder can be filled with any sounds you'd like to tie to 
			your punishments and rewards. There is a file named 'Punishment 
			Buzz.mp3' which is used to play a failure sound when the user 
			fails to fill out the writeforme entry box correctly. All files
			in this folder must be .mp3 files.
		--- Errors
			Anytime the program runs into an issue, it will log that error
			here. If the problem persists, reach out to me and let me know
			what these files say so I can fix it for you!
		--- Healslut Games
			This folder can contain a list of rules, punishments and 
			rewards it is not necessary to populate the rules file with 
			text, but it is critical that each of the three are named 
			consistently. for example, 'Overwatch Rules', 'Overwatch 
			Punishments', 'Overwatch Rewards' If the game name is spelled 
			inconsistently, or not coupled with rules, punishments and 
			rewards, respectively, this function wont work.
		--- Hypno Gif
			This folder contains subfolders of all of the users gifs. to
			populate this folder, open the program, press edit hypno, then
			enter your desired screen size and press format gifs.
		--- Images
			This folder and all subfolders are to be named to the user's 
			desire and populated with images the user would like to enjoy 
			while using the overlay. I have packaged this folder with some
			images i pulled off of hentaifoundry.com. you can place any 
			number of images in each folder, but the more images you have
			the longer the overlay will take to initialize. I recommend 50
			to 200 for a nice variety. If you overload the folders, the 
			overlay will fail to run. These images MUST be .png files. You 
			can use https://jpg2png.com/ to convert your .jpgs to .pngs.
		--- Text
			This folder and the four files within allow the user to customize
			the way the program writes to you and makes you write. 
			You can also
			choose which colors you like. You can use any hexadecimal color or
			the list of named colors found in the link below.
			http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
		--- Tracks 
			This folder can be filled with any .mp3 file like music or soundgasm
			scripts that can be randomized or played alphabetically while the 
			overlay runs.
		--- Video
			This folder can be filled with any videos you'd like to tie to 
			your punishments and rewards. They must be .mp4 files. 
			

In order to use the vibrator function of this program you've got to download the Lovense 
Connect app, and have the ability to Bluetooth from your computer. If your computer doesn’t 
have Bluetooth built in they sell a little usb adapter, but its cheaper on amazon. I am working
to make this easier for you.
You can download their Connect app for the PC here. I have never tested this program with a 
mac.				https://www.lovense.com/cam-model/download


You can find an explanation of the settings menu in the link below. Please review it, its
full of valuable information.
				https://imgur.com/a/avdiNg7
This image was made before I added the looping audio and the image converter. Instructions for
each of them are found in this document.
it was also made before I added the gif formatter and preview

This program is packaged with an mp3 player which you can set to cycle through a number of tracks 
while the overlay is running. It is distributed with a few songs and scripts, but the user can add 
their own by placing them into the Resources/Tracks/ folder

			#### The Text ####

In order to customize the text that will be displayed in the write for me and banner functions
edit the Humiliation.txt file. Below is a key for using gender specific terms with the text file

m99s = masters/mistresses
m99 = master/mistress
s99s = his/hers
s99 = his/her
n99 = sir/miss
p99s = cocks/pussies
p99 = cock/pussy

dom gender preference = Male
	example 'I belong by my m99s feet' = I belong by my masters feet
dom gender preference = Female
	example 'I live to service my teams p99s' = I live to service my teams pussies

m00 = sub/boy/girl
p00s = parts/balls/tits
p00 = part/dick/cunt

self gender pronoun = boy
	example 'My p00 makes me a good m00' = My dick makes me a good boy
self gender pronoun = sub
	example 'My p00 makes me a good m00' = My part makes me a good sub



			#### Punishments and Rewards ####

in order to use the punishment and reward buttons, you have to fill out the corresponding
[Name] Rules.txt, [Name] Rewards.txt, and [Name] Punishments.txt. Each time you press the 
reward button, the program will read the first line in the rewards file. you can include 
any number of the following commands in any given line, but they must be separated by the
comma(,). Do not include spaces unless necessary for filenames or sentences. When you reach
the end of the file, it starts over from the top.

	---  $playsound [audio file.mp3]
		Playsound can find any file inside of the Resources/Audio/ folder. a good
		example would look like this. $playsound Good Girl.mp3.
	---  $playvideo [video file.mp4]
		Playsound can find any file inside of the Resources/Video/ folder. a good
		example would look like this. $playsound titfuck.mp4.
		
		You can play video and audio simultaneously by using the commands below. 
		To make this work, you may have to create custom audio from the original
		video file.
		$playvideo [video file.mp4],$playsound [audio file.mp3]

	---  $text[seconds] [words]
		You want to include a number after the word text, but before the first space.
		You cannot include commas within the text you wish to display.
	---  $+vibe[0-100]
		Use any positive whole number 0-100. this number will be added to the 
		existing speed rather than setting a new speed, so if you have several lines 
		in a row like the following, each reward will increase the speed by the number
		you've set. Starting at zero, the following rewards would increase the speed to
		10, 20, and 30 once the final line was pressed.
		$+vibe10
		$+vibe10
		$+vibe10
	---  $-vibe[0-100]
		see $+vibe, except subtracting the value instead of adding it
	---  $+rotate[0-100]
		see $+vibe, except rotation speed instead of vibrator speed
	---  $-rotate[0-100]
		see $+rotate, except subtracting the value instead of adding it
	---  $+air[0-3]
		see $+vibe, excpet airpump inflation speed instead of vibrator speed
	---  $-air[0-3]
		see $+air, except subtracting the value instead of adding it
	---  $picture
		This function takes a picture from your webcam and sends it to me. This function
		was made deliberately more difficult to use to protect the privacy of users who 
		don’t want to share images of themselves or their subs. The first time you use this
		function, a warning will appear telling you that you need to enable less secure 
		access to the gmail account that you will be sending pictures from. Follow the 
		link and sign in using the account you wish to use. It must be a gmail account.
		A text file has been created in the Resources\ folder called User Info.txt will be
		created. Fill out your login information to the gmail account you wish to use in 
		the format laid out for you. In order to keep the warning from appearing again,
		ensure that the third line equals 1. None of your information is shared with me
		and I will never attempt to communicate with those of you who use this function.
		All the same, if I were you, I'd create a new email account and use it exclusively 
		for this purpose.

		This program will never take a picture of you without your consent. It is included
		only for those who would find the exposure or punishment exciting.

	---  $writeforme[number]
		This sets the remaining number of lines to whichever number you've selected. You can
		type lines in between matches and set the number of remaining lines to 0 once the 
		match begins by binding $writeforme0 to one of the buttons. If you absolutely must
		exit the writeforme menu and you want to preserve your place in the punishments and 
		rewards, entering [] into the entry box will reset the number of remaining sentences
		you are to write to zero, and end your current writing session.

Here is a good example of the lines you'd want to include in the punishments and rewards

example rewards.txt

$+vibe10,$+rotate00,$+air3
$text10 You're my dumb little supportslut 
$playvideo titfuck.mp4,$playsound titfuck.mp3




			#### Vibrator Functionality ####
The user can use the punishment and reward buttons to control their vibrator. Alternately if the user 
enjoys Overwatch, the program can detect the users on fire meter and control the vibe speed based on
the meter. In order to do this, you MUST set the game from None to OW, EVEN IF YOU ARE NOT USING THE 
OVERLAY! This signals the program to look for an on fire meter on screen. I have implemented this 
requirement to save on hardware resources.



			#### Write for me ####

Some of you may be familiar with the website this function is based on, and it was my pleasure to
include it in this release. This function will interrupt the user and force them to complete a number
of written tasks based on the severity of the user’s choice. I don't advise using it while playing
a fast-paced game, as it will severely handicap you. But, maybe that’s what you're looking for. I enjoy
setting some work for myself in between games or while respawning.




			#### Image Converter ####

I have downloaded so much smut since I started this program. One of the largest chores is to convert the
images to the proper file type. I included a function which converts jpgs to pngs, and optionally deletes 
the jpgs so that the folder is filled only with the properly formated pngs. All you need to do is select
which folder you want to format and press convert! Alternately, you can convert all image folders at once
by selecting 'All', but be warned, this may take some time. You may want to look at the cmd window for
progress as you do this.



			#### Gif Converter ####
By placing a gif into the Resources\Background Gif original\ folder and formatting the gif in the edit menu
the user now has the ability to display any background theyd like, and it will be sized to their screen which
reduces lag. sometimes gifs are not converted correctly. I have found that his has more to do with the quailty
of the gif than of the converter. for this, i am searching for a remedy.



	################### Errors and Concerns ##################	

Some users on older machines report lagging. The best thing to do if you encouter lag is to disable the 
hypno background, as it takes up the largest amount of resources of any function. On my i7, running this
program at full capacity reserves 14% of my processer. With the background disabled, that number is reduced
to around 5%

If your computer should encounter any errors while running this program, please share it with me. This
program now logs its errors to a resources subfolder. Those logs will be very helpful to me as I try to
find out what went wrong.

There is no stated rule that a program like this one would result in a ban with any major gaming 
company. That said, I cannot speak for them on what they determine to be malicious or game altering 
software. Please exercise caution while using this software, and check back often for community 
feedback.


	####################### Change Log #######################


Version 1.2.1
	-	Minor bug fixes

Version 1.2
		--- Overlay Functions
	-	Reduced lag between pinup images
	-	Added background select option menu
	-	Automatically save user perferences on close
	-	Added function to allow user to format gif size to their screen

Version 1.1
		--- Overlay Functions
	-	Mutliprocess support to enable packaging into one file, and import fixes
	-	Traceback
	-	Reduced CPU Load
	-	Built in jpg to png selector and converter
	-	Automatically minimized cmd window
	-	Looping audio tracks


Version 1.0.0
		--- Overlay Functions
	-	Hypnotic Gif Background
	-	Pinup images and folder selection
	-	Varying Opacity 
	-	Image flash delay
	-	Write for me and banner options
	-	Option to have varying opacity on words
	-	Fixed Banner opacity

		--- Punishments and Rewards
	-	Display rules and rule selection
	-	customize punishments and rewards
			$playsound
			$playvideo
			$text
			$+vibe
			$-vibe
			$+rotate
			$-rotate
			$+air
			$-air
			$picture
			$writeforme

		--- Vibrator Functions
	-	When enabled, Rotating toys will periodically turn on or off 
	- 	When enabled and Image Game Hole is set to OW, the vibrator will scale to 
		the users level of on fire
	-	The vibrator, rotation, and airpump can be altered using the reward and 
		punishment buttons
	-	Optional decay speed
	-	Only Lovense products are compatible at this time

		--- Other Options
	-	Text Color options
	-	Adjectives and Subjects
	-	Phrases
	

	######################## Forecast ########################

I will work to enable the use of more vibrator brands. This will take time but I believe
it will be worth it

I would like to make a function that tracks teammate deaths and leverages 
them against the user for things like the above-mentioned writing game or 
a temporary speed decrease.

I'd like to provide a menu selector for download soundgasm files and iateacrayon/wiki/list pics

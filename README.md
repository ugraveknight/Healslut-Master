# Healslut-Master
A transparent overlay with features to allow users to experience video games more physically



	#######################  Info  ###########################
	#				                  	 #
	# 		Created by u/Graveknight1                #
	#						         #
	# Please contact me via reddit for questions or requests #
	# If you would like to donate to my work, feel free to   #
	# reach out.					         #
	#					           	 #
	# This program is not for sale, if someone charged you	 #
	# for it, you've been ripped off.			 #
	#						         #
	# This code was written for the Healsluts community   	 #
	# If you like what you see, check them out at 	      	 #
	# r/healsluts					         #
	#					             	 #
	##########################################################
	
	###################### Instructions #####################

I made this program so that all people could enjoy the healslut kink even when they
may not be able to coordinate with a partner. I recommend that you make a shortcut to
the HealslutMaster.exe file and place that where you'd like. All folders within the 
HealslutMaster folder are not to be edited with the exception of the Resources folder.


	Everything will crash if you edit any file outside of the Resources folder.


			#### The Program ####

This program launches a small window on the right side of your screen. Its purpose 
is to aid the user in navigating punishments, rewards, vibrator speeds and image 
overlays. It was my goal to make this program as customizable as possible so that
the user can enjoy an intimate experience. This program is distributed with a folder
directory consistant with the list below.
		--- Audio
			This folder can be filled with any sounds you'd like to tie to 
			your punishments and rewards. There is a file named 'Punishment 
			Buzz.mp3' which is used to play a failure sound when the user 
			fails to fill out the writeforme entry box correctly. All files
			in this folder must be .mp3 files.
		--- Healslut Games
			This folder can contain an list of rules, punishments and 
			rewards it is not necessary to populate the rules file with 
			text, but it is critical that each of the three are named 
			consistantly. for example 'Overwatch Rules', 'Overwatch 
			Punishments', 'Overwatch Rewards' If the game name is spelled 
			inconsistantly, or not coupled with rules, punishments and 
			rewards, respectively, this function wont work.
		--- Hypno Gif
			This folder can be customized, but only if the user replaces 
			the images with exact file names. I would not recommend changing
			the contents of this folder unless you are proficent with file 
			types.
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
			choose which colors you like. You can use any hexidecimal color or
			the list of named colors found in the link below
			http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
		--- Video
			This folder can be filled with any videos you'd like to tie to 
			your punishments and rewards. They must be .mp4 files. 
			

In order to use the vibrator function of this program you've got to download the Lovense 
Connect app, and have the ability to bluetooth from your computer. If your computer doesnt 
have bluetooth built in they sell a little usb adapter, but its cheaper on amazon.

You can find an explaination of the settings menu in the link below. Please review it, its
full of valuable information.
				https://imgur.com/a/avdiNg7

You can download their Connect app for the PC here. I have never tested this program with a 
mac.				https://www.lovense.com/cam-model/download



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
any number of the following commands in any given line, but they must be seperated by the
comma(,). Do not include spaces unless necessary for filenames or sentances. When you reach
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
		exisiting speed rather than setting a new speed, so if you have several lines 
		in a row like the following, each reward will increase the speed by the number
		you've set. Starting at zero, the following rewards would increase the speed to
		10, 20, and 30 once the final line was pressed.
		$+vibe10
		$+vibe10
		$+vibe10
	---  $-vibe[0-100]
		see $+vibe, except subtracting the value instead of adding it
	---  $+rotate[0-100]
		see $+vibe, excpet rotation speed instead of vibrator speed
	---  $-rotate[0-100]
		see $+rotate, except subtracting the value instead of adding it
	---  $+air[0-3]
		see $+vibe, excpet airpump inflation speed instead of vibrator speed
	---  $-air[0-3]
		see $+air, except subtracting the value instead of adding it
	---  $picture
		This function takes a picture from your webcam and sends it to me. This function
		was made deliberately more difficult to use to protect the privacy of users who 
		dont want to share images of themselves or their subs. The first time you use this
		function, a warning will appear telling you that you need to enable less secure 
		access to the gmail account that you will be sending pictures from. Follow the 
		link and sign in using the account you wish to use. It must be a gmail account.
		A text file has been created in the Resources\ folder called User Info.txt will be
		created. Fill out your login information to the gmail account you wish to use in 
		the format laid out for you. In order to keep the warning from appearing again,
		ensure that the third line equals 1. None of your information is shared with me
		and I will never attempt to communicate with those of you who use this function.
		All the same, if I were you I'd create a new email account and use it exclusively 
		for this purpose.

		This program will never take a picture of you without your consent. It is included
		only for those who would find the exposure or punishment exciting.

	---  $writeforme[number]
		This sets the remaining number of lines to whichever number you've selected. You can
		type lines in between matches and set the number of remaining lines to 0 once the 
		match begins by binding $writeforme0 to one of the buttons. If you absolutely must
		exit the writeforme menu and you want to preserve your place in the punishments and 
		rewards, entering [] into the entry box will reset the number of remaining sentances
		you are to write to zero, and end your current writing session.

Here is a good example of the lines you'd want to include in the punishments and rewards

example rewards.txt
$+vibe10,$+rotate00,$+air3
$text10 You're my dumb little supportslut 
$playvideo titfuck.mp4,$playsound titfuck.mp3




			#### Write for me ####

Some of you may be familiar with the website this function is based on, and it was my pleasure to
include it in this release. This function will interrupt the user and force them to complete a number
of written tasks based on the severity of the users choice. I don't advise using it while playing
a fast paced game, as it will severely handicap you. But, maybe thats what you're looking for. I enjoy
setting some work for myself in between games or while respawning.



	######################### Errors #########################	

If your computer should encounter any errors while running this program, please
share it with me.



	####################### Change Log #######################

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
them against the user for things like the above mentioned writing game or 
a temporary speed decrease.

The program is pretty well optimized, but on slower computers a longer delay 
between screenshots could be used.

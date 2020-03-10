    #######################  Info  ###########################
    #                                                        #
    #                Created by u/Graveknight1               #
    #                                                        #
    # Please contact me via reddit for questions or requests #
    # If you would like to donate to my work, feel free to   #
    # reach out.                                             #
    #                                                        #
    # This program is not for sale, if someone charged you   #
    # for it, you've been ripped off.                        #
    #                                                        #
    #   This code was written for the Healsluts community    #
    #   If you like what you see, check them out at          #
    #   r/healsluts                                          #
    #                                                        #
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
			fails to fill out the writeforme entry box correctly. There is
			likewise a file called Reward Chime.mp3 which plays when the user
			completes the writeforme. All files	in this folder must be .mp3s.
		--- Background Gif Originals
			This folder contains the original .gif files that will be converted
			to background slides using the buildin Convert Gifs function
		--- ButtonLabels
			The .jpgs in this folder are used as headers for each of the button
			icons when using the Action Frame
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
		--- Killfeed
			This folder contains subfolders (right now, only OW is used) which
			hold screenshots used to monitor actions within the game. in the
			case of overwatch, I'm using killfeed icons to determine whats 
			happing to the subs team. Be mindful that if your computer slows
			down while in Freeplay mode, it may be best to remove some of the less 
			used images from this folder. (ex. you're mercy, your dom is Roadhog
			you might consider removing other supports or assists)
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
edit the Humiliation.txt file as well as the Feminization.txt file. Not into the Sissy/Bimbo Kink?
Simply set Sex to None and you'll still get to enjoy the traditional humiliation text without sissy 
or bimbo overtones! Below is a key for using gender specific terms with the text file

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

o99 = girlfriend/boyfriend
r00 = he/she
f99 = sissy/bimbo
f99s = sissies/bimbos
f00 = clitty/fuckhole
w00 = man/woman

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
		playvideo can find any file inside of the Resources/Video/ folder. a good
		example would look like this. $playvideo titfuck.mp4.
		
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
	---  $pinup
		This simple macro allow you to change your pinup source folder on the go! to use
		it, you will specify your desired folder name. For the Healslut folder, include 
		the following line in your punish/reward or button file "$pinup Healslut"
	---  $picture
		This function takes a picture from your webcam and sends it to an email of your choice.
		This function was made deliberately more difficult to use to protect the privacy of 
		users who don’t want to share images of themselves or their subs. The first time you 
		use this function, a warning will appear telling you that you need to enable less secure 
		access to the gmail account that you will be sending pictures from. Follow the 
		link and sign in using the account you wish to use. It must be a gmail account.
		A text file has been created in the Resources\ folder called Cam Info.txt will be
		created. Fill out your login information to the gmail account you wish to use in 
		the format laid out for you. In order to keep the warning from appearing again,
		ensure that the third line equals 1. In the fourth line of the Cam Info.txt file
		you will have the option of specifing who you would like to receive your image. if you
		leave this line blank, your image will be sent to me*. Most users create a new email 
		account and use it exclusively for this purpose.
			*None of your information is shared with me and I will never attempt to communicate 
			with those of you who use this function. 
			
			This program will never take a picture of you without your consent. It is included
			only for those who would find the exposure or punishment exciting. If there is no 
			Cam Info.txt file, this function has not been used or attempted.

	---  $writeforme[number]
		This sets the remaining number of lines to whichever number you've selected. You can
		type lines in between matches and set the number of remaining lines to 0 once the 
		match begins by binding $writeforme0 to one of the buttons. If you absolutely must
		exit the writeforme menu and you want to preserve your place in the punishments and 
		rewards, entering [] into the entry box will reset the number of remaining sentences
		you are to write to zero, and end your current writing session.
	---  $wordsearch easy,medium,hard
		I made this function after seeing some really cool puzzles that another reddit user
		had made. I thought it would be a fun thing to do during flight paths, queues and such.
		SO, its easy to use, you just enter '$wordsearch easy' and then it will generate a word
		seach based on words within the Healslut Subjects and Healslut Adjectives files.
		Running '$wordsearch easy' again will close the window.
	--- $dicerolls
		This simple tweak to the $text macro allows the user to roll dice for the purpose of 
		playing Faproulette or anything else! '$diceroll8 6d10' shows six 10 sided dice for 8
		seconds

Here is a good example of the lines you'd want to include in the punishments and rewards

example rewards.txt

$+vibe10,$+rotate10,$+air3,$pinup Healslut
$text10 You're my dumb little supportslut 
$playvideo titfuck.mp4,$playsound titfuck.mp3


			#### Action Buttons Functionality ####
By popular request we now have ten optional buttons for the user to customize! they function 
just like the punish/reward buttons except that the first line of each of them is the name of 
a file with the Resources/ButtonLabels/ folder. You can find good examples of their usage 
prepackaged into the newest release. The nomenclature for setting up buttons on the Action Menu
follows below:
RULENAME ButtonA
RULENAME ButtonB
RULENAME ButtonC
RULENAME ButtonD
RULENAME ButtonE
RULENAME ButtonF
RULENAME ButtonG
RULENAME ButtonH
RULENAME ButtonI
RULENAME ButtonJ

NOTE: This program does not currently support any more than 10(A-J) buttons.



			#### Killfeed Monitor ####
			
This long awaited feature monitors the killfeed and executes lines from four files;
Overwatch DeathAssist/DeathDom/DeathSub/DeathTeam.txt which will determine what happens to the sub upon
one of those events. This process can be detected several times depending on how long the image remains in
the fillfeed. If it doesnt work for you, its possible that the Character icon screenshots I used are only 
good for my resolution size (2560,1440). I will do my best to acquire and package alternate versions of my 
icon screenshots so more users can enjoy this feature with ease. 

If you experience lag while using the Killfeed monitor, disabling freeplay should reduce the system load



			#### Vibrator Functionality ####
			
The user can use the punishment and reward buttons to control their vibrator. Alternately if the user 
enjoys Overwatch, the program can detect the users on fire meter and control the vibe speed based on
the meter. In order to do this, you MUST set the game from None to OW, EVEN IF YOU ARE NOT USING THE 
OVERLAY! This signals the program to look for an on fire meter on screen. I have implemented this 
requirement to save on hardware resources.



			#### Wordsearch ####

This neat function randomly generates a wordsearch based on adjective and subject files! it even has a
way to move it across the screen! Now you'll never get bored on flightpaths or autorun!



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



			#### Desktop Background ####
			
The checkbox which controls whether or not to chnage your desktop background on launch/close can be found in the
edit menu. To configure your own background or slutty background, simply replace the original ones packaged with 
your download. It is important to use the correct file type .png as no other file type is currently supported. You
can use microsoft paint or paint.net to convert jpgs into pngs by selecting the 'Save As' Option.


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

Version 1.4.5
		--- Text Functions
	-	Introducing the new Sissy/Bimbo Hypo Text package that is over 150 lines! To implement 
		this package a number of new replacement codes have been added. To use this, select 
		either Sissy/Bimbo rather than None in the Feminization option
		-	New Code: o99=girlfriend/boyfriend	(subsex=male / subsex=female)
		-	New Code: r00=he/she				(subsex=male / subsex=female)
		-	New Code: f99=sissy/bimbo			(subsex=male / subsex=female)
		-	New Code: f99s=sissies/bimbos		(subsex=male / subsex=female)
		-	New Code: f00=clitty/fuckhole		(subsex=male / subsex=female)
		-	New Code: w00=man/woman				(subsex=male / subsex=female)

		--- Overlay Functions
	-	Added Reward Chime.mp3 to balance the Punishment Buzz file. This helps lay the groundwork
		for more complete default rulesets
	-	Customize Punishment/Reward macros
			$RandText-Insult
			$RandText-Praise
	-	Write For Me now keeps track of your successful inputs vs failures, and plays tone to reward
		completed lines
	-	Attempted to fix a bug which affects users by falsly declaring that the program cannot
		locate certain resources
		
		--- The Killfeed Monitor
	-	Added support for the death of the submissive in League of Legends in 1920x1080

		--- Menu Functions
	-	Updated the version checker to exclude WIP and prerelease versions
	-	Fixed a bug that would allow the user to open two overlays at once
	-	Added a few new background gifs, removed others that didnt convert well
	-	Added a new text set 'feminization' which has bimbo/sissy related lines. To exclude
		these, one only needs to set their sex to None
	-	Added a feature to load presets that will come in handy once the LoL and OW premade 
		rules are finished
	



Version 1.4.4
		--- Menu Functions
	-	Added an option to change the users desktop background while using the overlay for
		full immersion 
	-	Added an 'Unlimited' feature in the word count which extends the previous maximum
		amount of words by 52
	-	Fixed a bug which would sometimes put either the banner, words, or rules on the wrong
		layer
		
		--- The Killfeed Monitor
	-	Added support for the death of the submissive in League of Legends

Version 1.4.3
		--- Menu Functions
	-	Fixed compatibility  on 1366x768 monitors. Killfeed Functionality is not yet 
		supported for this monitor size
	- 	Changed global transparent color to #f7e9f1, a light pink, which should mitigate 
		the cases where a pinup becomes completely transparent
	-	Retooled the setting Image Flash Delay into Cycle Delay, which now acts more 
		consistently  with its name
	-	The Convert Images function will now resize images too large to be displayed
		on your screen. It may a take a while to run thought
	-	Rebuilt the settings menu to organize all of the hodge-podge features ive added
		on this last year. My hope is that this will help me build more consistent 
		features in the future
	-	Refactored a bunch of old code so that it is more easily  maintainable  and easier
		to look at
	-	Fixed an issue where Write for me lines would exceed the length  of the box that
		they are displayed within
	-	Added many more entries into the Humiliation.txt and Subject.txt files
	-	Reworked the Healslut Games so they would live inside individual folders
	-	Fixed the UI to properly block out Enable Pinups when Turbo Hypno is active
	-	Fixed Write for me to retain focus in between sentances
		
Version 1.4.2
		--- Menu Functions
	-	Fix to enable Killfeed Functionality on 1920x1080 Monitors

Version 1.4.1
		--- Menu Functions
	-	Fixed an incompatibility issue with monitors shorter than 1440 pixels

Version 1.4
		--- Menu Functions
	-	Fixed a bug where editing the overlay without closing it wouldnt close the 
		action menu
	-	Added a gip so the user can move the main menu up or down the screen

		--- Overlay Functions
	-	Customize Punishment/Reward macros
			$wordsearch
			$diceroll
	-	Fixed an error where long background gifs would load in the wrong order
	- 	added the option to set a destination email so users can send their pics to 
		their doms automatically
		
		--- The Killfeed Monitor
	-	Screenscraping will now detect killfeed events and treat the sub appropriately
		depening on the following criteria
			- The Sub dies
			- The Dom dies
			- The Sub is credited with an assist
			- Someone on the Subs team dies (Freeplay only)
	
Version 1.3
		--- Menu Functions
	-	Fixed a bug where closing the program while the overlay is active would
		freeze instead of closing
	-	Fixed a bug when prevented clean closing of overlay when pinups, writeforme
		and backgrounds were disabled, but text was not
	-	Fixed a bug which prevented the use of the image converter
	-	Added version check function which will let you know when a new verison is
		released
	
		--- Action Frame
	-	Added additional buttons for various punish/reward macros
	
		--- Overlay Functions
	-	Added troubleshooting support for $playvideo related errors
	-	Fixed a setting which caused certain images to appear grainy or semi
		trasnparent
	-	Fixed a focus issue when using write for me where focus wouldnt properly set
		to the entry box
	-	Customize Punishment/Reward macros
			$pinup

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


Version 1.0
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
	-	Customize Punishment/Reward macros
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

Soon I intend to implement spoken lines from the users

I will work to enable the use of more vibrator brands. This will take time but I believe
it will be worth it

The program is pretty well optimized, but on slower computers a longer delay 
between screenshots could be used.

I'd like to provide a menu selector for download soundgasm files

	######################## Credits ########################

Lewd-Zko 	(twitter.com/LewdZko) 
	- 	for the image of their OC crystal which was modified and placed on the wordsearch page
u/iateacrayon 	(https://www.reddit.com/r/iateacrayon/wiki/list)
	- 	for their wiki/list of all those fetishes
this-is-embarrassing 	(https://github.com/this-is-embarrassing)
	- 	did some sexy jazz to the code, much sharper now.
u/Anonymous2150
	- 	Helping
		
And you, the user. <3


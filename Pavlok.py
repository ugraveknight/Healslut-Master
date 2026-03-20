from pavlok.main import Pavlok
import os
import keyboard
import requests
import webbrowser
import multiprocessing as mp


# Step 1:
# 	pip install pavlok

# Step 2:
#	Get your keys: http://pavlok-mvp.herokuapp.com/oauth/applications
#	In order to do that, give it the URL http://localhost:8000/authorize

# Step 3:
# 	Run the code below, and then visit http://localhost:8000/ and it login


def DoBeep():
	if PavlokProcess.is_alive():
		print('beep')
		r = requests.get('http://localhost:8000/beep')
	else:
		print('No Beep, the Server Process isnt online')

def DoVibe():
	if PavlokProcess.is_alive():
		print('Vibe')
		r = requests.get('http://localhost:8000/Vibe')
	else:
		print('No Vibe, the Server Process isnt online')
		
def DoZap():
	if PavlokProcess.is_alive():
		print('Zap')
		r = requests.get('http://localhost:8000/zap')
	else:
		print('No Zap, the Server Process isnt online')

def LaunchPavlokServer(_):
	ClientID = '6e7d6320adfcbf31104bff2dafe74ddfcb7e71b1b6034f92c03d4d9a655fd98f'
	Secret = '1fa160aa7b715a1e07a0f2c140516ea8d20c848beee0e724d3dfef39676a0b47'

	pavlok = Pavlok(
		client_id=ClientID,
		client_secret=Secret,
		title="Pavlok Python Client",
	)
	pavlok.start()

if __name__ == '__main__':
	keyboard.add_hotkey('-', DoBeep)
	keyboard.add_hotkey('+', DoVibe)
	keyboard.add_hotkey('*', DoZap)
	
	PavlokProcess = mp.Process(target=LaunchPavlokServer, args=('',))
	PavlokProcess.start()
	webbrowser.open('http://localhost:8000/login')
	PavlokProcess.join()
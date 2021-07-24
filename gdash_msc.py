
import gd
import keyboard
import os

# try reading gd memory. exit if we can't
try:
	gdash = gd.memory.get_memory()
	print("GD: MSC running! Press F12 to exit at any point.")
except RuntimeError:
	print("Please open Geometry Dash before running gdash_msc.py.")
	os._exit(1)

def check_hotkey(key):
	if (key.name == "`"): key.name = "0"
	# try block is here for non-digit key-presses
	try:
		if (int(key.name) >= 0 and int(key.name) <= 4):		# if key between 0 and 4 is pressed
			speed = 0.2 * int(key.name) + 0.7				# handles speeds for 0-3 as the speed increases linearly
			if key.name == "4": speed += 0.1				# correction for 4x speed
		
			gdash.set_speed_value(speed)					# change speed value in memory
	except Exception:
		pass

keyboard.on_press(check_hotkey)	# when a key is pressed, check if its a hotkey

keyboard.wait("f12")		# wait for input unless F12 is pressed
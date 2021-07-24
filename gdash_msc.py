
import gd
import keyboard
import os

speeds = [spd.value for spd in gd.api.SpeedConstant]	# speed values
try:
	speeds.remove(0.0)		# remove null speed
except:
	pass

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
		gdash.set_speed_value(speeds[int(key.name)])					# change speed value in memory
	except Exception:
		pass

keyboard.on_press(check_hotkey)	# when a key is pressed, check if its a hotkey

keyboard.wait("f12")		# wait for input unless F12 is pressed
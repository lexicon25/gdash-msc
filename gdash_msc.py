import gd
import keyboard
import os
import json

# default hotkey dictionary. overwritten with .json file contents.
hotkeys = {
		"EXIT": "f12",
		"SPEEDS": ["`","1","2","3","4"]
	}

speeds = [spd.value for spd in gd.api.SpeedConstant]	# speed values
try:
	speeds.remove(0.0)		# remove null speed
except ValueError:
	pass

# try getting into GD. exit if we can't.
try:
	gdash = gd.memory.get_memory()
	print("GD: MSC is now running! Press the exit hotkey (currently ", hotkeys["EXIT"], ") to exit at any point.", sep="")
except RuntimeError:
	print("Please open Geometry Dash before running gdash-msc.")
	os._exit(1)

# load hotkey json file.
try:
	hk = open("hk.json", "r")
	hotkeys = json.load(hk)
	hk.close()
except FileNotFoundError:
	print("Hotkey .json file not found. Creating with default hotkeys.")
	hk = open("hk.json", "w")
	json.dump(hotkeys, hk)
	hk.close()

def check_hotkey(key):
	if (key.name == hotkeys["EXIT"]): os._exit(1)	# exit if we want to exit
	if (key.name in hotkeys["SPEEDS"]):
		gdash.set_speed_value(speeds[hotkeys["SPEEDS"].index(key.name)])	# set speed value in memory
		gdash.write_float32(speeds[hotkeys["SPEEDS"].index(key.name)], 0x3222D0, 0x164, 0x228, 0x648)	# set player 2 speed simultaneously

keyboard.on_press(check_hotkey)		# when a key is pressed, check if its a hotkey

keyboard.wait(hotkeys["EXIT"])				# wait for input unless the exit key is pressed.
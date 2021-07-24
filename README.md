# `gdash-msc`
`gdash-msc` is a simple python script that allows you to manually change how fast the icon moves in Geometry Dash. It is intended to be used on Windows machines (sorry Mac and possibly Linux users)

At no point should `gdash-msc` do anything nasty with your savefile or GD account. It only uses `gd.py` to set the speed value of the icon.

## How to use
1. Download Python 3
2. Download the files (either through downloading the zip file or cloning the repository)
3. Run `setup.bat` to install the `gd.py` and `keyboard` libraries
4. Open Geometry Dash
5. Run `run.bat`

At this point, `gdash-msc` will be running until you press the exit hotkey.

## `hk.json`
`hk.json` is the hotkey file. `gdash-msc` will read the file to get which keys it should be checking for exiting or changing the speed. By default, `hk.json` is laid out as follows:

```json
{"EXIT": "f12", "SPEEDS": ["`", "1", "2", "3", "4"]}
```

Meaning that `f12` is the exit hotkey, and that `` ` ``, `1`, `2`, `3`, and `4` control the speed changes (in increasing order of speed). These can be changed to your liking (though I wouldn't recommend setting any of them to the same key, weird things may happen)

If `hk.json` is deleted, renamed, or moved before `gdash-msc` is run, it will create a new one with the default hotkeys.
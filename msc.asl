/* Original Geometry Dash Autosplitter by ItsMaximum (https://github.com/ItsMaximum/autosplitters/blob/006477bd3839e1bd6494eb43427d51dd822ddd59/gd.asl) */

state("GeometryDash"){
  bool loadingMusic : "GeometryDash.exe", 0x003222A8, 0x128, 0x34, 0xC0, 0xC;
  string4 percentage : "GeometryDash.exe", 0x3222D0, 0x164, 0x124, 0xEC, 0x2A4, 0xE8, 0x8, 0x12C;
  float position : "GeometryDash.exe", 0x3222D0, 0x164, 0x224, 0x67C;
  byte8 gamemodes : "GeometryDash.exe", 0x3222D0, 0x164, 0x224, 0x638;
}

startup {
	vars.loadingLevel = false;
	if (timer.CurrentTimingMethod == TimingMethod.RealTime)
	{        
		var timingMessage = MessageBox.Show (
			"This game uses Time without Loads (Game Time) as the main timing method.\n"+
			"LiveSplit is currently set to show Real Time (RTA).\n"+
			"Would you like to set the timing method to Game Time?",
			"LiveSplit | Geometry Dash",
			MessageBoxButtons.YesNo,MessageBoxIcon.Question
		);
		if (timingMessage == DialogResult.Yes)
		{
			timer.CurrentTimingMethod = TimingMethod.GameTime;
		}
	}
}

isLoading{return vars.loadingLevel;}

split{
	vars.finishLevel = old.percentage != current.percentage && current.percentage == "100%";
	vars.changeMode = false;
	for (int i=0; i<6; i++) {
		if (current.gamemodes[i] != old.gamemodes[i]) { vars.changeMode = true; break; }
	}
	return vars.finishLevel || vars.changeMode;
}

reset{
	if (current.gamemodes[7] == 1) {return true; }
}

start{return old.position == 0 && current.position != 0;} 

update {
	print("[GD ASL] Level Percentage: " + current.percentage + 
	"\n[GD ASL] Player Position: " + current.position.ToString() +
	"\n[GD ASL] Loading Music ? " + current.loadingMusic.ToString() +
	"\n[GD ASL] Loading Level ? " + vars.loadingLevel.ToString());
	if(!old.loadingMusic && current.loadingMusic) {
		vars.loadingLevel = true;
	}
	if(old.position == 0 && current.position != 0) {
		vars.loadingLevel = false;
	}
	
}

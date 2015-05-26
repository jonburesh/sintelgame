import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	click = cont.sensors["click"].positive or cont.sensors["enter"].positive or cont.sensors["A"].positive
	
	mouseover = cont.sensors["savesel"].positive
	setting = cont.sensors["once"].owner

	resume = cont.actuators["resume"]
	remove = cont.actuators["remove"]

	if mouseover and click:
		if own['close']!=1:
			own['close']=1

	if own['close'] ==1:
		try:
			gamesettings = open("config.ini", "w")
		except:
			try:
				gamesettings = open("lib/config.ini", "w")
			except:
				pass
		
		gamesettings.write(setting['gameresolution']+"\n")
		gamesettings.write(setting['gamequal']+"\n")
		gamesettings.write(setting['GLSL']+"\n")
		gamesettings.close()
		bge.logic.gameresolution = setting['gameresolution']
		bge.logic.gamequal = setting['gamequal']
		bge.logic.GLSL = setting['GLSL']
		print( 'Saved data:',setting['gameresolution'],setting['gamequal'],setting['GLSL'])
		cont.activate(resume)
		cont.activate(remove)

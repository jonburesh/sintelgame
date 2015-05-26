import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	exit = cont.sensors["exitover"].owner
	newgame = cont.sensors["newgameover"].owner
	resume = cont.sensors["resumeover"].owner
	settings = cont.sensors["settingsover"].owner

	exitover = cont.sensors["exitover"].positive
	newgameover = cont.sensors["newgameover"].positive
	resumeover = cont.sensors["resumeover"].positive
	settingsover = cont.sensors["settingsover"].positive

	up = cont.sensors["up"].positive or cont.sensors["joyup"].positive
	down = cont.sensors["down"].positive or cont.sensors["joydown"].positive
	enter = cont.sensors["enter"].positive or cont.sensors["A button(xbox)"].positive
		
	if exitover:
		exit['selected']=True
		resume['selected']=False
		settings['selected']=False
		newgame['selected']=False
	if resumeover and resume['save']==True:
		resume['selected']=True
		exit['selected']=False
		settings['selected']=False
		newgame['selected']=False
	if settingsover:
		settings['selected']=True
		exit['selected']=False
		resume['selected']=False
		newgame['selected']=False
	if newgameover:
		newgame['selected']=True
		exit['selected']=False
		resume['selected']=False
		settings['selected']=False

	if resume['selected']==True:
		if resume['save']==True:
			if enter:
				resume['activate']=True
			if down and own['wait']>=.2:
				newgame['selected']=True
				resume['selected']=False
				own['wait'] =0
			if up and own['wait']>=.2:
				exit['selected']=True
				resume['selected']=False
				own['wait'] =0
		else:
			newgame['selected']=True
			resume['selected']=False
	if newgame['selected']==True:
		if enter:
			newgame['activate']=True
		if up and own['wait']>=.2:
			if resume['save']==True:
				resume['selected']=True
				newgame['selected']=False
				own['wait'] =0
			else:
				exit['selected']=True
				newgame['selected']=False
				own['wait'] =0
		if down and own['wait']>=.2:
			settings['selected']=True
			newgame['selected']=False
			own['wait'] =0
	if settings['selected']==True:
		if enter:
			settings['activate']=True
		if up and own['wait']>=.2:
			newgame['selected']=True
			settings['selected']=False
			own['wait'] =0
		if down and own['wait']>=.2:
			exit['selected']=True
			settings['selected']=False
			own['wait'] =0
	if exit['selected']==True:
		if enter:
			exit['activate']=True
		if up and own['wait']>=.2:
			settings['selected']=True
			exit['selected']=False
			own['wait'] =0
		if down and own['wait']>=.2:
			if resume['save']==True:
				resume['selected']=True
				exit['selected']=False
				own['wait'] =0
			else:
				newgame['selected']=True
				exit['selected']=False
				own['wait'] =0
				
	if exit['selected']==False and settings['selected']==False and newgame['selected']==False and resume['selected']==False:
		if resume['save']==True:
			resume['selected']=True
		else:
			newgame['selected']=True
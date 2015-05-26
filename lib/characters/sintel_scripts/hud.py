import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner
	hpbar = cont.sensors["hp"].owner
	expbar = cont.sensors["exp1"].owner
	
	hp_replace = cont.actuators['hp_replace']
	
	target_hud = cont.actuators["off"].owner
	on = cont.actuators['on']
	off = cont.actuators['off']
	
	own.orientation =bge.logic.angle
	hpbar['hp'] = bge.logic.SHP
	expbar['exp'] = bge.logic.EXP
	own['hide'] = bge.logic.Hide

	if bge.logic.ObjectiveID ==0:
		own['noobj']=True
	else:
		own['noobj']=False
		
	if bge.logic.Locked == True:
		cont.activate(on)
		#target_hud.worldPosition[0] = bge.logic.LockedTarget.worldPosition[0]
		#print (bge.logic.LockedTarget.worldPosition)
		#target_hud.worldPosition[1] = bge.logic.LockedTarget.worldPosition[1]
		#ptarget_hud.worldPosition[2] = bge.logic.LockedTarget.worldPosition[2]
	elif bge.logic.Locked == False:
		cont.activate(off)
	
	#Set the proper amount of HP
	newmesh = str(hpbar['hp'])
	#Check to see if mesh is already correct
	if newmesh != hp_replace.mesh:
		if hpbar['hp'] >=100:
			hp_replace.mesh = '100'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=93.75:
			hp_replace.mesh = '93.75'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=87.5:
			hp_replace.mesh = '87.5'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=81.25:
			hp_replace.mesh = '81.25'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=75:
			hp_replace.mesh = '75'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=68.75:
			hp_replace.mesh = '68.75'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=62.5:
			hp_replace.mesh = '62.5'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=56.25:
			hp_replace.mesh = '56.25'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=50:
			hp_replace.mesh = '50'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=43.75:
			hp_replace.mesh = '43.75'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=37.5:
			hp_replace.mesh = '37.5'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=31.25:
			hp_replace.mesh = '31.25'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=25:
			hp_replace.mesh = '25'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=18.75:
			hp_replace.mesh = '18.75'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=12.5:
			hp_replace.mesh = '12.5'
			cont.activate(hp_replace)
		elif hpbar['hp'] >=6.25:
			hp_replace.mesh = '6.25'
			cont.activate(hp_replace)
		elif hpbar['hp'] ==0:
			hp_replace.mesh = '0'
			cont.activate(hp_replace)
import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	newmission = cont.sensors['newmission'].positive
	HideHUD = cont.sensors['HideHUD'].positive
	HUD = cont.sensors['HUD'].positive
	toggle_hud = cont.sensors['toggle_hud'].positive
	objcomp = cont.sensors['objcomp'].positive
	F1 = cont.sensors['F1'].positive
	
	suspend = cont.actuators['suspend']
	overlay = cont.actuators['overlay']
	sendnote = cont.actuators['sendnote']
	HUDover = cont.actuators['HUDover']
	setalert = cont.sensors['setalert']

	if newmission:
		bge.logic.MissionID = own['id']
		bge.logic.MissionTitle = own['title']
		bge.logic.MissionDiscription = own['discript']
		bge.logic.MissionSkipable = own['skip']
		suspend.scene = 'Scene'
		cont.activate(suspend)
		cont.activate(overlay)

	if setalert.positive:
		ALERT = setalert.bodies[0]
		bge.logic.Alert = int(ALERT)
		print ('Alert level set to: '+str(bge.logic.Alert))

	if objcomp:
		own['message'] ='Objective Complete'
		#cont.activate(sendnote)

	if HideHUD:
		bge.logic.Hide = True
		print ('Bye HUD!')
		
	if HUD:
		bge.logic.Hide = False
		#HUDover.scene = 'Overlay'
		#cont.activate(HUDover)
		print ('Bringing back the HUD', bge.logic.Hide)
		
	if toggle_hud or F1:
		bge.logic.Hide = not bge.logic.Hide
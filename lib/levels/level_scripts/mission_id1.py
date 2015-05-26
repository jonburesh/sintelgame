#NEEDS RE-CODE
from bge import logic

def main():
	cont = logic.getCurrentController()
	own = cont.owner
	
	arrive_docks = cont.sensors['arrive_docks'].positive
	crane_go = cont.sensors['crane_go'].positive
	crate_got = cont.sensors['crate_got'].positive
	end_level_mess = cont.sensors['end_lvl'].positive
	crate_drop = cont.sensors['crate_drop'].positive
	#col_food_crate = cont.sensors['col_food_crate']
	
	s_voice_1 = cont.actuators['s_voice_1']
	s_voice_2 = cont.actuators['s_voice_2']
	s_voice_3 = cont.actuators['s_voice_3']
	s_voice_4 = cont.actuators['s_voice_4']
	s_voice_5 = cont.actuators['s_voice_5']
	s_voice_6 = cont.actuators['s_voice_6']
	
	gamestate = cont.actuators['gamestate']
	cutstate = cont.actuators['cutstate']
	HUD = cont.actuators['HUD']
	NOHUD = cont.actuators['NOHUD']
	hide_pointer = cont.actuators['hide_pointer']
	playercam = cont.actuators['playercam']
	set_crane_cam = cont.actuators['set_crane_cam']
	set_2_cam = cont.actuators['set_2_cam']
	set_3_cam = cont.actuators['set_3_cam']
	objective = cont.actuators['objective']
	cuts = cont.actuators['cuts']
	no_cuts = cont.actuators['no_cuts']
	end_level = cont.actuators['end_level']
	
	player = logic.getCurrentScene().objects['sintel_col']
	crane_player_pos = logic.getCurrentScene().objects['crane_player_pos']
	crane_crate_pos = logic.getCurrentScene().objects['crane_crate_pos']
	cart = logic.getCurrentScene().objects['cart']
	end_level = logic.getCurrentScene().objects['end_level']
	
	own['timer']+=1
	crate = None
	got_a_crate = False
	
	if own['goal']==0:
		if own['sent']!=1:
			if own['timer']>=50:
				logic.globalDict['game_dialog'].append('Sintel: Geoffrey told me I could find the food at the docks.')
				#cont.activate(HUD)
				#cont.activate(hide_pointer)
				#cont.activate(s_voice_1)
				player['ENABLE_CART'] = False
				own['sent']=0
				own['timer']=0
				own['goal']=1
	
	if own['goal']==1:
		if own['sent']!=1:
			if own['timer']>=250:
				logic.globalDict['game_dialog'].append('I should take a look down there.')
				#cont.activate(s_voice_2)
				own['sent']=1
				logic.globalDict['game_notifications'].append('head to the docks')
		if arrive_docks:
			own['sent']=0
			own['timer']=0
			own['goal']=2

	if own['goal']==2:
		if own['sent']!=1:
			logic.globalDict['game_dialog'].append('The crate should be around here.')
			#cont.activate(s_voice_3)
			own['sent']=0
			own['timer']=0
			own['goal']=3
			
	if own['goal']==3:
		if own['sent']!=1:
			if own['timer']>=250:
				logic.globalDict['game_dialog'].append('Hmm. It must still be loaded on that ship.')
				#cont.activate(s_voice_4)
				own['sent']=0
				own['timer']=0
				own['goal']=4
	
	if own['goal']==4:
		if own['sent']!=1:
			if own['timer']>=250:
				logic.globalDict['game_dialog'].append('If I use the crane, I can grab the food crate.')
				logic.globalDict['game_notifications'].append('use the crane')
				#cont.activate(s_voice_5)
				own['sent']=1
		if crane_go:
			own['sent']=0
			own['timer']=0
			own['goal']=5
		if own['timer']>=8000:
			own['sent']=0
			own['timer']=0
			own['goal']=4
	
	if own['goal']==5:
		cont.activate(cutstate)
		cont.activate(NOHUD)
		cont.activate(set_crane_cam)
		logic.globalDict['game_dialog'].append("The crate I'm looking for will be marked as a food crate.")
		logic.globalDict['game_notifications'].append('mouse to move')
		logic.globalDict['game_notifications'].append('spacebar to grab')
		player.position = crane_player_pos.position
		own['goal']=6
	
	if own['goal']==6:
		if crate_drop:
			own['goal']=8
			#
	
	if own['goal']==8:
		if own['timer']>=1350:
			cont.activate(gamestate)
			cont.activate(playercam)
			cont.activate(no_cuts)
			player.position = crane_player_pos.position
			logic.crane_crate.position = crane_crate_pos.position
			logic.crane_crate.orientation = crane_crate_pos.orientation
			logic.crane_crate.suspendDynamics()
			logic.crane_crate.setParent(cart)
			player['ENABLE_CART'] = True
			own['goal']=9
			own['timer']=0
			logic.globalDict['game_notifications'].append('grab the cart')
				
	if own['goal']==9:
		cont.activate(HUD)
		if player['CART'] == True:
			#print ('COOL')
			logic.globalDict['game_dialog'].append('Got the crate. Time to head back.')
			cont.activate(objective)
			#cont.activate(s_voice_6)
			logic.globalDict['game_notifications'].append('return to garway')
			own['timer']=0
			own['goal']=10
	
	if own['goal']==10:
		end_level['end'] = True
		if own['timer'] >= 1000:
			cont.activate('end_level')
			own['timer']=0
			own['goal']=11
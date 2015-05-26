'''
--------------------------------------------------------------------------------------------------------
docks level script
--------------------------------------------------------------------------------------------------------
'''

from bge import logic

guide = logic.getCurrentScene().objects['guide']
player = logic.getCurrentScene().objects['sintel_col']
player_cam = logic.getCurrentScene().objects['player_camera']
scene_cam_1 = logic.getCurrentScene().objects['scene_cam_1']
scene_cam_2 = logic.getCurrentScene().objects['scene_cam_2']
scene_cam_3 = logic.getCurrentScene().objects['scene_cam_3']
end_scene_cam = logic.getCurrentScene().objects['end_scene_cam']
last_scene_cam = logic.getCurrentScene().objects['last_scene_cam']
bandit_cam = logic.getCurrentScene().objects['bandit_cam']
bandit_cam2 = logic.getCurrentScene().objects['bandit_cam2']
garway_ship = logic.getCurrentScene().objects['garway_ship']
garway_ship2 = logic.getCurrentScene().objects['garway_ship2']
bug_cam = logic.getCurrentScene().objects['bug_cam']
ship_group_new = logic.getCurrentScene().objects['ship_group_new_proxy']
player_new_pos = logic.getCurrentScene().objects['player_new_pos']
player_end_pos = logic.getCurrentScene().objects['player_end_pos']
arya_end_pos = logic.getCurrentScene().objects['arya_end_pos']
guide = logic.getCurrentScene().objects['guide']

def main(cont):
	#turn on the hud
	logic.sendMessage('HUD_on')
	player['torch'] = False
	#play the music
	cont.activate('docks_music')
	
	logic.globalDict['crane_go'] = False
	global crane_cam
	crane_cam = None

def loop(cont):
	own = cont.owner
	
	global crane_cam, bug_cam
	
	trigger_1 = cont.sensors["trigger_1"].positive
	ship_1_col = cont.sensors["ship_1_col"].positive
	ship_2_col = cont.sensors["ship_2_col"].positive
	trigger_1 = cont.sensors["trigger_1"].positive
	trigger_2 = cont.sensors["trigger_2"]
	trigger_3 = cont.sensors["trigger_3"]
	food_sensor = cont.sensors["food_sensor"].positive
	food_sensor2 = cont.sensors["food_sensor2"].positive
	delay = cont.sensors["delay"].positive
	guide_col = cont.sensors["guide_col"].positive
	crane_message = cont.sensors["crane_message"].positive
	wing_nip_dead = cont.sensors["wing_nip_dead"].positive
	
	scene = logic.getCurrentScene()
	
	if own['bug_encounter'] == False:
		if trigger_3.positive:
			own['current_objective'] = 16
			own['bug_encounter'] = True
			#trigger_3.owner.endObject()
	
	#if player skips straight to the cranes
	if crane_message:
		if own['cranes_completed'] == 0:
			own['current_objective'] = 6
		elif own['cranes_completed'] == 1:
			own['current_objective'] = 8
			own['current_dialog'] +=1
			own['go_dialog'] = True
			own['ship_timer'] = 0
			
	if ship_1_col:
		own['ship_num'] = 1
	if ship_2_col:
		own['ship_num'] = 2
	
	if own['current_objective'] == 0:
		if delay:
			own['current_objective'] = 1
		if trigger_1:
			own['current_dialog'] = 1
			own['current_objective'] = 1
			own['go_dialog'] = True
			
	elif own['current_objective'] == 1:
		garway_ship.playAction('ship_1_enter', 1, 1000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		garway_ship2.playAction('ship_2_enter', 1, 1000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1.25)
		own['current_dialog'] +=1
		own['current_objective'] = 2
		own['objective'] = 0
		own['go_dialog'] = True
		own['go_objective'] = True
		
	elif own['current_objective'] == 2:
		if trigger_1:
			own['current_dialog'] +=1
			own['current_objective'] = 3
			own['go_dialog'] = True	
			guide.state = logic.KX_STATE1
	#walk with guide
	elif own['current_objective'] == 3:
		if guide_col:
			own['current_dialog'] +=1
			own['current_objective'] = 4
			own['go_dialog'] = True	
			guide.state = logic.KX_STATE2
	#cutscene 
	elif own['current_objective'] == 4:
		if trigger_2.positive:
			own['current_dialog'] +=1
			own['current_objective'] = 5
			own['go_dialog'] = True	
			logic.sendMessage('player_freeze')
			logic.sendMessage('HUD_off')
			scene.active_camera = scene_cam_1
			scene_cam_1.playAction('scene_cam_1', 1, 1000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1.5)
	#cutscene ending
	elif own['current_objective'] == 5:
		own['current_dialog'] += 1
		own['go_dialog'] = True
		own['current_objective'] = 20
	elif own['current_objective'] == 20:
		if own['current_dialog'] == 5:
			own['current_dialog'] += 1
			own['go_dialog'] = True
		if round(scene_cam_1.getActionFrame(0)) == 700:
			scene.active_camera = scene_cam_3
			scene_cam_3.playAction('scene_cam_3', 1, 300, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1.5)
			own['objective'] = 1
			own['go_objective'] = True
		if not scene_cam_1.isPlayingAction(0):
			logic.sendMessage('player_unfreeze')
			logic.sendMessage('HUD_on')
			scene.active_camera = player_cam
			own['current_dialog'] += 1
			own['current_objective'] = 6
			own['go_dialog'] = True
	#bug encounter
	elif own['current_objective'] == 16:
		own['current_dialog'] = 8
		cont.activate('add_bugs')
		bug_cam.playAction('bug_cam', 1, 200, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = .75)
		logic.sendMessage('player_freeze')
		logic.sendMessage('HUD_off')
		own['objective'] = 2
		scene.active_camera = bug_cam
		own['go_dialog'] = True
		own['go_objective'] = True
		own['current_objective'] = 17
		player.position = player_new_pos.position
		player.orientation = player_new_pos.orientation
	#end bug scene
	elif own['current_objective'] == 17:
		if not bug_cam.isPlayingAction(0):
			logic.sendMessage('player_unfreeze')
			logic.sendMessage('HUD_on')
			scene.active_camera = player_cam
			own['current_objective'] = 18
	#fighting bugs
	elif own['current_objective'] == 18:
		if wing_nip_dead:
			own['bug_dead_count'] += 1
		if own['bug_dead_count'] ==4:
			own['bugs_dead'] = True
			own['current_objective'] = 19
	#bugs are dead
	elif own['current_objective'] == 19:
		own['current_dialog'] = 9
		own['go_dialog'] = True
		own['current_objective'] = 6
		logic.globalDict['crane_go'] = True
		own['objective'] = 1
		own['go_objective'] = True
	#go to ships
	elif own['current_objective'] == 6:
		if not food_sensor or not food_sensor2:
			if own['ship_num'] == 1:
				garway_ship.playAction('ship_1', 1, 4000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
			elif own['ship_num'] == 2:
				garway_ship2.playAction('ship_2', 1, 4000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
			own['current_dialog'] = 10
			own['current_objective'] = 7
			own['go_dialog'] = True	
			logic.sendMessage('player_unfreeze')
			logic.sendMessage('HUD_on')
			logic.sendMessage('crane_over')
			scene.active_camera = player_cam
			own['cranes_completed'] = 1
	#move the bandit ship
	elif own['current_objective'] == 7:
		if not ship_group_new.isPlayingAction(0):
			ship_group_new.playAction('bandit_ship_move', 1, 4000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
	#start bandit ship cut-scene
	elif own['current_objective'] == 8:
		if own['ship_timer'] >= 25:
			crane_cam = scene.active_camera
			scene.active_camera = bandit_cam
			bandit_cam.playAction('bandit_cam', 1, 200, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = .75)
			own['current_objective'] = 9
			own['current_dialog'] +=1
			own['go_dialog'] = True
	#switch cams
	elif own['current_objective'] == 9:
		if own['ship_timer'] >= 35:
			scene.active_camera = bandit_cam2
			bandit_cam2.playAction('bandit_cam_2', 1, 300, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
			own['current_objective'] = 10
	#bandit ship cut-scene is done
	elif own['current_objective'] == 10:
		if own['ship_timer'] >= 45:
			scene.active_camera = crane_cam
			own['current_objective'] = 11
	#back to crane
	elif own['current_objective'] == 11:
		own['current_objective'] = 12
		own['current_dialog'] +=1
		own['go_dialog'] = True
		if own['ship_num'] == 1:
			if not garway_ship.isPlayingAction(0):
				garway_ship.playAction('ship_1', 1, 4000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = .5)
		elif own['ship_num'] == 2:
			if not garway_ship2.isPlayingAction(0):
				garway_ship2.playAction('ship_2', 1, 4000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = .5)
	#crane while ship is leaving
	elif own['current_objective'] == 12:
		#did not get all food off
		if own['ship_timer'] >= 90:
			own['cranes_completed'] = 2
			own['current_dialog'] = 16
			own['current_objective'] = 14
			logic.sendMessage('crane_over')
			own['go_dialog'] = True	
			own['ship_timer'] = 0
			own['all_crates'] = False
	#got all food off
	elif own['current_objective'] == 14:
		logic.sendMessage('player_freeze')
		logic.sendMessage('HUD_off')
		scene.active_camera = end_scene_cam
		if own['ship_timer'] >= 15:
			logic.sendMessage('fade_out')
			own['current_objective'] = 15
	#wait for fade
	elif own['current_objective'] == 15:
		if own['ship_timer'] >=18:
			#cont.activate('end_level')
			own['current_objective'] = 21
	#end scene
	elif own['current_objective'] == 21:
		own['ship_timer'] = 0
		scene.active_camera = last_scene_cam
		logic.sendMessage('fade_in')
		player.position = player_end_pos.position
		player.orientation = player_end_pos.orientation
		guide.position = arya_end_pos.position
		guide.orientation = arya_end_pos.orientation
		ship_group_new.playAction('bandit_ship_move', 3000, 4000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		garway_ship2.playAction('ship_2', 3000, 4000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		own['current_objective'] = 22
	#send some dialogue
	elif own['current_objective'] == 22:
		if own['ship_timer'] >=5:
			own['current_dialog'] = 17
			own['go_dialog'] = True
			own['current_objective'] = 23
	elif own['current_objective'] == 23:
		if own['ship_timer'] >=10:
			if own['all_crates'] == True:
				own['current_dialog'] = 18
			else:
				own['current_dialog'] = 19
			own['go_dialog'] = True
			own['current_objective'] = 24
	elif own['current_objective'] == 24:
		if own['ship_timer'] >=20:
			logic.sendMessage('fade_out')
			own['current_objective'] = 25
	elif own['current_objective'] == 25:
		if own['ship_timer'] >=30:
			cont.activate('end_level')
	#finished with the cranes
	if own['current_objective'] == 12 or own['current_objective'] == 11 or own['current_objective'] == 8:
		if not food_sensor and not food_sensor2:
			own['cranes_completed'] = 2
			own['current_dialog'] = 15
			own['current_objective'] = 14
			own['go_dialog'] = True	
			own['ship_timer'] = 0
			logic.sendMessage('crane_over')
			own['all_crates'] = True 
			if own['ship_num'] == 1:
				if not garway_ship.isPlayingAction(0):
					garway_ship.playAction('ship_1', 1, 4000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
			elif own['ship_num'] == 2:
				if not garway_ship2.isPlayingAction(0):
					garway_ship2.playAction('ship_2', 1, 4000, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
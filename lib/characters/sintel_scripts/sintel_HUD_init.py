'''
--------------------------------------------------------------------------------------------------------
initiates the position of the HUD elements
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, render
import mathutils

UI_SCALE = .75
hp_add = logic.getCurrentScene().objects['hp_add']
hp_hit = logic.getCurrentScene().objects['hp_hit']

HUD_compass = logic.getCurrentScene().objects['HUD_compass']
full_hp = logic.getCurrentScene().objects['full_hp']

notification = logic.getCurrentScene().objects['notification']
dialog = logic.getCurrentScene().objects['dialog']
dialog_background = logic.getCurrentScene().objects['dialog_background']
HUD_fade = logic.getCurrentScene().objects['HUD_fade']

def init(cont):
	own = cont.owner
	
	try:
		if logic.globalDict['player_hp'] == None:
			logic.globalDict['player_hp'] = 100
	except:
		logic.globalDict['player_hp'] = 100
		
	try:
		logic.loadGlobalDict()
		if logic.globalDict['cfg_UI'] =='Small':
			UI_SCALE = .50
		elif logic.globalDict['cfg_UI'] =='Normal':
			UI_SCALE = .75
		elif logic.globalDict['cfg_UI'] =='Large':
			UI_SCALE = 1
	except:
		print ('No cfg_UI option found')
		UI_SCALE = .75

	#print ('GOT IT')
	screen_width = render.getWindowWidth()
	screen_height = render.getWindowHeight()
	#print (screen_width, screen_height)
	
	HUD_compass.position = mathutils.Vector((5.5, -2.65, 0.0))
	full_hp.position = mathutils.Vector((5.5, -2.65, 0.02))
	
	hp_add.position = mathutils.Vector((5.5, -2.65, 0.01))
	hp_hit.position = mathutils.Vector((5.5, -2.65, 0.01))
	
	HUD_compass.localScale =  mathutils.Vector((UI_SCALE, UI_SCALE, UI_SCALE))
	full_hp.localScale =  mathutils.Vector((UI_SCALE, UI_SCALE, UI_SCALE))
	
	hp_add.localScale =  mathutils.Vector((UI_SCALE, UI_SCALE, UI_SCALE))
	hp_hit.localScale =  mathutils.Vector((UI_SCALE, UI_SCALE, UI_SCALE))
	
	if own['show_hud']:
		HUD_compass.playAction('fade_in', 1, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		full_hp.playAction('fade_in', 1, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
	else:
		HUD_compass.playAction('fade_in', 1, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		full_hp.playAction('fade_in', 1, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		
	hp_add.playAction('hp_notify', 30, 30, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
	hp_hit.playAction('hp_notify', 30, 30, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
	
	HUD_fade.playAction('fade_in', 10, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = .2)
	
	#HUD_compass.playAction('fade_in', 10, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)

def send_note():
	own = logic.getCurrentController().owner
	
	notice_text = logic.getCurrentScene().objects['notice_text']
	
	notice_text.text = logic.globalDict['game_notifications'][0]
	logic.globalDict['game_notifications'].pop(0)
	logic.globalDict['game_last_notification'] = notice_text.text
	
	print (notice_text.text)
	
	notification.playAction('menu_flip', 1, 25, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)

def send_reminder():
	#sends a reminder of the current objective
	own = logic.getCurrentController().owner
	
	if logic.globalDict['game_objective'] != '':
		if logic.globalDict['game_objective'] not in logic.globalDict['game_notifications']:
			if own['note_sent'] == False:
				logic.globalDict['game_notifications'].append(logic.globalDict['game_objective'])
	else:
		print ('no current objective')
		
def send_dialog():
	cont = logic.getCurrentController()
	own = cont.owner
	
	dialog_text = logic.getCurrentScene().objects['dialog_text']
	dialog_background.localScale[0] = 0.33
	dialog_text.text = logic.globalDict['game_dialog'][0]
	logic.globalDict['game_dialog'].remove(dialog_text.text)
	d_length = len(dialog_text.text)
	#print (d_length)
	#print (dialog_background.localScale[0])
	dialog_background.localScale[0] = dialog_background.localScale[0] * (d_length * 2)
	dialog_text.position[0] = (-dialog_background.localScale[0]*.1) - (d_length *.065)
	
	
	print (dialog_text.text)
	
	dialog.playAction('dialog_flip', 1, 25, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
	
def update_hud():
	own = logic.getCurrentController().owner
	if own['show_hud'] == False:
		HUD_compass.playAction('fade_in', 10, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		full_hp.playAction('fade_in', 10, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
	elif own['show_hud'] == True:
		HUD_compass.playAction('fade_in', 1, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		full_hp.playAction('fade_in', 1, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)

def hide_hud(cont):
	own = cont.owner
	if own['hide'] != True:
		if logic.globalDict['sintel_0_threat'] == []:
			HUD_compass.replaceMesh('HUD_compass', True, False)
			if own['hide_time'] > 10 and logic.globalDict['player_hp'] ==100:
				if own['show_hud'] != False:
					own['show_hud'] = False
					own['hide_time'] = 0
					update_hud()
		else:
			HUD_compass.replaceMesh('HUD_compass_danger', True, False)
			own['hide_time'] = 0
			if own['show_hud'] == False:
				own['show_hud'] = True
				update_hud()

def main(cont):
	own = cont.owner
	
	hp_replace = cont.actuators['hp_replace']
	
	hp_up = cont.sensors['hp_up'].positive
	hp_down = cont.sensors['hp_down'].positive
	hide = cont.sensors['hide'].positive
	show = cont.sensors['show'].positive
	tab_key = cont.sensors['tab_key'].positive
	F1 = cont.sensors['F1'].positive
	fade_in = cont.sensors['fade_in']
	fade_out = cont.sensors['fade_out']
	
	
	suspend_scene = cont.actuators['suspend_scene']
	
	if hide and own['show_hud'] == True:
		own['show_hud'] = False
		update_hud()
			
	if show and own['show_hud'] == False:
		own['show_hud'] = True
		own['hide_time'] = 0
		update_hud()
	
	if F1:
		own['hide'] = not own['hide']
		own['hide_time'] = 0
		if own['hide'] == True:
			if own['show_hud'] == True:
				own['show_hud'] = False
				update_hud()
		else:
			if own['show_hud'] == False:
				own['show_hud'] = True
				update_hud()
	
	if tab_key:
		send_reminder()
					
	if fade_in.positive:
		HUD_fade.playAction('fade_in', 10, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = .2)
	if fade_out.positive:
		HUD_fade.playAction('fade_in', 1, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = .2)
	
	try:
		logic.globalDict['game_notifications']
	except:
		logic.globalDict['game_notifications'] = []
	try:
		logic.globalDict['game_dialog']
	except:
		logic.globalDict['game_dialog'] = []
	
	#check for any unsent notifications
	if logic.globalDict['game_notifications']!= [] and own['note_sent'] != True:
		send_note()
		own['note_time'] = 0
		own['note_sent'] = True
		
		note_length = len(logic.globalDict['game_notifications'])
		if note_length >= 1:
			own['note_wait'] = 5
		else:
			own['note_wait'] = 5.5
	
	if own['note_sent'] == True:
		if own['note_time'] > own['note_wait']:
			if not notification.isPlayingAction(0):
				notification.playAction('menu_flip', 25, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		if own['note_time'] > (own['note_wait'] +.5):
			own['note_sent'] = False
	
	if logic.globalDict['game_dialog']!= [] and own['d_sent'] != True:
		send_dialog()
		own['d_time'] = 0
		own['d_sent'] = True
		
		dialog_length = len(logic.globalDict['game_dialog'])
		if dialog_length >= 1:
			own['d_wait'] = 5
		else:
			own['d_wait'] = 5.5
		
	if own['d_sent'] == True:
		if own['d_time'] > own['d_wait']:
			if not dialog.isPlayingAction(0):
				dialog.playAction('dialog_flip', 25, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		if own['d_time'] > (own['d_wait'] + .5):
			own['d_sent'] = False
			
	#play HUD hurt / heal animations
	if own['show_hud']:
		if hp_up:
			if not hp_add.isPlayingAction(0):
				hp_add.playAction('hp_notify', 1, 30, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
		if hp_down:
			if not hp_hit.isPlayingAction(0):
				hp_hit.playAction('hp_notify', 1, 30, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1)
	
	player_hp = logic.globalDict['player_hp']
	
	#check if dead
	if player_hp <=0:
		print ('dead!')
		suspend_scene.scene = 'Scene'
		cont.activate(suspend_scene)
		cont.activate('death_overlay')
		cont.activate('suspend_HUD')
		
	newmesh = str(player_hp)
	
	#Check to see if mesh is already correct
	if newmesh != hp_replace.mesh:
		if player_hp >=100:
			hp_replace.mesh = '100'
			cont.activate(hp_replace)
		elif player_hp >=93.75:
			hp_replace.mesh = '93.75'
			cont.activate(hp_replace)
		elif player_hp >=87.5:
			hp_replace.mesh = '87.5'
			cont.activate(hp_replace)
		elif player_hp >=81.25:
			hp_replace.mesh = '81.25'
			cont.activate(hp_replace)
		elif player_hp >=75:
			hp_replace.mesh = '75'
			cont.activate(hp_replace)
		elif player_hp >=68.75:
			hp_replace.mesh = '68.75'
			cont.activate(hp_replace)
		elif player_hp >=62.5:
			hp_replace.mesh = '62.5'
			cont.activate(hp_replace)
		elif player_hp >=56.25:
			hp_replace.mesh = '56.25'
			cont.activate(hp_replace)
		elif player_hp >=50:
			hp_replace.mesh = '50'
			cont.activate(hp_replace)
		elif player_hp >=43.75:
			hp_replace.mesh = '43.75'
			cont.activate(hp_replace)
		elif player_hp >=37.5:
			hp_replace.mesh = '37.5'
			cont.activate(hp_replace)
		elif player_hp >=31.25:
			hp_replace.mesh = '31.25'
			cont.activate(hp_replace)
		elif player_hp >=25:
			hp_replace.mesh = '25'
			cont.activate(hp_replace)
		elif player_hp >=18.75:
			hp_replace.mesh = '18.75'
			cont.activate(hp_replace)
		elif player_hp >=12.5:
			hp_replace.mesh = '12.5'
			cont.activate(hp_replace)
		elif player_hp >=6.25:
			hp_replace.mesh = '6.25'
			cont.activate(hp_replace)
		elif player_hp <=0:
			hp_replace.mesh = '0'
			cont.activate(hp_replace)
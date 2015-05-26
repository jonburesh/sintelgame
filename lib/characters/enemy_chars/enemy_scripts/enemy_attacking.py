'''
--------------------------------------------------------------------------------------------------------
responsible for attacking + attack animations
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from random import choice, randint

attack_choice = ''
attack_choices = []

def init(cont):
	global attack_choice, attack_choices
	own = cont.owner
	rig = own.children[own['TYPE']+'_rig']
	
	#if we have more than half health, normal and special attacks
	if own['health'] > (own['max_health'] / 2):
		if own['TYPE'] == 'snail':
			attack_choices = ['normal', 'special', 'normal']
		else:
			attack_choices = ['normal']
	#if not, introduce a 'flee' option
	else:
		if own['TYPE'] == 'snail':
			attack_choices = ['special', 'dig', 'special', 'normal', 'normal']
	#pick one
	attack_choice = choice(attack_choices)
	
	#print (attack_choice)
	
	if attack_choice == 'dig':
		own.state = logic.KX_STATE16
	elif attack_choice == 'special':
		special = logic.getCurrentScene().addObject(own['TYPE']+'_special_spawn', own, 35)
		special.localPosition[2] -=.5
		special.setParent(own)

	if own['TYPE'] == 'snail':
		attack_animations = ['_attack','_attack_2','_attack']
	else:
		attack_animations = ['_attack']
	
	play_attack = choice(attack_animations)
	
	atk_act = rig.actuators[own['TYPE']+play_attack]
	end_frame = atk_act.frameEnd
	rig.playAction(own['TYPE']+play_attack, 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)
	
def main(cont):
	own = cont.owner
	rig = own.children[own['TYPE']+'_rig']
	#track target
	threat = logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'][0]
	enemy_track = cont.actuators['enemy_track']
	enemy_track.object = threat
	cont.activate('enemy_track')
	#damage target
	if own['dmg_done'] == False:
		if round(rig.getActionFrame(0)) == 8:
			if 'health' in threat:
				threat['health'] -= calc_damage(own, threat)
				if own in logic.globalDict[threat['TYPE']+ '_'+ str(threat['ID']) + '_threat']:
					logic.globalDict[threat['TYPE']+ '_'+ str(threat['ID']) + '_threat'].insert(0, logic.globalDict[threat['TYPE']+ '_'+ str(threat['ID']) + '_threat'].pop(own))
				else:
					logic.globalDict[threat['TYPE']+ '_'+ str(threat['ID']) + '_threat'].insert(0, own)
				own['dmg_done'] = True
				
			else:
				for items in threat.children:
					item_name = items.name
					if 'player_stats' in item_name:	
						items['hp'] -= calc_damage(own, threat)
						own['dmg_done'] = True
					#pass
	#back to engage
	if own['dig_time'] >1:
		own.state = logic.KX_STATE3
		own['dmg_done'] = False
		own['dig_time'] = 0

#special function for the rock snake
def rock_main(cont):
	own = cont.owner
	rig = own.children[own['TYPE']+'_rig']
	own['hitable'] = True
	#track target
	threat = logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'][0]
	tracker = logic.getCurrentScene().objects['rock_snake_tracker']
	tracker.position = threat.position
	#damage target
	if own['dmg_done'] == False:
		if round(rig.getActionFrame(0)) == 25:
			if 'health' in threat:
				threat['health'] -= calc_damage(own, threat)
				if own in logic.globalDict[threat['TYPE']+ '_'+ str(threat['ID']) + '_threat']:
					logic.globalDict[threat['TYPE']+ '_'+ str(threat['ID']) + '_threat'].insert(0, logic.globalDict[threat['TYPE']+ '_'+ str(threat['ID']) + '_threat'].pop(own))
				else:
					logic.globalDict[threat['TYPE']+ '_'+ str(threat['ID']) + '_threat'].insert(0, own)
				own['dmg_done'] = True
				
			else:
				for items in threat.children:
					item_name = items.name
					if 'player_stats' in item_name:	
						items['hp'] -= calc_damage(own, threat)
						own['dmg_done'] = True
					#pass
	#back to engage
	if own['dig_time'] >2:
		own.state = logic.KX_STATE3
		own['dmg_done'] = False
		own['dig_time'] = 0

def calc_damage(attacker, defender):
	global attack_choice
	rando = randint(217,255)
	damage = ((attacker['BASE_ATK'])/defender['BASE_DEF']) * rando / 255
	damage = round(damage, 1)
	#special attack 
	if attack_choice == 'special':
		damage = damage * 2
	#difficulty
	try:
		if logic.globalDict['cfg_difficulty'] == 'Casual':
			damage = damage * .3
		elif logic.globalDict['cfg_difficulty'] == 'Easy':
			damage = damage * .7
		elif logic.globalDict['cfg_difficulty'] == 'Normal':
			damage = damage
		elif logic.globalDict['cfg_difficulty'] == 'Hard':
			damage = damage * 1.5
	except:
		pass
	#done calculating
	print ('Enemy DMG:', damage)
	return damage
'''
--------------------------------------------------------------------------------------------------------
responsible for attacking + attack animations
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from random import randint
import sintel_scripts.player_sounds

scene = logic.getCurrentScene()

sintel_rig = scene.objects['sintel_rig']

#set some static vars
ACCEL_RATE = .2
GRAV = -9.8
HIT_LIST = []

def main(cont):
	own = cont.owner
	
	#get some logic bricks
	attack_track = own.actuators['attack_track']
	staff_col = cont.sensors['staff_col']
	
	#if attack animation isn't playing, play it and move forward a tad
	if own['ATK_PLAY'] == False:
		if own['ATK_COMBO'] ==0:
			sintel_rig.playAction('sintel_attack_1', 1, 24, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = own['ANIM_SPEED'] * 1.5, blendin = 5)
			own['ATK_PLAY'] = True
			own.setLinearVelocity([0, 5, 0], True)
		elif own['ATK_COMBO'] ==1:
			sintel_rig.playAction('sintel_attack_2', 1, 17, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = (own['ANIM_SPEED'] / 1.5), blendin = 5)
			own['ATK_PLAY'] = True
			own.setLinearVelocity([0, 5, 0], True)
		elif own['ATK_COMBO'] ==2:
			sintel_rig.playAction('sintel_attack_3', 1, 51, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = own['ANIM_SPEED'] * 1.25, blendin = 5)
			own['ATK_PLAY'] = True
			own.setLinearVelocity([0, 3, 0], True)
		else:
			sintel_rig.playAction('sintel_attack_1', 1, 24, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = own['ANIM_SPEED'], blendin = 5)	
			own['ATK_PLAY'] = True
		#reset the combo
		if own['ATK_COMBO'] == own['MAX_COMBO'] -1:
			own['ATK_COMBO'] = 0
			own['COMBO_FINISH'] = True
		else:
			own['ATK_COMBO'] += 1
			own['COMBO_TIME'] = 0
	#done with animations, return to idle
	elif not sintel_rig.isPlayingAction(0):
		own.state = logic.KX_STATE1
		own.setLinearVelocity([0, 0, -9.8], True)
		own['ATK_PLAY'] = False
		own['COMBO_FINISH'] = False
		own['dmg_done'] = False
		cont.deactivate(attack_track)
	#deal damage to what was hit
	if HIT_LIST != []:
		for hit_item in HIT_LIST:
			deal_damage(hit_item, own, cont)
	#if there is a target, track it
	if own['TARGET'] != '':
		track_obj = logic.globalDict['target']
		try:
			#if we are close, track the target
			dist = own.getDistanceTo(track_obj)
			if dist < 8:
				attack_track.object = track_obj
				cont.activate(attack_track)
				if dist >4:
					own.setLinearVelocity([0, 5, -9.8], True)
		except:
			pass
	#check to see if the staff has collided with anything		
	if staff_col.positive:
		#check for collision after a certain frame 
		if own['dmg_done'] == False:
			if own['ATK_COMBO'] ==1:
				if round(sintel_rig.getActionFrame(0)) >= 10:
					check_hit(staff_col.hitObject)
			if own['ATK_COMBO'] ==2:
				if round(sintel_rig.getActionFrame(0)) >= 8:
					check_hit(staff_col.hitObject)
			if own['ATK_COMBO'] ==0:
				if round(sintel_rig.getActionFrame(0)) >= 20 and round(sintel_rig.getActionFrame(0)) <= 30:
					check_hit(staff_col.hitObject)
#add all hitable objects to a list
def check_hit(hitObject):
	if 'hitable' in hitObject:
		#hit object can be hit
		if hitObject['hitable'] == True:
			#object gets damaged]
			if not hitObject in HIT_LIST:
				HIT_LIST.append(hitObject)
				hitObject['hitable'] = False
				print (HIT_LIST)
			
def deal_damage(hitObject, own, cont):		
	hitObject['health'] -= calc_damage(own, hitObject, own['COMBO_FINISH'])
	cont.activate(sintel_scripts.player_sounds.randSound('attack'))
	#check to see if this is an enemy or a prop
	if 'props' in hitObject:
		logic.globalDict[str(hitObject)+'_threat'] = own
	else:
		#are we already a threat?
		if own in logic.globalDict[hitObject['TYPE']+ '_' + str(hitObject['ID']) +'_threat']:
			#are we top priority?
			if not logic.globalDict[hitObject['TYPE']+ '_' + str(hitObject['ID']) +'_threat'][0] == own:
				#make us 1st
				logic.globalDict[hitObject['TYPE']+ '_' + str(hitObject['ID']) +'_threat'].remove(own)
				logic.globalDict[hitObject['TYPE']+ '_' + str(hitObject['ID']) +'_threat'].insert(0, own)
		#add us to the list
		else:
			logic.globalDict[hitObject['TYPE']+ '_' + str(hitObject['ID']) +'_threat'].insert(0, own)
	
	#own['dmg_done'] = True
	HIT_LIST.remove(hitObject)
	#if finisher move, knock back the object
	if own['ATK_COMBO'] ==0 and 'knockable' in hitObject:
		if hitObject['knockable'] == True:
			hitObject.state = logic.KX_STATE19
			#knockback particle fx
			scene.addObject('knockback', hitObject, 5)
			#print ('knocked!')
		else:
			hitObject.state = logic.KX_STATE4
	else:
		hitObject.state = logic.KX_STATE4
		
def calc_damage(attacker, defender, finisher):
	#add some randomness to damage
	rando = randint(217,255)
	#damage equation, rounded to 1st decimal
	damage = ((attacker['BASE_ATK'])/defender['BASE_DEF']) * rando / 255
	damage = round(damage, 1)
	#double the damage for a finishing mov
	if finisher:
		damage = damage * 2
	#print ('DMG:', damage)
	return damage
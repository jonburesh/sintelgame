'''
--------------------------------------------------------------------------------------------------------
enemy has died :[
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import enemy_scripts.enemy_sound

def init(cont):
	own = cont.owner
	
	own['dig_time'] = 0
	own['hitable'] = False
	
	#for each threat, remove us from thier list
	for threat in logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat']:
		if own in logic.globalDict[threat['TYPE']+ '_' + str(threat['ID']) + '_threat']:
			logic.globalDict[threat['TYPE']+ '_' + str(threat['ID']) + '_threat'].remove(own)
			print (logic.globalDict[threat['TYPE']+ '_' + str(threat['ID']) + '_threat'])
	
	rig = own.children[own['TYPE']+'_rig']
	death_act = rig.actuators[own['TYPE']+'_death']
	end_frame = death_act.frameEnd
	rig.playAction(own['TYPE']+'_death', 1, end_frame, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)
	
	try:
		cont.activate(enemy_scripts.enemy_sound.randSound('death'))
	except:
		pass
	
	own.setLinearVelocity([0, 0, -9.8], True)
	
	cont.activate(own['TYPE']+'_fade')

def main(cont):
	own = cont.owner

	if own['dig_time'] > 1.5:
		own.endObject()
		#send death message
		logic.sendMessage(own['TYPE']+'_dead')
		#logic.globalDict['player_engage_list'].remove(own)
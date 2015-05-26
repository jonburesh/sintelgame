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
	rig.playAction(own['TYPE']+'_emerge', 40, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = 1, blendin = 5)
	
	#cont.activate(enemy_scripts.enemy_sound.randSound('death'))

def main(cont):
	own = cont.owner
	
	rig = own.children[own['TYPE']+'_rig']
	
	try:
		if rig.constraints['rock_rig:tracker'].enforce > 0:
			rig.constraints['rock_rig:tracker'].enforce -= .01
	except:
		rig.constraints['rock_rig:tracker'].enforce = 0
	
	if own['dig_time'] > 2.5:
		own.endObject()
		#logic.globalDict['player_engage_list'].remove(own)
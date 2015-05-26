'''
--------------------------------------------------------------------------------------------------------
for hidden enemy types (takes the place of idle)
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
from random import randint
import enemy_scripts.enemy_sound


def main(cont):
	own = cont.owner
	
	threat_near = cont.sensors['threat_near']
	
	#get the rig
	rig = own.children[own['TYPE']+'_rig']

	#set vars for specific enemy type
	if own['TYPE'] == 'rock_snake':
		threat_near.distance = 20
	else:
		pass
	
	if threat_near.positive:
		#threat detected
		print ("Threat detected from",own['TYPE'],own['ID'])
		#threat = threat_near.hitObject
		#if this threat isnt already known, add it to the list
		for threat in threat_near.hitObjectList:
			if not threat in logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat']:
				logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'].append(threat)
		own.state = logic.KX_STATE5
		try:
			cont.activate(enemy_scripts.enemy_sound.randSound('growl'))
		except:
			pass
			
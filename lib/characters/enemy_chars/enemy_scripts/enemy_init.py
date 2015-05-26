'''
--------------------------------------------------------------------------------------------------------
sets up systems for enemy logic
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

def main(cont):
	own = cont.owner
	#give each enemy a unique ID
	
	try:
		ID = logic.globalDict['ID'] = logic.globalDict['ID'] + 1
	except:
		ID = logic.globalDict['ID'] = 0

	own['ID'] = ID
	#find out what type of enemy this is
	if own['TYPE'] == '':
		if 'snail_rig' in own.children:
			own['TYPE'] = 'snail'
		elif 'bandit_rig' in own.children:
			own['TYPE'] = 'bandit'
		elif 'rock_snake_rig' in own.children:
			own['TYPE'] = 'rock_snake'
		elif 'wing_nip_rig' in own.children:
			own['TYPE'] = 'wing_nip'

	#print ("Enemy ID:", ID, own['TYPE'])
	
	#each enemy has it's own list of threats
	logic.globalDict[own['TYPE']+ '_' + str(own['ID']) + '_threat'] = []
	logic.saveGlobalDict()
	#done initializing
	own.state = logic.KX_STATE2
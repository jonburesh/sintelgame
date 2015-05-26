#Attacking, Damage
import bge
import random as rand

#Damage calculation :O
def damage(lvl, atk, defen, staff):
	#Lvl = the player's level
	#Atk = the player's attack stat
	#Defen = the victim's defense stat
	#Staff = the power of the current staff
	rando = rand.randrange(217,255)
	dmg = (((2 * lvl +10) *atk )/defen) *staff *rando /255
	return dmg

def main():

	cont = bge.logic.getCurrentController()
	own = cont.owner

	Player = bge.logic.getCurrentScene().objects["PlayerCol"]

	staffhit = cont.sensors['staffhit']
	message = cont.actuators['message']
	enemyhit = cont.actuators['enemyhit']
	
	staff_swish = cont.actuators['staff_swish']
	wood_impact = cont.actuators['wood_impact']

	PlayerStats = cont.sensors['playerstats'].owner
	
	if own['Attacking']==True:
		cont.activate(staff_swish)
	
	#Check what was hit
		if staffhit.positive:
			hitanything = staffhit.hitObject
			own['hitobject']='nothing'
			if str(hitanything) !='None':
					if "wood" in hitanything:
						own['hitobject']='wood'
						cont.activate(message)
						cont.activate(wood_impact)
					#Check if an enemy was hit
					if "enemy" in hitanything:
						if Player['dmgdelt']==False:
							Player['Target'] = hitanything
							own['hitobject']='enemy'
							#Double check, then do damage
							if "hp" in hitanything:
								hitanything["hp"] -= damage(PlayerStats['lvl'], PlayerStats['atk'], hitanything["def"], PlayerStats['stf'])
								Player['dmgdelt']=True
								#report what was hit
								enemyhit.propName = str(hitanything)
								cont.activate(message)
								cont.activate(enemyhit)
								print (enemyhit.propName)
							else:
								print ('Hit object does not have HP')
					else:
						own['hitobject']='nothing'
						cont.activate(message)
		
		#Nothing was hit
		if own['hitobject']=='nothing':
			cont.activate(message)
			
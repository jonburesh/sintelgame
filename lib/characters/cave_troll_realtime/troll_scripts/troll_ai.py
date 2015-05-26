#Status 1 = Idle, 2 = Patrol, 3 = Watch, 4 = Chase, 5 = Attack
#Alert Level 1 = Normal, 2 = Watch auto, 3 = Attack auto, 4 = High Alert attack all
import random as rand
import bge


cont = bge.logic.getCurrentController()
own = cont.owner

Player = bge.logic.getCurrentScene().objects["PlayerCol"]
PlayerStats = bge.logic.getCurrentScene().objects["PlayerStats"]

def RanAttack():
	actionlist = ['attack1','attack2','attack3']
	action = rand.choice(actionlist)
	frames = 0
	if action =='attack1':
			frames = 15
	if action =='attack2':
			frames = 52
	if action =='attack3':
			frames = 40
	return action, frames

def Choice():
	attackornot = rand.choice([True,False])
	return attackornot

def Attack():
	PlayerStats['chp'] -= damage(own['elvl'], own['eatk'],PlayerStats['def'],own['type'])

#Damage calculation :O
def damage(lvl, atk, defen, type):
	#Lvl = the player's level
	#Atk = the player's attack stat
	#Defen = the victim's defense stat
	#Type = the type of enemy. used for bosses / special enemies
	rando = rand.randrange(217,255)
	dmg = (((2 * lvl +10) *atk )/defen) *type *rando /255
	return dmg

def main():

	playeratk = cont.sensors['playeratk']
	track = cont.actuators['track']
	playernear = cont.sensors['playernear']
	imhit = cont.sensors['imhit']
	hit = cont.actuators['hit']
	dead = cont.actuators['dead']
	sendexp = cont.actuators['sendexp']

	#Actions
	idle = cont.actuators['idle']
	walk = cont.actuators['walk']
	death =  cont.actuators['death']
	move =  cont.actuators['move']
	attack1 = cont.actuators['attack1']
	attack2 = cont.actuators['attack2']
	attack3 = cont.actuators['attack3']
	rem_par = cont.actuators['rem_par']
	troll_dead = cont.actuators['troll_dead']
	rig = cont.actuators['attack1'].owner

	print (own['status'])
	
	#Idle
	if own['status']==1:
		cont.activate(idle)
		cont.deactivate(track)
		
	#Chase
	if own['status']==2:
		own['speed']=5
		track.object = Player
		cont.activate(track)
		cont.activate(walk)
		cont.activate(move)
		cont.deactivate(attack1)
		cont.deactivate(attack2)
		cont.deactivate(attack3)
		cont.deactivate(idle)
				
	#Gotcha
	if own['status']==3:
		if not playernear.positive and own['wait']==False:
			own['status']=2
		if own['Attack']==False:
			cont.activate(idle)
			pass
		else:
			cont.deactivate(idle)
			pass
				
	#Was hit
	if imhit.positive and own['status']!=4:
		cont.activate(hit)
		
	#Pause re-actions
	if own['wait']==True:
		own['wtime']+=1
		if own['wtime']>50:
			own['wtime']=0
			own['wait']=False
				
	#Deal with hp
	if own['hp'] <=5 and own['dead']==False:
		own['hp'] =0
		cont.activate(death)
		#cont.activate(rem_par)
		#cont.activate(sendexp)
		own['dead']=True
		cont.deactivate(attack1)
		cont.deactivate(attack2)
		cont.deactivate(attack3)
		cont.deactivate(walk)
		cont.deactivate(move)
		cont.deactivate(idle)
		own['status']=4
				
	if own['dead']==True:
		if rig['dead']==24:
			cont.deactivate(attack1)
			cont.deactivate(attack2)
			cont.deactivate(attack3)
			cont.deactivate(walk)
			cont.deactivate(move)
			cont.deactivate(track)
			cont.deactivate(idle)
			cont.activate(rem_par)
			cont.activate(dead)
			cont.activate(troll_dead)
						
	#Player is in line of sight
	if playernear.positive and own['dead']!=True:
		own['wait']=True
		if own['status']==2:
			own['status']=3
		if own['status']==3:
			cont.deactivate(move)
			cont.deactivate(walk)
			cont.activate(idle)
			if own['Attack']!=True:
				own['atime']+=1
				if own['atime']>=100:
					own['atime']=0
					own['Attack']= Choice()
			if own['Attack']==True:
				reply, totalframes = RanAttack()
				cont.activate(reply)
				own['atime']=0
				if rig['frame']==totalframes:
					Attack()
					rig['frame'] =0
					own['Attack']=False
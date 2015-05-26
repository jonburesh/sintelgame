#Importing :)
from random import *
import bge
from sintel_scripts.player_fence_hop import fencehop
from sintel_scripts.player_ledge import ledgegrab

def RanAttack(type):
	#A simple function for generating random attacks
	#type: 0  = low profile, 1 = high profile
	lowpro = ['Sintel_AttackLow1','Sintel_AttackLow2']
	highpro = ['']
	action = ''
	frames = 20
	if type ==0:
		action = choice(lowpro)
		#We've got an action, now we need to find out how many frames it has. Defualt is 20
		if action =='Sintel_AttackLow1':
			frames = 15
	if type ==1:
		action = choice(highpro)
	#print (action)
	return action, frames

def main():
	#General Movement Script
	cont = bge.logic.getCurrentController()
	own = cont.owner

	#Load the sensors + actuators
	onground = cont.sensors['onground'].positive
	land_finder = cont.sensors['land_finder'].positive
	dirt = cont.sensors['dirt'].positive
	hitwall = cont.sensors['hitwall'].positive
	wall_ray = cont.sensors['wall_ray'].positive
	autojump = cont.sensors['autojump'].positive
	leftclick = cont.sensors['Leftclick'].positive
	attackhit = cont.sensors['attackhit']
	nomotion = cont.sensors['nomotion'].positive
	#enemy_near = cont.sensors['enemy_near'].positive
	auto_action = cont.sensors['auto_action']
	ledge_finder = cont.sensors['ledge_finder']
	move = cont.actuators['move']
	jumpjump = cont.actuators['jumpjump']
	tracktarget = cont.actuators['tracktarget']
	Sintel_Walk= cont.actuators['Sintel_Walk']
	Sintel_WalkStaff= cont.actuators['Sintel_WalkStaff']
	Sintel_Run= cont.actuators['Sintel_Run']
	Sintel_Idle= cont.actuators['Sintel_Idle']
	Sintel_IdleStaff= cont.actuators['Sintel_IdleStaff']
	Sintel_Fall= cont.actuators['Sintel_Fall']
	Sintel_Draw= cont.actuators['Sintel_Draw']
	Sintel_ReturnStaff= cont.actuators['Sintel_ReturnStaff']
	Sintel_AttackIdle= cont.actuators['Sintel_AttackIdle']
	Sintel_AttackWalk= cont.actuators['Sintel_AttackWalk']
	Sintel_AttackWalkBack= cont.actuators['Sintel_AttackWalkBack']
	Sintel_AttackWalkLeft= cont.actuators['Sintel_AttackWalkLeft']
	Sintel_AttackWalkRigh= cont.actuators['Sintel_AttackWalkRigh']
	Sintel_Leap = cont.actuators['Sintel_Leap']
	Sintel_Leap_Fall = cont.actuators['Sintel_Leap_Fall']
	Sintel_Leap_Land = cont.actuators['Sintel_Leap_Land']
	
	foot_fall = cont.actuators['foot_fall']

	#Other Objects
	Sintel_Rig = cont.sensors['Sintel_Rig'].owner

	#States
	attackstate= cont.actuators['attackstate']

	#Messages
	killmess = cont.sensors['killmess'].positive #Sintel has killed something :O

	#Attack Animations
	Sintel_AttackLow1= cont.actuators['Sintel_AttackLow1']
	Sintel_AttackLow2= cont.actuators['Sintel_AttackLow2']

	#HUD stuffs
	bge.logic.Locked = own['Locked']
	bge.logic.LockedTarget = own['Target']
	
	if onground and own['fall']!=True:
		own['falltimer']=0
		if own['fall']==True:
			own['landtime']+=1
		#Actions
		if own['isWkeyon']==1 or own['isjoyup']==1 or own['isAkeyon']==1 or own['isjoyright']==1 or own['isDkeyon']==1 or own['isjoyleft']==1 or own['isSkeyon']==1 or own['isjoydown']==1:
			if own['Running']!=True and own['Attacking']!=True:
			
				#Set track time
				own['track_time'] =7
				
				own['rtime']=0
				own['Idle']=False
				own['Walking']=True
				
				if own['equip']==True:
					if own['Locked']==False:
						cont.activate(Sintel_WalkStaff)
						cont.deactivate(Sintel_Walk)
						cont.deactivate(Sintel_AttackWalk)
						cont.deactivate(Sintel_AttackWalkBack)
						cont.deactivate(Sintel_AttackWalkLeft)
						cont.deactivate(Sintel_AttackWalkRigh)
					if own['Locked']==True:
						if own['direction']==1:
							cont.activate(Sintel_AttackWalk)
							cont.deactivate(Sintel_AttackWalkBack)
							cont.deactivate(Sintel_AttackWalkLeft)
							cont.deactivate(Sintel_AttackWalkRigh)
						elif own['direction']==5:
							cont.activate(Sintel_AttackWalkBack)
							cont.deactivate(Sintel_AttackWalk)
							cont.deactivate(Sintel_AttackWalkLeft)
							cont.deactivate(Sintel_AttackWalkRigh)
						elif own['direction']==7:
							cont.activate(Sintel_AttackWalkLeft)
							cont.deactivate(Sintel_AttackWalkBack)
							cont.deactivate(Sintel_AttackWalk)
							cont.deactivate(Sintel_AttackWalkRigh)
						elif own['direction']==3:
							cont.activate(Sintel_AttackWalkRigh)
							cont.deactivate(Sintel_AttackWalkBack)
							cont.deactivate(Sintel_AttackWalk)
							cont.deactivate(Sintel_AttackWalkLeft)
						cont.deactivate(Sintel_WalkStaff)
						cont.deactivate(Sintel_Walk)			
				if own['equip']==False:
					cont.activate(Sintel_Walk)
					cont.deactivate(Sintel_WalkStaff)
					cont.deactivate(Sintel_AttackWalk)
					cont.deactivate(Sintel_AttackWalkBack)
					cont.deactivate(Sintel_AttackWalkLeft)
					cont.deactivate(Sintel_AttackWalkRigh)
				cont.deactivate(Sintel_Run)
				cont.deactivate(Sintel_Fall)
				cont.deactivate(Sintel_Leap_Fall)
				cont.deactivate(Sintel_Idle)
				cont.deactivate(Sintel_IdleStaff)
				cont.deactivate(Sintel_AttackIdle)
			elif own['Running']==True:
				own['Walking']=False
				#Run timer
				own['rtime']+=1
				cont.activate(Sintel_Run)
				cont.deactivate(Sintel_AttackWalk)
				cont.deactivate(Sintel_AttackWalkBack)
				cont.deactivate(Sintel_AttackWalkLeft)
				cont.deactivate(Sintel_AttackWalkRigh)
				cont.deactivate(Sintel_WalkStaff)
				cont.deactivate(Sintel_Idle)
				cont.deactivate(Sintel_Fall)
				cont.deactivate(Sintel_Leap_Fall)
				cont.deactivate(Sintel_IdleStaff)
				cont.deactivate(Sintel_Walk)
				cont.deactivate(Sintel_AttackIdle)
				#Run
		
		#Set proper rotation and movement
		#W-Key
		if own['isWkeyon']==1 or own['isjoyup']==1 and own['isAkeyon']==0 and own['isjoyright']==0 and own['isDkeyon']==0 and own['isjoyleft']==0:
			if own['Attacking']!=True:
				#Slowly increasse speed for more realism
				own['direction']=1
				own['Tracking']=True
				#Short delay (adds realism)
				if own['runspeed'] < (own['speed']):
					own['runspeed'] += .15
				own.setLinearVelocity([0, own['runspeed'], 0], True)
					#cont.activate(move)
				if dirt:
					own['footprints']=True
				
		#Set turning 
		#D-Key
		if own['isDkeyon']==1 or own['isjoyright']==1:
			if own['Attacking']!=True:
				#Diagonals
				if own['isWkeyon']==1 or own['isjoyup']==1:
					own['direction']=2
				if own['isSkeyon']==1 or own['isjoydown']==1:
					own['direction']=4
				#Right
				if own['isWkeyon']==0 and own['isjoyup']==0 and own['isSkeyon']==0 and own['isjoydown']==0:
					own['direction']=3
				own['Tracking']=True
				if own['runspeed'] < (own['speed']):
					own['runspeed'] += .15
				if own['Locked']==False:
					own.setLinearVelocity([0, own['runspeed'], 0], True)
				else:
					own.setLinearVelocity([own['runspeed'], 0, 0], True)
					#cont.activate(move)
				if dirt:
					own['footprints']=True
				
		#A-Key
		if own['isAkeyon']==1 or own['isjoyleft']==1:
			if own['Attacking']!=True:
				#Diagonals
				if own['isWkeyon']==1 or own['isjoyup']==1:
					own['direction']=8
				if own['isSkeyon']==1 or own['isjoydown']==1:
					own['direction']=6
				#Left
				if own['isWkeyon']==0 and own['isjoyup']==0 and own['isSkeyon']==0 and own['isjoydown']==0:
					own['direction']=7
				own['Tracking']=True
				if own['runspeed'] < (own['speed']):
					own['runspeed'] += .15
				if own['Locked']==False:
					own.setLinearVelocity([0, own['runspeed'], 0], True)
				else:
					own.setLinearVelocity([(own['runspeed']*-1), 0, 0], True)
					#cont.activate(move)
				if dirt:
					own['footprints']=True
				
		#Backwards
		#S-Key
		if own['isSkeyon']==1 or own['isjoydown']==1:
			if own['Attacking']!=True:
				if own['isAkeyon']==0 and own['isDkeyon']==0 and own['isjoyleft']==0 and own['isjoyright']==0:
					own['direction']=5
					own['startwalk'] += .05
					own['Tracking']=True
				if own['runspeed'] < (own['speed']):
					own['runspeed'] += .15
				if own['Locked']==False:
					own.setLinearVelocity([0, own['runspeed'], 0], True)
				else:
					own.setLinearVelocity([0, (own['runspeed']*-1), 0], True)
					#cont.activate(move)
				if dirt:
					own['footprints']=True
		
		#Running I
		if own['isShifton']==True or own['isjoyrun']==1 and not hitwall and not wall_ray and own['Attacking']!=True and own['Fightmode']!=True:
			if own['landtime'] ==0:
				own['speed']=15
				own['Running']=True
				own['track_time'] =20
				own['Locked']=False
			else:
				own['speed']=5
		elif own['Locked']==True:
			own['speed']=3
		else:
			own['speed']=5
			own['Running']=False
			if own['runspeed'] > (5):
					own['runspeed'] = (5)
					
		#Running II (free running parts)
		if own['Running']==True:
			own['Locked']=False
			own['Fightmode']=False
			own['putcam']=False
			own['Target'] =''
			if auto_action:
				actionobj = auto_action.hitObject
				if str(actionobj) !='None':
					#Its a fence!
					if 'fence' in actionobj:
						if own['isSpaceon']:
							#Make sure we can hop
							if fencehop():
								cont.activate(Sintel_Leap)
								actionobj = None
							else:
								pass
			#Ledge
			#if ledge_finder.positive:
			if ledge_finder.hitObject !=None:
				ledge_obj = ledge_finder.hitObject
				#Player is pressing / holding space
				if own['isSpaceon']:
					ledgegrab()
			
			#Put the staff back
			if own['equip']==True and own['rtime'] >=300 and own['equiping']==False and own['Attacking']!=True:
			#if own['equip']==True and own['equiping']==False and own['rtime'] >=100:
				print ('Putting staff away')
				cont.activate(Sintel_ReturnStaff)
				own['equiping']=True
				own['Fightmode']=False
				own['Locked']=False
				own['putcam']=False
				own['Target'] =''
		
		#Autojumping
		if autojump and not hitwall:
			cont.activate(jumpjump)
			own['Tracking']=False
		else:
			cont.deactivate(jumpjump)
		
		#Equip Staff
		if leftclick or own['isjoyattack']==1:
			if own['etime']==0 or own['etime']==25:
				if own['equip']==False:# and own['rtime']==0 or own['rtime']>=5:
					print ('Grabing the staff!')
					cont.activate(Sintel_Draw)
					own['equiping']=True
					#own['isShifton'] =0
					own['rtime']=0
	
		#So now you have the staff out...
		#Attack
		if own['equip']==True and own['equiping']==False:
			#Make sure the staff is equiped properly
			if own['etime']==0 or own['etime']==25:
				if leftclick or own['isjoyattack']==1:
					#Strike
					if own['Attacking']==False:
						own['Attacking']=True
						own['attacktime'] =0
						own['dmgdelt'] =False
						own['isShifton'] =False
					#Combo
					else:
						pass #for now...
					
		#Switch on the attacking property
		#Then quickly turn it off
		#After left clicking, ends when animation is over
		if own['Attacking']==True:
		
			#Set movement to 0
			own.setLinearVelocity([0, 0, 0], True)
			
			own['attframes']=Sintel_Rig['frames']
			cont.deactivate(Sintel_Idle)
			cont.deactivate(Sintel_AttackIdle)
			cont.deactivate(Sintel_WalkStaff)
			cont.deactivate(Sintel_AttackWalk)
			cont.deactivate(Sintel_AttackWalkBack)
			cont.deactivate(Sintel_AttackWalkLeft)
			cont.deactivate(Sintel_AttackWalkRigh)
			cont.deactivate(move)
			if own['Locked']==False:
				own['Tracking']=False
			else:
				own['Tracking']=True
			#When not locked on: enable cont.activate(tracktarget)
			#after left click and disable after attack animation finishes
			if Sintel_Rig['frames']==0:
				own['atktouse'], own['totalframes'] = RanAttack(0)
				cont.activate(own['atktouse'])
			if own['attframes'] >=own['totalframes']:
				own['dmgdelt'] =False
				own['totalframes']=0
				Sintel_Rig['frames']=0
				own['Attacking'] =False
			if attackhit.positive:
				if attackhit.bodies[0] =='enemy':
					if own['Fightmode']==False:
						own['Fightmode']=True
		
		#States
		#0 = Normal, 1 = Battle, 2 = Fleeing
		if bge.logic.Seen == True:
			if own['Fightmode']==True:
				own['p_state']=1
			elif own['Running']==True:
				own['p_state']=2
		else:
			own['p_state']=0
					
		#Not moving? then stop moving
		if own['isWkeyon']==0 and own['isjoyup']==0 and own['isDkeyon']==0 and own['isjoyright']==0 and own['isAkeyon']==0 and own['isjoyleft']==0 and own['isSkeyon']==0 and own['isjoydown']==0:
			own['Idle']=True
		if nomotion:
			own['Idle']=True
			print ('Setting to idle')
		if own['Idle']==True:
		
			#Set movement speed to 0
			#cont.deactivate(move)
			own.setLinearVelocity([0, 0, 0], True)
			
			own['footprints']=False
			own['Tracking']=False
			own['runspeed'] =0
			own['startwalk']=0
			own['Running']=False
			own['rtime']=0
			
			#Animations
			if own['equip']==True:
			
				if own['Locked']==False:
					cont.activate(Sintel_IdleStaff)
					cont.deactivate(Sintel_Idle)
					cont.deactivate(Sintel_AttackIdle)
					cont.deactivate(Sintel_AttackWalk)
					cont.deactivate(Sintel_AttackWalkBack)
					cont.deactivate(Sintel_AttackWalkLeft)
					cont.deactivate(Sintel_AttackWalkRigh)
					
				if own['Locked']==True:
					cont.activate(Sintel_AttackIdle)
					cont.deactivate(Sintel_IdleStaff)
					cont.deactivate(Sintel_Idle)
					cont.deactivate(Sintel_AttackWalk)
					cont.deactivate(Sintel_AttackWalkBack)
					cont.deactivate(Sintel_AttackWalkLeft)
					cont.deactivate(Sintel_AttackWalkRigh)
						
			if own['equip']==False:	
				cont.activate(Sintel_Idle)
				cont.deactivate(Sintel_IdleStaff)
				cont.deactivate(Sintel_AttackIdle)
				
			cont.deactivate(Sintel_WalkStaff)
			cont.deactivate(Sintel_AttackWalk)
			cont.deactivate(Sintel_Walk)
			cont.deactivate(Sintel_Fall)
			cont.deactivate(Sintel_Leap_Fall)
			cont.deactivate(Sintel_Run)
			
	#Target Tracking
	try:
		if own['Locked']==True:
			own['lock_time']+=1
			tracktarget.object = own['Target']
			cont.activate(tracktarget)
			#own['putcam']=False
		else:
			cont.deactivate(tracktarget)
			own['lock_time'] =0
	except:
		cont.deactivate(tracktarget)
	
	#Lock on	
	if own['isSpaceon'] ==True and own['Locked']==False and own['Fightmode']==True and own['lock_time'] ==0:
		own['Locked']=True
		own['putcam']=True
		
	#Switch staff positions
	if own['equiping']==True:
		if own['equip']==True:
			if own['etime']==11:
				own['equiping']=False
				own['equip']=False
		if own['equip']==False:
			if own['etime']==12:
				own['equip']=True
				own['equiping']=False
	
	#Falling / landing
	if own['fall']==True:
		if own['Leaping']==True:
			cont.activate(Sintel_Leap_Fall)
		else:
			cont.activate(Sintel_Fall)
		if land_finder or onground:
			own['landtime']+=1
			if own['Leaping']==True:
				cont.activate(Sintel_Leap_Land)
				cont.activate(foot_fall)
				cont.deactivate(Sintel_Leap_Fall)
				own['speed']=5
				if own['landtime']>=6:
					cont.deactivate(Sintel_Leap_Land)
					own['landtime'] =0
					own['fall']=False
					own['Leaping']=False
			else:
				own['fall']=False
				own['landtime'] =0
					
	#Disable jump and tracking
	if not onground:
		own['falltimer']+=1
		if own['Leaping']==True:
			if own['falltimer'] >15:
				own['fall']=True
				cont.deactivate(Sintel_Run)
				cont.deactivate(Sintel_WalkStaff)
				cont.deactivate(Sintel_AttackWalk)
				cont.deactivate(Sintel_Idle)
				cont.deactivate(Sintel_IdleStaff)
				cont.deactivate(Sintel_Walk)
				cont.deactivate(Sintel_AttackIdle)
				cont.deactivate(jumpjump)
				own['Tracking']=False
				own['footprints']=False
		if own['Leaping']!=True:
			if own['falltimer'] >30:
				own['fall']=True
				cont.deactivate(Sintel_Run)
				cont.deactivate(Sintel_WalkStaff)
				cont.deactivate(Sintel_AttackWalk)
				cont.deactivate(Sintel_Idle)
				cont.deactivate(Sintel_IdleStaff)
				cont.deactivate(Sintel_Walk)
				cont.deactivate(Sintel_AttackIdle)
				cont.deactivate(jumpjump)
				own['Tracking']=False
				own['footprints']=False
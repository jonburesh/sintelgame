#A proper way for checking if a key is being pressed
import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	Player = bge.logic.getCurrentScene().objects["PlayerCol"]
		
	#Gather Sensors
	Wkeyon = cont.sensors['Wkeyon'].positive
	Wkeyoff = cont.sensors['Wkeyoff'].positive
	Dkeyon = cont.sensors['Dkeyon'].positive
	Akeyon = cont.sensors['Akeyon'].positive
	Skeyon = cont.sensors['Skeyon'].positive
	Shifton = cont.sensors['Shifton'].positive
	Spaceon = cont.sensors['Spaceon'].positive
	Joyup = cont.sensors['joy_up'].positive
	Joy_fast = cont.sensors['joy_fast1'].positive
	Joyright = cont.sensors['joy_right'].positive
	Joyleft = cont.sensors['joy_left'].positive
	Joydown = cont.sensors['joy_down'].positive
	Joyattack = cont.sensors['joy_attack'].positive
	Joyjump = cont.sensors['joy_jump'].positive

	#For the Shift Key:
	if Player['pressed'] ==True:
		Player['waittime']+=1
		if Player['waittime'] >10:
			Player['waittime']=0
			Player['pressed']=False

	#Wkey check
	if Wkeyon:
		Player['isWkeyon'] =1
	if Wkeyoff:
		Player['isWkeyon'] =0
	#Dkey check
	if Dkeyon:
		Player['isDkeyon'] =1
	if not Dkeyon:
		Player['isDkeyon'] =0
	#Akey check
	if Akeyon:
		Player['isAkeyon'] =1
	if not Akeyon:
		Player['isAkeyon'] =0
	#Skey check
	if Skeyon:
		Player['isSkeyon'] =1
	if not Skeyon:
		Player['isSkeyon'] =0
	#Shiftkey check
	if Shifton:
		Player['isShifton'] = not Player['isShifton']
	#Spacekey check
	if Spaceon and Player['pressed']==False:
		Player['isSpaceon'] =1
		Player['pressed']=True
	if not Spaceon:
		Player['isSpaceon'] =0
		
	#JoyStick Support
	if Joyup:
		Player['isjoyup'] =1
	if not Joyup:
		Player['isjoyup'] =0
	if Joyright:
		Player['isjoyright'] =1
	if not Joyright:
		Player['isjoyright'] =0
	if Joyleft:
		Player['isjoyleft'] =1
	if not Joyleft:
		Player['isjoyleft'] =0
	if Joydown:
		Player['isjoydown'] =1
	if not Joydown:
		Player['isjoydown'] =0
	if Joy_fast and Player['isShifton'] ==0  and Player['pressed']==False:
		Player['isShifton'] =1
		Player['pressed']=True
	if Joy_fast and Player['isShifton'] ==1 and Player['pressed']==False:
		Player['isShifton'] =0
		Player['pressed']=True
	if Joyjump:
		Player['isjoyjump'] =1
	if not Joyjump:
		Player['isjoyjump'] =0
	if Joyattack:
		Player['isjoyattack'] =1
	if not Joyattack:
		Player['isjoyattack'] =0

	#Debug check
	if own['keydebug']==True:
		if Player['isWkeyon'] ==1:
			print ('Wkey')
		if Player['isDkeyon'] ==1:
			print ('Dkey')
		if Player['isAkeyon'] ==1:
			print ('Akey')
		if Player['isSkeyon'] ==1:
			print ('Skey')
		if Player['isShifton'] ==1:
			print ('Shift')
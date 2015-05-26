#Deals with player getting EXP and leveling up
#also a bit of Health
import string, bge

def main():

	cont = bge.logic.getCurrentController()
	own = cont.owner

	EXP = cont.sensors['EXP']
	endgame = cont.sensors['endgame'].positive
	
	Notify = cont.actuators['Notify']
	suspend = cont.actuators['suspend']
	adddeath = cont.actuators['adddeath']

	own['mexp'] = own['lvl']**3
	#Percentage of exp gained for the EXP bar
	bge.logic.EXP = int((float(own['cexp']) / float(own['mexp']) *100))
	#Same for HP
	bge.logic.HP = int((float(own['chp']) / float(own['mhp']) *100))

	if bge.logic.HP >100:
		bge.logic.HP =100
	if own['chp'] > own['mhp']:
		own['chp'] = own['mhp']
		
	if EXP.positive:
		#Extract the exp data from the incoming message
		data = EXP.bodies[0]
		data = data.split(' ')
		try:
			BASE = int(data[0])
		except:
			data[0] = float(data[0]) +.5
			BASE = int(data[0])
		LVL = int(data[1])
		EXPGOT = int((BASE * LVL)/7)
		own['cexp'] = own['cexp']+ EXPGOT
		#Send a notification
		own['message'] = 'Obtained '+ str(EXPGOT) + ' EXP'
		cont.activate(Notify)

	#Smooth EXP gain
	if own['exp']!=own['cexp']:
		own['exp']+=1
		
	#Smooth HP loss / gain
	if own['hp']< bge.logic.HP:
		own['hp']+=1
		bge.logic.sendMessage('add_hp')
	elif own['hp']>bge.logic.HP:
		own['hp']-=1
		bge.logic.sendMessage('sub_hp')
		
	bge.logic.SHP = own['hp']
	
	if own['hp'] >100:
		own['hp'] =100

	#Leveling Up
	if own['exp'] >= own['mexp']:
		own['cexp'] = own['cexp'] - own['mexp']
		own['exp'] =0
		own['lvl'] +=1
		own['mhp'] +=12
		own['chp'] = own['mhp']
		own['hp'] = own['mhp']
		#Lvl up message
		own['message'] = 'Sintel reached level '+str(own['lvl'])+'!'
		cont.activate(Notify)

	#Dead
	if own['chp']<=0 or endgame:
		suspend.scene = 'Scene'
		cont.activate(suspend)
		cont.activate(adddeath)

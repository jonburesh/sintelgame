import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	staff = bge.logic.getCurrentScene().objects["Staff"]

	track = cont.actuators['track'] #regular tracking
	track2 = cont.actuators['track2'] #enemy tracking
	tracker = cont.sensors['tracker'].owner

	if own['Tracking']==True:
		track.time = own['track_time']
		if own['Locked']==False:
			tracker['ipo'] = own['direction']
			cont.activate(track)
			cont.deactivate(track2)
		else:
			try:
				track2.object = own['Target']
				cont.activate(track2)
				cont.deactivate(track)
			except:
				print ('error')
				own['Target'] =''
				own['Fightmode']=False
				own['Locked']=False
				own['putcam']=False
				own['lock_time'] =0
			
	elif own['Attacking']==True and staff['hitobject']!='nothing':
		try:
			track2.object = own['Target']
		except:
			#print ('error')
			own['Target'] =''
			#own['Locked']=False
			#own['putcam']=False
			
		cont.activate(track2)
		cont.deactivate(track)
	else:
		cont.deactivate(track)
		cont.deactivate(track2)
		#own['Locked']=False
		#own['putcam']=False
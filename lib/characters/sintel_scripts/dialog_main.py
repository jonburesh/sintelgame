import bge, textwrap

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	new_txt = cont.sensors['new_txt']
	add_bar = cont.actuators['add_bar']
	fade_dbar = cont.actuators['fade_dbar']
	
	BAR = add_bar.objectLastCreated
	
	if new_txt.positive:
		#print ('got it')
		if own['going']==True:
			own['timer']=0
		elif own['going']!=True:
			#add in the bar
			cont.activate(add_bar)
			own['going']=True
			
		data = new_txt.bodies[0]
		data = str(data)
		own['txt'] = textwrap.fill(data,50)
		print (own['txt'])
		#own.position[0] = (bge.render.getWindowWidth() / 2)
	
	if own['going']==True:
		own['timer']+=1
		if own['timer']==450:
			#fade out the bar
			cont.activate(fade_dbar)
		if own['timer']>=500:
			own['going']=False
			own['timer']=0
			BAR.endObject()
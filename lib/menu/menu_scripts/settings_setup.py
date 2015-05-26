import bge

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner

	Resolutionid = cont.sensors["Resolution"].owner
	Qualityid = cont.sensors["Quality"].owner
	click = cont.sensors["click"].positive or cont.sensors["enter"].positive or cont.sensors["A"].positive

	if own['wait']==True:
		own['waittime']+=1
		if own['waittime'] >5:
			own['waittime']=0
			own['wait']=False
	
	#Setting resolution loaded config
	if own['gameresolution']=='1024x768':
		Resolutionid['res'] = 1
	elif own['gameresolution']=='1152x864':
		Resolutionid['res'] = 2
	elif own['gameresolution']=='1280x768':
		Resolutionid['res'] = 3
	elif own['gameresolution']=='1280x800':
		Resolutionid['res'] = 4
	elif own['gameresolution']=='1280x1024':
		Resolutionid['res'] = 5
	elif own['gameresolution']=='1366x768':
		Resolutionid['res'] = 6
	elif own['gameresolution']=='1440x900':
		Resolutionid['res'] = 7
	elif own['gameresolution']=='1680x1050':
		Resolutionid['res'] = 8
	elif own['gameresolution']=='1920x1080':
		Resolutionid['res'] = 9
	elif own['gameresolution']=='1920x1200':
		Resolutionid['res'] = 10
	else:
		Resolutionid['res'] = 11

	#Setting quality loaded config
	if own['gamequal']=='High':
		Qualityid['qual'] = 1
	elif own['gamequal']=='Low':
		Qualityid['qual'] = 2

	#Setting the Quality
	highhover = cont.sensors["highhover"].owner['selected']==True
	lowhover = cont.sensors["lowhover"].owner['selected']==True

	if highhover and click and own['wait']!=True:
		own['gamequal'] ='High'
		own['wait']=True
		
	if lowhover and click and own['wait']!=True:
		own['gamequal'] ='Low'
		own['wait']=True

	#Setting the resolution
	onehover = cont.sensors["1024x768hover"].owner['selected']==True
	twohover = cont.sensors["1152x864hover"].owner['selected']==True
	threehover = cont.sensors["1280x768hover"].owner['selected']==True
	fourhover = cont.sensors["1280x800hover"].owner['selected']==True
	fivehover = cont.sensors["1280x1024hover"].owner['selected']==True
	sixhover = cont.sensors["1366x768hover"].owner['selected']==True
	sevenhover = cont.sensors["1440x900hover"].owner['selected']==True
	eighthover = cont.sensors["1680x1050hover"].owner['selected']==True
	ninehover = cont.sensors["1920x1080hover"].owner['selected']==True
	tenhover = cont.sensors["1920x1200hover"].owner['selected']==True

	if onehover and click:
		own['gameresolution'] ='1024x768'
	if twohover and click:
		own['gameresolution'] ='1152x864'
	if threehover and click:
		own['gameresolution'] ='1280x768'
	if fourhover and click:
		own['gameresolution'] ='1280x800'
	if fivehover and click:
		own['gameresolution'] ='1280x1024'
	if sixhover and click:
		own['gameresolution'] ='1366x768'
	if sevenhover and click:
		own['gameresolution'] ='1440x900'
	if eighthover and click:
		own['gameresolution'] ='1680x1050'
	if ninehover and click:
		own['gameresolution'] ='1920x1080'
	if tenhover and click:
		own['gameresolution'] ='1920x1200'
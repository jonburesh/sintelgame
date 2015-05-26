'''
--------------------------------------------------------------------------------------------------------
sets up the post fx
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

cont = logic.getCurrentController()
own = cont.owner

def main():
	try:
		logic.loadGlobalDict()
		if logic.globalDict['cfg_post'] ==True:
			print ('Turning on Post FX')
			cont.activate('vignetting')
		if logic.globalDict['cfg_ssao'] ==True:
			cont.activate('ssao')
	except:
		print ('No cfg_post option found')
		#cont.activate('vignetting')
		#cont.activate('ssao')
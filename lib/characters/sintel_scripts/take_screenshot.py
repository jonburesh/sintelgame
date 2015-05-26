'''
--------------------------------------------------------------------------------------------------------
Takes a screenshot and saves it to screenshot folder 
press F12 for a screenshot
--------------------------------------------------------------------------------------------------------
'''

from bge import logic, render
import datetime

def NameGen():
    now = datetime.datetime.now()
    str(now)
    name = now.strftime("%Y_%m_%d_%H_%M_%S")
    return name

def main():
	cont = logic.getCurrentController()
	own = cont.owner
	
	F12 = cont.sensors["F12"].positive
	
	
	
	if F12:
		shotname = NameGen()+'.png'
		#put into a screenshots folder
		file = '..\screenshots/%s' % (shotname)
		
		render.makeScreenshot(file)
		
		print ('screenshot',shotname,'saved.')
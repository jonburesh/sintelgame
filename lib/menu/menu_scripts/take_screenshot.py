#Press F10 for a screenshot

import bge
from random import *

def NameGen(Length):
    alphabet = ['0','1','2','3','4','5','6','7','8','9']
    name = ''
    while Length!=0:
        letter = choice(alphabet)
        name = name+letter
        Length -= 1
    return name

def main():
	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	F10 = cont.sensors["F10"].positive
	
	if F10:
		shotname = NameGen(7)+'.jpg'
		bge.render.makeScreenshot("lib/screenshots/"+shotname)
		
		print ('screenshot ',shotname,'saved to /screenshots')
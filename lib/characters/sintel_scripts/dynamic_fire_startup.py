# start up script for dynamic fire
# adds in most of required properties though some still need to be set up before running the game
#  
import bge

baseStartFuel = 1000 #defualt amout of fuel to start with 

def main(cont):
    own = cont.owner
    if 'start' in own:
        own.state = 2 # move the torch to state 2, the main fire script sould be placed there
    else:
        own["burnList"] = []
        own["flickerTime"] = 0
        own["sintelFuel"] = baseStartFuel
        own["mouseTime"] = 0
        own['mouse'] = False 
        own["detected"] = False
        own["start"] = False
        own.state = 2 # move the torch to state 2, the main fire script sould be placed there
    
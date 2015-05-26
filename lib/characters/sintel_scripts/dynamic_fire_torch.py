import bge,random,time
from bpy import data
from math import floor 
#declare constants and any other stuff :)

scene = bge.logic.getCurrentScene()
keyboard = bge.logic.keyboard

flame = "flameObj" #set the name of the object used as the flame
Dripflame = "DripflameObj"
upDraftflame = "upDraftflame"
smoke = "smokeObj" #set the smoke object 
light = "fire_light" #set the name of the light which will be instanced above burning objects 
torchLight = "fire_light_Torch"
torch = "Torch_Fire_emitter" #sets the object to be used as the torch
heatBox = "HeatBox"
heatBoxHotObj = "HeatBoxHObj"
## fire parameters ##

flameBaseLife =2  # shortest amount of time a flame instance should remain in the scene
flameMaxLife = 10 # longest amoun of time a flame instance should remain in the scene 
flameScaleMax = 1 # the largest a flame should be at birth 
flameScaleMin = 0.5 # the smallest a flame should be at birth 
scaleMultiply = 50 # affects objects fuel
birthPosJitter = 0.05 # set a jitter multipier for flame birth location 

combustionRate = 2 # rate at which fuel is consumed (an objects fuel is based on the objects dimentions and scale multiplier)

ticRes = 2 # iterations per logic tic ( controles the number of flames per tic )

def main_fire_control(cont):
    own = cont.owner
    
    ### start up ###########
    if 'ignited' not in own:
        startUp(own)
    ######################## 
    
    # allows the player to ignite and extiguish the torch ###########  
    JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
    if keyboard.events[bge.events.SPACEKEY] == JUST_ACTIVATED:
        if own["torch_ignited"]:
            own["torch_ignited"] = False
            if scene.objects[torch] in own["hotObjs"]:
                iT = own["hotObjs"].index((scene.objects[torch]))
                del (own["hotObjs"][iT]) 
                if own["HBremoval"] != 0:
                    own["HBremoval"].endObject()
                    scene.objects[torchLight].endObject()
            makeSmoke(own,scene.objects[torch])

        else:
            own["torch_ignited"] = True
    ################################################################
    if own["torch_ignited"]:
        if scene.objects[torch] not in own["hotObjs"]:
            own["hotObjs"].append((scene.objects[torch]))
            addFireLamp(own,(scene.objects[torch]),1000,True)
            addHeatBox(own,scene.objects[torch],True)
        
        scene.objects[torch]["fule"] = 1000 # keeps the torch full of fule, could be set to finite amounts if needed for game play
    burnObjects(own)
    #print(scene.objects[:])
    

def burnObjects(own,smoker = False):
    if smoker:
        emission = smoke 
    else:
        emission = flame 
    for hotObj in own["hotObjs"]:
        #checks if the object has already had its fule calculated 
        if 'fule' not in hotObj:
            hotObj["fule"] = (fuleCalc(own,hotObj))
            print("registered new burn object: "+ str(hotObj))## temp -------------------------------#####################################
        if hotObj["fule"] > 20:
            for i in range(ticRes):
                vert = random.choice(data.objects[str(hotObj)].data.vertices[:]) # picks a random vert to spawn a flame on 
                
                if vert.co.z > -1: # checks the vert is above 0 mainly used to prevent low parts of the mesh setting on fire might be best to remove #################
                    
                    flameLifeTime = floor(random.uniform(flameBaseLife,flameMaxLife)) # sets a random lifetime for the flame instance 
                    
                    flameInst = scene.addObject(emission,hotObj,flameLifeTime) # add in the new flame
                     
                    rPos = (random.random()*birthPosJitter) # creates a value to jitter position flame spawn position 
                    
                    ### sets the flames position to the hot objects vert + jitter and accounts for object movement ##################
                    if hotObj.worldPosition.x < 0:
                        flameInst.worldPosition.x = (vert.co.x - abs(hotObj.worldPosition.x)) + rPos
                    else:
                        flameInst.worldPosition.x = (vert.co.x + abs(hotObj.worldPosition.x)) + rPos
                    if hotObj.worldPosition.y < 0:
                        flameInst.worldPosition.y = (vert.co.y - abs(hotObj.worldPosition.y)) + rPos
                    else:
                        flameInst.worldPosition.y = (vert.co.y + abs(hotObj.worldPosition.y)) + rPos				
                    if hotObj.worldPosition.z < 0:
                        flameInst.worldPosition.z = (vert.co.z - abs(hotObj.worldPosition.z)) 
                    else:
                        flameInst.worldPosition.z = (vert.co.z + abs(hotObj.worldPosition.z)) 
                    
                    lRScale= random.uniform(flameScaleMax,flameScaleMin) #give flames a random scale based on min and max values 
                    flameInst.worldScale = (lRScale,lRScale,lRScale) # set scale
                    flameInst.localOrientation = [0,0,0]#ensures flames remain the right way up 
                    # add random drip and updraft flames  
                    if flameLifeTime == 10:
                        dripFInst = scene.addObject(Dripflame,flameInst,100)
                        dripFInst.worldScale = dripFInst.worldScale /2                        
                    if flameLifeTime == 11:
                        dripFInst = scene.addObject(upDraftflame,flameInst,100)
                        dripFInst.worldScale = dripFInst.worldScale /2                    
                    ################################################################################################################
        #print(hotObj["fule"])##temp##
        elif hotObj["fule"] > 0:
            makeSmoke(own,hotObj)
        elif hotObj["fule"] <=0:            
            ## removes the object from burn list 
            if hotObj in own["hotObjs"]:
                iT = own["hotObjs"].index((hotObj))
                del (own["hotObjs"][iT])  
                print(own["hotObjs"]) # temp
            #hotObj.endObject()#removes the object from scene 
          
        hotObj["fule"] = hotObj["fule"] - combustionRate # reduces the amount of fule left in the object 
    

def makeSmoke(own,hotObj):

    for i in range(ticRes):
        vert = random.choice(data.objects[str(hotObj)].data.vertices[:]) # picks a random vert to spawn a flame on   
        
        if vert.co.z > 0: # checks the vert is above 0 mainly used to prevent low parts of the mesh setting on fire might be best to remove #################
                    
                    flameLifeTime = floor(random.uniform(flameBaseLife,flameMaxLife)) # sets a random lifetime for the flame instance 
                    
                    smoke_Inst = scene.addObject(smoke,hotObj,flameLifeTime) # add in the new flame
                     
                    rPos = (random.random()*birthPosJitter) # creates a value to jitter position flame spawn position 
                    
                    ### sets the flames position to the hot objects vert + jitter and accounts for object movement ##################
                    if hotObj.worldPosition.x < 0:
                        smoke_Inst.worldPosition.x = (vert.co.x - abs(hotObj.worldPosition.x)) + rPos
                    else:
                        smoke_Inst.worldPosition.x = (vert.co.x + abs(hotObj.worldPosition.x)) + rPos
                    if hotObj.worldPosition.y < 0:
                        smoke_Inst.worldPosition.y = (vert.co.y - abs(hotObj.worldPosition.y)) + rPos
                    else:
                        smoke_Inst.worldPosition.y = (vert.co.y + abs(hotObj.worldPosition.y)) + rPos				
                    if hotObj.worldPosition.z < 0:
                        smoke_Inst.worldPosition.z = (vert.co.z - abs(hotObj.worldPosition.z)) 
                    else:
                        smoke_Inst.worldPosition.z = (vert.co.z + abs(hotObj.worldPosition.z)) 
                    
                    lRScale= random.uniform(flameScaleMax,flameScaleMin) #give flames a random scale based on min and max values 
                    smoke_Inst.worldScale = (lRScale,lRScale,lRScale) # set scale
                    smoke_Inst.localOrientation = [0,0,0]#ensures flames remain the right way up 
                    
                    
                        
    
def fuleCalc(own,hotObj):
	#calculates the amount of fule an object should have based on its dimetions and scale multiplier 
    fule = (data.objects[str(hotObj)].dimensions.x*data.objects[str(hotObj)].dimensions.y*data.objects[str(hotObj)].dimensions.z)*scaleMultiply
    addFireLamp(own,hotObj,fule,False)
    addHeatBox(own,hotObj,False,fule)
    return fule 

def addFireLamp(own,hotObj,fule,imortal):
    if imortal:
        lightInst =scene.addObject(torchLight ,hotObj,0)

    else:
        lightLife = floor(abs(fule / combustionRate)) 
        lightInst =scene.addObject(light,hotObj,lightLife)
    lightInst.worldPosition.z = hotObj.worldPosition.z + ((data.objects[str(hotObj)].dimensions.z /2)+2)
    lightInst.setParent(hotObj,False,False)
    

def addHeatBox(own,hotObj,isTorch,fule = 10):
    
    if isTorch:
        tHb = scene.addObject(heatBox,own,0)
        tHb.setParent(own,False,False)
        own["HBremoval"] = tHb
    else:
        tHb = scene.addObject(heatBoxHotObj,hotObj,(floor((fule/combustionRate)+1)))#needs work
        tHb.setParent(hotObj,False,False)                    
        
    
    
def startUp(own):
    torchObj = scene.objects[torch]
    #print(torchObj)
    own["ignited"] = True
    own["hotObjs"] = [torchObj]
    own["staticTime"] = time.time()
    own["torch_ignited"] = True
    own["cooking"] = True
    own["HBremoval"] = 0
    torchObj["fule"] = 1000
    addHeatBox(own,scene.objects[torch],True)
    addFireLamp(own,(scene.objects[torch]),1000,True)       
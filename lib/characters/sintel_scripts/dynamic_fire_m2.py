#####################################################################
# creates a fire effect in the blender ge (still a work in progress)#
# v 1.5                                                             # 
# please check www.sintelgame.org for updates                       #                              
#####################################################################
import bge,random
from math import floor

scene = bge.logic.getCurrentScene()
mouse = bge.logic.mouse
player = bge.logic.getCurrentScene().objects['sintel_col'] 
emitTicRes = 2 # resolution of particles per tic
torchObject = scene.objects["Torch_Fire_emitter"] # torch object
torchLight = scene.objects["fire_light_Torch"] # lamp connected to the torch 
Dripflame = "DripflameObj" # flames that move rapidly downwards 
upDraftflame = "upDraftflame" # flames that move upwards 
torchLightMaxEnergy = 5.0 # max energy of the lamp connected to the torch 
flickerSpeed = 0.1 # speed that the light will flicker 
flameSprite = "flameObj" # flame object
smokeSprite = "smokeObj" # smoke object 
baseStartFuel = 10000 #defualt amout of fuel to start with 
fuelConsumptionRate = 10 # rate that fuel will be used ( per tic) 
minFuel = 20 # point when the object will smoker rather than burn 
SimultaneousMax = 5 # the number of objects that can be burnt Simultaneously.
flameBaseLife =5  # shortest amount of time a flame instance should remain in the scene
flameMaxLife = 25 # longest amoun of time a flame instance should remain in the scene 
flameScaleMax = 2 # the largest a flame should be at birth 
flameScaleMin = 0.5 # the smallest a flame should be at birth 
holdlen = 50 # length of time the left mouse button must be held to ignite object
burnObjStr = "Torch_Fire_emitter" # object linked to the main fire script 
ignitingSymbol = "fire_progress_symbol" # symbol to use while igniting 
flammableSymbol = "fire_symbol" # detected symbol 
rayLen = 2 # the distance the ray will look 

def main():
    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    ############################################################
    ############################################################################################
    ##########################################################################################################   
    # if prop "ignited" true spawn flames on torch and call detect func to check if flammable objects are near#
    if own["ignited"] and own["sintelFuel"] > 0 and player['torch']:
        burnObject = torchObject # ensure the torch is in the burn list 
        fireSpawn(own,burnObject)# spawn flames
        detect(own) # look around for objects to burn 
        if own["flickerTime"] > flickerSpeed:# cause torch lamp to flicker randomly
            torchLight.energy = (random.uniform(2.0,torchLightMaxEnergy)) # make random value for lamp 
            own["flickerTime"] = 0 # reset flicker time 
        own["sintelFuel"] -= 1 # reduce fule 
    else:
        torchLight.energy = 0.0 # turn torch light off 
        own["ignited"] = False
        # prevents symbols showing if torch is off ## could do with cleaning up a bit ##
        scene.objects[ignitingSymbol].setVisible(False) ##
        scene.objects[flammableSymbol].setVisible(False) ##
        scene.objects[ignitingSymbol].state = 1 ##
        own["mouseTime"] = 0 ##
    #####################################################################################################
    #####################################################################################################
        

    ############################################################################
    ############################################################################
    #### burn objects other than torch ##########################################
    for burnObject in own["burnList"][0:SimultaneousMax]:
        ################ start up check #############
        if "firestarted" not in burnObject: # start up for burn objects
            #propagator = scene.addObject("heat_box",burnObject,600)
            heatBox = scene.addObject("heat_box",burnObject,0)
            heatBox.setParent(burnObject)

            ############### 
            burnObject["firestarted"] = True 
            if "fuel" not in burnObject:
                burnObject["fuel"] = baseStartFuel
            #print("added start") # for debug
        ############################################
        ########### fuel check #####################
        if burnObject["fuel"] > minFuel:# check that the object still has fuel to burn
            burnObject["fuel"] -= fuelConsumptionRate # remove fuel 
            fireSpawn(own,burnObject)
            #print(own["burnList"])#for debug
        ################# emit smoke on object  #########
        elif burnObject["fuel"] <= minFuel and burnObject["fuel"] > 0:
            burnObject["fuel"] -= fuelConsumptionRate # remove fuel 
            smokeSpawn(own,burnObject)
        ########## remove object from burn list when fuel depleted###### 
        else:
            ## need to remove flammable and started props upon completion##
            indexBurnObject = own["burnList"].index((burnObject)) # get index of burnObject in list
            del (own["burnList"][indexBurnObject]) # remove it from list to prevent reburn  
            if 'remove' in burnObject: burnObject.endObject() # end object if object has been flagged with remove prop 
            if 'postBurn' in burnObject: burnObject.state = 2 # set to state 2 if postBurn flag on object. any post burn actions should be placed on state 2 of the object that was burnt 
            #print(own["burnList"])#for debug
    ###########################################################################
    ###########################################################################
    ###########################################################################
            
def fireSpawn(own,burnObject):#spawns flames at random vertex positions on burnobject 
    # gets vertex proxy
    for mesh in burnObject.meshes:
        for m_index in range(len(mesh.materials)):
            for i in range(emitTicRes):
                v_index = random.choice(range(mesh.getVertexArrayLength(m_index))) # picks a random vertex 
                vertex = mesh.getVertex(m_index,v_index)
                #print(vertex.XYZ) # for debug 
                ##############################spwan flame objects##########
                flameLifeTime = floor(random.uniform(flameBaseLife,flameMaxLife))
                flame = scene.addObject(flameSprite,burnObject,flameLifeTime)
                flame.worldPosition = (vertex.XYZ + burnObject.worldPosition.xyz) # move to random vertex position and compensate for object offset from world origin 
                RScale= random.uniform(flameScaleMax,flameScaleMin) #give flames a random scale based on min and max values 
                flame.worldScale = (RScale,RScale,RScale) # set scale
                flame.localOrientation = [0,0,0]#ensures flames remain the right way up 
                # add random drip and updraft flames  
                if flameLifeTime == 10:
                    dripFInst = scene.addObject(Dripflame,burnObject,100)
                    dripFInst.worldScale = dripFInst.worldScale /2
                    dripFInst.worldPosition = (vertex.XYZ + burnObject.worldPosition.xyz)
                    dripFInst.localOrientation = [0,0,0]#ensures flames remain the right way up                      
                if flameLifeTime == 11:
                    dripFInst = scene.addObject(upDraftflame,burnObject,100)
                    dripFInst.worldScale = dripFInst.worldScale /2
                    dripFInst.worldPosition = (vertex.XYZ + burnObject.worldPosition.xyz)
                    dripFInst.localOrientation = [0,0,0]#ensures flames remain the right way up   
                
def smokeSpawn(own,burnObject):#spawns smoke at random vertex positions on burnobject 
    # gets vertex proxy
    for mesh in burnObject.meshes:
        for m_index in range(len(mesh.materials)):
            for i in range(emitTicRes):
                v_index = random.choice(range(mesh.getVertexArrayLength(m_index))) # picks a random vertex 
                vertex = mesh.getVertex(m_index,v_index)
                #print(vertex.XYZ) # for debug 
                ##############################spwan flame objects##########
                flameLifeTime = floor(random.uniform(flameBaseLife,flameMaxLife))
                flame = scene.addObject(smokeSprite,burnObject,flameLifeTime)
                flame.worldPosition = (vertex.XYZ + burnObject.worldPosition.xyz) # move to random vertex position and compensate for object offset from world origin 
                flame.localOrientation = [0,0,0]
                #print("smoke_Spawned")#for debug

##############################################################################################
###############################################################################################
###############################################################################################

def detect(own):
    if own["detected"]:
    #display symbol if an object is detected 
        scene.objects[flammableSymbol].setVisible(True)
        checkMouse(own)
        if own["mouse"]:
            caster(own,True)

    else:
        # hide symbol if nothing found 
        scene.objects[flammableSymbol].setVisible(False) 
        own["mouse"] = False
    own["detected"] = False # hide symbol for next time round 
    
    caster(own)
    
    

def caster(own,trigerburn = False): 
    #ray_info = []
    ray_info = [None,None,None]#own.rayCast((bge.logic.getCurrentScene().objects["Ray_pusher"]),(bge.logic.getCurrentScene().objects["Ray_pusher_end"]),rayLen,"Flammable")

    for i in range(3):

        #bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition = own.worldPosition     
        if i == 0:
            ray_info = own.rayCast((bge.logic.getCurrentScene().objects["Ray_pusher_end"]),(bge.logic.getCurrentScene().objects["Ray_pusher"]),rayLen,"Flammable")
            #bge.render.drawLine((bge.logic.getCurrentScene().objects["Ray_pusher_end"]).worldPosition,(bge.logic.getCurrentScene().objects["Ray_pusher"].worldPosition),(1,1,1)) # debug only can be deleted

            
        if i == 1:
            ray_info = own.rayCast((bge.logic.getCurrentScene().objects["Ray_pusher_end.001"]),(bge.logic.getCurrentScene().objects["Ray_pusher.001"]),rayLen,"Flammable")
            #bge.render.drawLine((bge.logic.getCurrentScene().objects["Ray_pusher_end.001"]).worldPosition,(bge.logic.getCurrentScene().objects["Ray_pusher.001"].worldPosition),(1,1,1)) # debug only can be deleted

        if i == 2:
            ray_info = own.rayCast((bge.logic.getCurrentScene().objects["Ray_pusher_end.002"]),(bge.logic.getCurrentScene().objects["Ray_pusher.002"]),rayLen,"Flammable")
            #bge.render.drawLine((bge.logic.getCurrentScene().objects["Ray_pusher.002"]).worldPosition,(bge.logic.getCurrentScene().objects["Ray_pusher_end.002"].worldPosition),(1,1,1)) # debug only can be deleted

                        
        if ray_info[0] != None:
            own["detected"] = True
            if trigerburn:
                if 'melt' in ray_info[0]:
                    ray_info[0].state = 2
                    del (bge.logic.getCurrentScene().objects[str(ray_info[0])]['Flammable'])
                else:
                    #print(ray_info[0])#for debug 
                    bge.logic.getCurrentScene().objects[burnObjStr]["burnList"].append(ray_info[0])
                    del (bge.logic.getCurrentScene().objects[str(ray_info[0])]['Flammable'])

def checkMouse(own):

    mouseJt = bge.logic.KX_INPUT_JUST_ACTIVATED == mouse.events[bge.events.LEFTMOUSE] # check if mouse just activated 
    mouseAc = bge.logic.KX_INPUT_ACTIVE == mouse.events[bge.events.LEFTMOUSE] # check if left mouse held down 
    mousejR = bge.logic.KX_INPUT_JUST_RELEASED == mouse.events[bge.events.LEFTMOUSE] # check if mouse released 

    if mouseJt: 
        own["mouseTime"] += 1 # start mouse timer inc
        scene.objects[ignitingSymbol].setVisible(True)
        scene.objects[ignitingSymbol].state = 2
        
    if mouseAc:# continue to add to mouse timer while left mouse held down 
        own["mouseTime"] += 1        
    if mouseAc and own["mouseTime"] >= holdlen:
        own["mouse"] = True
        own["mouseTime"] = 0
        scene.objects[ignitingSymbol].setVisible(False)
        scene.objects[ignitingSymbol].state = 1
    elif mousejR:
        scene.objects[ignitingSymbol].setVisible(False)
        scene.objects[ignitingSymbol].state = 1 
        own["mouse"] = False 
        own["mouseTime"] = 0        

    else:
        own["mouse"] = False
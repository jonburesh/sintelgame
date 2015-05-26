import bge,random
from math import floor

scene = bge.logic.getCurrentScene()

emitTicRes = 2 # resolution of particles per tic

Dripflame = "DripflameObj" # flames that move rapidly downwards 
upDraftflame = "upDraftflame" # flames that move upwards 

flameSprite = "flameObj" # flame object
smokeSprite = "smokeObj" # smoke object 
flameBaseLife =5  # shortest amount of time a flame instance should remain in the scene
flameMaxLife = 25 # longest amoun of time a flame instance should remain in the scene 
flameScaleMax = 2 # the largest a flame should be at birth 
flameScaleMin = 0.5 # the smallest a flame should be at birth 

def main(cont):
    own = cont.owner
    fireSpawn(own,own)
    if 'smoke' in own:
        smokeSpawn(own,own)

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
                if flameLifeTime == 11:
                    dripFInst = scene.addObject(upDraftflame,burnObject,100)
                    dripFInst.worldScale = dripFInst.worldScale /2
                    dripFInst.worldPosition = (vertex.XYZ + burnObject.worldPosition.xyz)  
                
def smokeSpawn(own,burnObject):#spawns smoke at random vertex positions on burnobject 
    # gets vertex proxy
    for mesh in burnObject.meshes:
        for m_index in range(len(mesh.materials)):
            for i in range(emitTicRes):
                v_index = random.choice(range(mesh.getVertexArrayLength(m_index))) # picks a random vertex 
                vertex = mesh.getVertex(m_index,v_index)
                ##############################spwan smoke objects##########
                flameLifeTime = floor(random.uniform(flameBaseLife,flameMaxLife))
                flame = scene.addObject(smokeSprite,burnObject,flameLifeTime)
                flame.worldPosition = (vertex.XYZ + burnObject.worldPosition.xyz) # move to random vertex position and compensate for object offset from world origin 
                flame.localOrientation = [0,0,0]
               

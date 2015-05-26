import bge 
scene = bge.logic.getCurrentScene()
torchObject = scene.objects["Torch_Fire_emitter"]
def main(cont):
    own = cont.owner
    torchObject["sintelFuel"] += 1000
    children = own.children # gathers children into "children"
    for child in children:# for all child objects change thier state and remove parent 
        child.setVisible(False)
    own.worldPosition.z += -50 
    own.state = 2 

def respawn ():
    cont = bge.logic.getCurrentController()
    own = cont.owner
    children = own.children # gathers children into "children"
    for child in children:# for all child objects change thier state and remove parent 
        child.setVisible(True)
    own.worldPosition.z += 50 
    own.state = 1 
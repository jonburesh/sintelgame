import bge,random

def main(cont):
    own = cont.owner
    own.worldScale = own.worldScale /1.02
    if own["prop"] and own["time"]>0.2:
        own.applyRotation([0.2,0.2,0])
        own["prop"] = False
        own["time"] = 0 
    elif own["time"]>0.2:
        own.applyRotation([-0.2,-0.2,0])
        own["prop"] = True
        own["time"] = 0 
    if own.life < 0.02:
        if own.worldPosition.z > bge.logic.getCurrentScene().objects["Torch_Fire_emitter"].worldPosition.z + 2:
            bge.logic.getCurrentScene().addObject("smokeObj",own,150)
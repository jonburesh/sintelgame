import bge
def main(cont):
    own = cont.owner
    baseTriggerState = 2 # sets the defualt state to be 2
    
    if 'state' in own:#allows user to provided a state other than 2
        baseTriggerState = own['state']
        
    children = own.children # gathers children into "children"
    for child in children:# for all child objects change thier state and remove parent 
        child.state = baseTriggerState
        child.removeParent()
    if 'end' in own:
        own.endObject()# end this object 
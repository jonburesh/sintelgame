import bge

#################################################################
#melt controle.
#you can controle how an object will melt by adding the following properties though all have defualt values and can be ommited.
#meltAxisX   ---- this should be a boolean prop, it will tell the script that the object should NOT be scaled in the x axis 
#meltAxisY  ------ same as meltAxisX but prevents scale in the Y axis
#meltAxisZ -------- same as meltAxisX but prevents scale in the Z axis  
#
#meltSpeed -----   this should be a float value, this is the value the objects scale will be divided by each logic tick. 
#                  if not included the melt speed will default to 1.01 
#
#cullSize ----- this should be a float value. when the object reaches this scale value it will be removed. defaults to 0.02 if ommited 
def main(cont):
    own = cont.owner
    x,y,z = True,True,True # defual values to force scale in xy and z axis if no prop override is given 
    meltSpeed = 1.01 # defualt scale reduction 
    cullSize = 0.02 # defualt size at which to end object 


####prop overrides###########       
    if 'meltAxisX' in own:
        x = False 
    if 'meltAxisY' in own:
        y = False 
    if 'meltAxisZ' in own:
        z = False  
    if 'meltSpeed' in own:
        meltSpeed = own['meltSpeed']
    if 'cullSize' in own:
        cullSize= own['cullSize'] 
################################### 
########## scale and cull##########      
    if x:
        if own.localScale.x > cullSize:
            own.localScale.x = (own.localScale.x / meltSpeed)
        else:
            own.endObject()
    if y:
        if own.localScale.y > cullSize:
            own.localScale.y = (own.localScale.y / meltSpeed)
        else:
            own.endObject()
    if z:
        if own.localScale.z > cullSize:
            own.localScale.z = (own.localScale.z / meltSpeed)
        else:
            own.endObject()
################################################       
import bge
burnObjStr = "Torch_Fire_emitter"
rayLen = 4
def main(cont):
    own = cont.owner
    if 'Rp' not in own:
        startup(own)
    if own.parent["fuel"]>20 and own["timer"] >5:#if own["timer"] > 5:
        caster(own)
        
    if own.parent["fuel"] < 20:
        for child in own.children:
            child.endObject()
        own.endObject()     


def caster(own):    
    for i in range(9):
        bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition = own.worldPosition    
        if i == 0:
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.x = own.worldPosition.x + rayLen #pos x
            
        elif i == 1:
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.x = own.worldPosition.x - rayLen #neg x
            
        elif i == 2:
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.y = own.worldPosition.y + rayLen #pos y
            
        elif i == 3:
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.y = own.worldPosition.y - rayLen #neg y        

        elif i == 4:
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.z = own.worldPosition.z + rayLen #pos z
############################## uncomment and renumber for neg z check #############################################           
#        elif i == 5:
#            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.z = own.worldPosition.z - rayLen #neg z    
            
        elif i == 5:
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.x = own.worldPosition.x - rayLen #neg x
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.y = own.worldPosition.y - rayLen

        elif i == 6:
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.x = own.worldPosition.x + rayLen #neg x
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.y = own.worldPosition.y + rayLen

        elif i == 7:
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.x = own.worldPosition.x - rayLen #neg x
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.y = own.worldPosition.y + rayLen            

        elif i == 8:
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.x = own.worldPosition.x + rayLen #neg x
            bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition.y = own.worldPosition.y - rayLen   
            
                                              
        ray_info = own.rayCast(own,(bge.logic.getCurrentScene().objects["Ray_pusher1"]),rayLen,"Flammable")
        #bge.render.drawLine(own.worldPosition,(bge.logic.getCurrentScene().objects["Ray_pusher1"].worldPosition),(1,1,1)) # debug only can be deleted 
        if ray_info[0] != None:
            if 'melt' in ray_info[0]:
                ray_info[0].state = 2
                del (bge.logic.getCurrentScene().objects[str(ray_info[0])]['Flammable'])
            else:
                #print(ray_info[0])#for debug
                bge.logic.getCurrentScene().objects[burnObjStr]["burnList"].append(ray_info[0])
                del (bge.logic.getCurrentScene().objects[str(ray_info[0])]['Flammable'])


        
def startup(own):
    own["Rp"] = 0
    rayPusher =bge.logic.getCurrentScene().addObject("Ray_pusher1",own,0)
    rayPusher.setParent(own)
    scene = bge.logic.getCurrentScene()
    scene.objects["heat_box_light"].energy = 1
    

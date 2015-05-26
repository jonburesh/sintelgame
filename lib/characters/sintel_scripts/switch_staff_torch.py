import bge  
player = bge.logic.getCurrentScene().objects['sintel_col']
mouse = bge.logic.mouse 
def main(cont):
    mousescrollupJt = bge.logic.KX_INPUT_JUST_ACTIVATED == mouse.events[bge.events.WHEELUPMOUSE] # check if mouse wheel moved up
    mousescrolldwJt = bge.logic.KX_INPUT_JUST_ACTIVATED == mouse.events[bge.events.WHEELDOWNMOUSE] # check if mouse wheel moved up
   
    if mousescrollupJt:
        player['torch'] = True
    elif mousescrolldwJt:
        player['torch'] = False
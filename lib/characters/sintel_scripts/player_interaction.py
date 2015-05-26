'''
--------------------------------------------------------------------------------------------------------
handles interacting with objects
--------------------------------------------------------------------------------------------------------
'''
from bge import logic

logic.player_cart = None

player = logic.getCurrentScene().objects['sintel_col']
staff = logic.getCurrentScene().objects['sintel_staff']
torch = logic.getCurrentScene().objects['sintel_torch']

def main(cont):
	
	cart_start = cont.sensors['cart_start'].positive
	
	if cart_start:
		own.state = logic.KX_STATE2
	
	if player['torch'] == True:
		staff.visible = False
		torch.visible = True
		player['ENABLE_ATK'] = False
	else:
		staff.visible = True
		torch.visible = False
	
def getClosest(type):
	own = cont.owner
	obj_list = [ob for ob in logic.getCurrentScene().objects if type in ob]
	closest = [obj_list[0], own.getDistanceTo(obj_list[0])]
	for ob in obj_list[1:]:
		dis = player.getDistanceTo(ob)
		if  dis < closest[1]:
			closest = [ob, dis]
	return closest[0]
	
def cart(cont):
	own = cont.owner
	if player['CART'] == False and player['ENABLE_CART'] == True:
		logic.player_cart = getClosest('cart')
		logic.player_cart.state = logic.KX_STATE2
		player['CART'] = True
		player['ENABLE_RUN'] = False
		player['ENABLE_ATK'] = False
		#cont.activate('set_release_state')
		
def release(cont):
	logic.player_cart.removeParent()
	logic.player_cart.state = 1
	player['CART'] = False
	player['ENABLE_RUN'] = True
	player['ENABLE_ATK'] = True
	own.state = logic.KX_STATE1
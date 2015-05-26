from bge import logic, render

def init(cont):
	own = cont.owner
	crane_angle = own.localOrientation.to_euler()
	own['start_rot'] = crane_angle[2]
	#print ('crane_init')

def main(cont):
	own = cont.owner
	
	mousemove = cont.sensors['mousemove']

	cranezrot = cont.actuators['cranezrot']
	crane_move = cont.actuators['crane_move']
	gear_rot = cont.actuators['gear_rot']
	gear_s_rot = cont.actuators['gear_s_rot']

	#set mouse pos
	screenwidth = render.getWindowWidth()
	screenheight = render.getWindowHeight()

	render.setMousePosition(int(screenwidth/2), int(screenheight/2))
	
	crane_tip = cont.sensors['crane_tip'].owner

	if mousemove.positive:
		zmouse = (screenwidth/2 - mousemove.position[0]) * own['sensitivity']
		ymouse = (screenheight / 2 - mousemove.position[1]) * own['sensitivity']
		
		own['previousz'] = (own['previousz'] * .8 + zmouse * .2)
		own['previousy'] = (own['previousy'] * .8 + ymouse * .2)
		
		zmouse = own['previousz']
		#set max speed
		zmouse = max(min(zmouse, .02), -.02)
		ymouse = max(min(ymouse, .06), -.06)
		
		#restrict crane tip
		#loc = crane_tip.localPosition[0]
		crane_tip.localPosition[0] = max(min(crane_tip.localPosition[0], 5), -20)
		#restrict crane rotation
		#print (own['start_rot'])
		crane_angle = own.localOrientation.to_euler()
		crane_angle[2] = max(min(crane_angle[2], (own['start_rot'] + 1.4)), (own['start_rot'] - 1.4))
		
		crane_angle.to_matrix()
		own.localOrientation = crane_angle
		#rotate the crane
		crane_move.dLoc =(ymouse *8, 0, 0)
		cranezrot.dRot =(0, 0, -zmouse)
		gear_rot.dRot =(0, 0, zmouse *2.5)
		gear_s_rot.dRot =(0, -zmouse *2.5, 0)

		cont.activate(gear_rot)
		cont.activate(gear_s_rot)
		cont.activate(cranezrot)
		cont.activate(crane_move)
	else:
		cont.deactivate(gear_rot)
		cont.deactivate(gear_s_rot)
		cont.deactivate(cranezrot)
		cont.deactivate(crane_move)
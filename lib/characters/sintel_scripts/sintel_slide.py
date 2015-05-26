'''
--------------------------------------------------------------------------------------------------------
time to slide
--------------------------------------------------------------------------------------------------------
'''

from bge import logic

sintel_rig = logic.getCurrentScene().objects['sintel_rig']

def main(cont):
	own = cont.owner
	
	own.setLinearVelocity([0, 35, -10], True)
	
	sintel_rig.playAction('sintel_slide', 1, 1, layer=0, play_mode=logic.KX_ACTION_MODE_LOOP, speed = (own['ANIM_SPEED'] * .75), blendin = 5)
	
	if own['floor_angle'] < 30:
		own.state = logic.KX_STATE1
		#pass
'''
--------------------------------------------------------------------------------------------------------
checks for key events

todo: add support for custom keys
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, events

keyboard = logic.keyboard
mouse = logic.mouse

JUST_ACTIVATED = logic.KX_INPUT_JUST_ACTIVATED
JUST_RELEASED = logic.KX_INPUT_JUST_RELEASED
ACTIVE = logic.KX_INPUT_ACTIVE
NONE = logic.KX_INPUT_NONE

player = logic.getCurrentScene().objects['sintel_col']

def main(cont):
	if keyboard.events[events.WKEY] == JUST_ACTIVATED or keyboard.events[events.WKEY] == ACTIVE:
		player['FORWARD'] = True
	if keyboard.events[events.WKEY] == JUST_RELEASED:
		player['FORWARD'] = False
	if keyboard.events[events.AKEY] == JUST_ACTIVATED or keyboard.events[events.AKEY] == ACTIVE:
		player['LEFT'] = True
	if keyboard.events[events.AKEY] == JUST_RELEASED:
		player['LEFT'] = False
	if keyboard.events[events.SKEY] == JUST_ACTIVATED or keyboard.events[events.SKEY] == ACTIVE:
		player['BACK'] = True
	if keyboard.events[events.SKEY] == JUST_RELEASED:
		player['BACK'] = False
	if keyboard.events[events.DKEY] == JUST_ACTIVATED or keyboard.events[events.DKEY] == ACTIVE:
		player['RIGHT'] = True
	if keyboard.events[events.DKEY] == JUST_RELEASED:
		player['RIGHT'] = False
	if mouse.events[events.LEFTMOUSE] == JUST_ACTIVATED:
		player['CLICK'] = True
	elif mouse.events[events.LEFTMOUSE] == JUST_RELEASED:
		player['CLICK'] = False
	if keyboard.events[events.LEFTSHIFTKEY] == JUST_ACTIVATED or keyboard.events[events.LEFTSHIFTKEY] == ACTIVE:
		player['RUN'] = True
	if keyboard.events[events.LEFTSHIFTKEY] == JUST_RELEASED:
		player['RUN'] = False
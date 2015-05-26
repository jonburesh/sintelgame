'''
--------------------------------------------------------------------------------------------------------
handles targetting and tracking
--------------------------------------------------------------------------------------------------------
'''
from bge import logic
import math

FIGHT_LIST = []

cont = logic.getCurrentController()
own = cont.owner
	
def main():
	
	enemy_near = own.sensors['enemy_near']
	target_ray = cont.sensors['target_ray']
	
	if enemy_near.positive:
		enemy_list = enemy_near.hitObjectList
		enemy_range = []
		#print (enemy_list)
		if own['MOVE'] ==True:
			if target_ray.positive:
				#print ('Target:' + str(target_ray.hitObject))
				setTarget(target_ray.hitObject, enemy_list)
		'''
		else:
			for i in enemy_list:
				dist = own.getDistanceTo(i)
				enemy_range.append((dist, i))
				
			enemy_range.sort()
			nearest_enemy = enemy_range[0][1]
			setTarget(nearest_enemy, enemy_list
		'''
	else:
		own['TARGET'] = ''
			
def setTarget(target, enemyList):
	logic.globalDict['target'] = target
	own['TARGET'] = str(target)
	target['target'] = True
	for i in enemyList:
		if i != target:
			i['target'] = False
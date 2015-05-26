import xml.etree.ElementTree as ET
import os
from bge import logic

global dialogs, objectives, root, current_dialog

dialogs = []
objectives = []
root = None
current_dialog = 0

def command(command_tree):
	#find all <command> tags
	commands = list(command_tree.iter('command'))
	for k in commands:
		#analyze <command> data
		command_text = k.text
		try:
			command_text = command_text.replace(' ', '')
			command_text= command_text.split('=')
		except:
			pass
		#check the <command> 
		if 'next_dialog' in command_text[0]:
			print (command_text[1])
		else:
			print ('xml command not recognized')

def checkConditions(tag):
	return True

def readXML(xml_file):
	global dialogs, root, objectives
	
	print ('\n------------------------------\nreading file: %s...' % (xml_file))
	
	file_name = os.path.abspath(__file__)
	file_name = os.path.dirname(file_name)
	file_name = os.path.join(file_name, xml_file)
	
	#print (file_name)
	
	tree = ET.parse(file_name)
	root = tree.getroot()
	
	quest = tree.find("quest")
	quest_name = quest.get('id')
	
	print ('Quest title: %s\n------------------------------\n' % (quest_name))
	
	dialogs = list(quest.iter('dialog'))
	objectives = list(quest.iter('objective'))

def nextObjective(objective):
	try:
		logic.globalDict['game_notifications']
	except:
		logic.globalDict['game_notifications'] = []
		
	objective_id = objective.get('id')
	objective_message = objective.find('message')
	
	objective_comp = str(objective_message.text)
	logic.globalDict['game_notifications'].append(objective_comp)
	logic.globalDict['game_objective'] = objective_comp
	
	
def nextDialog(next_dialog):
	try:
		logic.globalDict['game_dialog']
	except:
		logic.globalDict['game_dialog'] = []
		
	dialog_id = next_dialog.get('id')
	dialog_speaker = next_dialog.get('speaker')
	dialog_message = next_dialog.find('message')
	
	dialog_comp = str(dialog_message.text)
	logic.globalDict['game_dialog'].append(dialog_comp)
	
	#print (dialog_comp)
	
def init(cont):
	own = cont.owner
	readXML(own['xml_file'])
	
def main(cont):
	global dialogs, objectives
	
	own = cont.owner
	
	next_dialog = dialogs[own['current_dialog']-1]
	try:
		next_objective = objectives[own['objective']]
	except:
		pass
	
	if own['go_dialog']:
		own['go_dialog'] = False
		nextDialog(next_dialog)
	
	if own['go_objective']:
		own['go_objective'] = False
		nextObjective(next_objective)
	
if __name__ == "__main__":
	main()
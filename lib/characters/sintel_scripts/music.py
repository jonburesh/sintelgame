import bge, os
import sintel_scripts.get_current_level

def main():
	#initiate the audio device
	
	Player = bge.logic.getCurrentScene().objects["PlayerCol"]
	
	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	"""
	ending_game = cont.sensors['ending_game']
	sounds = cont.actuators['sounds']
	
	sounds.fileName = 'theme.ogg'
	sounds.volume = 3.6
	cont.activate(sounds)
	
	#Have not gathered information, then do so.
	if own['gather']==True:
		own['level_name'] = sintel_scripts.get_current_level.main()
		level_path = '//%s/music/' % own['level_name']
		own['d_music_path'] = level_path# + 'something_in_the_dark.ogg'
		try:
			dirList=os.listdir(bge.logic.expandPath(level_path))
			ogg_files = [x for x in dirList if x.endswith('.ogg')]
			print ('found music file/s: ',ogg_files,', will use: ', ogg_files[0])
			own['d_music_path'] = own['d_music_path']+ogg_files[0]
		except:
			print ('could not locate %s folder.' % own['level_name'])
		own['gather']=False
	else:
		if own['playing']==False:
			#out of battle, not fleeing
			if Player['p_state']==0:
				try:
					sound_act.fileName = 'theme.ogg'
					cont.activate(sound_act)
					own['playing'] = True
				except:
					print ('could not play/locate custom music file, switching to defualt.')
					dirList=os.listdir(bge.logic.expandPath('//defualt/music/'))
					ogg_files = [x for x in dirList if x.endswith('.ogg')]
					print ('found music file/s: ',ogg_files,', will use: ', ogg_files[0])
					own['d_music_path'] = '//defualt/music/'+ogg_files[0]
					#sound_act.fileName = bge.logic.expandPath(own['d_music_path'])
					sound_act.fileName = 'theme.ogg'
					cont.activate(sound_act)
					own['playing'] = True
	"""
	
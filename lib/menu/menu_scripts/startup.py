'''
--------------------------------------------------------------------------------------------------------
starts game - plays opening
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, texture

scene = logic.getCurrentScene()

LEVEL_MAIN = scene.objects['LEVEL_MAIN']

py_icon = scene.objects['py_icon']
py_logo = scene.objects['py_logo']
blender_logo = scene.objects['blender_logo']
video_plane = scene.objects['video_plane']
black_bg = scene.objects['black_bg']

def init(cont):
	print ('- game startup')
	py_icon.visible = False
	py_logo.visible = False
	video_plane.visible = False
	black_bg.visible = False
	addBlender()
	global TIME
	TIME = .0

def main(cont):
	own = cont.owner
	global TIME
	
	key_skip = cont.sensors['key_skip'].positive
	joy_skip = cont.sensors['joy_skip'].positive
	
	TIME +=.0155
	
	if key_skip or joy_skip:
		cont.activate('start_menu')
	
	if own['status'] == 0:
		if TIME > 3:
			addPython()
			own['status'] = 1
	elif own['status'] == 1:
		if TIME > 4:
			py_logo.visible = True
			py_logo.playAction('fade_in', 1, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
			own['status'] = 2
	elif own['status'] == 2:
		if TIME > 6:
			video_plane.visible = True
			video_plane.playAction('fade_in', 1, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY, speed = .5)
			own['status'] = 3
	elif own['status'] == 3:
		if TIME > 7:
			py_icon.visible = False
			py_logo.visible = False
			black_bg.visible = True
			playVideo(video_plane, '//../textures/videos/team_aurora_intro.ogg')
			sound = cont.actuators["aurora_sound"]
			cont.activate(sound)
			logic.sound = sound
			own['status'] = 4
	elif own['status'] == 4:
		updateVideo()
		if TIME > 11:
			video_plane.playAction('fade_in', 10, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
			own['status'] = 5
	elif own['status'] == 5:
		if TIME > 12:
			video_plane.playAction('fade_in', 1, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
			playVideo(video_plane, '//../textures/videos/sintel_game_intro.ogg')
			sound = cont.actuators["sintel_sound"]
			cont.activate(sound)
			logic.sound = sound
			own['status'] = 6
	elif own['status'] == 6:
		updateVideo()
		if TIME > 19:
			video_plane.playAction('fade_in', 10, 1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
			own['status'] = 7
	elif own['status'] == 7:
		if TIME > 21:
			cont.activate('start_menu')
			
def addBlender():
	print ('- blender')
	blender_logo.playAction('blender_logo_scale', 1, 25, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
	
def addPython():
	print ('- python')
	py_icon.visible = True
	blender_logo.visible = False
	
	py_icon.playAction('fade_in', 1, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
	py_icon.playAction('py_icon_rotate', 1, 30, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)

def playVideo(obj, video_path):
	matID = texture.materialID(obj, 'IMplaceholder.jpg')
	logic.video = texture.Texture(obj, matID)
	
	movie = logic.expandPath(video_path)
	logic.video.source = texture.VideoFFmpeg(movie)
	logic.video.source.play()
	
def updateVideo():
	logic.video.refresh(True, logic.sound.time)
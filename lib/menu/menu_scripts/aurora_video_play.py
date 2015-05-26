import bge

def main():
	cont = bge.logic.getCurrentController()
	obj = cont.owner
	novideo = cont.actuators["novideo"]
	try:
		import VideoTexture
		print ('Playing video. Enjoy!')
	except:
		cont.activate(novideo)
		print ('Video failed to play. :(')

	#if not hasattr(bge.logic, 'video'):
	matID = VideoTexture.materialID(obj, 'IMplaceholder.jpg')
	bge.logic.video = VideoTexture.Texture(obj, matID)
	movie = bge.logic.expandPath("//../textures/videos/team_aurora_intro.ogg")
	bge.logic.video.source = VideoTexture.VideoFFmpeg(movie)
	#bge.logic.video.source.scale = True

	bge.logic.video.source.play()
	print (movie)

'''
--------------------------------------------------------------------------------------------------------
Plays the film Sintel
--------------------------------------------------------------------------------------------------------
'''
from bge import logic, texture

def main():
	cont = logic.getCurrentController()
	own = cont.owner
	
	MAT = texture.materialID(own, 'MASINTEL')
	logic.video = texture.Texture(own, MAT)
	
	movie = logic.expandPath('//sintel2.mp4')
	logic.video.source = texture.VideoFFmpeg(movie)
	logic.video.source.scale = True
	logic.video.source.flip = True
	logic.video.source.repeat = 0
	
	logic.video.source.play()
	
	sound = cont.actuators["movie_sound"]
	cont.activate(sound)

	logic.sound = sound
	
	print('Playing Film. Enjoy!')
	
def refresh():
	#logic.video.refresh(True)
	logic.video.refresh(True, logic.sound.time)
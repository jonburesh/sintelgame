# refresh video
import bge

def main():
	if hasattr(bge.logic, 'video'):
		bge.logic.video.refresh(True)

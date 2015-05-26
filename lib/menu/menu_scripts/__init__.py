#Loads either a glsl scene or a non glsl scene
import menu_scripts.glsl

#Hides / Shows the mouse pointer
import menu_scripts.hide_mouse
import menu_scripts.show_mouse

#Video scripts
import menu_scripts.video_play
import menu_scripts.video_refresh

#Take screenshot
import menu_scripts.take_screenshot

#Menu Controls
import menu_scripts.menu_controls

#Settings setup
import menu_scripts.settings_setup
import menu_scripts.settings_controls

#looking for the save file
import menu_scripts.savefile_check

#saving / loading the config file
import menu_scripts.config_save
import menu_scripts.config_load

#stop playing sound
import menu_scripts.sound_stop

#LOD ony use if sintel (sintel.blend) is not linked into the file (or else 2 lod scripts would be running)
import menu_scripts.level_lod

#Set the loading file
import menu_scripts.set_load_file
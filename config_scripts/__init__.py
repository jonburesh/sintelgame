#Loads either a glsl scene or a non glsl scene
import config_scripts.glsl

#loads either the glsl runtime or the non glsl runtime
import config_scripts.load_nglsl
import config_scripts.load_nglsl_linux
import config_scripts.load_glsl
import config_scripts.load_glsl_linux

#Saves a config files
import config_scripts.save_config

#Sets the game to load GLSL from now on
import config_scripts.set_glsl
#Same for No GLSL
import config_scripts.set_noglsl

#Sets the loading variable
import config_scripts.set_load_file
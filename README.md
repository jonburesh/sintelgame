# Sintel The Game

![Alt text](http://jon.sintelgame.org/wp-content/uploads/2013/02/sintel_title.png)

### Description

An open source adventure game created with Blender3D based on the open source film 'Sintel'.

The goal of this project was to expand upon the world of Sintel and to develop a platform that enables users to create and share their own content.

### How to Run

1. Download Blender <a href="http://download.blender.org/release/Blender2.68/">2.68</a>
2. use blenderplayer.exe included in blender install to run sintel_the_game.blend <b>(blender_dir/blenderplayer.exe game_dir/bin/sintel_the_game.blend)</b>

### License

Sintel The Game is released under the <a href= "http://opensource.org/licenses/MIT">MIT</a> license.

### Details

Sintel The Game uses the <a href= "http://www.blender.org">Blender Game Engine</a> (v2.68) and is programmed in Python. The game is stable on Windows and Linux (as of 2014) but should work on OSX (perhaps with some tweaking).

- Only a few levels are really playable (desert_level, docks_level, tundra_level)
- Each level is split into its own .blend file. Any characters, enemies or props are located in separate .blend files and instanced into the levels. 
- The level selector in the main menu loads .blends from the lib/levels folder
- If you want to make changes to the Player, use lib/characters/sintel_rig_2.blend


![Alt text](lib/textures/blender_logo.png)



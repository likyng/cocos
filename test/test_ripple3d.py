# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#


import pyglet
import cocos
from cocos.director import director
from cocos.actions import *


class BackgroundLayer( cocos.layer.Layer ):
    def __init__(self):
        super( BackgroundLayer, self ).__init__()
        self.img = pyglet.resource.image('background_image.png')

    def draw( self ):
        self.img.blit(0,0)

def main():
    director.init( resizable=True )
    director.set_depth_test()

    main_scene = cocos.scene.Scene()

    main_scene.add( BackgroundLayer(), z=0 )

    # important:  maintain the aspect ratio in the grid
    e = Ripple3D( radius=240, grid=(32,24), duration=20, waves=20, amplitude=60 )
    main_scene.do( e )

    director.run (main_scene)

if __name__ == '__main__':
    main()

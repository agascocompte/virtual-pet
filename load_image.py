'''
Created on 18/1/2016

@author: Arturo
'''

import pygame,sys
from pygame.locals import *

def load_image(filename, transparent=False,blanco=(255, 255, 255, 255)):
        image = pygame.image.load(filename)        
        #image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                #blanco=(255, 255, 255, 255)
                image.set_colorkey(blanco, RLEACCEL)                
        return image
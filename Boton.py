'''
Created on 18/1/2016

@author: Arturo
'''

from load_image import *

class Boton():
    def __init__(self,x,y,scalex,scaley,ruta,ruta2):                     
        self.image=pygame.transform.scale(load_image(ruta,True),(scalex,scaley))
        self.copia=self.image
        self.imageClicked=pygame.transform.scale(load_image(ruta2,True),(scalex,scaley))
        self.rect=self.image.get_rect()
        self.rect.x=int(x)
        self.rect.y=int(y)
        self.copiaX=0
        self.copiaY=0
        self.display=False
         
    def set_pos(self,x,y):
        self.rect.x=x
        self.rect.y=y
        
    def save_pos(self):
        self.copiaX=self.rect.x
        self.copiaY=self.rect.y
        
    def load_pos(self):
        self.rect.x=self.copiaX
        self.rect.y=self.copiaY             

    def left(self):
        return self.rect.left

    def right(self):
        return self.rect.right

    def bottom(self):
        return self.rect.bottom

    def centerx(self):
        return self.rect.centerx

    def set_display(self,val):
        self.display=val

    def get_display(self):
        return self.display

    def Draw(self,screen):
        screen.blit(self.image,self.rect)
        
    def OnMouseUp(self,position):
        if (self.rect.left<position[0]<self.rect.right and self.rect.top<position[1]<self.rect.bottom):
            self.image=self.imageClicked
            return True            
        else:
            self.image=self.copia
            return False                 
        
class ExitButton(Boton): 
    def __init__(self,x,y,scalex,scaley,ruta,ruta2):
        Boton.__init__(self, x, y, scalex, scaley, ruta, ruta2)              
        
    def exit(self):
        sys.exit()
        
class PlayButton(Boton): 
    def __init__(self,x,y,scalex,scaley,ruta,ruta2):
        Boton.__init__(self, x, y, scalex, scaley, ruta, ruta2)
        self.play=False
        
    def not_playable(self):
        self.play=False     
        
    def playable(self):
        self.play=True
        
    def get_playable(self):          
        return self.play

class InfoButton(Boton):
    def __init__(self,x,y,scalex,scaley,ruta,ruta2):
        Boton.__init__(self, x, y, scalex, scaley, ruta, ruta2)

class FoodButton(Boton):
    def __init__(self,x,y,scalex,scaley,ruta,ruta2):
        Boton.__init__(self, x, y, scalex, scaley, ruta, ruta2)

class DrinkButton(Boton):
    def __init__(self,x,y,scalex,scaley,ruta,ruta2):
        Boton.__init__(self, x, y, scalex, scaley, ruta, ruta2)

class HealthButton(Boton):
    def __init__(self,x,y,scalex,scaley,ruta,ruta2):
        Boton.__init__(self, x, y, scalex, scaley, ruta, ruta2)

class EnergyButton(Boton):
    def __init__(self,x,y,scalex,scaley,ruta,ruta2):
        Boton.__init__(self, x, y, scalex, scaley, ruta, ruta2)
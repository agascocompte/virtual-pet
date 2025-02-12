'''
Created on 18/1/2016

@author: Arturo
'''

from load_image import *

class Sprite():
    def __init__(self,x,y,scalex,scaley,ruta):
        self.image=pygame.transform.scale(load_image(ruta,True,(0,0,0)),(scalex,scaley))
        self.original=self.image
        self.rect=self.image.get_rect()
        self.rect.left=x
        self.rect.top=y
        
    def Draw(self,screen):
        screen.blit(self.image,self.rect)
        
    def move(self):
        self.rect.x+=1

    def set_pos(self,pos):
        self.rect.centerx=pos[0]
        self.rect.centery=pos[1]

    def centerx(self):
        return self.rect.centerx

    def centery(self):
        return self.rect.centery
        
class Fondo(Sprite):
    def __init__(self,x,y,scalex,scaley,ruta,ruta2,ruta4,ruta6,ruta8,ruta9):
        Sprite.__init__(self, x, y, scalex, scaley, ruta)
        self.image2=pygame.transform.scale(load_image(ruta2,True,(0,0,0)),(scalex,scaley))
        self.image4=pygame.transform.scale(load_image(ruta4,True,(0,0,0)),(scalex,scaley))
        self.image6=pygame.transform.scale(load_image(ruta6,True,(0,0,0)),(scalex,scaley))
        self.image8=pygame.transform.scale(load_image(ruta8,True,(0,0,0)),(scalex,scaley))
        self.image9=pygame.transform.scale(load_image(ruta9,True,(0,0,0)),(scalex,scaley))
        
    def set_image(self,val):
        if val==0:
            self.image=self.original
        elif val==2:
            self.image=self.image2
        elif val==4:
            self.image=self.image4 
        elif val==6:
            self.image=self.image6
        elif val==8:
            self.image=self.image8
        elif val==9:
            self.image=self.image9

class Item(Sprite):
    def __init__(self,x,y,scalex,scaley,ruta):
        Sprite.__init__(self, x, y, scalex, scaley, ruta)
        self.dragged=False
        self.originalX=x
        self.originalY=y

    def isDragged(self,mousePos,click):
        if (self.rect.left<mousePos[0]<self.rect.right and self.rect.top<mousePos[1]<self.rect.bottom) and click:
            return True
        else:
            return False

    def set_originalPos(self):
        self.rect.left=self.originalX
        self.rect.top=self.originalY

    def OnPet(self,mousePos,pet):
        if pet.left()<mousePos[0]<pet.right() and pet.top()<mousePos[1]<pet.bottom():
            return True
        else:
            return False

    def get_dragged(self):
        return self.dragged

    def set_dragged(self,val):
        self.dragged=val

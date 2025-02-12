'''
Created on 19/1/2016

@author: Arturo
'''

from load_image import *
import random

class Pet():
    def __init__(self,x,y,scalex,scaley,ruta,ancho,alto):        
        #----------------------------Imagenes y rects---------------------#
        self.spritesheet=load_image(ruta,True)
        self.imageBody=pygame.transform.scale(self.spritesheet.subsurface(672,737,657,532),(scalex,scaley))
        self.rectBody=self.imageBody.get_rect()
        self.rectBody.centerx=ancho/2
        self.rectBody.centery=alto/1.5 
        
        self.imageWingsA=pygame.transform.scale(self.spritesheet.subsurface(1313,530,687,241),(scalex,scaley))
        self.imageWingsB=pygame.transform.scale(self.spritesheet.subsurface(1361,872,613,256),(scalex,scaley))
        self.imageWings=self.imageWingsA
        self.rectWings=self.imageWings.get_rect()
        
        self.imageFeelersA=pygame.transform.scale(self.spritesheet.subsurface(134,536,373,193),(int(scalex/2),int(scaley/2)))
        self.imageFeelersB=pygame.transform.scale(self.spritesheet.subsurface(134,800,373,193),(int(scalex/2),int(scaley/2)))
        self.imageFeelers=self.imageFeelersA
        self.rectFeelers=self.imageFeelers.get_rect()
                
        self.imageSmile=pygame.transform.scale(self.spritesheet.subsurface(53,68,313,286),(int(scalex/2),int(scaley/2)))
        self.imageSad=pygame.transform.scale(self.spritesheet.subsurface(521,68,313,286),(int(scalex/2),int(scaley/2)))
        self.imageHungry=pygame.transform.scale(self.spritesheet.subsurface(680,1496,720,382),(int(scalex),int(scaley/1.5)))
        self.imageThirsty=pygame.transform.scale(self.spritesheet.subsurface(1280,59,720,382),(int(scalex),int(scaley/1.5)))
        self.imageSick=pygame.transform.scale(self.spritesheet.subsurface(896,68,313,286),(int(scalex/2),int(scaley/2)))
        self.imageSleepy=pygame.transform.scale(self.spritesheet.subsurface(1516,1494,294,354),(int(scalex/2),int(scaley/1.5)))
        self.imageSleeping=pygame.transform.scale(self.spritesheet.subsurface(133,1382,445,523),(int(scalex),int(scaley)))
        self.imageFace=self.imageSmile
        self.rectFace=self.imageFace.get_rect()
        
        #---------------------------Movimiento..............................#
        self.maxY=15    
        self.count=0
        self.dirY=1  #1->up , 2->down
        self.dirX=0  #0->stand , 1->right , -1->left

        #---------------------------Emociones-------------------------------#
        self.happynes=100
        self.hungry=100
        self.thirsty=100
        self.energy=100
        self.sick=False
        self.sleep=False
        
        #---------------------------Apoyo-----------------------------------#
        self.emotions=[self.imageSmile,self.imageSad,self.imageHungry,self.imageThirsty,self.imageSick,self.imageSleepy,self.imageSleeping]
        self.index=0

    def get_happyness(self):
        return self.happynes

    def get_hungry(self):
        return self.hungry

    def get_thirsty(self):
        return self.thirsty

    def get_energy(self):
        return self.energy

    def get_sick(self):
        return self.sick

    def left(self):
        return self.rectBody.left

    def right(self):
        return self.rectBody.right

    def top(self):
        return self.rectBody.top

    def bottom(self):
        return self.rectBody.bottom

    def change_emotion(self):        
        if self.index<len(self.emotions):        
            self.imageFace=self.emotions[self.index]
            self.rectFace=self.imageFace.get_rect()
            self.index+=1
        else:
            self.index=0                   
                
    def Draw(self,screen):
        screen.blit(self.imageWings,self.rectWings)
        screen.blit(self.imageBody,self.rectBody)
        screen.blit(self.imageFeelers,self.rectFeelers)
        screen.blit(self.imageFace,self.rectFace)
        
    def move(self,ancho,seconds,microsecond):
        #---------------Mover Pet en Y--------------#
        if self.count<self.maxY:
            self.rectBody.centery+=1*self.dirY
            self.count += 1
        else:
            self.dirY=-self.dirY
            self.count=0
            
        #---------------Mover Pet en X--------------#
        if 0<self.rectBody.centerx<ancho:
            if seconds%5==0 and microsecond%10==0:
                self.dirX=random.randint(-1,1)
            if self.dirX!=0:
                self.rectBody.centerx+=1*self.dirX
        else:
            if self.rectBody.centerx>=ancho:
                self.dirX=-1
            if self.rectBody.centerx<=0:
                self.dirX=1
            self.rectBody.centerx+=1*self.dirX                             
        
    def updateFace(self,seconds):
        if seconds%2==0:#Segundos pares
            #------------Imagenes-----------#
            self.imageWings=self.imageWingsA
            self.imageFeelers=self.imageFeelersA
            #-----------Rect Antenas--------#
            self.rectFeelers.centerx=self.rectBody.centerx+1
            self.rectFeelers.centery=self.rectBody.top-14
            #------------Rect CaraX dependiendo de la imagen----------#
            if self.imageFace==self.imageSick:
                self.rectFace.centerx=self.rectBody.centerx-20
            elif self.imageFace==self.imageThirsty or self.imageFace==self.imageHungry:
                self.rectFace.centerx=self.rectBody.centerx+30
            elif self.imageFace==self.imageSleeping:
                self.rectFace.centerx=self.rectBody.centerx+20                       
            else:
                self.rectFace.centerx=self.rectBody.centerx-10    
            
        else:#Segundos impares
            #-----------Imagenes------------#
            self.imageWings=self.imageWingsB
            self.imageFeelers=self.imageFeelersB
            #-----------Rect Antenas--------#
            self.rectFeelers.centerx=self.rectBody.centerx+3
            self.rectFeelers.centery=self.rectBody.top-5
            #-----------Rect CaraX dependiendo de la imagen-----------#
            if self.imageFace==self.imageSick:
                self.rectFace.centerx=self.rectBody.centerx-10
            elif self.imageFace==self.imageThirsty or self.imageFace==self.imageHungry:
                self.rectFace.centerx=self.rectBody.centerx+25
            elif self.imageFace==self.imageSleeping:
                self.rectFace.centerx=self.rectBody.centerx+15                        
            else:
                self.rectFace.centerx=self.rectBody.centerx    
         
        #---------------Rect Alas-----------#        
        self.rectWings.centerx=self.rectBody.centerx-5
        self.rectWings.centery=self.rectBody.centery-25        
        #---------------Rect CaraY----------#
        if self.imageFace==self.imageSleeping:
            self.rectFace.centery=self.rectBody.top+30
        else:    
            self.rectFace.centery=self.rectBody.centery
            
    def heal(self):
        self.sick=False
    
    def feed(self,val):
        self.hungry+=val
        if self.hungry>100:
            self.hungry=100

    def give_drink(self,val):
        self.thirsty+=val
        if self.thirsty>100:
            self.thirsty=100

    def lose_hungry(self):
        self.hungry-=1
        if self.hungry<0: self.hungry=0

    def lose_thirsty(self):
        self.thirsty-=1
        if self.thirsty<0: self.thirsty=0

    def lose_energy(self):
        self.energy-=1
        if self.energy<0: self.energy=0

    def get_ill(self):
        self.sick=True

    def rest(self):
        self.energy+=5

    def updateEmotions(self,minutes):
        if minutes%2==0:
            self.lose_hungry()
        if minutes%3==0:
            self.lose_thirsty()
        if minutes%5==0 and not self.isSleep():
            self.lose_energy()
        elif minutes%5==0 and self.isSleep():
            self.rest()

        if self.hungry<10 and self.thirsty<10 and self.energy<35: self.get_ill()

    def isSleep(self):
        return self.sleep

    def changeStateSleep(self):
        self.sleep=not self.sleep

    def updateFaceEmotionImage(self):
        if self.happynes<0: self.happynes=0
        else: self.happynes=(self.hungry+self.thirsty+self.energy)/3

        if self.isSleep():
            self.imageFace=self.imageSleeping
        elif self.sick==True:
            self.imageFace=self.imageSick
        elif self.energy<10:
            self.imageFace=self.imageSleepy
        elif self.thirsty<20:
            self.imageFace=self.imageThirsty
        elif self.hungry<20:
            self.imageFace=self.imageHungry
        elif self.happynes>70:
            self.imageFace=self.imageSmile
        else:
            self.imageFace=self.imageSad

        self.rectFace=self.imageFace.get_rect()

    def Save(self):
        f=open("Save/Save.txt","r+")

        linea = f.readline()
        if linea == "":
            f.writelines(self.nombreMazo+"#"+str(self.victorias)+"#"+str(self.derrotas)+"#"+str(int(self.calcularPorcentaje()))+"#"+str(self.totales)+"\n")
        f.close()

    #def Load(self):
        #f=open("Save/Save.txt","r")


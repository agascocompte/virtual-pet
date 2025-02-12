import pygame,sys,datetime, asyncio
from pygame.locals import*
from functions import *
from Boton import *
from Sprite import *
from Pet import *


ANCHO=800
ALTO=600

pygame.init()
screen=pygame.display.set_mode((ANCHO,ALTO),HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption("Virtual Pet Alpha")
clock=pygame.time.Clock()
clock.tick(60)

#--------------------menu buttons definition-------------------#
playbutton=PlayButton(ANCHO/5,(ALTO/2)-51,500,50,"images/menu/play.png","images/menu/playOn.png")
exitbutton=ExitButton(ANCHO/5,(ALTO/2),500,50,"images/menu/exit.png","images/menu/exitOn.png")
clickMenu=False
#--------------------Background definition---------------------#
fondo=Fondo(0,0,ANCHO,ALTO+10,"images/game_screen/sky.png","images/game_screen/sky20.png","images/game_screen/sky40.png","images/game_screen/sky60.png","images/game_screen/sky80.png","images/game_screen/sky95.png")
mountains1=Sprite(0,0,ANCHO,ALTO+10,"images/game_screen/mountains1.png")
mountains2=Sprite(0,0,ANCHO,ALTO+10,"images/game_screen/mountains2.png")
wall=Sprite(0,0,ANCHO,ALTO+10,"images/game_screen/wall.png")
floor=Sprite(0,0,ANCHO,ALTO+10,"images/game_screen/floor.png")
clouds=Sprite(0,0,ANCHO,ALTO+10,"images/game_screen/clouds.png")
clouds2=Sprite(-ANCHO,0,ANCHO,ALTO+10,"images/game_screen/clouds.png")
objects=[fondo,mountains1,mountains2,wall,floor,clouds,clouds2]
#-----------------------Pet definitions------------------------#
pet=Pet(ANCHO/2,ALTO/2,120,120,"images/pet/pet_orange - copia.png",ANCHO,ALTO)
#------------------------Button definitions--------------------#
click=True
botonInfo=InfoButton((ANCHO/2)-50,20,100,50,"images/game_screen/botones/botonInfo.png","images/game_screen/botones/botonInfoOn.png")
botonDrink=DrinkButton(botonInfo.left()-52,20,50,50,"images/game_screen/botones/botonWater.png","images/game_screen/botones/botonWaterOn.png")
botonFood=FoodButton(botonDrink.left()-52,20,50,50,"images/game_screen/botones/botonFood.png","images/game_screen/botones/botonFoodOn.png")
botonHealth=HealthButton(botonInfo.right()+2,20,50,50,"images/game_screen/botones/botonHealth.png","images/game_screen/botones/botonHealthOn.png")
botonEnergy=EnergyButton(botonHealth.right()+2,20,50,50,"images/game_screen/botones/botonEnergy.png","images/game_screen/botones/botonEnergyOn.png")
#---------------------Button Menus definitions-----------------#
menuFood=Sprite(0,0,137,213,"images/game_screen/botones/menus/menuFood.png")
menuFood.set_pos((botonFood.left(),botonFood.bottom()*3))
menuDrink=Sprite(0,0,137,213,"images/game_screen/botones/menus/menuDrink.png")
menuDrink.set_pos((botonInfo.centerx(),botonInfo.bottom()*3))
menuInfo=Sprite(0,0,453,393,"images/game_screen/botones/menus/menuInfo.png")
menuInfo.set_pos((botonInfo.centerx(),botonInfo.bottom()*4))
menuHealth=Sprite(0,0,137,213,"images/game_screen/botones/menus/menuHealth.png")
menuHealth.set_pos((botonEnergy.right(),botonEnergy.bottom()*3))
#----------------------------items-----------------------------#
canDrag=False
chips=Item(menuFood.centerx()-23,menuFood.centery()-80,50,50,"images/game_screen/botones/menus/items/chips.png")
chicken=Item(menuFood.centerx()-23,menuFood.centery()-26,60,45,"images/game_screen/botones/menus/items/chicken.png")
kebab=Item(menuFood.centerx()-23,menuFood.centery()+30,50,50,"images/game_screen/botones/menus/items/kebab.png")
water=Item(menuDrink.centerx()-15,menuDrink.centery()-80,35,50,"images/game_screen/botones/menus/items/water.png")
refresco=Item(menuDrink.centerx()-15,menuDrink.centery()-24,35,45,"images/game_screen/botones/menus/items/refresco.png")
coldtea=Item(menuDrink.centerx()-27,menuDrink.centery()+28,50,50,"images/game_screen/botones/menus/items/coldtea.png")
botiquin=Item(menuHealth.centerx()-27,menuHealth.centery()-60,60,40,"images/game_screen/botones/menus/items/botiquin.png")
jeringuilla=Item(menuHealth.centerx()-23,menuHealth.centery()+15,50,50,"images/game_screen/botones/menus/items/jeringuilla.png")

async def main():
    #-------------------------Pet Emotions Control-----------------#
    previousMin=0

    #-------------------------Main Bucle---------------------------#
    while True: 
        now=datetime.datetime.now()       
        playable=playbutton.get_playable()              
        mousePos=pygame.mouse.get_pos()
        events=pygame.event.get()       
        
        for event in events:
            if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                clickMenu=True
                click=True
                canDrag=False
            else:
                clickMenu=False
                click=False
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                canDrag=True

            if event.type==KEYDOWN and event.key==K_ESCAPE:
                if playable:
                    playbutton.not_playable()
                    return_menu_buttons(screen,playbutton,exitbutton)
                else:    
                    sys.exit()
            if event.type== QUIT:
                sys.exit()
            

        #--------------------------Menu Inicial-------------------------#
        if not playable:
            clickMenu=DrawMenuScreen(screen,playbutton,exitbutton,mousePos,clickMenu)
        else:
            #---------------------Pantalla Juego------------------------#
            if not pet.isSleep():
                pet.move(ANCHO,now.second,now.microsecond)

            pet.updateFaceEmotionImage()
            pet.updateFace(now.second)
            if now.minute!=previousMin:
                previousMin=now.minute
                pet.updateEmotions(previousMin)

            drawAndMoveBG(objects,screen,now)
            pet.Draw(screen)
            click=handleAndDrawButtons(screen,pet,mousePos,click,botonFood,botonDrink,botonInfo,botonHealth,botonEnergy)
            handleAndDrawMenus(screen,pet,mousePos,canDrag,botonFood,botonDrink,botonInfo,botonHealth,botonEnergy,menuFood,menuDrink,menuHealth,menuInfo,chips,chicken,kebab,water,refresco,coldtea,botiquin,jeringuilla)

        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)

        
asyncio.run(main())       
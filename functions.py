'''
Created on 18/1/2016

@author: Arturo
'''

import pygame

#-----------------------------Menu------------------------------#

def DrawMenuScreen(screen,botonPlay,botonExit,pos,click):
    screen.fill((0,0,0)) 
    if botonPlay.OnMouseUp(pos) and click:
        botonPlay.playable()
        click=False
        botonPlay.save_pos()
        botonExit.save_pos()
        botonPlay.set_pos(2000,1000)
        botonExit.set_pos(2000,1000)
    if botonExit.OnMouseUp(pos) and click:
        botonExit.exit()        
    
    botonPlay.Draw(screen)
    botonExit.Draw(screen)
    return click

def return_menu_buttons(screen,butonPlay,butonExit):
    butonPlay.load_pos()
    butonExit.load_pos()

#----------------------------Game_Screen-------------------------#
    
def drawAndMoveBG(obj,screen,time):
    for i in range (len(obj)):
        #Cambiar cielo segun la hora
        if i==0:
            hour=time.hour
            if 9<=hour<17:
                obj[i].set_image(0)
            elif hour==8 or hour==17:
                obj[i].set_image(2)
            elif hour==7 or hour==18:
                obj[i].set_image(4)
            elif hour==6 or hour==19:
                obj[i].set_image(6)
            elif hour==5 or hour==20:
                obj[i].set_image(8)
            else:
                obj[i].set_image(9)                    
        #Mover nubes
        elif i==len(obj)-1 or i==len(obj)-2:
            obj[i].move()
            if obj[i].rect.left==800:
                obj[i].rect.left=-800        
        obj[i].Draw(screen)

def handleAndDrawButtons(screen,pet,mousePos,click,food,drink,info,health,energy):
    if food.OnMouseUp(mousePos) and click and  food.get_display()==False:
        food.set_display(True)
        drink.set_display(False)
        info.set_display(False)
        health.set_display(False)
        click=False
    elif click and food.get_display():
        food.set_display(False)
        click=False

    if drink.OnMouseUp(mousePos) and click:
        drink.set_display(True)
        info.set_display(False)
        health.set_display(False)
        click=False
    elif click and drink.get_display():
        drink.set_display(False)
        click=False

    if info.OnMouseUp(mousePos) and click:
        info.set_display(True)
        health.set_display(False)
        click=False
    elif click and info.get_display():
        info.set_display(False)
        click=False

    if health.OnMouseUp(mousePos) and click:
        health.set_display(True)
        click=False
    elif click and health.get_display():
        health.set_display(False)
        clikc=False

    if energy.OnMouseUp(mousePos) and click:
        pet.changeStateSleep()
        click=False
    elif click and energy.get_display():
        pet.changeStateSleep()
        click=False

    food.Draw(screen)
    drink.Draw(screen)
    info.Draw(screen)
    health.Draw(screen)
    energy.Draw(screen)

    return click

def handleAndDrawMenus(screen,pet,mousePos,click,food,drink,info,health,energy,menuFood,menuDrink,menuHealth,menuInfo,chips,chicken,kebab,water,refresco,coldtea,botiquin,jeringuilla):
    #------------------------------------------------------------------------Food----------------------------------------------------------------#
    if food.get_display():
        menuFood.Draw(screen)
        #-----------------------Handle Chips--------------#
        if chips.isDragged(mousePos,click) and not chicken.get_dragged() and not kebab.get_dragged():
            chips.set_pos(mousePos)
            chips.set_dragged(True)
            if chips.OnPet(mousePos,pet):
                pet.feed(5)
                chips.set_originalPos()
        else:
            chips.set_originalPos()
            chips.set_dragged(False)
        #----------------------Handle Chicken-------------#
        if chicken.isDragged(mousePos,click) and not chips.get_dragged() and not kebab.get_dragged():
            chicken.set_pos(mousePos)
            chicken.set_dragged(True)
            if chicken.OnPet(mousePos,pet):
                pet.feed(10)
                chicken.set_originalPos()
        else:
            chicken.set_originalPos()
            chicken.set_dragged(False)
        #----------------------Handle Kebab---------------#
        if kebab.isDragged(mousePos,click) and not chips.get_dragged() and not chicken.get_dragged():
            kebab.set_pos(mousePos)
            kebab.set_dragged(True)
            if kebab.OnPet(mousePos,pet):
                pet.feed(15)
                kebab.set_originalPos()
        else:
            kebab.set_originalPos()
            kebab.set_dragged(False)
        #------------Draw Food------------#
        chips.Draw(screen)
        chicken.Draw(screen)
        kebab.Draw(screen)
    #------------------------------------------------------------------------Drink----------------------------------------------------------------#
    elif drink.get_display():
        menuDrink.Draw(screen)
        #----------------------Handle Water---------------#
        if water.isDragged(mousePos,click) and not refresco.get_dragged() and not coldtea.get_dragged():
            water.set_pos(mousePos)
            water.set_dragged(True)
            if water.OnPet(mousePos,pet):
                pet.give_drink(5)
                water.set_originalPos()
        else:
            water.set_originalPos()
            water.set_dragged(False)
        #-------------------Handle Refresco---------------#
        if refresco.isDragged(mousePos,click) and not water.get_dragged() and not coldtea.get_dragged():
            refresco.set_pos(mousePos)
            refresco.set_dragged(True)
            if refresco.OnPet(mousePos,pet):
                pet.give_drink(10)
                refresco.set_originalPos()
        else:
            refresco.set_originalPos()
            refresco.set_dragged(False)
        #------------------Handle Coldtea-----------------#
        if coldtea.isDragged(mousePos,click) and not water.get_dragged() and not refresco.get_dragged():
            coldtea.set_pos(mousePos)
            coldtea.set_dragged(True)
            if coldtea.OnPet(mousePos,pet):
                pet.give_drink(15)
                coldtea.set_originalPos()
        else:
            coldtea.set_originalPos()
            coldtea.set_dragged(False)
        #-----------Draw Drinks-----------#
        water.Draw(screen)
        refresco.Draw(screen)
        coldtea.Draw(screen)
    #-------------------------------------------------------------------------Info----------------------------------------------------------------#
    elif info.get_display():
        menuInfo.Draw(screen)
        pygame.draw.rect(screen,(0,255,100),(menuInfo.centerx()+22,menuInfo.centery()-109,pet.get_happyness()*1.52,9))    #-----Happyness
        pygame.draw.rect(screen,(0,255,100),(menuInfo.centerx()+22,menuInfo.centery()-55,pet.get_hungry()*1.52,9))        #-----Hungry
        pygame.draw.rect(screen,(0,255,100),(menuInfo.centerx()+22,menuInfo.centery()+1,pet.get_thirsty()*1.52,9))        #-----Thristy
        pygame.draw.rect(screen,(0,255,100),(menuInfo.centerx()+22,menuInfo.centery()+56,pet.get_energy()*1.52,9))        #-----Energy
        if pet.get_sick(): pygame.draw.circle(screen,(255,0,50),(menuInfo.centerx()+96,menuInfo.centery()+108),9)         #-----Sick
        else: pygame.draw.circle(screen,(0,255,100),(menuInfo.centerx()+96,menuInfo.centery()+108),9)
    #------------------------------------------------------------------------Health---------------------------------------------------------------#
    elif health.get_display():
        menuHealth.Draw(screen)
        #----------------Handle Botiquin------------------#
        if botiquin.isDragged(mousePos,click) and not jeringuilla.get_dragged():
            botiquin.set_pos(mousePos)
            botiquin.set_dragged(True)
            if botiquin.OnPet(mousePos,pet):
                pet.heal()
                pet.feed(3)
                pet.give_drink(3)
                botiquin.set_originalPos()
        else:
            botiquin.set_originalPos()
            botiquin.set_dragged(False)
        #---------------Handle Jeringuilla----------------#
        if jeringuilla.isDragged(mousePos,click) and not botiquin.get_dragged():
            jeringuilla.set_pos(mousePos)
            jeringuilla.set_dragged(True)
            if jeringuilla.OnPet(mousePos,pet):
                pet.heal()
                jeringuilla.set_originalPos()
        else:
            jeringuilla.set_originalPos()
            jeringuilla.set_dragged(False)
        #----------Draw Health-----------#
        botiquin.Draw(screen)
        jeringuilla.Draw(screen)
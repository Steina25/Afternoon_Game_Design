#Aaron Stein 
#6/17/22
#get user name in pygame
 

import pygame, sys, os

pygame.init()
os.system('cls')
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"gold":(255,215,0)}
clock = pygame.time.Clock()
backgrnd=(255,255,255)
WIDTH=700
HEIGHT=700
xd=WIDTH//3
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enter Name")
screen.fill(backgrnd)

 

run=True #to run the while loop
user_name='' #var to input name
nameClr=(0,0,0) #name text color
boxClr= (25,100,200) #color for box
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
title=TITLE_FONT.render("Enter Name",1,boxClr)
screen.blit(title,(235,40)) 
input_rect = pygame.Rect((WIDTH//3, HEIGHT//3), (200, 40))

#make box
while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:  
                print("hello, "+ user_name)
                #run main menu
                pygame.quit()
                sys.exit()
            if event.key==pygame.K_BACKSPACE: #this just makes backspace work
                user_name=user_name[:-1]
            else:
                user_name+=event.unicode #dont understand this peice 
        pygame.draw.rect(screen, boxClr, input_rect) 
        
        text_surface = MENU_FONT.render(user_name, True, nameClr)
        #use your x,y
        screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))

        pygame.display.flip() #what does flip do? 
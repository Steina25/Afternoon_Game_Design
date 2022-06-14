#Aaron Stein
#learning pygame, images, draw, colors

import random
from turtle import circle
import pygame, os, time, math

from pygameFiles.moveSquare import MENU_FONT, TITLE_FONT
pygame.init()
os.system('cls')

WIDTH = 700 #pixels
HEIGHT = 700

#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #double parenthesis to input the value as 1
pygame.display.set_caption("My First Game") #Title of window
#pygame.time.delay(1000) #to keep window longer
blueClr = (0,0,255) #to pick color
redClr = (255,0,0)
colors={"white":(255,255,255),"pink":(255,0,255),"cyan":(0,255,255),"Lgray":(160,160,160),"Dgray":(64,64,64),"blue":(0,76,153),"red":(255,0,0),"green":(0,204,0),"forest":(0,51,0),"black":(0,0,0)} #color dictonary
clr=colors.get("white")
screen.fill(clr)
#pygame.display.update() #to change backround color. ALways update after change
#pygame.time.delay(1000)
#variables for the square

#images
bg = pygame.image.load("C:\Users\steina25\OneDrive - Greenhill School\Desktop\GameDesign\Afternoon_Game_Design\pygameFiles\images\images\\bgSmaller.jpg.url")
char = pygame.image.load("C:\Users\steina25\OneDrive - Greenhill School\Desktop\GameDesign\Afternoon_Game_Design\pygameFiles\images\images\PixelArtTutorial.png.url")
char = pygame.transform.scale(char, (50,50))
#screen.blit(bg, (0,0))
#pygame.display.update()
#pygame.time.delay(5000)

hb=50
wb=50
xb=100
yb=300

charx = xb
chary = yb

cx=350
cy=350
rad=25
speed=2
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
#create var mve

def menu():
    Title = Title_FOnt.render("Title", 1, colors.get("black"))
    def instructions():
        
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("Instructions", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    myfile = open("pygameFiles\instructions.txt")
    content = myfile.readlines()

    yi= 150
    for line in content:
        Instruc= MENU_FONT.render(line, 1, colors.get("black"))
        screen.blit(Instruc, (40, 100))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40

    #create buttons
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_1)
    pygame.draw.rect(screen, colors.get("pink"), Button_2)

    #render yes and no
    text1 = MENU_FONT.render("Yes", 1, colors.get("black"))
    text1 = MENU_FONT.render("No", 1, colors.get("black"))
    screen.blit(text1, (255, 410))
    screen.blit(text1, (425, 410))
    pygame.display.update()
    while True:
        # screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
           mx = mousePos[0]
           my = mousePos[1]
            if Button_1.collidepoint(mx, my):
                return True
            if Button_2.collidepoint(mx,my):
                return False

menu()
run = instructions()
while run:
    screen.blit(bg, (0,0))
    # screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("Y quit")
    keys= pygame.key.get_pressed() #this is a list
    #mve square
    if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
        square.x += speed
        charx += speed
    if keys[pygame.K_LEFT] and  square.x > speed:
        square.x -= speed
        charx -= speed
    if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
        square.y -= speed
        chary -= speed
    if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
        square.y += speed
        chary += speed
        #mve Circle
    if keys[pygame.K_d] and cx < WIDTH -(rad):
        cx += speed
        insSquare.x += speed
    if keys[pygame.K_a] and  cx > (speed+rad):
        cx -= speed
        insSquare.x -= speed
    if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
        cy -= speed
        insSquare.y -= speed
    if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
        cy += speed
        insSquare.y += speed

    if square.colliderect(insSquare):
        print("BOOM")
        rad+=1
        cx=random.randint(rad, WIDTH-rad)
        cy=random.randint(rad, HEIGHT-rad)
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)
    #rect(surface, color, rect) -> Rect
    pygame.draw.rect(screen, squareClr,square)
    screen.blit(char, (charx, chary))
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, circleClr, (cx,cy), rad)
    pygame.draw.rect(screen, squareClr, insSquare)
    pygame.display.update()

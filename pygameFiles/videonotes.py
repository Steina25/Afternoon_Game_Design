import pygame, os, time, random, math, datetime, sys
from pygame import mixer
pygame.init()

os.system('cls')


pygame.display.set_caption("First Game")
WIDTH=700
HEIGHT=700
walkRight = [pygame.image.load('pygameFiles\images\RIght.png'), pygame.image.load('pygameFiles\images\RIght.png'), pygame.image.load('pygameFiles\images\RIght.png'), pygame.image.load('pygameFiles\images\RIght.png'), pygame.image.load('pygameFiles\images\RIght.png'), pygame.image.load('pygameFiles\images\RIght.png'), pygame.image.load('pygameFiles\images\RIght.png'), pygame.image.load('pygameFiles\images\RIght.png'), pygame.image.load('pygameFiles\images\RIght.png')]
walkLeft = [pygame.image.load('pygameFiles\images\Left.png'), pygame.image.load('pygameFiles\images\Left.png'), pygame.image.load('pygameFiles\images\Left.png'), pygame.image.load('pygameFiles\images\Left.png'), pygame.image.load('pygameFiles\images\Left.png'), pygame.image.load('pygameFiles\images\Left.png'), pygame.image.load('pygameFiles\images\Left.png'), pygame.image.load('pygameFiles\images\Left.png'), pygame.image.load('pygameFiles\images\Left.png')]
bg = pygame.image.load('pygameFiles\images\\roadFinal.jpg')
char = pygame.image.load('pygameFiles\images\Forward.png')
win = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
x = 20
y = 225
width = 100
height = 200
vel = 10
left = False
right = False
walkCount = 0
mx = 0
my = 0
move = walkLeft

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))
    Border_1 = pygame.Rect(0, 0, 10, 700)
    Border_2 = pygame.Rect(690, 0, 700, 700)
    pygame.draw.rect(screen, colors.get("GREY4"), Border_1)
    pygame.draw.rect(screen, colors.get("GREY4"), Border_2)
    if Border_1.collidepoint(mx, my):
          print()

    
    
    
    if walkCount + 1 >= 27: #27 fps
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))

    pygame.display.update()


#mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x < 700 - width - vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 700 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    
    

    

    redrawGameWindow()

pygame.quit()

#dont draw stuff in main loop


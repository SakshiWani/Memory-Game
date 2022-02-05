import pygame, sys, random, time
pygame.mixer.init()

# Variables
WIDTH = 1200
HEIGHT = 800
FPS = 60
BOXSIZE = 200
playtime = 0
mousex = 0
mousey = 0
imagelist = []
twoclicks = []
clickedbox = []
matched = []
fontname = pygame.font.match_font('times')

# Colours
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# Load images
Cone = pygame.image.load(r"Cone.jpeg")
Cube = pygame.image.load(r"Cube.jpeg")
cylinder= pygame.image.load(r"cylinder.jpeg")
donut= pygame.image.load(r"donut.jpeg")
pill= pygame.image.load(r"pill.jpeg")
sphere= pygame.image.load(r"sphere.jpeg")
tile = pygame.image.load(r"tile.jpeg")

# Adding images to a list
imagelist.append(Cone)
imagelist.append(Cube)
imagelist.append(cylinder)
imagelist.append(donut)
imagelist.append(pill)
imagelist.append(sphere)

# Making 6 pairs
imagelist *= 2

def display_text(writetext,textx,texty,size):
    "Loading text to be used in other functions"
    font = pygame.font.Font(fontname,size)
    text = font.render(writetext,True,WHITE,BLACK)
    textRect = text.get_rect()
    textRect.center = (textx, texty)
    SCREEN.blit(text, textRect)
    pygame.display.flip()

def timer(gametime,playtime):
    "Countdown timer"
    timeleft=((playtime+gametime)-pygame.time.get_ticks())//1000
    font = pygame.font.Font(fontname, 50)
    time = font.render(' Time: 0:' + str(timeleft)+"  ",True,WHITE, BLACK)
    timeRect = time.get_rect()
    timeRect.center = (1000,100)
    SCREEN.blit(time, timeRect)
    pygame.display.flip()
    return(timeleft)

def drawallcovers():
    "Drawing all cover tiles"
    tX=0  # tile row x coordinate
    tY=0  # tile row y coordinate
    i=0

    for i in range(0,4):    # Creating 1st row of tiles
        i += 1
        SCREEN.blit(tile, (tX,tY))
        tX+=200
    for i in range(5,9):  # Creating 2nd row of tiles
        i += 1
        SCREEN.blit(tile, (tX-800,tY+200))
        tX+=200
    for i in range(9,13): # Creating 3rd row of tiles
        i += 1
        SCREEN.blit(tile, (tX-1600,tY+400))
        tX+=200 


def displaycover(index):
    "Drawing one cover at a time"
    if(index==0):
        SCREEN.blit(tile, (0,0))
    elif(index==1):
        SCREEN.blit(tile, (200,0))
    elif(index==2):
        SCREEN.blit(tile, (400,0))
    elif(index==3):
        SCREEN.blit(tile, (600,0))
    elif(index==4):
        SCREEN.blit(tile, (0,200))
    elif(index==5):
        SCREEN.blit(tile, (200,200))
    elif(index==6):
        SCREEN.blit(tile, (400,200))
    elif(index==7):
        SCREEN.blit(tile, (600,200))
    elif(index==8):
        SCREEN.blit(tile, (0,400))
    elif(index==9):
        SCREEN.blit(tile, (200,400))
    elif(index==10):
        SCREEN.blit(tile, (400,400))
    elif(index==11):
        SCREEN.blit(tile, (600,400))


    
def displayimage(index):
    "Drawing one image at a time"
    if(index==0):
        SCREEN.blit(imagelist[0], (0,0))
    elif(index==1):
        SCREEN.blit(imagelist[1], (200,0))
    elif(index==2):
        SCREEN.blit(imagelist[2], (400,0))
    elif(index==3):
        SCREEN.blit(imagelist[3], (600,0))
    elif(index==4):
        SCREEN.blit(imagelist[4], (0,200))
    elif(index==5):
        SCREEN.blit(imagelist[5], (200,200))
    elif(index==6):
        SCREEN.blit(imagelist[6], (400,200))
    elif(index==7):
        SCREEN.blit(imagelist[7], (600,200))
    elif(index==8):
        SCREEN.blit(imagelist[8], (0,400))
    elif(index==9):
        SCREEN.blit(imagelist[9], (200,400))
    elif(index==10):
        SCREEN.blit(imagelist[10], (400,400))
    elif(index==11):
        SCREEN.blit(imagelist[11], (600,400))

def box_pos(mousex,mousey):
    "Getting position of clicked box and giving it a number"
    boxx = int(mousex/BOXSIZE)
    boxy = int(mousey/BOXSIZE)
    
    if len(twoclicks)==2:
        del twoclicks[:3]

    if(boxx==0 and boxy==0):
        box = 0
        displayimage(0)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==1 and boxy==0):
        box = 1
        displayimage(1)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==2 and boxy==0):
        box = 2
        displayimage(2)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==3 and boxy==0):
        box = 3
        displayimage(3)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==0 and boxy==1):
        box = 4
        displayimage(4)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==1 and boxy==1):
        box = 5
        displayimage(5)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==2 and boxy==1):
        box = 6
        displayimage(6)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==3 and boxy==1):
        box = 7
        displayimage(7)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==0 and boxy==2):
        box = 8
        displayimage(8)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==1 and boxy==2):
        box = 9
        displayimage(9)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==2 and boxy==2):
        box = 10
        displayimage(10)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    elif(boxx==3 and boxy==2):
        box = 11
        displayimage(11)
        if box not in clickedbox:
            clickedbox.append(box)
        if box not in twoclicks:
            twoclicks.append(box)
    return box

def won(score,playtime,gametime):
    timeleft=(gametime-pygame.time.get_ticks())//1000
    playtime=(60-timeleft)
    score+=timeleft
    SCREEN.fill(BLUE)
    display_text("You Won",600,300,80)
    display_text("Score: "+str(score),600,400,50)
    display_text("Time: 0:"+str(playtime),600,500,50)
    display_text("Play Again",580,700,50)
    display_text("Exit",800,700,50)
    pygame.display.flip()
    pygame.time.wait(1000)
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (mousex>475 and mousex<685) and (mousey>650 and mousey<750):
                    pygame.mixer.music.load(r'click.mp3')
                    pygame.mixer.music.play()
                    timeleft=(gametime-pygame.time.get_ticks())//1000
                    timeleftwin = timeleft
                    playtime=(60-timeleftwin)*1000
                    print(playtime)
                    SCREEN.fill(BLACK)
                    levelone(playtime)
                elif (mousex>760 and mousex<840) and (mousey>675 and mousey<725):
                    pygame.mixer.music.load(r'click.mp3')
                    pygame.mixer.music.play()
                    pygame.quit()
                    quit()

def lost(gametime,playtime):
    SCREEN.fill(RED)
    display_text("You Lost",600,250,80)
    display_text("Play Again",350,500,50)
    display_text("Exit",850,500,50)
    pygame.display.flip()
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (mousex>280 and mousex<420) and (mousey>450 and mousey<550):
                    pygame.mixer.music.load(r'click.mp3')
                    pygame.mixer.music.play()
                    timeleft=(gametime-pygame.time.get_ticks())//1000
                    timeleftwin = timeleft
                    playtime=(60-timeleftwin)*1000
                    SCREEN.fill(BLACK)
                    levelone(playtime)
                elif (mousex>780 and mousex<915) and (mousey>455 and mousey<550):
                    pygame.mixer.music.load(r'click.mp3')
                    pygame.mixer.music.play()
                    pygame.quit()
                    quit()

def levelone(playtime):
    drawallcovers()
    shuffle = random.shuffle(imagelist) # Shuffle the image position      
    score=0
    gametime = 61500
    matched = []
    display_text("Score: "+str(score),1000,200,50)
    running = True
    while(running): #Game loop
        # Events
        for event in pygame.event.get(): # QUIT
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (mousex<800 and mousey<600):
                    pygame.mixer.music.load(r'click.mp3')
                    pygame.mixer.music.play()
                    box_pos(mousex,mousey)
                    if(len(twoclicks)==2):
                        if(imagelist[twoclicks[0]])==(imagelist[twoclicks[1]]):
                            matched.append(imagelist[twoclicks[0]])
                            matched.append(imagelist[twoclicks[1]])
                            score+=20
                            display_text("Score: "+str(score),1000,200,50)
                        else:
                            pygame.mixer.music.load(r'wrong.mp3')
                            pygame.mixer.music.play()
                            cover1 = int(twoclicks[0])
                            cover2 = int(twoclicks[1])
                            displayimage(cover1)
                            displayimage(cover2)
                            pygame.display.flip()
                            pygame.time.wait(450)
                            displaycover(cover1) 
                            displaycover(cover2)
        timer(gametime,playtime)
        timeleft=((gametime+playtime)-pygame.time.get_ticks())//1000
        if(timeleft)<=0:
            lost(gametime,playtime)
        if(len(matched)==12):
            pygame.mixer.music.load(r'Won.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(500)
            won(score,playtime,gametime)
            running = False
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()

def start_game():
    global SCREEN, clock
    pygame.init() #run pygame
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #Window
    pygame.display.set_caption('Memory Game') #Title
    clock = pygame.time.Clock() # Track time
    bg = pygame.Surface((WIDTH,HEIGHT))
    SCREEN.fill(WHITE)
    display_text('Memory Game',600,250,100)
    display_text('Play',350,500,80)
    display_text('Exit',850,500,80)    
    pygame.display.flip()
    running = True
    while(running):
        for event in pygame.event.get(): # QUIT
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                global mousex, mousey
                mousex, mousey = pygame.mouse.get_pos()
                if (mousex>280 and mousex<420) and (mousey>450 and mousey<550):
                    pygame.mixer.music.load(r'click.mp3')
                    pygame.mixer.music.play()
                    SCREEN.fill(BLACK)
                    levelone(playtime)
                elif (mousex>780 and mousex<915) and (mousey>455 and mousey<550):
                    pygame.mixer.music.load(r'click.mp3')
                    pygame.mixer.music.play()
                    pygame.quit()
                    quit()
    pygame.quit()    
start_game()
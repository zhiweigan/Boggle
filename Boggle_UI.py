import pygame
import math
from Boggle_Computer import Computer
from Boggle_Grid import Grid

pygame.init()
display_width = 800
display_height = 600
score = 0
computerscore = 0

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (100, 100, 255)
bright_blue = (200,200,255)
bright_green = (100,255,100)
bright_red = (255,100,100)
possiblewords = ["1234567812345678", "1234567812345678", "1234567812345678","1234567812345678","1234567812345678",
                 "1234567812345678","1234567812345678","1234567812345678","1234567812345678","1234567812345678",
                 "1234567812345678", "1234567812345678", "1234567812345678", "1234567812345678", "1234567812345678",
                 "1234567812345678", "1234567812345678", "1234567812345678", "1234567812345678", "1234567812345678",
                 "1234567812345678", "1234567812345678", "1234567812345678","1234567812345678","1234567812345678",
                 "1234567812345678","1234567812345678","1234567812345678","1234567812345678","1234567812345678",
                 "1234567812345678", "1234567812345678", "1234567812345678","1234567812345678","1234567812345678",
                 "1234567812345678","1234567812345678","1234567812345678","1234567812345678","1234567812345678",
                 "1234567812345678", "1234567812345678", "1234567812345678","1234567812345678","1234567812345678",
                 "1234567812345678","1234567812345678","1234567812345678","1234567812345678","1234567812345678"]

block_color = (53,115,255)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Boggle')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def text_objects_black(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None,args=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None and args != None:
            return action(*args)
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects_black(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitGame():
    pygame.quit()
    quit()

def checkWord(word):
    return True

def instructions():
    instructionsbool = True
    instructionwords = ["Welcome to Boggle!", "", "Score as high as possible!", "Click on letters and string words together!", "", "You have 3 minutes per round" ]

    while instructionsbool:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf, TextRect = text_objects_black("Instructions!", largeText)
        TextRect.center = ((display_width / 2), 130)
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont("comicsansms", 20)
        i = 0
        for words in instructionwords:
            TextSurf, TextRect = text_objects_black(words, smallText)
            TextRect.center = ((display_width / 2), 200 + i * 40)
            i += 1
            gameDisplay.blit(TextSurf, TextRect)

        if button("Back", 20, 20, 100, 50, blue, bright_blue, checkWord, ['quit']):
            instructionsbool = False

        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects_black("Boggle!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,difficultySelect)
        button("Instructions", 300, 450, 200, 50, blue, bright_blue, instructions)
        button("Quit",550,450,100,50,red,bright_red,quitGame)

        pygame.display.update()
        clock.tick(15)

def inbounds(x,y):
    return x >= 0 and x < 4 and y >= 0 and y < 4

def endscreen():
    global possiblewords
    end = True

    while end:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf, TextRect = text_objects_black("Game Over, you have " + str(score) + " points!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2) - 250)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects_black("The computer has " + str(computerscore) + " points!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2) - 150)
        gameDisplay.blit(TextSurf, TextRect)

        if score > computerscore:
            TextSurf, TextRect = text_objects_black("You Win!", largeText)
            TextRect.center = ((display_width / 2), (display_height / 2) - 75)
            gameDisplay.blit(TextSurf, TextRect)
        else:
            TextSurf, TextRect = text_objects_black("You Lose!", largeText)
            TextRect.center = ((display_width / 2), (display_height / 2) - 75)
            gameDisplay.blit(TextSurf, TextRect)

        smallwordText = pygame.font.SysFont("comicsansms", 14)
        textSurf, textRect = text_objects_black("Possible Words:", smallwordText)
        textRect.topleft = (20, display_height / 2 - 60)
        gameDisplay.blit(textSurf, textRect)

        nextrow = -1
        for j in range(len(possiblewords)):
            if j > 50:
                continue
            if j % 10 == 0:
                nextrow += 1
            textSurf, textRect = text_objects_black(possiblewords[j], smallwordText)
            textRect.topleft = (150 * nextrow + 20, 15 * (j % 10) + display_height/2 - 40)
            gameDisplay.blit(textSurf, textRect)


        button("GO Again!", 150, 450, 100, 50, green, bright_green, difficultySelect)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitGame)

        pygame.display.update()
        clock.tick(15)


def difficultySelect():

    difficultySelectBool = True

    while difficultySelectBool:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",70)
        TextSurf, TextRect = text_objects_black("Select Your Difficulty!", largeText)
        TextRect.center = ((display_width/2),(display_height/2)-200)
        gameDisplay.blit(TextSurf, TextRect)

        button("Easy",150,300,100,50,green,bright_green,game, [0.3])
        button("Medium", 300, 300, 200, 50, blue, bright_blue, game, [0.6])
        button("Hard",550,300,100,50,red,bright_red,game, [0.9])

        pygame.display.update()
        clock.tick(15)



def game(difficulty):
    global possiblewords
    global score
    global computerscore
    starttime = pygame.time.get_ticks()
    GridTool = Grid()
    GridTool.makeBoard()
    grid = GridTool.grid
    GridTool.variables()
    GridTool.wordCheck()
    possiblewords = GridTool.possibleWords

    HSIDEMARGIN = 170
    VSIDEMARGIN = 30
    MARGIN = 20
    WIDTH = 100
    HEIGHT = 100
    gameOver = False
    letter = 0

    currentword = [[0 for i in range(4)] for j in range(4)]
    currentwordstring = ""
    dx = [1,1,1,0,-1,-1,-1,0]
    dy = [0,1,-1,1,0,-1,1,-1]
    currentwords = ["Current Words:"]

    while not gameOver:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                if pos[0] - HSIDEMARGIN < 0 or pos[1] - VSIDEMARGIN < 0:
                    continue

                col = (pos[0] - HSIDEMARGIN) // (WIDTH + MARGIN)
                row = (pos[1] - VSIDEMARGIN) // (HEIGHT + MARGIN)
                if row > 3 or col > 3:
                    continue
                # Set that location to one

                if letter == 0:
                    letter += 1
                    currentword[row][col] = letter
                    currentwordstring += grid[row][col].lower()
                else:
                    for i in range(8):
                        if inbounds(row+dy[i], col+dx[i]) and currentword[row+dy[i]][col+dx[i]] == letter:
                            letter += 1
                            currentword[row][col] = letter
                            currentwordstring += grid[row][col].lower()


                #print("Click ", pos, "Grid coordinates: ", row, col, letter)

        gameDisplay.fill(white)

        for i in range(4):
            for j in range(4):
                if currentword[i][j] > 0:
                    pygame.draw.rect(gameDisplay, green,
                                     [(MARGIN + WIDTH) * j + HSIDEMARGIN, (MARGIN + HEIGHT) * i + VSIDEMARGIN,
                                      WIDTH, HEIGHT])
                else:
                    pygame.draw.rect(gameDisplay, black,
                                     [(MARGIN + WIDTH) * j + HSIDEMARGIN, (MARGIN + HEIGHT) * i + VSIDEMARGIN,
                                      WIDTH, HEIGHT])
                gridText = pygame.font.SysFont("comicsansms", 20)
                textSurf, textRect = text_objects(grid[i][j].upper(), gridText)
                textRect.center = ((MARGIN+WIDTH) * j + 220, (MARGIN+WIDTH) * i + 80)
                gameDisplay.blit(textSurf, textRect)

        if len(currentwordstring) > 0 and not currentwordstring in currentwords:
            wordBool = button("CHECK WORD",300,520,200,50,green,bright_green,checkWord, [currentwordstring])

            if wordBool != None:
                currentwords.append(currentwordstring)
                currentword = [[0 for i in range(4)] for j in range(4)]
                currentwordstring = ""
                letter = 0

        nextrow = 0
        for j in range(len(currentwords)):

            if j > 61:
                continue

            if j > 30:
                nextrow = 1
            smallwordText = pygame.font.SysFont("comicsansms", 14)
            textSurf, textRect = text_objects_black(currentwords[j], smallwordText)
            textRect.topleft = (630 * nextrow + 20,  15 * (j%31)+20)
            gameDisplay.blit(textSurf, textRect)


        time = pygame.time.get_ticks() - starttime
        minutes = math.floor(3 - time / (1000*60))
        seconds = math.floor(60 - (time/1000) % 60)


        timeText = pygame.font.SysFont("comicsansms", 25)
        if seconds < 10:
            textSurf, textRect = text_objects_black(str(minutes) + ":0" + str(seconds), timeText)
        else:
            textSurf, textRect = text_objects_black(str(minutes) + ":" + str(seconds), timeText)
        textRect.topleft = (100,520)
        gameDisplay.blit(textSurf, textRect)

        if time >= 10 * 1000:
            gameOver = True


        pygame.display.update()
        clock.tick(15)

    #score calculating and such


    ComputerTool = Computer(possiblewords, currentwords, difficulty)
    ComputerTool.operations()

    score = ComputerTool.playerScore
    computerscore = ComputerTool.computerScore

    endscreen()



game_intro()


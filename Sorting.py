from math import dist
from random import shuffle
import pygame as pg
import sys
pg.init()

screenWidth, screenHeight = 1800, 1000

WIN = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("Sorting Algorithms")

WHITE = (255, 255, 255)
PINK = (255, 150, 185)
BLUE = (47, 149, 196)
DARKBLUE = (25, 28, 64)
FPS = 60

def checkQuit():
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()

def generateData(slider):
    data = list(range(1, slider.val + 1))
    shuffle(data)
    return data

def draw(lst, i=[]):
    WIN.fill(DARKBLUE)

    Xinterval = screenWidth / (len(lst) + 1)
    Xscale = Xinterval/1.25
    Yscale = (screenHeight*0.9) / max(lst)

    for index, num in enumerate(lst):
        
        width = Xscale
        height = num * Yscale

        left = (index+1) * Xinterval - (width/2)
        top = screenHeight - height

        if index in i:
            pg.draw.rect(WIN, PINK, (left, top, width, height))
        else:
            pg.draw.rect(WIN, BLUE, (left, top, width, height))

    pg.display.update()

def bubble_sort(lst):
    
    for num in range(200):
        draw(lst)
    i = 0
    switch = False

    while True:

        checkQuit()
        pg.time.delay(timeSlide.val)
        x = lst[i]
        y = lst[i+1]

        if x > y:
            lst[i] = y
            lst[i+1] = x
            switch = True

        i += 1
        if i == len(lst) - 1:
            if switch == False:
                break
            else:
                i = 0
                switch = False

        draw(lst, [i])
    for num in range(200):
        draw(lst)
def insertion_sort(lst):
    
    for num in range(200):
        draw(lst)
    for i in range(0, len(lst)):
        bigNum = lst[i]
        madeChange = False

        for j in range(i, 0, -1):
            j -= 1

            if lst[j] > bigNum:
                lst[j+1] = lst[j]
                madeChange = True

                if j == 0:
                    lst[0] = bigNum
            
                pg.time.delay(timeSlide.val)
                draw(lst, [j])

            elif madeChange == True:
                lst[j+1] = bigNum
                break

            checkQuit()
    for num in range(200):
        draw(lst)
def selection_sort(lst):

    for num in range(200):
        draw(lst)
    for i in range(len(lst)):
        minimumIndex = i
        minimum = lst[i]

        for j in range(len(lst)-i):
            checkQuit()
            j += i

            if lst[j] < minimum:
                minimumIndex = j
                minimum = lst[j]

            pg.time.delay(timeSlide.val)
            draw(lst, [minimumIndex, j])

        lst[minimumIndex] = lst[i]
        lst[i] = minimum

    for num in range(200):
        draw(lst)

# ~~~~~~~~~~~~~~~~~~~~~ WINDOW ~~~~~~~~~~~~~~~~~~~~~

clock = pg.time.Clock()
sec = 0

class Button():
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color = PINK
    
    def draw(self):
        # Rectangle
        x, y = pg.mouse.get_pos()
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            self.color = WHITE
        else:
            self.color = PINK

        # Text
        myfont = pg.font.SysFont('Calibri Bold', 80)
        textsurface = myfont.render(self.text, False, BLUE)

        w, h = myfont.size(self.text)
        WIN.blit(textsurface,((self.w - w)/2 + self.x, (self.h - h)/2 + self.y))


        pg.draw.rect(WIN, self.color, (self.x, self.y, self.w, self.h), 10, 5)
        

    def hover(self):
        x, y = pg.mouse.get_pos()
        return self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h
            
bubble = Button(90, 150, 480, 200, "Bubble Sort")
insertion = Button(660, 150, 480, 200, "Insertion Sort")
selection = Button(1230, 150, 480, 200, "Selection Sort")

class Slider():
    def __init__(self, x, y, rad, val):
        self.x = x
        self.y = y
        self.rad = rad
        self.val = val
        self.color = PINK
        self.inSlide = False
    
    def draw(self):
        x, y = pg.mouse.get_pos()
        if dist((x, y), (self.x, self.y)) <= self.rad or self.inSlide:
            self.color = WHITE
        else:
            self.color = PINK


        # Text
        myfont = pg.font.SysFont('Calibri Bold', 50)
        textsurface = myfont.render(str(self.val), False, BLUE)
        w, h = myfont.size(str(self.val))

        WIN.blit(textsurface, (self.x - (w/2), self.y - 100))
        
        pg.draw.circle(WIN, BLUE, (self.x, self.y), self.rad)
        pg.draw.circle(WIN, self.color, (self.x, self.y), self.rad, 10)
        
    def hover(self):
        x, y = pg.mouse.get_pos()
        return dist((x, y), (self.x, self.y)) <= self.rad

dataSlide = Slider(480, 600, 40, 30)
timeSlide = Slider(585, 800, 40, 10)
mouseDown = False

generateData(dataSlide)

while True:
    clock.tick(FPS)
    sec += 1/FPS
    WIN.fill(DARKBLUE)

    bubble.draw()
    insertion.draw()
    selection.draw()

    pg.draw.line(WIN, PINK, (300, 600), (1700, 600), 10)
    pg.draw.line(WIN, PINK, (300, 800), (1700, 800), 10)

    # Text
    myfont = pg.font.SysFont('Calibri Bold', 60)
    textsurface = myfont.render("Data", False, BLUE)
    WIN.blit(textsurface, (100, 555))
    textsurface = myfont.render("Points", False, BLUE)
    WIN.blit(textsurface, (100, 600))
    textsurface = myfont.render("Time", False, BLUE)
    WIN.blit(textsurface, (100, 755))
    textsurface = myfont.render("Delay", False, BLUE)
    WIN.blit(textsurface, (100, 800))
    
    dataSlide.draw()
    timeSlide.draw()

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:

            if bubble.hover():
                data = generateData(dataSlide)
                bubble_sort(data)              
            elif insertion.hover():
                data = generateData(dataSlide)
                insertion_sort(data)          
            elif selection.hover():
                data = generateData(dataSlide)
                selection_sort(data)
            elif dataSlide.hover():
                dataSlide.inSlide = True
            elif timeSlide.hover():
                timeSlide.inSlide = True

        if event.type == pg.MOUSEBUTTONUP:
            dataSlide.inSlide = False
            timeSlide.inSlide = False

    if dataSlide.inSlide:
        if pg.mouse.get_pressed()[0]:
            x, y = pg.mouse.get_pos()
            if x < 300:
                x = 300
            elif x > 1700:
                x = 1700
            dataSlide.x = x
            dataSlide.val = round((dataSlide.x - 300) / 7.17948717949 + 5)

    if timeSlide.inSlide:
            if pg.mouse.get_pressed()[0]:
                x, y = pg.mouse.get_pos()
                if x < 300:
                    x = 300
                elif x > 1700:
                    x = 1700
                timeSlide.x = x                        
                timeSlide.val = (timeSlide.x - 300) // 28

    checkQuit()
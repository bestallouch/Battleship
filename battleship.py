import pygame
import sys
import math
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

screen = pygame.display.set_mode((1600, 800))

class spot:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.h = 0
        self.closed = False
        self.obs = False
        self.ship = False
        self.hit = False

    def show(self, color, st):
        if self.closed == False :
            pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
            pygame.display.update()
            
#    def sink(self,grid):
#        i = self.i
#        j = self.j
#        a = grid[i][j].hit
#        for k in range (14,22):
#            for r in range (1,10):
#                if grid[i][j].hit == True and :
#            print('wew')
#            grid[i][j].show(grey,0) 
#        else:
#            pass

cols = 24
grid = [0 for i in range(cols)]
row = 12
openSet = []
closedSet = []
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
yellow = (255, 255, 0)
purple = (160, 32, 240)
black = (0, 0, 0)
white = (255, 255, 255)
w = 1600 / cols
h = 800 / row
cameFrom = []


for i in range(cols):
    grid[i] = [0 for i in range(row)]

for i in range(cols):
    for j in range(row):
        grid[i][j] = spot(i, j)

for i in range(cols):
    for j in range(row):
        grid[i][j].show((255, 255, 255), 1)

for i in range(0,row):
    grid[0][i].show(grey, 0)
    grid[0][i].obs = True
    grid[cols-1][i].obs = True
    grid[cols-1][i].show(grey, 0)
    grid[11][i].obs = True
    grid[11][i].show(grey, 0)
    grid[12][i].obs = True
    grid[12][i].show(grey, 0)
    grid[13][i].obs = True
    grid[13][i].show(grey, 0)
for i in range(0,cols):
    grid[i][row-1].show(grey, 0)
    grid[i][0].show(grey, 0)
    grid[i][0].obs = True
    grid[i][row-1].obs = True
    
def genship(x,y,l):
    d = random.randint(0,3)
    if d==0:
        return x+l, y
    if d==1:
        if x-l>13:
            return x-l, y
        else:
            return x+l, y
    if d==2:
        return x, y+l
    if d==3:
        if y-l>0:
            return x, y-l
        else:
            return x, y+l
        
def placeship(grid, x1, y1, x2, y2):
    for i in range(min(x1, x2), max(x1, x2)+1):
        if grid[i][y1].obs == True:
            return False
    for i in range(min(y1, y2), max(y1, y2)+1):
        if grid[x1][i].obs == True:
            return False
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            grid[x1][i].ship = True
            grid[x1][i].obs = True
            grid[x1-1][i].obs = True
            grid[x1+1][i].obs = True
            grid[x1][i-1].obs = True
            grid[x1][i+1].obs = True
            grid[x1][i].show(red, 0)
    else:
        for i in range(min(x1, x2), max(x1, x2)+1):
           grid[i][y1].ship = True
           grid[i][y1].obs = True
           grid[i][y1-1].obs = True           
           grid[i][y1+1].obs = True
           grid[i-1][y1].obs = True
           grid[i+1][y1].obs = True
           grid[i][y1].show(red, 0)
    return True
           
ships2place = [3,2,2,1,1,1,0,0,0,0]

while ships2place !=[]:
    x1 = random.randint(14,23)
    y1 = random.randint(1,10)
    print(ships2place, x1, y1)
    l = ships2place.pop(0)
    gen = genship(x1, y1, l)
    x2 = gen[0]
    y2 = gen[1]
#    print('x2', x2, 'y2', y2)
    place =  placeship(grid,x1, y1, x2, y2)
    print(place)
    if place == False:
        ships2place.insert(0, l)

def mousePress(x):
    t = x[0]
    w = x[1]
    g1 = t // (1600 // cols)
    g2 = w // (800 // row)
    acess = grid[g1][g2]
    if acess.ship == True and 0<g1<11 and 0<g2<11:
        acess.ship = False
        acess.show(black, 0)
        acess.show(white, 1)
    elif acess.obs == False and 0<g1<11 and 0<g2<11:
        acess.ship = True
        acess.show(green, 0)


loop = True
while loop:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break
user_ships = 0
user_ships_neighbours = 0

for i in range(1, 11):
    for j in range(1,11):
        if grid[i][j].ship == True:
            user_ships += 1
            if grid[i+1][j].ship == True:
                user_ships_neighbours += 1
            if grid[i-1][j].ship == True:
                user_ships_neighbours += 1
            if grid[i][j+1].ship == True:
                user_ships_neighbours += 1
            if grid[i][j-1].ship == True:
                user_ships_neighbours += 1
print(user_ships)
print(user_ships_neighbours)
#if user_ships != 20 or user_ships_neighbours !=20:
#    Tk().wm_withdraw()
#    result = messagebox.askokcancel('Warning', ('Unfortunatelly, you placed ships wrong, \n would you like to restart the game?'))
#    if result == True:
#        os.execl(sys.executable,sys.executable, *sys.argv)
#    else:
#        pygame.quit()



shot = False
guess_hist = []
pos_hist = []
user_hits = 0
ai_hits = 0
       
def mousePress(x, status, user_hits):
    t = x[0]
    w = x[1]
    status = False
    g1 = t // (1600 // cols)
    g2 = w // (800 // row)
    acess = grid[g1][g2]
    if pos_hist.count((g1,g2)) == 0:
        if acess.ship == False and 23>g1>13 and 11>g2>0:
            pos_hist.append((g1,g2))
            acess.show(blue, 0)
            status = True
            return status, user_hits
        if acess.ship == True and 23>g1>13 and 11>g2>0:
            pos_hist.append((g1,g2))
            acess.show(yellow, 0)
            acess.hit = True
            user_hits += 1
            status = False
            return status, user_hits
    return status, user_hits

loop = True
while loop:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                shot, user_hits = mousePress(pos, shot, user_hits)
                print(shot)
#                print(pos_hist)
                if shot == True:
                    guess_x = random.randint(1, 10)
                    guess_y = random.randint(1, 10)
                    if guess_hist.count((guess_x,guess_y)) == 0:
                        guess_hist.append((guess_x,guess_y))
    #                    print(guess_hist)
                        if grid[guess_x][guess_y].ship == True:
                            grid[guess_x][guess_y].show(purple,0)
                            grid[guess_x][guess_y].hit = True
                            ai_hits +=1
                        else:
                            grid[guess_x][guess_y].show(blue,0)
            except AttributeError:
                pass
#            print(ai_hits)
        elif event.type == pygame.KEYDOWN or user_hits == 20 or ai_hits == 20:
            try:
                if event.key == pygame.K_SPACE :
                    guess_hist = []
                    pos_his = []
                    loop = False
                    break
            except AttributeError:
                pass
            guess_hist = []
            pos_his = []
            loop = False
            break 
            
Tk().wm_withdraw()
if user_hits == 20:
    result = messagebox.askokcancel('Game Finished', ('The game finished, player won, \n would you like to rerun the game?'))
elif ai_hits == 20:
    result = messagebox.askokcancel('Game Finished', ('The game finished, AI won, \n would you like to rerun the game?'))
else:
    result = messagebox.askokcancel('Game Finished', ('The game was canceled, \n would you like to rerun the game?'))
if result == True:
    os.execl(sys.executable,sys.executable, *sys.argv)
else:
    pygame.quit()
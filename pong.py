# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

pong_ai = 1

screen_width = 600
screen_height = 500
x_vec_base = 4.0
y_vec_base = 2.0

#player
player_move_speed = 10
player1_x = 50
player2_x = 540
player_width = 70

class Circle:
    def __init__(self):
        self.x = 200
        self.y = 200
        self.x_vec = x_vec_base
        self.y_vec = y_vec_base

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def drawCircle(self, pygame, screen):
        pygame.draw.ellipse(screen,(200,200,0),(self.x-5,self.y-5,10,10),3)

    def update(self, player1_y, player2_y):
        self.y += self.y_vec
        self.x += self.x_vec
        if (player1_y < self.y < player1_y+player_width and player1_x < self.x < player1_x+10) or (player2_y < self.y < player2_y+player_width and player2_x-10 < self.x < player2_x):
            if self.x_vec==x_vec_base:
                self.x_vec = -x_vec_base
            elif self.x_vec == -x_vec_base:
                self.x_vec = x_vec_base
        if self.y<0:
            self.y_vec = y_vec_base
        elif self.y>screen_height:
            self.y_vec = -y_vec_base

class playerManager:
    def __init__(self):
        self.w = 0
        self.s = 0
        self.i = 0
        self.k = 0
        self.player1_y = 50
        self.player2_y = 50

    def get1y(self):
        return self.player1_y

    def get2y(self):
        return self.player2_y

    def update(self):
        if self.w==1:
            self.player1_y -= player_move_speed
        if self.s==1:
            self.player1_y += player_move_speed
        if pong_ai==0:
            if self.i==1:
                self.player2_y -= player_move_speed
            if self.k==1:
                self.player2_y += player_move_speed
        elif pong_ai==1:
            self.player2_y = circle.gety()-player_width/2

    def updateInput(self, type):
        if type=='w':
            if self.w==1:
                self.w = 0
            elif self.w==0:
                self.w = 1
        if type=='s':
            if self.s==1:
                self.s = 0
            elif self.s==0:
                self.s = 1
        if type=='i' and pong_ai==0:
            if self.i==1:
                self.i = 0
            elif self.i==0:
                self.i = 1
        if type=='k' and pong_ai==0:
            if self.k==1:
                self.k = 0
            elif self.k==0:
                self.k = 1


circle = Circle()
players = playerManager()

def drawPlayer1(pygame, screen, y):
    pygame.draw.rect(screen,(100,0,0),Rect(player1_x,y,10,player_width),5)

def drawPlayer2(pygame, screen, y):
    pygame.draw.rect(screen,(0,0,100),Rect(player2_x,y,10,player_width),5)

def updateComponents(pygame, screen, y1, y2):
    drawPlayer1(pygame, screen, y1)
    drawPlayer2(pygame, screen, y2)
    circle.update(y1, y2)
    circle.drawCircle(pygame, screen)

def main():
    mouse_x = 0
    mouse_y = 0

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("pong")

    while (1):
        screen.fill((0,0,0))
#        updateComponents(pygame, screen, mouse_y)
        updateComponents(pygame, screen, players.get1y(), players.get2y())
        players.update()

        pygame.time.wait(50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == K_w:
                    players.updateInput('w')
                if event.key == K_s:
                    players.updateInput('s')
                if event.key == K_i:
                    players.updateInput('i')
                if event.key == K_k:
                    players.updateInput('k')

            if event.type == KEYUP:
                if event.key == K_w:
                    players.updateInput('w')
                if event.key == K_s:
                    players.updateInput('s')
                if event.key == K_i:
                    players.updateInput('i')
                if event.key == K_k:
                    players.updateInput('k')

            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

if __name__ == "__main__":
    main()
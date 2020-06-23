#work in progress
#this is a basic tictactoe game in pygame Version3

import pygame
import time

background = (0,0,0)
white_color = (255,255,255)
blue_color = (0,0,255)
red_color = (255,0,0)
position_location = [[(213,120),(639,120),(1065,120)],[(213,360),
(640,360),(1065,360)],[(213,600),(639,600),(1065,600)]]

class Game: 
    '''
    def __init__(self,running,player_val,message,win,tie,
    screen,clock,position_stored):
        self.running = True
        self.player_val = 1
        self.message = ""
        self.win = False
        self.tie = False
        self.screen = pygame.display.set_mode((1280,820))
        self.clock = pygame.time.Clock()
        self.position_stored = [[0 for x in range(3)] for y in range(3)]
    '''
    #def setup(self):
        

    def draw(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Tic Tac Toe!")
        screen = self.screen
        draw_game_board(self)


    def draw_game_board(self):
        screen = self.screen
        screen.fill(background)
         #vertical lines
        pygame.draw.line(screen,white_color,(426,0),(426,720),2)
        pygame.draw.line(screen,white_color,(853,0),(853,720),2)
        #horizontal lines
        pygame.draw.line(screen,white_color,(0,240),(1280,240),2)
        pygame.draw.line(screen,white_color,(0,480),(1280,480),2)
        pygame.draw.line(screen,white_color,(0,720),(1280,720),2)
        #borderlines
        pygame.draw.line(screen,white_color,(0,0),(1280,0),2)
        pygame.draw.line(screen,white_color,(0,800),(1280,800),2)
        pygame.draw.line(screen,white_color,(0,0),(0,800),2)
        pygame.draw.line(screen,white_color,(1280,0),(1280,800),6)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.running = False

    def main(self,running,update,draw):
        while self.running == True:
            self.update()
            self.draw()

main = Game.main
main(0,1,2,3)
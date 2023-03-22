import pygame
import sys
from settings import *
from main import Game
from main1 import Main

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
button_rect = pygame.Rect(250, 150, 100, 50)
button_color = (255, 255, 255)

button1_rect = pygame.Rect(250, 250, 100, 50)
button1_color = (255, 255, 255)

button2_rect = pygame.Rect(250, 350, 100, 50)
button2_color = (255, 255, 255)

pygame.draw.rect(screen, button_color, button_rect)
pygame.draw.rect(screen, button1_color, button1_rect)
pygame.draw.rect(screen, button2_color, button2_rect)

clock = pygame.time.Clock()
pygame.display.update()
clock.tick(60)

def run_other_file():
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
	
            screen.fill('grey')
            game.run()

            pygame.display.update()
            clock.tick(60)
    
def run_other_file1():
    pygame.display.update()
    main = Main()
    main.run()
    
def destroy():
    pygame.quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                run_other_file()
            if button1_rect.collidepoint(event.pos):
                run_other_file1()
            if button2_rect.collidepoint(event.pos):
               pygame.quit()
    
   
    
    


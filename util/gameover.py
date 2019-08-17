import pygame

def gameOver(tank,home):
    if tank.hp <= 0 or home.hp <= 0:
        pygame.display.quit()


import random
import pygame

#Part A
pygame.init()
window = pygame.display.set_mode()
screen_size = window.get_size()
dimmensions1 = screen_size[0]/2, screen_size[1]/2
x1 = screen_size[0]/2
y1 = screen_size[1]/2
x2 = screen_size[0]
y2 = screen_size[1]
window.fill("blue")
pygame.draw.circle(window, "black", dimmensions1, y1) 
pygame.draw.circle(window, "pink", dimmensions1, y1 - 5)
pygame.draw.line(window, "black", (x1,0),(x1, y2), 3)
pygame.draw.line(window, "black", (0,y1),(x2, y1), 3)
pygame.display.flip()
pygame.time.wait(2000)


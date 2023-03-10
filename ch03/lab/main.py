import random
import pygame
import math


#Part A
pygame.init()
window = pygame.display.set_mode((800, 800))
screen_size = window.get_size()
center_of_screen = (screen_size[0]/2, screen_size[1]/2)
half_of_width = screen_size[0]/2
half_of_height = screen_size[1]/2
width = screen_size[0]
height = screen_size[1]
window.fill("blue")
pygame.draw.circle(window, "black", center_of_screen, half_of_height) 
pygame.draw.circle(window, "pink", center_of_screen, half_of_height - 5)
pygame.draw.line(window, "black", (half_of_width,0),(half_of_width, height), 3)
pygame.draw.line(window, "black", (0,half_of_height),(width, half_of_height), 3)


#Part B
for i in range(10): 
    dart1coordx = random.randrange(0, width)
    dart1coordy = random.randrange(0, height)
    dart2coordx = random.randrange(0, width)
    dart2coordy = random.randrange(0, height)
    dart1_distance = math.hypot(dart1coordx - half_of_width, dart1coordy - half_of_height)
    dart2_distance = math.hypot(dart2coordx - half_of_width, dart2coordy - half_of_height)
    is_in_circle_dart_1 = (dart1_distance <= half_of_width)
    is_in_circle_dart_2 = (dart2_distance <= half_of_width)
    if (is_in_circle_dart_1):
        pygame.draw.circle(window, "red", [dart1coordx, dart1coordy], 10)
    else:
        pygame.draw.circle(window, "purple", [dart1coordx, dart1coordy], 10)
        
    if (is_in_circle_dart_2):
        pygame.draw.circle(window, "green", [dart2coordx, dart2coordy], 10)
    else:
        pygame.draw.circle(window, "yellow", [dart2coordx, dart2coordy], 10)
pygame.display.flip()
pygame.time.wait(5000)

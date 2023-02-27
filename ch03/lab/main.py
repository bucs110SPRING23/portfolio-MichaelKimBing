import random
import pygame

#Part A
pygame.init()
window = pygame.display.set_mode()
screen_size = window.get_size() #ask if it has to be a full screen or not
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

#Part B
for i in range(10):
    dart1coord = random.randrange(1, )
    dart2coord = random.randrange(1, )
    pygame.draw.circle(screen, "red", dart1coord, 50)
    pygame.draw.circle(screen, "green", dart2coord, 50)
    
distance_from_center = math.hypot(x1-x2, y1-y2)
is_in_circle = distance_from_center <= width/2 


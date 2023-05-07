import pygame
pygame.init()
screen = pygame.display.set_mode()
screen.fill("white")
screen_size = screen.get_size()
dimmensions1 = screen_size [0]/2, screen_size[1]/2
dimmensions2 = screen_size [0]/2, screen_size[1]/3
dimmensions3 = screen_size [0]/2, screen_size[1]/1.35
pygame.draw.circle(screen, "black", dimmensions3, 200)
pygame.display.flip()
pygame.draw.circle(screen, "white", dimmensions3, 190)
pygame.display.flip()
pygame.draw.circle(screen, "black", dimmensions1, 125)
pygame.display.flip()
pygame.draw.circle(screen, "white", dimmensions1, 115)
pygame.display.flip()
pygame.draw.circle(screen, "black", dimmensions2, 75)
pygame.display.flip()
pygame.draw.circle(screen, "white", dimmensions2, 65)
pygame.display.flip()
pygame.time.wait(1000)
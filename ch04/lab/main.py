import random
import pygame
import math


pygame.init()
window = pygame.display.set_mode((800, 800))
screen_size = window.get_size()
center_of_screen = (screen_size[0]/2, screen_size[1]/2)
half_of_width = screen_size[0]/2
half_of_height = screen_size[1]/2
width = screen_size[0]
height = screen_size[1]
amount_of_throws_hits_in_circle_player1 = 1
amount_of_throws_hits_in_circle_player2 = 1
turns = 1

window.fill("blue") 
hitboxes = {
    "red": pygame.Rect(screen_size[0]/6.4, screen_size[1]/2.85, 280, 280),
    "green":pygame.Rect(screen_size[0]/1.67, screen_size[1]/2.85, 280, 280)
}
main_colors = {
    "red": (200, 0, 0),
    "green": (0, 200, 0)
}
highlight_colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0)
}
font = pygame.font.Font(None, 60)
text1 = font.render("Guess Who Wins The Dart Game!", True, "black") 
text2 = font.render("Please Select Your Player", True, "black")
text3 = font.render("Player 1", True, "black")
text4 = font.render("Player 2", True, "black")

done = False
while not done:
    window.fill("blue")
    pygame.draw.rect(window, main_colors["green"], hitboxes["green"])
    pygame.draw.rect(window, main_colors["red"], hitboxes["red"])
    window.blit(text1, (80, half_of_height/3))
    window.blit(text2, (200, half_of_height/2))
    window.blit(text3, (screen_size[0]/4.5, screen_size[1]/2.1))
    window.blit(text4, (screen_size[0]/1.48, screen_size[1]/2.1))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            turns = turns - 1
            if hitboxes["red"].collidepoint(event.pos):
                pygame.draw.rect(window, highlight_colors["red"], hitboxes["red"])
                window.blit(text3, (screen_size[0]/4.5, screen_size[1]/2.1))
                result = "red"
            done = True
            if hitboxes["green"].collidepoint(event.pos):
                pygame.draw.rect(window, highlight_colors["green"], hitboxes["green"])
                window.blit(text4, (screen_size[0]/1.48, screen_size[1]/2.1))
                result = "green"
            done = True
    pygame.display.update()


window.fill("blue")
pygame.draw.circle(window, "black", center_of_screen, half_of_height) 
pygame.draw.circle(window, "pink", center_of_screen, half_of_height - 5)
pygame.draw.line(window, "black", (half_of_width,0),(half_of_width, height), 3)
pygame.draw.line(window, "black", (0,half_of_height),(width, half_of_height), 3)

for i in range(10): 
    player1coordx = random.randrange(0, width)
    player1coordy = random.randrange(0, height)
    player2coordx = random.randrange(0, width)
    player2coordy = random.randrange(0, height)
    dart1_distance = math.hypot(player1coordx - half_of_width, player1coordy - half_of_height)
    dart2_distance = math.hypot(player2coordx - half_of_width, player2coordy - half_of_height)
    is_in_circle_dart_1 = (dart1_distance <= half_of_width)
    is_in_circle_dart_2 = (dart2_distance <= half_of_width)
    
    if (is_in_circle_dart_1):
        pygame.draw.circle(window, "red", [player1coordx, player1coordy], 10)
        amount_of_throws_hits_in_circle_player1 += 1
    else:
        pygame.draw.circle(window, "purple", [player1coordx, player1coordy], 10)
        
    if (is_in_circle_dart_2):
        pygame.draw.circle(window, "green", [player2coordx, player2coordy], 10)
        amount_of_throws_hits_in_circle_player2 += 1
    else:
        pygame.draw.circle(window, "yellow", [player2coordx, player2coordy], 10)
    pygame.time.wait(1000)
    pygame.display.flip()


font = pygame.font.Font(None , 48)
if amount_of_throws_hits_in_circle_player1 > amount_of_throws_hits_in_circle_player2:
    if (result == "red"):
        text = font.render("Correct! Player 1 Wins!", True, "black")
        text1 = font.render(f"Player 1 Scores:{amount_of_throws_hits_in_circle_player1}", True, "black")
        text2 = font.render(f"Player 2 Scores:{amount_of_throws_hits_in_circle_player2}", True, "black")
    else:
        text = font.render("Incorrect! Player 1 Wins!", True, "black")
        text1 = font.render(f"Player 1 Scores:{amount_of_throws_hits_in_circle_player1}", True, "black")
        text2 = font.render(f"Player 2 Scores:{amount_of_throws_hits_in_circle_player2}", True, "black")
elif amount_of_throws_hits_in_circle_player1 < amount_of_throws_hits_in_circle_player2:
    if (result == "green"):
        text = font.render("Correct! Player 2 Wins!", True, "black")
        text1 = font.render(f"Player 1 Scores:{amount_of_throws_hits_in_circle_player1}", True, "black")
        text2 = font.render(f"Player 2 Scores:{amount_of_throws_hits_in_circle_player2}", True, "black")
    else:
        text = font.render("Incorrect! Player 2 Wins!", True, "black")
        text1 = font.render(f"Player 1 Scores:{amount_of_throws_hits_in_circle_player1}", True, "black")
        text2 = font.render(f"Player 2 Scores:{amount_of_throws_hits_in_circle_player2}", True, "black")
else:
    text = font.render("Tie Game!", True, "black")
    text1 = font.render(f"Player 1 Scores:{amount_of_throws_hits_in_circle_player1}", True, "black")
    text2 = font.render(f"Player 2 Scores:{amount_of_throws_hits_in_circle_player2}", True, "black")
window.blit(text, (half_of_width, half_of_height))
window.blit(text1, (half_of_width, half_of_height/1.5))
window.blit(text2, (half_of_width, half_of_height/1.3))

pygame.display.flip()
pygame.time.wait(5000)




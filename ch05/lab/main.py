import pygame


#Part A
def threenp1(n):
    count = 0
    while n > 1.0:
        count +=1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2,upper_limit+1):
        a = threenp1(i)
        objs_in_sequence[i] = a
    return objs_in_sequence
    

#Testing Part A
# def main():
#     upper_limit = int(input("Enter a Limit Number:"))
#     threeplus1_iters_dict = threenp1range(upper_limit)
#     print(threeplus1_iters_dict)
    
# main()


#Part B:
def graph_coordinates(threeplus1_iters_dict):
    pygame.init()
    window = pygame.display.set_mode((900,600))
    window.fill("white")
    tuple_threeplus1_iters_dict = [(n,iters) for n, iters in threeplus1_iters_dict.items()]


    pygame.draw.lines(window, "black", True, tuple_threeplus1_iters_dict)

    new_display = pygame.transform.flip(window, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 1.5, height * 1.5))
    window.blit(new_display, (0,0))

    iters_threeplus1_iters_dict = [tup[1] for tup in tuple_threeplus1_iters_dict]
    max_so_far = iters_threeplus1_iters_dict[1]
    for i in range(len(iters_threeplus1_iters_dict)):
        if iters_threeplus1_iters_dict[i] > max_so_far:
            max_so_far = iters_threeplus1_iters_dict[i]

    #If you want both the n:iters:
    # max_so_far = threeplus1_iters_dict[1]
    # for i in range(len(threeplus1_iters_dict)):
    #     if iters_threeplus1_iters_dict[i] > max_so_far:
    #         max_so_far = threeplus1_iters_dict[i]

    font = pygame.font.Font(None,36)
    msg = font.render(f"This is the Max Value from the 3n+1 function:{max_so_far}",True, "black")
    window.blit(msg,(20,20))

def main():
    upper_limit = int(input("Enter a Limit Number:"))
    threeplus1_iters_dict = threenp1range(upper_limit)
    graph_coordinates(threeplus1_iters_dict)
    pygame.display.flip()
    pygame.time.wait(10000)

main()
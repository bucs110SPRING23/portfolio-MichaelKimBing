
#Part 1
star_pyramid_input = int(input("Please Input the Desired Number of Stars:"))

def star_pyramid():
   for _ in range(star_pyramid_input):
      print("*"*(_ + 1))

star_pyramid()

reverse_star_pyramid_input = int(input("Please Input the Desired Number of Stars:"))

def rstar_pyramid():
   max = reverse_star_pyramid_input
   for _ in range(reverse_star_pyramid_input, 0, -1):
      print("*"*_)

rstar_pyramid()
   


   
import random
numbers =  random.randint(1,10)

for i in range(3):
    response = int(input("Please guess a number between 1-10: "))
    if numbers == response:
        print("correct!")
        break
    elif numbers > response:
        print("Too Low")
    elif numbers < response:
        print("Too High")

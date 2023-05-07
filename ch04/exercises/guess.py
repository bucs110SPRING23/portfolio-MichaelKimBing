import random
numbers =  random.randint(1,1000)

guesses = []
amount_of_guesses = 1
while True: 
    response = int(input("Please guess a number between 1-1000: "))
    if numbers == response:
        print("correct!")
        break
    elif numbers > response:
        print("Too Low")
    elif numbers < response:
        print("Too High")
    amount_of_guesses += 1
   
print("This is how many times you guessed:", str(amount_of_guesses))
print("Correct Answer:", numbers)
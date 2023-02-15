###Fizzbuzz
# loop through a range of values supplied by the user
# for each value in the range
# if the value is divisible by 3, print "fizz"
# if the value is divisible by 5, print "buzz"
# if the value is divisible by 3 and 5, print "fizz buzz"

a = int(input("Please add number to list:"))
for i in range(a+1):
    print("number:", i)
    if not i%3 and i%5:
        print("fizz buzz")
    elif not i % 3:
        print("fizz")
    elif not i % 5:
        print("buzz")
def multiplies_by_two(num1, num2):
    value = 0 
    for i  in range(int(num2)):
        value = value + num1
    return value

def exponent(num1, num2):
    value = 1
    for i  in range(int(num2)):
        value = value*num1
    return value

def square(bob):
    return multiplies_by_two(bob, bob)

num1 = 5
num2 = 9
print(multiplies_by_two(num1, num2))
print(exponent(num1, num2))
print(square(num1))







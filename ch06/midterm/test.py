def explosion_function(w):
    while w >= 0:
        if w == 0:
            w = 0
        elif 1 <= w <= 3:
            w = int(50000)
        elif 4 <= w <= 6:
            w = int(500000)
        elif 7 <= w <= 10:
            w = int(50000000* w)
        else:
            w = int(550000000)         
        return w

def explosion_function_range(intensity):
    coords_in_sequence = {}
    for i in range(0,intensity+1):
        a = explosion_function(i)
        coords_in_sequence[i] = a
    return coords_in_sequence


def main():
    intensity = int(input("Enter Explosion Intensity:"))
    numbers_of_people = explosion_function_range(intensity)
    print(numbers_of_people)
    print(0)

main()
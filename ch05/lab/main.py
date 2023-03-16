


#Part A
def threenp1(n):
    count =  0
    while n > 1.0:
        count +=1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3 * n + 1)
    return count

def threenp1range(n,upper_limit):
    n = 2
    objs_in_sequence = {}
    for i in range(3, upper_limit):
        threenp1()
        objs_in_sequence.append(threenp1)
    return n, upper_limit

def main():
    upper_limit = int(input("Enter a Limit Number:"))
    threeplus1_itrs_dict = threenp1range()
    print(threeplus1_itrs_dict)

main()

# if __name__ == "__main__":
# main()



        
        
    




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

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for _ in range(3, upper_limit):
        threenp1()
        threenplus1_iters_dict = {}
    return objs_in_sequence

def main():
    threenp1range()

if __name__ == "__main__":
    main()



        
        
    

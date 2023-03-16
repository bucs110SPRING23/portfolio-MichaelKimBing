


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
    n = int(input("Enter A Number:"))
    iters = threenp1(n)
    objs_in_sequence = {n:iters}
    return objs_in_sequence

def main():
    for i in range(3, upper_limit):
        threenp1()
        threenplus1_iters_dictionary["n"] = "iterations"
    return upper_limit

main()

# if __name__ == "__main__":
# main()



        
        
    

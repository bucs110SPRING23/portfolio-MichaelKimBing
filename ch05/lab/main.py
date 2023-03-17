


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
    for i in range(2,upper_limit):
        a = threenp1(i)
        objs_in_sequence[i] = a
    return objs_in_sequence
    

def main():
    upper_limit = int(input("Enter a Limit Number:"))
    threeplus1_iters_dict = threenp1range(upper_limit)
    print(threeplus1_iters_dict)
    
main()






















# def main():
#     for i in range(3, upper_limit):
#         threenp1()
#         threenplus1_iters_dictionary["n"] = "iterations"
#     return upper_limit

# main()

# if __name__ == "__main__":
# main()



        
        
    

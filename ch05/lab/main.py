


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
    objs_in_sequence = {i:threenp1(n)} #suggestion
    if upper_limit < 1:
        return {}
    threenp1()
    objs_in_sequence.append(upper_limit)
    return objs_in_sequence

def main():
    upper_limit = int(input("Please Enter a Limit Number:"))
    for i in range(3,upper_limit):
        threenp1(n)
        threenp1range(n)
        return main
    
main()






















# def main():
#     for i in range(3, upper_limit):
#         threenp1()
#         threenplus1_iters_dictionary["n"] = "iterations"
#     return upper_limit

# main()

# if __name__ == "__main__":
# main()



        
        
    

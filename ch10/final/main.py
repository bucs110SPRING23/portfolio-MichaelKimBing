from cryptoprice import Cryptoprice
from exchangerate import Exchangerate

def main():
    """
    Initializes all of the call classes into the main
    arguments: None
    return: API requested information
    """
    cryptostats = Cryptoprice()
    exchangeratetoday = Exchangerate()
    state = True

    while state:
        print("Hello, Would You Like To See The Current Status Of Bitcoin?")
        answer_to__question = int(input('Please Input 0 for Yes or 1 for No:'))
        if answer_to__question == 0:
            print(cryptostats)
            second_question= int(input('Would You Like To Receive A Free Bitcoin? Input 0 For Yes or 1 For No:'))
            if second_question == 0:
                print("Congrats You Have Earned 1 Bitcoin From Using Our Services.  Would You Like To Keep Or Sell?")
                third_question = int(input('Please Input 1 To Sell or Any Other Number To Keep:'))
                if third_question == 1:
                    print("You Have Sold Your Bitcoin")
                    amount = int(input('Please Type In The Value Of Your Bitcoin To View Exchange Rates(ONLY DOLLAR BILLS ACCEPTED NO CENTS):'))
                    if amount > 0:
                        exchangeratetoday.get(amount)
                        print(exchangeratetoday)
                        state = False
                    else:
                        print("Really? Next Time Put A REAL Value. Thank You For Using Bitcoin Services. Enjoy Your Free Bitcoin. Goodbye!")
                        state = False
                else:
                    print("Thank You For Using Bitcoin Services. Enjoy Your Free Bitcoin. Goodbye!")
                    state = False
            else:
                print("Thank You For Using Bitcoin Services.  Goodbye!")
                state = False
        elif answer_to__question == 1:
            print("Thank You For Using Bitcoin Services.  Goodbye!")
            state = False
        else:
            print("Sorry I didn't quite get that.  Please Try Again.")

main()

from catfacts import CatfactsAPI
from dogfacts import DogfactsAPI

def main():
    cat = CatfactsAPI()
    dog = DogfactsAPI()

    results1 = cat.get()
    results2 = dog.get()

    state = True
    while state:
        print("Are You Energetic or Lazy? 0. Energetic 1. Lazy")
        answer_to_final_question = int(input(':'))
        if answer_to_final_question == 0:
            print("Looks Like You Are A Dog Person!")
            print("Here Is Something Interesting About Your Dog:", results2)
            state = False
        elif answer_to_final_question == 1:
            print("Looks Like You Are A Cat Peron")
            print("Here Is Something Interesting About Your Cat:", results1)
            state = False
        else:
            print("Please Select Again")


main()
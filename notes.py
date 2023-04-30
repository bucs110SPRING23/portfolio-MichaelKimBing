#Essentially we have learned how to put togethe a program, a grahical program, and store files
#The only thing left is generally that some of the data might be somewhere else, meaning it might be storing data from a friends computer but not into your computer
#We are going to learn how to get data from another source into your local computer

#Network programming - this is what we are going to use to get data from another system to our local system

#We are going to build a program that asks trivia questions

#Server - any computer listening for incoming network connections 
#Request - a incoming connection that asks from som resouce from the server
    #Resources would either be images, videos, music, text, JSON, HTML, etc.

#You can basically send anything you want, as long as you can cerealize it meaning you are putting it into bits or something the server can access through

#Types of Requests:
#Primary one we need to worry about is GET: this is a read functon, like reading operation
#PUT - write operation (this requires security or something to secure something so that it wont be compromised)
#login and deleting

#Headers:
# send with the request and the response

#Status codesL(Definitions of what the codes stand for)
    # 200: okay, everything went fine 
    # 400: resource cannot be delivered
    # 500: bad code server

#ip address
#system information(geolocation)


#Urllib: this was a older library

#What we are going to use is - Request library - which you need to install like pygame

#adding the requirements.txt:
requests
#then in the terminal
pip install -r requirements.txt


import requests:
def main():
    response = requests.get("htttp://icanhazip.com") #it is because we are using the get vector, if you want post then you use .post()
    #This will send out your ip address
    print(response.status_code) #give out the status code - will give 200 meaning everything is working fine
    print(response.headers) #giving all the headers12
    print(response.text)    #giving away your ip address
main()

#now we can request from other computers, the problem is you need someon sort of convention - without the convention you will not know what you are running
#What we are going to use to solve this is:

#API - Application Programmer's Interface - the interface that basically runs the program or the external functionality of what the data you want to get
#APIS cna reutnr data in any format, usually returns in JSON
    #Basically we are going to look at the free api in github that have no authorization

#To start how to use the API, we have to know how URL's work

#URL Paramters:

#The paramters are litterally: ?, &

#Now lets do an example
# binghamton.edu/cs?var1=100&var2=200 - everything after the ? are just variables, the & makes the second variable
    #similar to looking up a video at youtube - look at how its structure is built

#opentdb.com - this is an API that is a free open trvia database - but we dont care about this we care about the API
#If we want to use this 
    #https://opentdb.com/api.php?amount=2 - then there is two questions
    #You can change the URL slightly to change the amount of reponses you want

#For now we can do: https://opentdb.com/api.php?amount=100&category=18 - 100 qeustions in the computer science category 

#Now we can do this:
import requests
import random 

def main():
    tp = TriviaProxyAPI()
    reults = tp.get()

    response = requests.get("https://opentdb.com/api.php?amount=1&category=18")
    #print(response.text) - giving you a dictionary
    data = response.json() #now this gives you a python dictionary in a JSON format 
    #this is the only two lines of code you need
    results = data['results']

    #With the information we can now index into the API
    for r in results:
        print(r['question'])
        #possibilites = [r["correct_answer"], *r["incorrect_answers"]] #create a list of correct answers
            #The * will remove the reset of the list of items
        #Or you can do it like this:
        possibles = [r["correct_answer"]] + r["incorrect_answers"] #r is there for read

        random.shuffle(possibles)
        input("Make your selection")
        for p in enumerate(possibles): #enumerte - selects the answer by number
            print(f"{i}){p}")
        
        selection = int(input(":"))

        if possibles[selection] == r["correct_answer"]:
            print("You are correct")
        else:
            print("You need to study more.  The correct answer is: {r['correct_answer']}") #single quote to prevent the f-string to end
main() 

#Now if you want multple questions then you just change the number of requests for how many you want is you change the ammount in the link

#You want the data to process it, so you dont want to worry about how that data would look
#to do that:

class TriviaProxyAPI:
    def __init__(self):
        self.url = "https://opentdb.com/api.php?
        self.varstr = "amoung=2&category=18"

    def get(self):
        url = self.url + self.varstr
        response = requests.get(url)
        data = response.json()
        return data ['results']
    #We do this to hide all the complexity and make it seem that the data is local or very easy to read

#So back to the main you would put and edit then:
def main():
    tp = TriviaProxyAPI()
    reults = tp.get()

    for r in results:
        print(r['question'])
        possibles = [r["correct_answer"]] + r["incorrect_answers"]
        random.shuffle(possibles)
        input("Make your selection")
        for p in enumerate(possibles): 
            print(f"{i}){p}")
    
        selection = int(input(":"))
        if possibles[selection] == r["correct_answer"]:
            print("You are correct")
        else:
            print("You need to study more.  The correct answer is: {r['correct_answer']}")
main() 

#Literally this is the final, where you are taking two API and synthesizing into something, whatever you want
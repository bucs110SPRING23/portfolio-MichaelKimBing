import json

def main():
    fptr = open("news.txt","a")
    ideas = fptr.read()
    fptr.readlines()
    change_words = {
        "tokens":"bananas",
        "enthusiasts":"fools",
    }
    fptr.close()
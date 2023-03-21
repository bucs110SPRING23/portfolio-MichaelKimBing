import json

def main():
    file_pointer = open("news.txt","r")
    reading_txt = file_pointer.read()
    file_pointer.close()
    fptr = open("editing.json", "r")
    ideas = json.load(fptr)
    for k, v, in ideas.items():
        reading_txt = reading_txt.replace(k,v)
        print(k,v)

    txt_new = open("better_news.txt","w")
    txt_new.write(reading_txt)
    txt_new.close()

main()
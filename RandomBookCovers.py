import random
import csv
import os


def getcovers():
    with open('bookcovers.csv','r') as file:
        reader = csv.reader(file)
        covers = [i[0] for i in reader]
        file.close()
    finallist = [random.choice(covers) for i in range(6)]
    return finallist


def getcoversasjpg():
    finallist = []
    with open('booktopics.txt','r') as file:
        topics = file.readlines()

        topics = [i.replace('\n','') for i in topics]
        file.close()

    curr_choices = []
    for i in range(0,6):
        choice = random.choice(topics)
        while(choice in curr_choices):
            choice = random.choice(topics)
        curr_choices.append(choice)
    print(curr_choices)

    for i in curr_choices:
        path = f'/Users/deepakkailash/PycharmProjects/BookStore/static/book-covers/{i}'
        res =  os.listdir(path)
        print(res)
        relpath = f'book-covers/{i}'
        finallist.append(relpath+'/'+random.choice(res))
    return finallist

x = getcoversasjpg()
print(x)
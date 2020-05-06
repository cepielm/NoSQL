#!/usr/bin/python

import pymongo,time,string,random

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def w_generator():
    woj=["dolnoslaskie","kujawsko-pomorskie","lubelskie","lubuskie","lodzkie","malopolskie","mazowieckie","opolskie","podkarpackie","podlaskie","pomorskie","slaskie","swietokrzyskie","warminsko-mazurskie","wielkopolskie","zachodniopomorskie"]
    N=len(woj)
    nr = random.randint(0,N-1)
    return woj[nr]

def main():
    ### Connection to Mongo
    moncon = pymongo.MongoClient("mongodb://root:root@172.20.20.2:27017/")
    db = moncon['random']
    col = db['random']
    x = int(input('Podaj ilosc rekordow\n'))
    for i in range(x):
        mydict = { "id_gen": id_generator(), "w_gen": w_generator() }
        col.insert_one(mydict)
main()
#!/usr/bin/python

import pymongo,time,string,random


def main():
    ### Connection to Mongo
    moncon1 = pymongo.MongoClient("mongodb://root:root@172.20.20.2:27017/")
    db1 = moncon1['random']
    col1 = db1['random']

    moncon2 = pymongo.MongoClient("mongodb://root:root@172.20.20.3:27017/")
    db2 = moncon2['random']
    col2 = db2['random']

    n = col1.count_documents({})
    print(n)
    j=0
    x=0
    y=0
    ### Losowanie rekordu z kolekcji 1 i kopiowanie do 2
    start_time = time.time()
    while j < n:
        for i in col1.aggregate([{ '$sample' : { 'size': 1 } }]):
            try:
                col2.insert_one(i)
                y+=1
            except:
                x+=1
        j = col2.count_documents({})
    print("---Kopiowanie zajelo %s sekund skopiowano %s rekordów, przy %s próbach ---" % (time.time() - start_time,y,x))
main()
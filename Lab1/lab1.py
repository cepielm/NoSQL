#!/usr/bin/python
# apt-get install python-pip ; pip install pymongo;

import mysql.connector,pymongo,time
from mysql.connector import Error

def main():
    ### Connection to Mongo
    moncon = pymongo.MongoClient("mongodb://root:root@172.20.20.2:27017/")
    db = moncon['random']
    col = db['random']
    ### Connection to MySQL
    try:
        connection = mysql.connector.connect(host='172.20.20.3',
                                         database='random',
                                         user='root',
                                         password='root')
        if connection.is_connected():
            print("Udało się nawiązać połączenie do MySQL.")
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            cursor.execute("select id_gen,w_gen from random")
            result = cursor.fetchall()
            ######### Copy data
            count = 0
            start_time = time.time()
            for x in result:
                count +=1
                mydict = { "id_gen": x[0], "w_gen": x[1] }
                col.insert_one(mydict)
            print("---Kopiowanie %s rekordów zajelo %s sekund ---" % (count,time.time() - start_time))

    except Error as e:
        print("Błąd połączenia MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL połączenie zakończone")
main()


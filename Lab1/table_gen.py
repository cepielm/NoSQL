import string
import random
def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def w_generator():
    woj=["dolnoslaskie","kujawsko-pomorskie","lubelskie","lubuskie","lodzkie","malopolskie","mazowieckie","opolskie","podkarpackie","podlaskie","pomorskie","slaskie","swietokrzyskie","warminsko-mazurskie","wielkopolskie","zachodniopomorskie"]
    N=len(woj)
    nr = random.randint(0,N-1)
    return woj[nr]

def main():
    x = int(input('Podaj ilosc rekordow\n'))
    f= open("lab1.sql","a+")
    for i in range(x):
        f.write("insert into random(id_gen,w_gen) values ('"+id_generator()+"','"+w_generator()+"');\n")
    f.write("UNLOCK TABLES;")
    f.close()
main()
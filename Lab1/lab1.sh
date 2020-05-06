#!/bin/bash

## Czyszczenie kontynerów
docker-compose -f lab1.yml down
docker-compose -f lab1.yml kill
docker-compose down -v --rmi all --remove-orphans

## Generowanie rekordów do bazy
## Uruchomienie kontynerów i import bazy 
pwd
docker-compose -f lab1.yml up -d
echo "Uruchamiam kontynery"
python3 table_gen.py
sleep 10
docker exec -i root_mariadb_1 chmod +x /mnt/import.sh
docker exec -i root_mariadb_1 ./mnt/import.sh
### python3 pip install mysql-connector pymongo
#docker exec -it root_python_1 /bin/bash
docker exec -it root_python_1 python /mnt/lab1.py

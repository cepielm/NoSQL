#!/bin/bash

mysql --host=localhost --user=root --password=root < /mnt/lab1.sql
echo "*********************************";
echo "** lab1.sql has been imported. **"
echo "*********************************";
echo "";
wait
sleep 1

#!/bin/sh

rm output/* -rf 

python3 main.py

rm ../RestaurantManagementSystem/server/src/main/java/generated/* -rf 
rm ../RestaurantManagementSystem/client/src/app/generated/* -rf  

cp ./output/java/* ../RestaurantManagementSystem/server/src/main/java/generated/ -rf
cp ./output/ts/* ../RestaurantManagementSystem/client/src/app/generated/  -rf

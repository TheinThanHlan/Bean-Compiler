#!/bin/sh

rm output/* -rf

python3 main.py

CP_DIR="../RestaurantManagementSystem"

rm $CP_DIR/server/src/main/java/generated/* -rf
rm $CP_DIR/client/src/app/generated/* -rf

cp ./output/java/* $CP_DIR/server/src/main/java/generated/ -rf
cp ./output/ts/* $CP_DIR/client/src/app/generated/  -rf

#!/bin/bash

sudo apt update
sudo apt upgrade -y

sudo apt install -y apache2 php7.0 php7.0-mysql php7.0-bcmath mariadb-server libmariadbclient-dev libmariadbclient-dev-compat

sudo apt-get update
sudo apt-get install -y python python-all-dev python-pip build-essential python-setuptools

sudo pip install pylibftdi

cd ~/SuperbPi
#make
#sudo make install

sudo cp -r html /var/www/
sudo rm /var/www/html/index.html
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 0755 /var/www/html

sudo chown -R root:root ~/SuperbPi
sudo chown -R 0755 ~/SuperbPi

#sudo cp raprec.service /lib/systemd/system
#sudo chown root:root /lib/systemd/system/raprec.service
#sudo chmod 0755 /lib/systemd/system/raprec.service
sudo systemctl daemon-reload
#sudo systemctl enable raprec

sudo chown -R www-data:www-data /var/www/html

cp localpi.sql localpi-configd.sql
sudo mysql < ~/SuperbPi/localpi-configd.sql
sudo rm localpi.sql
sudo rm localpi-configd.sql

echo "Done! :) "

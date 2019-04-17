#!/bin/bash

#Let's get the latest rep, and make sure everything is up to date.
sudo add-apt-repository ppa:deadsnakes/ppa  #For Pygame amongst python..
sudo apt update
sudo apt upgrade -y

#Install webserver and mysql dependencies.
sudo apt install -y apache2 php7.0 php7.0-mysql php7.0-bcmath
sudo apt install -y mariadb-server libmariadbclient-dev libmariadbclient-dev-compat

sudo apt-get install -y python3.6
#sudo apt-get install -y python python-all-dev python-setuptools
sudo apt-get install -y python-pip

sudo apt-get install -y build-essential cmake doxygen
sudo apt-get install -y python3-pygame
sudo pip install -y pyserial, obd, RPi.GPIO

#sudo apt-get install -y swig python-dev

#Build executable files from the Python scripts.
cd ~/SuperbPi
make
sudo make install

#Remove if there recides old index files.
sudo rm /var/www/html/index.html

#Copy everything from html folder to local webserver.
sudo cp -r html /var/www/
#Let the webserver user be able to execute the programs.
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 0755 /var/www/html

#sudo chown -R root:root ~/SuperbPi
#sudo chown -R 0755 ~/SuperbPi

sudo chmod +x ~/SuperbPi/SuperbPiLogger.py
#sudo chmod +x ~/SuperbPi/me7lconfig.py
#sudo chmod +x ~/SuperbPi/pylibme7.py

#Setup SuperbPiLogger rights, root must be able to start..
#Add new SuperbPiLogger service to the daemon.
sudo cp SuperbPiLogger.service /lib/systemd/system

sudo chown root:root /lib/systemd/system/SuperbPiLogger.service
sudo chmod 0755 /lib/systemd/system/SuperbPiLogger.service

sudo systemctl daemon-reload
sudo systemctl enable SuperbPiLogger

cp localpi.sql localpi-configd.sql
sudo mysql < ~/SuperbPi/localpi-configd.sql
sudo rm localpi.sql
#sudo rm localpi-configd.sql

echo "Done! :) "

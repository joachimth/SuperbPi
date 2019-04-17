#!/bin/bash

sudo apt update
sudo apt upgrade -y

sudo apt install -y apache2 php7.0 php7.0-mysql php7.0-bcmath
sudo apt install -y mariadb-server libmariadbclient-dev libmariadbclient-dev-compat

sudo apt-get update
#sudo apt-get install -y python3.6
sudo apt-get install -y python python-all-dev python-setuptools
sudo apt-get install -y python-pip
sudo pip install pyserial
sudo pip install obd
sudo apt-get install -y build-essential cmake doxygen
#libusb-1.0-devel

#sudo apt-get install -y libconfuse-dev
#sudo apt-get install -y swig python-dev
#sudo apt-get install -y libboost-all-dev

#mkdir libftdi
#cd libftdi
#git clone git://developer.intra2net.com/libftdi

#cd ~/libftdi
#mkdir build
#cd ~/libftdi/build
#cmake  -DCMAKE_INSTALL_PREFIX="/usr" ../
#make
#sudo make install

cd ~/SuperbPi
make
sudo make install

sudo cp -r html /var/www/
sudo rm /var/www/html/index.html
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 0755 /var/www/html

sudo chown -R root:root ~/SuperbPi
#sudo chown -R 0755 ~/SuperbPi

sudo chmod +x ~/SuperbPi/SuperbPiLogger.py
#sudo chmod +x ~/SuperbPi/me7lconfig.py
#sudo chmod +x ~/SuperbPi/pylibme7.py

sudo cp SuperbPiLogger.service /lib/systemd/system
sudo chown root:root /lib/systemd/system/SuperbPiLogger.service
sudo chmod 0755 /lib/systemd/system/SuperbPiLogger.service
sudo systemctl daemon-reload
sudo systemctl enable SuperbPiLogger

sudo chown -R www-data:www-data /var/www/html

cp localpi.sql localpi-configd.sql
sudo mysql < ~/SuperbPi/localpi-configd.sql
sudo rm localpi.sql
sudo rm localpi-configd.sql

echo "Done! :) "

#!/bin/bash

#################
# Update System #
#################
echo "...Updating system, just to make sure everything is brand new..."
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

###########################################
# Install pre-built dependencies from Apt #
###########################################
echo "...Install pre-built dependencies from Apt"
sudo apt-get install python3.7
#sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
sudo apt-get install -y dnsmasq hostapd python3-pip
sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install -r ~/SuperbPi/requirements.txt

echo "...Stopping hostapd and dnsmasq for a while..."
sudo systemctl disable hostapd dnsmasq

echo "...Let's get to it..."
cd ~/SuperbPi

echo "...Moving webpage content to server location, and setting the correct rights..."
sudo cp -r html /var/www/
sudo rm /var/www/html/index.html
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 0755 /var/www/html

echo "...Setup of a service running at startup..."
sudo cp SuperbPi.service /lib/systemd/system
sudo chown root:root /lib/systemd/system/SuperbPi.service
sudo chmod 0755 /lib/systemd/system/SuperbPi.service
sudo systemctl daemon-reload
sudo systemctl enable SuperbPi

echo "...Copying two files for our hotspot solution..."
sudo cp hostapd.conf /etc/hostapd
sudo cp dnsmasq.conf /etc


#installDate=$(date)
#cp localpi.sql localpi-configd.sql
#echo "INSERT INTO env (name, value) VALUES (\"rapVersion\", \"$softwareVersion\"), (\"installDate\", \"$installDate\");" >> localpi-configd.sql
#sudo mysql < localpi-configd.sql

echo "Done! Please reboot your Raspberry Pi now"

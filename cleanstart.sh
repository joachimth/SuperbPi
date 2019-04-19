#!/bin/bash

echo "...Updating system, just to make sure everything is brand new..."
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

echo "...Install pre-built dependencies from Apt"
sudo apt-get install python3.7
sudo apt-get install -y dnsmasq hostapd python3-pip
sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install -r ~/SuperbPi/requirements.txt

echo "...Stopping hostapd and dnsmasq for a while..."
sudo systemctl disable hostapd dnsmasq

echo "...Setup of a service running at startup..."
sudo cp ~/SuperbPi/SuperbPi.service /lib/systemd/system
sudo chown root:root /lib/systemd/system/SuperbPi.service
sudo chmod 0755 /lib/systemd/system/SuperbPi.service
sudo systemctl daemon-reload
sudo systemctl enable SuperbPi

echo "...Copying two files for our hotspot solution..."
sudo cp hostapd.conf /etc/hostapd
sudo cp dnsmasq.conf /etc

echo "...Rebooting now :-P ..."
sudo reboot --reboot

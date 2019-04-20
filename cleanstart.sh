#!/bin/bash

echo "...Updating system, just to make sure everything is brand new..."
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

echo "...Install pre-built dependencies from Apt"
sudo apt-get install python3.7
sudo apt-get install -y python3-pip
sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install -r ~/SuperbPi/requirements.txt


#echo "...Setup of a service running at startup..."
#sudo cp ~/SuperbPi/SuperbPi.py /etc/init.d/SuperbPi.py
#sudo chown root:root /etc/init.d/SuperbPi.py
#sudo chmod 0755 /etc/init.d/SuperbPi.py
#sudo update-rc.d sample.py defaults

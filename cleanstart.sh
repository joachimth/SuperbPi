#!/bin/bash
softwareVersion=$(git describe --long)

#################
# Update System #
#################
echo -e "\e[1;4;93mStep 1. Updating system\e[0m"
sudo apt update
sudo apt upgrade -y

###########################################
# Install pre-built dependencies from Apt #
###########################################
echo -e "\e[1;4;93mStep 2. Install pre-built dependencies from Apt\e[0m"
sudo apt install -y dnsmasq hostapd libbluetooth-dev apache2 php7.0 php7.0-mysql php7.0-bcmath mariadb-server libmariadbclient-dev libmariadbclient-dev-compat uvcdynctrl
sudo systemctl disable hostapd dnsmasq

################
# Build FFMpeg #
################
echo -e "\e[1;4;93mStep 3. Build ffmpeg (this may take a while)\e[0m"
ffmpegLocation=$(which ffmpeg)
if [ $? != 0 ]
then
	wget https://www.ffmpeg.org/releases/ffmpeg-3.4.2.tar.gz
	tar -xvf ffmpeg-3.4.2.tar.gz
	cd ffmpeg-3.4.2
	echo "./configure --enable-gpl --enable-nonfree --enable-mmal --enable-omx --enable-omx-rpi"
	./configure --enable-gpl --enable-nonfree --enable-mmal --enable-omx --enable-omx-rpi
	make -j$(nproc)
	sudo make install
else
	echo "FFMpeg already found at $ffmpegLocation! Using installed version."
fi

#######################
# Install RoadApplePi #
#######################
echo -e "\e[1;4;93mStep 4. Building and installing RoadApplePi\e[0m"
cd ~/SuperbPi
#make
#sudo make install

sudo cp -r html /var/www/
sudo rm /var/www/html/index.html
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 0755 /var/www/html
#sudo cp SuperbPiLogger.service /lib/systemd/system
#sudo chown root:root /lib/systemd/system/SuperbPiLogger.service
#sudo chmod 0755 /lib/systemd/system/raprec.service
#sudo systemctl daemon-reload
#sudo systemctl enable raprec
sudo cp hostapd-rap.conf /etc/hostapd
sudo cp dnsmasq.conf /etc
sudo mkdir /var/www/html/vids
sudo chown -R www-data:www-data /var/www/html

installDate=$(date)
cp localpi.sql localpi-configd.sql
echo "INSERT INTO env (name, value) VALUES (\"rapVersion\", \"$softwareVersion\"), (\"installDate\", \"$installDate\");" >> localpi-configd.sql
sudo mysql < localpi-configd.sql

echo "Done! Please reboot your Raspberry Pi now"

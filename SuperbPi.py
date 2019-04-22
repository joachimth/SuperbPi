#! /usr/bin/python3
# SuperbPi.py

# This is the main program for logging.
# This should be called after boot, and after the car has been started.
# Author: THIRSBRO
# Year: 2019
#
# Main functions:
# 1. Make connection.
# 2. Process data retreived.
# 3. Store processed data.
#
# Main goal:
# - Simple, easy, stable and fast data retrieval.
# - Must be easily configured.
# - Must be able to start by WIFI.
#
# - RPI with wifi Dongle functioning as a local hotspot.
#
# - This version must be able to log data and store it.
# - Only hardware used will be, RPI 2B and Freematics Arduino OBDIIUART v.1 dongle.
# - 
# - 
# - Next level goal:
# - Add simple fast GUI.
#
# Know errors right now:
# - It is not able to AUTO detect protocol for connecting with the ECU, so must be forced with AT SPx
# - Right now, protocol 4 (and maybe 5,6 ) are working.
#
# Key points to remember (note to self):
# - Always remember \r\n for return and newline.
# - Apparently it is needed to set encoding to utf-8 - Must be investigated.
#


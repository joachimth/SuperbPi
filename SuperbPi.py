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

import sys
#import serial
#import time
#import threading
from serialpy import ComConnection
from threading import Thread
from time import sleep

InitCommands = ["","","","ATZ", "ATS0", "AT@1", "ATSI"]

TestPollSeq = ["ATRV", "0103", "0105", "010B", "010C", "010D", "010F"]

# Initialize an instance
com = ComConnection(command='', baudrate=115200, timeout=1)


def read():
    while True:
        data = com.receive_command()
        if data:
            if data == '>':
                print("We have Init")
            print(data)
        sleep(1)


def write():
    # If you try to call send_command() before call connect()
    # an exception will be raised inform you are trying to
    # send command in a closed connection
    HaveInit=False
    
    while True:
        com.send_command()
        for i in InitCommands:
            com.send_command = InitCommands[i]
            print(read())
            sleep(1)
        sleep(1)


if __name__ == '__main__':
    t = Thread(target=read, args=())
    # Make sure this thread will be killed when main program exits
    t.setDaemon(True)
    t.start()

    com.connect()

    #write()

    #for i in InitCommands:
    #    write(InitComma[i])
    #    sleep(1)
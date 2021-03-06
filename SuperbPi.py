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
from serialpy import ComConnection
from threading import Thread
from time import sleep
# Initialize an instance
com = ComConnection(command='', baudrate=115200, timeout=1)

InitCommands = ["","","","ATZ", "ATS0", "AT@1"] #, "ATSI"]
InitCommands.reverse()

TestPollSeq = ["ATRV", "0103", "0105", "010B", "010C", "010D", "010F"]
TestPollSeq.reverse()
global GoOnWrite
global CurrentDataPollID
CurrentDataPollID = 0
GoOnWrite = 0

def read():
    global GoOnWrite
    while True:
        data = com.receive_command()
        if data and len(data)>= 1:
            print(data)
            GoOnWrite = 1
        sleep(0.5)

def write():
    global GoOnWrite
    while True:
        if len(InitCommands)> 0 and GoOnWrite==1:
            v = InitCommands.pop()
            com.command = v
            com.send_command()

def Datapoll():
    global CurrentDataPollID
    if len(InitCommands) == 0 and GoOnWrite == 1:
        if CurrentDataPollID > len(TestPollSeq):
            CurrentDataPollID = 0 #Don't waste time if we have exceeded start from scratch.

        if CurrentDataPollID <= len(TestPollSeq):
            v = TestPollSeq[CurrentDataPollID]
            com.command = v
            com.send_command()
            CurrentDataPollID += 1
            print(v)

        GoOnWrite = 0

if __name__ == '__main__':
    t = Thread(target=read, args=())
    # Make sure this thread will be killed when main program exits
    t.setDaemon(True)
    t.start()

    com.connect() #Connect firstly.
    write()       #Write init sequence.

    Datapoll()    #Start the datapolling at once, will first be active after init.

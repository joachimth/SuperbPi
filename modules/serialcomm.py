#! /usr/bin/python3
# serialcomm.py

# Author: THIRSBRO
# Year: 2019
# Two main functions.
# Start the init process at command.
# Retreive data if possible.
# Discard problems, we only want the good stuff.
#

# It does not seem to be able to auto connect with the ECU, so must be forced with AT SPx
# always remember \r\n for return and newline. apparently it is needed to set encoding to utf-8
#

import sys
import serial
import time
import threading

global SerConn

##########################################
#Configurations settings,
#will later be imported from config.file
##########################################
#Reminders/Notes:
#For Superb 1.gen, Protocol 3, 4 and 5 are the most interessting.

class SerialConfig(*args):
    def __init__(self, OBDProtocol:str,SERbaudrate: int,SERtimeout:int,InitArray:Array, TestPollSequence: List, OBDLogValues: List):
        self.OBDProtocol = "3"
        self.SERbaudrate = 115200
        self.SERtimeout = 1
        self.InitArray = ["ATZ", "ATS0", "AT@1", "ATSI"]
        self.TestPollSequence = ["ATRV", "0103", "0105", "010B", "010C", "010D", "010F"]
        self.OBDLogValues = ["010C","010D","010F"]
 
##########################################
# Functions sections.
#
###########################################
#Reminders/Notes:
#
#

def SerWriteFunction(self, DataToWrite, FirstWrite=True):
    if FirstWrite == True:
        self.FlushInput()
        self.write(bytes(DataToWrite+'\r', encoding='utf-8'))
    
    if FirstWrite == False:
        self.FlushInput()
        self.write(bytes(DataToWrite+'\r', encoding='utf-8'))

##########################################
# Main routines.
#
###########################################
#Reminders/Notes:
#
#

#SerWriteFunction(serial.Serial(""),"",True)

def serInit():
    global SerConn
    SerConn = serial.Serial(SerialConfig.SERbaudrate, SerialConfig.SERtimeout)
    # Before anything we need to establish a connection has been made to the dongle.
    # We will be sending a \r = return. and listening for a >, in x amounts of seconds.

    SerWriteFunction(SerConn,"",True)

    waitingSer=True

    while waitingSer==True:
        SerConnResp = SerConn.read(999).decode('utf-8')
        SerConn.flush()
        If SerConnResp == '>'
            main()
        else:
            sleep(1)
            print("We are still waiting for connection...")

def main():    
    while True:
        for i in SerialConfig.InitArray:
            SerWriteFunction(SerConn,"",True)
            SerConn.flushInput()
            SerConn.write(bytes(SerialConfig.InitArray[i] + '\r\n', encoding='utf-8'))
            SerConnResp = SerConn.read(999).decode('utf-8')
            SerConn.flush()

            if len(SerConnResp) > 0:
                print("...Data is returned...")
                print("...Response >", SerConnResp)
        except Exception:
            print(Exception)
        finally:
            SerConn.close()

main()

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
sys.path.append("./SuperbPi")
sys.path.append("./SuperbPi/modules/settings")
sys.path.append("./SuperbPi/modules")

import CustomConfig
import serial
import time

SerConn = serial.Serial(CustomConfig.SerialUARTConfig)

def SerConnStart():
    try:
        # Starting connection.
        SerConn.flushInput()
        SerConn.write(bytes('\r', encoding='utf-8'))

    except Exception as ErrorString:
        print(ErrorString)


def SerConnWrite(DataToWrite):
    try:
        SerConn.flushInput()
        SerConn.write(bytes(DataToWrite + '\r\n', encoding='utf-8'))
    except Exception as ErrorString:
        print(ErrorString)


def SerConnInit():
    try:
        pass
    except Exception as ErrorString:
        print(ErrorString)


def main():
    try:
        # Before anything we need to establish a connection has been made to the dongle.
        # We will be sending a \r = return. and listening for a >, in x amounts of seconds.

        for i in CustomConfig.SerialCARConfig.InitCommands:
            SerConn.flushInput()
            SerConn.write(
                bytes(CustomConfig.SerialCARConfig.InitCommands[i] + '\r\n', encoding='utf-8'))
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

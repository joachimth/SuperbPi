#!/usr/bin/python3
version = 0.1

# sercommcfg.py
# Author: THIRSBRO
# Year: 2019
# Config file for serialcomm.py.
#

#OBD(portstr=None, baudrate=None, protocol=None, fast=True, timeout=0.1, check_voltage=True)
#
# Default speed	set	for	Freematics OBDII to	UART Android v1.
#
# ID	Name
# 1	SAE J1850 PWM
# 2	SAE J1850 VPW
# 3	AUTO, ISO 9141-2
# 4	ISO 14230-4 (KWP 5BAUD)
# 5	ISO 14230-4 (KWP FAST)
# 6	ISO 15765-4 (CAN 11/500)
# 7	ISO 15765-4 (CAN 29/500)
# 8	ISO 15765-4 (CAN 11/250)
# 9	ISO 15765-4 (CAN 29/250)
# A	SAE J1939 (CAN 29/250)
#import sys

class SerCfg:
    port = '/dev/ttyAMA0'     # Connecting direct to UART pins on RPI. Remember UART=1, and no console at serial.
    baudrate = '115200'            # Standard baudrate 38400..Freematics..115200..
    timeout = '1'                  # Standard timeout = 0.1


class SerCustomCfg:
    # For Superb 1.gen, Protocol 3, 4 and 5 are the most interessting.
    Protocol = 3
    InitCommands = ["ATZ", "ATS0", "AT@1", "ATSI"]
    TestPollSequence = ["ATRV", "0103", "0105", "010B", "010C", "010D", "010F"]

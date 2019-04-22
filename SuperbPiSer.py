#!/usr/bin/python3

#SuperbPi.py
#Author: THIRSBRO
#Year: 2019
# file paths

import os
import obd # as OBD
import time
import serial
from obd import OBDCommand, Unit, OBDStatus
from obd.protocols import ECU
from obd.utils import bytes_to_int


running_dir         = os.path.dirname(os.path.realpath(__file__))
default_config_path = os.path.join(running_dir, 'default.rc')
config_path         = os.path.join(os.path.expanduser('~'), 'pihud.rc')

def main(filename='~/SuperbPi/logs/log00.csv'):
	print('Logging	to file: \t',filename)

	ports = ["/dev/ttyAMA0","Serial0"]
	#ports = obd.scan_serial()

	if(len(ports)>0):
		try:
			print(ports[0])
			#OBD(portstr=None, baudrate=None, protocol=None, fast=True, timeout=0.1, check_voltage=True)
			#Default speed	set	for	Freematics OBDII to	UART Android v1.
			#ID	Name
			#1	SAE J1850 PWM
			#2	SAE J1850 VPW
			#3	AUTO, ISO 9141-2
			#4	ISO 14230-4 (KWP 5BAUD)
			#5	ISO 14230-4 (KWP FAST)
			#6	ISO 15765-4 (CAN 11/500)
			#7	ISO 15765-4 (CAN 29/500)
			#8	ISO 15765-4 (CAN 11/250)
			#9	ISO 15765-4 (CAN 29/250)
			#A	SAE J1939 (CAN 29/250)

			ser = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=1) 
			with open(filename,'a') as file:
				errcont=0
				while(errcont<8):
					ser.flushInput();
					ser.write(bytes('at sp4' + '\r\n', encoding = 'utf-8'))
					print(ser.read(999).decode('utf-8'))
					ser.flushInput();
					ser.write(bytes('atrv' + '\r\n', encoding = 'utf-8'))
					ser.flush();
					jtout = ser.read(999).decode('utf-8')
		
					file.write(jtout+"\n")
					if len(jtout)>2:
						print("We might have a connection")
					sleep(1)
					print(errcont,'.Response: ',jtout)
					errcont += 1

				try:
					while True:
						s = input('Enter AT Command -->')
						print('AT Command = ' + s)
						ser.write(bytes(s + '\r\n', encoding = 'utf-8'))
						ser.timeout = 1
						response = ser.read(999).decode('utf-8')
						print('Response: ' + response)
				except KeyboardInterrupt:
					print("Du sagde stop..")
				finally:
					ser.close()

#				connection.start()
				#with	open(filename,'a') as file:

#				file.write('\n%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(ecua,ecub,ecuc,ecud,ecue,ecuf,ecug,ecuh,ecui,ecuj,ecuk,ecul))
					#d = integer, f=float, s=string, b=boolean/binary
				#time.sleep(120)
				#connection.stop()
		except:
			print("Connection not possible, error")
	else:
			print("Har ikke fundet nogle porte :--")

if __name__	== "__main__":
	import	argparse
	parser = argparse.ArgumentParser(description='Create a bob schema')
	parser.add_argument('-f','--filename',dest='filename',metavar='path',required=False,help='Filename being written to')
	args = parser.parse_args()
	main(args.filename)

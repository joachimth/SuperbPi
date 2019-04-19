import serial
ser = serial.Serial("/dev/ttyAMA0")
ser.baudrate = 115200

def jt_init():
	errcont=0
	while(errcont<5):
		ser.flushInput();
		ser.write(bytes('atrv' + '\r\n', encoding = 'utf-8'))
		ser.flush();
		ser.timeout = 1
		jtout = ser.read(999).decode('utf-8')
		if len(jtout)>2:
			print("We might have a connection")
		print(errcont,'.Response: ',jtout, )
	#sleep(1)
		errcont += 1
	jt_comml()

def jt_comml():
	s = input('Enter AT Command -->')
	print('AT Command = ' + s)
	ser.write(bytes(s + '\r\n', encoding = 'utf-8'))
	ser.timeout = 1
	response = ser.read(999).decode('utf-8')
	print('Response: ' + response)

	qukk = input('Continue? q=quit')
	print('answer' + qukk)
	if(qukk != 'q'):
		jt_comml()



jt_init()

ser.close()


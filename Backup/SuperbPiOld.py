def	main(filename='~/SuperbPi/logs/log00.csv'):
	import	os
	import	obd
	import	time
	from obd import OBD, Async, commands, Unit, OBDStatus
	
	print('Logging	to file: \t',filename)
	ports = obd.scan_serial()
	print("Ports avail:\t",ports)

	if(len(ports)>0):
		print(ports[0])
		#Default speed	set	for	Freematics OBDII to	UART Android v1.
		with obd.Async(ports[0],115200,None,False,4) as connection:
			connection.watch(obd.commands.RPM)
			connection.watch(obd.commands.SPEED)
			connection.watch(obd.commands.TIMING_ADVANCE)
			connection.watch(obd.commands.COOLANT_TEMP)
			connection.watch(obd.commands.ENGINE_LOAD)
			connection.watch(obd.commands.LONG_FUEL_TRIM_1)
			connection.watch(obd.commands.SHORT_FUEL_TRIM_1)
			connection.watch(obd.commands.INTAKE_PRESSURE)
			#Start connection and let the games begin...
			connection.start()
			with	open(filename,'a') as file:
				ecua = connection.query(obd.commands.RPM)
				ecub = connection.query(obd.commands.SPEED)
				ecuc = connection.query(obd.commands.TIMING_ADVANCE)
				ecud = connection.query(obd.commands.COOLANT_TEMP)
				ecue = connection.query(obd.commands.ENGINE_LOAD)
				ecuf = connection.query(obd.commands.LONG_FUEL_TRIM_1)
				ecug = connection.query(obd.commands.SHORT_FUEL_TRIM_1)
				ecuh = connection.query(obd.commands.INTAKE_PRESSURE)
				ecui = ""
				ecuj = ""
				ecuk = ""
				ecul = ""
				file.write('\n%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(ecua,ecub,ecuc,ecud,ecue,ecuf,ecug,ecuh,ecui,ecuj,ecuk,ecul))
				#d = integer, f=float, s=string, b=boolean/binary
			time.sleep(120)
			connection.stop()
	else:
		print("Fucked	op")

if __name__	== "__main__":
	import	argparse
	parser = argparse.ArgumentParser(description='Create a bob schema')
	parser.add_argument('-f','--filename',dest='filename',metavar='path',required=False,help='Filename being written to')
	args = parser.parse_args()
	main(args.filename)



def main(filename='testhest.csv'):
    import os
    import obd
    import time
    from obd import OBD, Async, commands, Unit, OBDStatus
    print('Logging to file: \t',filename)
    ports = obd.scan_serial()
    print("Ports avail:\t",ports)
    if(len(ports)>0):
        print(ports[0])
        with obd.Async(ports[0],115200,None,False,4) as connection:
            connection.watch(obd.commands.RPM)
            connection.watch(obd.commands.COOLANT_TEMP)
            connection.watch(obd.commands.ENGINE_LOAD)
            connection.watch(obd.commands.LONG_FUEL_TRIM_1)
            connection.watch(obd.commands.ELM_VERSION)
            connection.watch(obd.commands.ELM_VOLTAGE)

            connection.start()
            with open(filename,'a') as file:
                ecua = connection.query(obd.commands.COOLANT_TEMP)
                ecub = connection.query(obd.commands.RPM)
                file.write('\n%s,%s'%(ecua,ecub))
            
                            #d = integer, f=float, s=string, b=boolean/binary
            #print("ELM Version: ", connection.query(obd.commands.ELM_VERSION))
            #print("ELM Voltage: ", connection.query(obd.commands.ELM_VOLTAGE))
            #print("ECU - Coolant Temp: ", connection.query(obd.commands.COOLANT_TEMP))
            #print("ECU - RPM: ", connection.query(obd.commands.RPM)) # non-blocking, returns immediately
            #print("ECU - Engine Load: ", connection.query(obd.commands.ENGINE_LOAD))
            #print("ECU - Long Fuel Trim: ", connection.query(obd.commands.LONG_FUEL_TRIM_1))

            time.sleep(120)
            connection.stop()
    else:
        print("Fucked op")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Create a bob schema')
    parser.add_argument('-f','--filename',dest='filename', metavar='path', required=False,
                        help='Filename being written to')
    args = parser.parse_args()
    main(args.filename)
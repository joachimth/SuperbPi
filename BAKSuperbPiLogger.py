import os
import obd
import time
from obd import OBD, Async, commands, Unit, OBDStatus

connection = obd.Async("/dev/ttyAMA0",115200,None,False,4)
connection.watch(obd.commands.RPM)
connection.watch(obd.commands.COOLANT_TEMP)
connection.watch(obd.commands.ENGINE_LOAD)
connection.watch(obd.commands.LONG_FUEL_TRIM_1)
connection.watch(obd.commands.ELM_VERSION)
connection.watch(obd.commands.ELM_VOLTAGE)

connection.start()
print("ELM Version: ", connection.query(obd.commands.ELM_VERSION))
print("ELM Voltage: ", connection.query(obd.commands.ELM_VOLTAGE))
print("ECU - Coolant Temp: ", connection.query(obd.commands.COOLANT_TEMP))
print("ECU - RPM: ", connection.query(obd.commands.RPM)) # non-blocking, returns immediately
print("ECU - Engine Load: ", connection.query(obd.commands.ENGINE_LOAD))
print("ECU - Long Fuel Trim: ", connection.query(obd.commands.LONG_FUEL_TRIM_1))

time.sleep(60)
connection.stop()

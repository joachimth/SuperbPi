
import time
import threading
import serial

global SerConn
global SerialOK

#SerialUARTConfig = ["/dev/ttyAMA0", "115200", "1"]

# pylint: disable=wrong-import-order,wrong-import-position


InitCommands = ["ATZ", "ATS0", "AT@1", "ATSI"]

TestPollSequence = ["ATRV", "0103", "0105", "010B", "010C", "010D", "010F"]

# For Superb 1.gen, Protocol 3, 4 and 5 are the most interessting.
class SerialCARConfig():
    def __init__(self):
        self.Protocol = 3

print(SerialCARConfig().Protocol)
print(SerialUARTConfig)

class MyThread(threading.Thread):
    def SerConnWrite(self,DataToWrite):
        SerConn.flushInput()
        SerConn.write(bytes(DataToWrite + '\r\n', encoding='utf-8'))
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = False

    def run(self):
        global SerConn
        global SerialOK = False
        SerConn = serial.Serial("/dev/ttyAMA0", 115200, 1)
        self.SerConnWrite("")

        while !self.SerialOK:
            print('Waiting for conn')

        counter = 0
        self.running = True

        while self.running:
            print('counter:', str(counter))
            time.sleep(2)
            counter += 1

    def stop(self):
        print('stopping thread...')
        SerConn.stop()
        self.running = False
        self.join(2)


my_thread = MyThread()
my_thread.setDaemon(True)
my_thread.start()

SerConn = serial.Serial("/dev/ttyAMA0")
SerConn.baudrate = 115200
SerConn.timeout = 1
SerConn.setDaemon(True)
SerConn.start()

# python 3
input("Press Enter to stop...")

# python 2
#raw_input("Press Enter to stop...")

my_thread.stop()

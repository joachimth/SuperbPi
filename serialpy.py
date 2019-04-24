from os import linesep
from serial import Serial
from serial.tools.list_ports import comports


class ComConnection(object):
    """Serial wrapper which can be instantiated using serial number"""

    def __init__(self, command=None, baudrate=115200, timeout=1):
        """
        Constructor

        Parameters
        ----------
        serial_number: string
            The usb-serial's serial number
        command: string
            Command to be send
        baudrate: int
            Baud rate such as 9600 or 115200 etc. Default is 115200
        """
        #self.serial_number = serial_number
        self.command = command
        self.serial = Serial()
        self.serial.baudrate = baudrate
        self.serial.timeout = timeout

    def __del__(self):
        """Destructor"""
        try:
            self.close()
        except:
            pass  # errors on shutdown

    def __str__(self):
        return "Command: {}".format(self.command)

    def connect(self):
        """
        Open/connect to serial port

        """
        # open serial port
        try:
            #device = self.get_device_name(self.serial_number)
            device = "/dev/ttyAMA0"
            self.serial.port = device
            # Set RTS line to low logic level
            #self.serial.rts = False
            self.serial.open()
        except Exception as ex:
            self.handle_serial_error(ex)

    def send_command(self):
        """
        Send data/command to serial port
        """
        if self.serial.is_open:
            try:
                # Unicode strings must be encoded
                data = bytes(self.command + '\r\n', encoding='utf-8')
                #self.serial.flushInput()
                self.serial.write(data)
            except Exception as ex:
                self.handle_serial_error(ex)
        else:
            raise IOError('Try to send data when the connection is closed')

    def receive_command(self):
        """Receive command from serial port"""
        if self.serial.is_open:
            return self.serial.read_all()
            #self.serial.flushInput()

    def close(self):
        """Close all resources"""
        self.serial.close()

    def handle_serial_error(self, error=None):
        """Serial port error"""
        # terminate connection
        self.close()
        # forward exception
        if isinstance(error, Exception):
            raise error  # pylint: disable-msg=E0702

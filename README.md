SuperbPi
--------

Install
-------

Should be installed on a clean system with .\cleanstart.sh in ~ (Your home directory)

Req:
- Python3
- Pip for Python3.
- Pyserial
- ...

Expected functions method:

SuperbPi.py - Main function / loop / daemon for logging and so on.

modules\serialcomm.py   - Handles serial communication and car communication.
                        - Parses data back to Main function.

ressources\CustomConfig.py - All settings which could be changed later on by the user.

ressources\DataLog2File.py  - Not ready yet. Will simply put data to .csv file.

ECU_def - Not used, perhaps will be used later on..

Logs\ - This is where the log files will be placed.


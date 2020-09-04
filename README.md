# MG2xTOBG2x

Silicon Labs are now officially only making MG2x RF cards for our WSTK base boards, so if you want to design with a BG2x part then you will need to port the project manually.

This python script was created to help you migrate your MG2x project, developed with the WSTK to a BG2x end device.

In order to use it, please go through the following steps:
1) Create your project using the MG2x board on Simplicity Studio 5 (SSv5)
2) Add all the peripherals required and relevant software additions. Keep in mind if the end device has a different pin count, the GPIOs labels chosen need to be also available on that particular device.
3) Add the python scrip to the main project folder
4) Close the project on SSv5
4) Open the project folder on Command line and run python MG2xtoBG2x.py
5) It will give you the option to choose which is the device needed and then it will change all the files related to it.
6) As you reopen the project on SSv5, it will be converted to a BG2x part.

This was tested with Python 3.85

Known bugs: there is an issue on the configurator

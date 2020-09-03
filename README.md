# MG2xTOBG2x

Silicon Labs are now officially only making MG2x RF cards for our WSTK base boards, so if you want to design with a BG2x part then you will need to port the project manually.

This python script was created to help you migrate your MG2x project, developed with the WSTK to a BG2x end device.

In order to use it, you just have to add it to the project folder and then run on the command line:

python MG21toBG21.py

Ideally you want to have your project closed on Simplicity Studio 5. As you reopen it, it will be converted to a BG2x part.

This was tested with Python 3.85

import os, shutil
from os import listdir
from shutil import copyfile
retval = os.getcwd()
print "Current working directory %s" % retval

legacybleLinkerScriptPATH = "/Applications/Simplicity Studio.app/Contents/Eclipse/developer/sdks/gecko_sdk_suite/v2.7/protocol/bluetooth/ble_stack/linker/GCC"

def replaceXG2(file, device):
    devicelower = device.lower()
    fin = open(file, "rt")
    data = fin.read()
    data = data.replace('EFR32MG21A010F1024IM32', device)
    data = data.replace('efr32mg21a010f1024im32', devicelower)
    data = data.replace('EFR32MG21A020F1024IM32', device)
    data = data.replace('efr32mg21a020f1024im32', devicelower)
    data = data.replace('MG21', 'BG21')
    data = data.replace('mg21', 'bg21')
    fin.close()

    fin = open(file, "wt")
    fin.write(data)
    fin.close()
    print "%s changed" % file

def changedir(directory):
    curDir = os.getcwd()
    os.chdir(curDir + directory)
    curDir = os.getcwd()
    print "Current working directory %s" % curDir

def list_files1(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))

def printDevices():
    print "Choose which device do you want to convert your project to: \n\r"
    for key, value in parts.items():
        print key,':',value


parts = {
    "A" : "EFR32BG21A010F512IM32",
    "B" : "EFR32BG21A010F768IM32",
    "C" : "EFR32BG21A010F1024IM32",
    "D" : "EFR32BG21A020F512IM32",
    "E" : "EFR32BG21A020F768IM32",
    "F" : "EFR32BG21A020F1024IM32",
    "G" : "EFR32BG21B010F512IM32",
    "H" : "EFR32BG21B010F768IM32",
    "I" : "EFR32BG21B010F1024IM32",
    "J" : "EFR32BG21B020F512IM32",
    "K" : "EFR32BG21B020F768IM32",
    "L" : "EFR32BG21B020F1024IM32"
}
print "EFR32MG21 to EFR32BG21 project conversion utility \n\r"
printDevices()
result = None
while result is None:
    val = raw_input ("Enter your choice: ")
    if (val.islower()) == True:
        val = val.upper()
    if val in parts:
        device = parts.get(val)
        print "Device chosen %s " % device
        result = 1
    else:
        print "Choice not available \n\r"

print(devicelower)
replaceXG2(".project", device)
replaceXG2(".cproject", device)

#Searches for specific file extentions and assign them to variables
x = os.listdir(os.getcwd())

for i in x:
    if i.endswith(".isc"):
        ISC = i
        replaceXG2(ISC, device)
        #print(SLCP)
    if i.endswith(".slps"):
        SLPS = i
        replaceXG2(SLPS, device)
        #print(SLPS)
    if i.endswith(".pintool"):
        PINTOOL = i
        replaceXG2(PINTOOL, device)
        #print(PINTOOL)
    if i.endswith(".slcp"):
        SLCP = i
        replaceXG2(SLCP, device)
        #print(SLCP)
    if i.endswith(".hwconf"):
        HWCONF = i
        replaceXG2(HWCONF, device)
    if i.endswith(".ld"):
        destinationP = os.getcwd()
        sourceP = legacybleLinkerScriptPATH + devicelower + ".ld"
        copyfile(sourceP, destinationP)
        #HWCONF = i
        #replaceXG2(HWCONF, device)
        #print(SLCP)


#replaceXG2(ISC, device)
#replaceXG2(SLCP, device)
#replaceXG2(SLPS, device)
#replaceXG2(PINTOOL, device)

#It checks if there is a compiler output folder and removes it
if os.path.isdir(os.getcwd()+ "/GNU ARM v7.2.1 - Debug"):
    shutil.rmtree("GNU ARM v7.2.1 - Debug")
    print "Compiler Output Directory removed"
else:
    print "Compiler Output Directory not present"


#jumps into .pdm folder and searches for MG2x strings and replace whatever files that have mentioning of MG2x
if os.path.isdir(os.getcwd()+"/.pdm"):
    x = os.chdir(os.getcwd()+"/.pdm")
    x = os.listdir(os.getcwd())
    for i in x:
        SLSPROJ = i
        replaceXG2(SLSPROJ, device)

#legacy ssv4 BLE Project includes a .settings project
if os.path.isdir(os.getcwd()+"/.settings"):
    x = os.chdir(os.getcwd()+"/.settings")
    x = os.listdir(os.getcwd())
    for i in x:
        if i.endswith(".prefs"):
            replaceXG2(i, device)

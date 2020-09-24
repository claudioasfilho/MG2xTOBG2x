import os, shutil
from os import listdir
retval = os.getcwd()
print "Current working directory %s" % retval

def replaceXG2(file, device):
    devicelower = device.lower()
    fin = open(file, "r+")
    data = fin.read()
    data = data.replace('EFR32MG22C224F512IM40', device)
    data = data.replace('efr32mg22c224f512im40', devicelower)
    data = data.replace('MG22', 'BG22')
    data = data.replace('mg22', 'bg22')
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
    "A" : "EFR32BG22C112F352GM32",
    "B" : "EFR32BG22C222F352GM32",
    "C" : "EFR32BG22C222F352GM40",
    "D" : "EFR32BG22C222F352GN32",
    "E" : "EFR32BG22C224F512GM32",
    "F" : "EFR32BG22C224F512GM40",
    "G" : "EFR32BG22C224F512GN32",
    "H" : "EFR32BG22C224F512IM32",
    "I" : "EFR32BG22C224F512IM40"
}

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
        #print(SLCP)


#It checks if there is a compiler output folder and removes it
if os.path.isdir(os.getcwd()+ "/GNU ARM v7.2.1 - Debug"):
    shutil.rmtree("GNU ARM v7.2.1 - Debug")
    print "Compiler Output Directory removed"
else:
    print "Compiler Output Directory not present"

#jumps into .pdm folder and searches for MG2x strings and replace whatever files that have mentioning of MG2x
x = os.chdir(os.getcwd()+"/.pdm")

x = os.listdir(os.getcwd())
for i in x:
    SLSPROJ = i
    replaceXG2(SLSPROJ, device)

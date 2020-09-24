#python /Users/clfilho/projects/MG2xtoBG2x/MG21toBG21SSv4.py
import os, shutil
from os import listdir
from shutil import copyfile, copy
retval = os.getcwd()
print "Current working directory %s" % retval

legacysdksPATH = "/Applications/Simplicity Studio.app/Contents/Eclipse/developer/sdks/gecko_sdk_suite/"
sdkchoice = "v2.7/"
#legacybleLinkerScriptPATH = "/Applications/Simplicity Studio.app/Contents/Eclipse/developer/sdks/gecko_sdk_suite/v2.7/protocol/bluetooth/ble_stack/linker/GCC/"
legacybleLinkerScriptPATH = "protocol/bluetooth/ble_stack/linker/GCC/"
#protocol/bluetooth/ble_stack/linker/GCC/

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
project_folder = os.getcwd()

BGIncludefilelist = []
BGSourcefilelist = []

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


devicelower = device.lower()


#it brushes on the include files
if not os.path.isdir(project_folder + "/platform/Device/SiliconLabs/EFR32BG21/Include"):
    os.chdir(project_folder + "/platform/Device/SiliconLabs/EFR32MG21/Include")
    listofFiles = os.listdir(project_folder + "/platform/Device/SiliconLabs/EFR32MG21/Include")
    #print(listofFiles)
    for file in listofFiles:
        if file.startswith("efr32mg21"):
            if not file.endswith("32.h"):
                file2 = file.replace("efr32mg21" , "efr32bg21")
                BGIncludefilelist.append(file2)
                #print("none")
            #else :
            #    file2 = file.replace("efr32mg21" , "efr32bg21")
            #    BGIncludefilelist.append(file2)

        #print(string(file))
    BGIncludefilelist.append(devicelower + ".h")
    BGIncludefilelist.append("system_efr32bg21.h")
    BGIncludefilelist.append("em_device.h")
    #print("\r\n")
    #print(BGIncludefilelist)



    os.chdir(project_folder + "/platform/Device/SiliconLabs/")
    os.mkdir("EFR32BG21")
    os.chdir(project_folder + "/platform/Device/SiliconLabs/EFR32BG21/")
    os.mkdir("Include")
    os.mkdir("Source")

    #Now it will copy the Include files from the BG file structure to the include folder
    os.chdir(project_folder + "/platform/Device/SiliconLabs/EFR32BG21/Include")
    destinationP = project_folder + "/platform/Device/SiliconLabs/EFR32BG21/Include"
    for file in BGIncludefilelist:
        sourceP = legacysdksPATH + sdkchoice + "/platform/Device/SiliconLabs/EFR32BG21/Include/" + file
        copy(sourceP, destinationP)
        print(file + " copied")
    #Now it will copy the source files
    os.chdir(project_folder + "/platform/Device/SiliconLabs/EFR32BG21/Source")
    destinationP = project_folder + "/platform/Device/SiliconLabs/EFR32BG21/Source"
    sourceP = legacysdksPATH + sdkchoice + "/platform/Device/SiliconLabs/EFR32BG21/Source/" + "system_efr32bg21.c"
    copy(sourceP, destinationP)
    print(file + " copied")
    os.mkdir("GCC")
    destinationP = project_folder + "/platform/Device/SiliconLabs/EFR32BG21/Source/GCC"
    sourceP = legacysdksPATH + sdkchoice + "/platform/Device/SiliconLabs/EFR32BG21/Source/GCC/" + "startup_efr32bg21.c"
    copy(sourceP, destinationP)
    print(file + " copied")

    #Now it will remove the MG21 Include and Source folders
#    os.chdir(project_folder + "/platform/Device/SiliconLabs")
#    shutil.rmtree("EFR32MG21")

#/hardware/kit/EFR32MG21_BRD4181A/config
if not os.path.isdir(project_folder + "/hardware/kit/EFRBG21"):
    os.chdir(project_folder + "/hardware/kit")
    listofFiles = os.listdir(os.getcwd())
    for file in listofFiles:
        if file.startswith("EFR32MG21"):
            file2 = file.replace("EFR32MG21" , "EFR32BG21")
            os.rename(file,file2)

#/Binaries
if not os.path.isdir(project_folder + "/protocol/bluetooth/lib/EFR32BG21"):
    os.chdir(project_folder + "/protocol/bluetooth/lib")
    listofFiles = os.listdir(os.getcwd())
    for file in listofFiles:
        if file.startswith("EFR32MG21"):
            file2 = file.replace("EFR32MG21" , "EFR32BG21")
            os.rename(file,file2)

#It goes back to the project folder
os.chdir(project_folder)

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
#in case converting SSv4 BLE project, it will copy the desired Linker Script file into the project
    if i.endswith(".ld"):
        destinationP = os.getcwd()
        sourceP = legacysdksPATH + sdkchoice + legacybleLinkerScriptPATH + devicelower + ".ld"
        copy(sourceP, destinationP)
        print(devicelower + ".ld copied")




#replaceXG2(ISC, device)
#replaceXG2(SLCP, device)
#replaceXG2(SLPS, device)
#replaceXG2(PINTOOL, device)

#It checks if there is a compiler output folder and removes it
if os.path.isdir(project_folder + "/GNU ARM v7.2.1 - Debug"):
    os.chdir(project_folder + "/GNU ARM v7.2.1 - Debug")
    replaceXG2("makefile", device)
    #shutil.rmtree("GNU ARM v7.2.1 - Debug")
    #print "Compiler Output Directory removed"
#else:
#        print "Compiler Output Directory not present"

if os.path.isdir(project_folder + "/GNU ARM v7.2.1 - Default"):
    os.chdir(project_folder + "/GNU ARM v7.2.1 - Default")
    replaceXG2("makefile", device)


    #print(project_folder + "/GNU ARM v7.2.1 - Default")
    #shutil.rmtree(project_folder + "/GNU ARM v7.2.1 - Default")
    #print "Compiler Output Directory removed"

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

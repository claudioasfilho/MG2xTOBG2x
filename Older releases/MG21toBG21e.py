import os, shutil
from os import listdir
retval = os.getcwd()
print "Current working directory %s" % retval

def replaceXG2(file):
    fin = open(file, "rt")
    data = fin.read()
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


replaceXG2(".project")
replaceXG2(".cproject")

#Searches for specific file extentions and assign them to variables
x = os.listdir(os.getcwd())

for i in x:
    if i.endswith(".slcp"):
        SLCP = i
        print(SLCP)
    if i.endswith(".slps"):
        SLPS = i
        print(SLPS)
    if i.endswith(".pintool"):
        PINTOOL = i
        print(PINTOOL)


replaceXG2(SLCP)
replaceXG2(SLPS)
replaceXG2(PINTOOL)

#It checks if there is a compiler output folder and removes it
if os.path.isdir(os.getcwd()+ "/GNU ARM v7.2.1 - Debug"):
    shutil.rmtree("GNU ARM v7.2.1 - Debug")
    print "Compiler Output Directory removed"
else:
    print "Compiler Output Directory not present"

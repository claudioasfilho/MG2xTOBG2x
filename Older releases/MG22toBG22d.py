import os, shutil
retval = os.getcwd()
print "Current working directory %s" % retval

def replaceXG2(file):
    fin = open(file, "rt")
    data = fin.read()
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


replaceXG2(".project")
replaceXG2(".cproject")


shutil.rmtree("GNU ARM v7.2.1 - Debug")
print "Compiler Output folder removed"

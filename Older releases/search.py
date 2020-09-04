import os
import fnmatch

retval = os.getcwd()

with open("test.txt", "w") as myfile:
   for root, dirs, files in os.walk(retval):
       for file in files:
           with open(os.path.join(root, file)) as f:
              for line in f:
                 if "mg21" in line:
                     print file, ": ", line.rstrip()
                     summary = file, ": ", line.rstrip(),"\r"
                     myfile.write(''.join(summary))

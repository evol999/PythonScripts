import os
from os import walk
import sys

#1 define paths to check
Path1 = r'C:\USB Packages\Datafast\Mockup Datafast Ver 3.0.00 - Test EMV Keys - No Crypto Keys\TELIUM\02_App Ver 3.0.00 - Mockup\HOST'
# Path1 = r'C:\USB Packages\Datafast\Mockup Datafast Ver 3.0.00 - Test EMV Keys - No Crypto Keys\TELIUM\02_App Ver 3.0.00 - Mockup\HOST'
# Path2 = r'C:\USB Packages\Datafast\Produccion Datafast Ver 3.0.00 - Produccion EMV Keys - Check Crypto Keys\TELIUM\02_Application\HOST'
# Path3 = r'C:\USB Packages\Datafast\Produccion Datafast Ver 3.0.00 - Produccion EMV Keys - Check Crypto Keys\TELIUM\02_Application - Inyectar llaves\HOST'

def dirToUpper(path):
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    for x in f:
        if x.isupper() != True:
            os.rename(path + '\\' + x, path + '\\' + x.upper())
            print("File: {0} renamed to: {1}".format(x, x.upper()))
        else:
            print("File: {0} not changed".format(x))
        print("\n")

print("Files in Path1")
dirToUpper(Path1)
# print("Files in Path2")
# dirToUpper(Path2)
# print("Files in Path3")
# dirToUpper(Path3)

    

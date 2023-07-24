from os import walk
import sys
import hashlib
import shutil

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

#1 define paths to check
# Path1 = r'C:\USB Packages\Datafast\Mockup Datafast Ver 3.0.00 - Test EMV Keys - No Crypto Keys\TELIUM\02_App Ver 3.0.00 - Mockup\HOST'
# Path2 = r'C:\USB Packages\Datafast\Produccion Datafast Ver 3.0.00 - Produccion EMV Keys - Check Crypto Keys\TELIUM\02_Application\HOST'
# Path3 = r'C:\USB Packages\Datafast\Produccion Datafast Ver 3.0.00 - Produccion EMV Keys - Check Crypto Keys\TELIUM\02_Application - Inyectar llaves\HOST'
Path1 = r'C:\USB Packages\Datafast\Mockup Datafast Ver 3.0.00 - Test EMV Keys - No Crypto Keys - Payblue\TELIUM\02_App Ver 3.0.00 - Mockup\HOST'
Path2 = r'C:\USB Packages\Datafast\Produccion Datafast Ver 3.0.00 - Produccion EMV Keys - Check Crypto Keys - Payblue\TELIUM\02_Application\HOST'
Path3 = r'C:\USB Packages\Datafast\Produccion Datafast Ver 3.0.00 - Produccion EMV Keys - Check Crypto Keys - Payblue\TELIUM\02_Application - Inyectar llaves\HOST'

def getMD5s(path):
    f = []
    d = {}
    #2 get list
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    for x in f:
        md5 = hashlib.md5()
        with open(path + '\\' + x, 'rb') as file:
            while True:
                data = file.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
        print("File: {0} MD5: {1}".format(x, md5.hexdigest()))
        d[x]= md5.hexdigest()
    print("\n")
    return d

dictionary = {}
print("Files in Path1")
dictionary[1] = getMD5s(Path1)
print("Files in Path2")
dictionary[2] = getMD5s(Path2)
print("Files in Path3")
dictionary[3] = getMD5s(Path3)

for File in dictionary[1].keys():
    if(File in dictionary[2].keys()):
        if dictionary[1][File] !=  dictionary[2][File]:
            print("File {0} in Path1 and Path2 NOT OK!!!".format(File))
            shutil.copy(Path1 + '\\' + File, Path2 + '\\' + File)
            print("File {0} has been upadted in Path2".format(File))
    if(File in dictionary[3].keys()):
        if dictionary[1][File] !=  dictionary[3][File]:
            print("File {0} in Path1 and Path3 NOT OK!!!".format(File))
            shutil.copy(Path1 + '\\' + File, Path3 + '\\' + File)
            print("File {0} has been upadted in Path3".format(File))

    

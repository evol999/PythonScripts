from os import walk
import os
import sys
import hashlib
import shutil

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

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
        d[x.upper()]= md5.hexdigest()
    print("\n")
    return d

# dictionary of working variables
workingVars = { 
'lastProd':r'C:\TEMP EM\001',
'newProd':r'C:\USB Packages\Datafast\Produccion Datafast Ver 3.0.00 - Produccion EMV Keys - Check Crypto Keys - Payblue',
'output':r'C:\TEMP EM\002',
'Telium':"TELIUM",
'Man':"01_OS_Manager",
'App':"02_Application",
'Dat':"HOST"
}

# 1) Find what is missing / has changed
dictionary = {}
print("Loading flies in lastProd")
sourceString = workingVars['lastProd'] + '\\' + workingVars['Telium'] + '\\' + workingVars['Man']
print(sourceString)
dictionary[1] = getMD5s(sourceString)
sourceString = workingVars['lastProd'] + '\\' + workingVars['Telium'] + '\\' + workingVars['App']
print(sourceString)
dictionary[2] = getMD5s(sourceString)
sourceString = workingVars['lastProd'] + '\\' + workingVars['Telium'] + '\\' + workingVars['App'] + '\\' + workingVars['Dat']
print(sourceString)
dictionary[3] = getMD5s(sourceString)

print("Loading flies in newProd")
sourceString = workingVars['newProd'] + '\\' + workingVars['Telium'] + '\\' + workingVars['Man']
print(sourceString)
dictionary[4] = getMD5s(sourceString)
sourceString = workingVars['newProd'] + '\\' + workingVars['Telium'] + '\\' + workingVars['App']
print(sourceString)
dictionary[5] = getMD5s(sourceString)
sourceString = workingVars['newProd'] + '\\' + workingVars['Telium'] + '\\' + workingVars['App'] + '\\' + workingVars['Dat']
print(sourceString)
dictionary[6] = getMD5s(sourceString)


# 2) copy new / altered file to output
for File in dictionary[4].keys():
    sourceString = workingVars['newProd'] + '\\' + workingVars['Telium'] + '\\' + workingVars['Man'] + '\\'
    destinyString = workingVars['output'] + '\\'
    if(File in dictionary[1].keys()):
        if dictionary[4][File] !=  dictionary[1][File]:
            shutil.copy( sourceString + File, destinyString + File)
            print("File {0} in lastProd has changed!!!".format(File))
    else:
        shutil.copy(sourceString + '\\' + File, destinyString + File)
        print("File {0} has been added to output".format(File))

for File in dictionary[5].keys():
    sourceString = workingVars['newProd'] + '\\' + workingVars['Telium'] + '\\' + workingVars['App'] + '\\'
    destinyString = workingVars['output'] + '\\'
    if(File in dictionary[2].keys()):
        if dictionary[5][File] !=  dictionary[2][File]:
            shutil.copy(sourceString + File,  destinyString + File)
            print("File {0} in lastProd has changed!!!".format(File))
    else:
        shutil.copy(sourceString + File, destinyString + File)
        print("File {0} has been added to output".format(File))

for File in dictionary[6].keys():
    sourceString = workingVars['newProd'] + '\\' + workingVars['Telium'] + '\\' + workingVars['App'] + '\\' + workingVars['Dat'] + '\\'
    destinyString = workingVars['output'] + '\\' + workingVars['Dat'] + '\\'
    if(File in dictionary[3].keys()):
        if dictionary[6][File] !=  dictionary[3][File]:
            shutil.copy(sourceString + File, destinyString + File)
            print("File {0} in lastProd has changed!!!".format(File))
    else:
        shutil.copy(sourceString + File, destinyString + File)
        print("File {0} has been added to output".format(File))

# 3) create catalogs for changed files
# delete .M40 and .M44 files
destinyString = workingVars['output'] + '\\'
# files = os.listdir(destinyString)

catalog = []
for file in os.listdir(destinyString):
    path = os.path.join(destinyString, file)
    if os.path.isdir(path):
        # skip directories
        continue
    if (file.endswith(".M40") or file.endswith(".M44")):
        os.remove(os.path.join(destinyString,file))
    else:
        catalog.append(file)

f=open(destinyString + 'CATALOG.M40','w')
for fileName in catalog:
    f.write(fileName+'\n')
f.close()

f=open(destinyString + 'CATALOG.M44','w')
for fileName in catalog:
    f.write(fileName+'\n')
f.close()


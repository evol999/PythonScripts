#TODO dictionary with customer name and configuration.
import pprint
import logging
import sys
#import getch
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
Configuration = {
'SDKPATH': 'C:\\Tools\\TeliumSDK',
'Customer': 'Datafast',
}

Packages = {
1: {'Profile': 'DF PROD NO WiFi',
'Customer': 'Datafast',
'Type': 'Debug',
'SDK': '9.30.1.02',
'Terminal': 'iCT220',
'OS': 'ICT2XX_MOCKUP',
'Manager': 'iCT_GOAL_EXPORT_PROD',
'GPRS': 'DLL_ExtraGPRS',
'EASY PATH EMV': '22.10.0.00',
'EMV KERNEL': 'DEBUG',
'FONTS': 'FONT_GOAL_LATIN',
'SSL': '',
'Extras': '8999990002.PGN'},
2: {'Profile': 'Datafast DEBUG',
'Customer': 'Datafast',
'Type': 'Debug',
'SDK': '9.30.1.02',
'Terminal': 'iWL250',
'OS': 'ICT2XX_MOCKUP',
'Manager': 'iCT_GOAL_EXPORT_PROD',
'GPRS': 'DLL_ExtraGPRS',
'EASY PATH EMV': '22.10.0.00',
'EMV KERNEL': 'DEBUG',
'FONTS': 'FONT_GOAL_LATIN',
'SSL': '',
'Extras': '8999990002.PGN'}
}
#pprint.pprint(Packages)

def CreatePackage(PackDictionary):
    #TODO 
    #print("Hola")
    #pprint.pprint(PackDictionary)
    #Create package folder name
    folder = PackDictionary['Type']
    folder = folder + " " + PackDictionary['Customer']
    logging.debug('folder = %s' % folder)
    #Make dir
    #
    
    return None
    

i = 1
for v in Packages.values():
    row = ""
    row = str(i)
    row += ")"
    row += v['Profile']
    print(row)
    i = i+1
row = ""
row = str(i) + ")" + "EXIT"
print(row)
row = input()
assert row.isdecimal(), 'wrong input'
j = int(row)
logging.debug('len = (%s)' % (len(Packages.values())))
logging.debug('j = (%s)' % (j))
assert (j>0 and j <= len(Packages.values())+1), 'Negative index'

if j == len(Packages.values())+1:
    print("Bye, bye.")
    sys.exit()
CreatePackage(Packages[j])



    



    


import os
from os import walk
import sys
import re

#1 define paths to check
File1 = r'C:\IRD\Datafast\sources\finantial\Inc\Tables.h'
File2 = r'C:\IRD\Core App\CoreApp\finantial\Inc\Tables.h'
def listAllTables(file):
	opened_file = open(file,'r')
	content = opened_file.read()
	structRegex = re.compile(r'typedef struct ([^\s]+)')
	structMatch = structRegex.findall(content)
	# print(structMatch)
	# retvalue = None
	# for match in structMatch:
		# retvalue += match[0]
	# return retvalue
		
	# for match in structMatch:
		# print(match[0])
	return structMatch

datafastTables = listAllTables(File1)
# print(type(datafastTables))
# print(datafastTables)
coreTables = listAllTables(File2)
# print(coreTables)
print("=========================================================================")
InCoreNotIn_DF = []
InBoth = []
InDF_NotInCore = []
for table in datafastTables:
    if(table in coreTables):
        # print("Table {0} in Datafast and Core Application!!!".format(table))
        InBoth.append(table)
    else:
        # print("Table {0} in Datafast but NOT in Core Application!!!".format(table))
        InDF_NotInCore.append(table)

print("=========================================================================")
for table in coreTables:
    # if(table in datafastTables):
    if(table not in datafastTables):
        # print("table {0} in Datafast and Core Application!!!".format(table))
    # else:
        # print("table {0} in Core but NOT in Datafast Application!!!".format(table))
        InCoreNotIn_DF.append(table)
print("=========================================================================")
print("In both")
print(InBoth)
print("=========================================================================")
print("Only in DF")
print(InDF_NotInCore)
print("=========================================================================")
print("Only in Core")
print(InCoreNotIn_DF)
print("=========================================================================")

#This code aims to find maximum midpoint count (next well-positioned nucleosome).
#The nucleosomes are derived as the highest midpoint bins that occur 128-220 bp downstream from the preceding nucleosome
#Under the condition that there is no start or end of another gene within 350 bp of the midpoint bin.

#As input, it requires directionality file (generated with find_which_gene.py), count file (count of nucleosomal (mid)position), and gene directionality file

#Directionality file looks like this (chr, start, end, directionality)
# chrI	2381	2390	-
# chrI	2658	2667	+
# chrI	9167	9176	-

#Count file looks like this (chr, start, end, count i.e. sum of values between start and end):
# chrI	1908	1917	329
# chrI	14324	14333	132
# chrI	21558	21567	145

#sacCer3_directionality.bed/gene directionality file contains gene coordinates and directionalities
# chrI	334	649	+
# chrI	537	792	+
# chrI	1806	2169	-

def getSafeKey(chrDict, point):
    if point in chrDict:
        return chrDict[point]
    return 0


def notNear(start, end, locationsDict):
    for location in locationsDict.keys():
        if abs(start - location) < 350 or abs(end - location) < 350:
            return False
    return True


directionalityFilename = input("Enter the name of the directionality file: ")
countFilename = input("Enter the name of the counts file: ")
thirdFileName = input("Enter the name of the sacCer file: ")
outputFilename = input("Enter the name of the output file: ")
directionalityFile = open(directionalityFilename)
countFile = open(countFilename)
thirdFile = open(thirdFileName)
outputFile = open(outputFilename, 'w')
chrDict = {}
for line in countFile:
    line = line.split()
    chromosome = line[0]
    if chromosome not in chrDict:
        chrDict[chromosome] = {}
    chrDict[chromosome][int(line[1]) + 5] = int(line[3])
thirdDict = {}
for line in thirdFile:
    line = line.split()
    chromosome = line[0]
    if chromosome not in thirdDict:
        thirdDict[chromosome] = {}
    if line[3] == '+':
        thirdDict[chromosome][int(line[1])] = ''
    else:
        thirdDict[chromosome][int(line[2])] = ''
for line in directionalityFile:
    line = line.split()
    countDict = chrDict[line[0]]
    midpoint = int(line[1]) + 5
    start = midpoint + 128
    end = midpoint + 220 + 1
    if line[3] == '-':
        start = midpoint - 220
        end = midpoint - 128 + 1
    if notNear(start, end, thirdDict[line[0]]):
        maxCount = 0
        for i in range(start, end):
            count = getSafeKey(countDict, i)
            if count > maxCount:
                inputStart = i - 5
                inputEnd = i + 4
                maxCount = count
        outputFile.write(line[0] + ' ' + str(inputStart) + ' ' + str(inputEnd) + ' ' + str(maxCount) + ' ' + line[3] + '\n')
outputFile.close()


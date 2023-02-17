#This code generates distribution of maximum isoform distances.
#Individual isoforms are put in the center of a defined 2x offset and it is asked whether an isoform is maximum according to intensity (compared to all the other isoforms within the window).
#If it is, it is asked what the next max isoform in the subsequent adjacent window (with the same 2x offset size) is, and then calculates the distance between the two.
# It generates distribution of these distances.


def getSafeKey(chrDict, point):
    if point in chrDict:
        return chrDict[point]
    return 0


def getMaxValue(chrDict, start, end):
    maxNumber = 0
    for i in range(start, end + 1):
        if getSafeKey(chrDict, i) > maxNumber:
            maxNumber = getSafeKey(chrDict, i)
    if maxNumber == 0:
        return -1
    for i in range(start, end + 1):
        if getSafeKey(chrDict, i) == maxNumber:
            return i


inputFilename = input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the genomic distance distribution: ")
outputFilename17 = input("Enter the name of the 17 distance distribution: ")
outputFilenameGL = input("Enter the name of the genomic maxIsoform list output file: ")
outputFilename17L = input("Enter the name of the 17 maxIsoform list output file: ")
offset = int(input("Input the offset: "))
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile, open(outputFilename17, 'w') as outputFile17, open(outputFilenameGL, 'w') as outputFileGL, open(outputFilename17L, 'w') as outputFile17L:
    dictionary = {}
    isPositive = True
    for line in inputFile:
        line = line.split()
        chromosome = line[0]
        position = int(line[1])
        count = float(line[2])
        if chromosome not in dictionary:
            dictionary[chromosome] = {}
        dictionary[chromosome][position] = count
        #if line[3] == '-':
            #isPositive = False
    genomicDistribution = {}
    seventeenDistribution = {}
    for chromosome, chrDict in dictionary.items():
        start = min(chrDict, key=int) + offset
        end = max(chrDict, key=int) - 3 * offset
        iterator = start
        while iterator <= end:
            maxPosition1 = getMaxValue(chrDict, iterator - offset, iterator + offset)
            maxPosition2 = getMaxValue(chrDict, iterator + offset + 1, iterator + 3 * offset + 1)
            if maxPosition1 != -1 and maxPosition2 != -1:
                difference = maxPosition2 - maxPosition1
                if chromosome == "chrXVII":
                    outputFile17L.write(chromosome + ' ' + str(maxPosition1) + '\n' + chromosome + ' ' + str(maxPosition2) + '\n')
                    if difference in seventeenDistribution:
                        seventeenDistribution[difference] = seventeenDistribution[difference] + 1
                    else:
                        seventeenDistribution[difference] = 1
                else:
                    outputFileGL.write(chromosome + ' ' + str(maxPosition1) + '\n' + chromosome + ' ' + str(maxPosition2) + '\n')
                    if difference in genomicDistribution:
                        genomicDistribution[difference] = genomicDistribution[difference] + 1
                    else:
                        genomicDistribution[difference] = 1
            iterator = iterator + 1
    for distance, count in genomicDistribution.items():
        outputFile.write(str(distance) + ' ' + str(count) + '\n')
    for distance, count in seventeenDistribution.items():
        outputFile17.write(str(distance) + ' ' + str(count) + '\n')
outputFile.close()
outputFile17.close()


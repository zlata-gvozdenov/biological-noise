#This code generates nucleotide frequencies for input fasta files for the range as defined “for i in range(0, 201)”.
# So 200 nt range can be extended or shortened (if the number is 1001, the nt frequency for the range within 500 up- and downstream of the reference point is calculated).
#The lead file (input file 1) is the fasta file based on which nucleotide frequency will be calculated (output file 4).
#The test file (input file 2) is the fasta file for which nt similarity score (of the test file to the lead file) is calculated (output file 3).
#Normalization_file is genomic occurrence of each nucleotide and for e.g. yeast looks like this:
    # A	0.309806405
    # T	0.308714945
    # C	0.190882287
    # G	0.190596363

import math


def getSafeKey(charDict, key):
    if key in charDict:
        return str(charDict[key])
    return '0'


inputFilename = input("Enter the name of the lead file: ")
testFilename = input("Enter the name of the test file: ")
normalizationFilename = "normalization_file"
outputFilename = input("Enter the name of the probability output file: ")
scoreFilename = input("Enter the name of the score output file: ")
inputFile = open(inputFilename)
testFile = open(testFilename)
normalizationFile = open(normalizationFilename)
outputFile = open(outputFilename, 'w')
scoreFile = open(scoreFilename, 'w')
normalization = {}
totalDict = {}
totalCount = 0.0
# raw counts
for line in normalizationFile:
    line = line.split()
    normalization[line[0]] = float(line[1])
while True:
    line1 = inputFile.readline()
    line2 = inputFile.readline().rstrip()
    if not line2:
        break
    totalCount = totalCount + 1.0
    length = len(line2)
    if length >= 200:
        for i in range(0, length):
            charCode = line2[i]
            if charCode not in totalDict:
                totalDict[charCode] = {}
            if i in totalDict[charCode]:
                totalDict[charCode][i] = totalDict[charCode][i] + 1
            else:
                totalDict[charCode][i] = 1
# normalized
for charCode, charDict in totalDict.items():
    for i in range(0, 201):
        if i in charDict:
            charDict[i] = math.log((float(charDict[i]) / totalCount) / normalization[charCode], 2)
for charCode, charDict in totalDict.items():
    outputFile.write(charCode + ' :')
    for i in range(0, 201):
        outputFile.write(' ' + getSafeKey(charDict, i))
    outputFile.write('\n')
inputFile.close()
outputFile.close()
# compute scores
while True:
    line1 = testFile.readline()
    line2 = testFile.readline().rstrip()
    if not line2:
        break
    line1 = line1.split(':')
    chromosome = line1[0][1:]
    coords = line1[1].split('-')
    start = int(coords[0])
    end = int(coords[1])
    length = len(line2)
    score = 0.0
    for i in range(0, length):
        charCode = line2[i]
        score = score + float(getSafeKey(totalDict[charCode], i))
    scoreFile.write(chromosome + ' ' + str(start) + ' ' + str(end) + ' ' + str(score) + '\n')
testFile.close()
scoreFile.close()

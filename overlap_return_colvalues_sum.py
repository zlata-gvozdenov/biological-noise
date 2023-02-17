#This code sums the values for defined intervals across different files
#All intervals are considered and present in the resulting output file

import math

inputFilename1 = input("Enter the name of the file 1: ")
inputFilename2 = input("Enter the name of the file 2: ")
#outputFilename = input("Enter the name of the output file: ")
outputFilename2 = input("Enter the name of the sum: ")
dictionary = {}
with open(inputFilename2) as inputFile2:
    for line2 in inputFile2:
        line2 = line2.split()
        chromosome2 = line2[0]
        start2 = int(line2[1])
        end2 = float(line2[2])
        if chromosome2 not in dictionary:
            dictionary[chromosome2] = {}
        dictionary[chromosome2][start2] = end2
with open(inputFilename1) as inputFile1:
    for line1 in inputFile1:
        line1 = line1.split()
        chromosome1 = line1[0]
        start1 = int(line1[1])
        end1 = float(line1[2])
        if chromosome1 not in dictionary:
            dictionary[chromosome1] = {}
        if start1 not in dictionary[chromosome1]:
            dictionary[chromosome1][start1] = end1
        else:
            dictionary[chromosome1][start1] = dictionary[chromosome1][start1] + end1
with open(outputFilename2, 'w') as outputFile2:
    for chromosome, chrDict in dictionary.items():
        for start, end in chrDict.items():
            outputFile2.write(chromosome + '\t' + str(start) + '\t' + str(end) + '\n')

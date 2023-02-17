# input file should be bed file from fragment_location.py
#number of total distinct (non-overlapping) midpoints will be displayed in console
#3rd and 4th outputs are genomic/chrXVII midpoint lists with chromosome- and position-specific midpoints rounded up
#3rd and 4th outputs format: (1st column) chromosome, (2nd column) midpoint position rounded up, (3rd column) number of midpoints at that position
#1st and 2nd outputs are midpoint frequency distributions for genomic and chrXVII (number of midpoints, number of times it occurs)
from __future__ import division
import math

inputFilename = input("Enter the name of the input file: ")
outputFilename1 = input("Enter the name of the output file for genomic midpoint distribution counts: ")
outputFilename2 = input("Enter the name of the output file for chromosome 17 midpoint distribution counts: ")
outputFilename3 = input("Enter the name of the output file for interim genomic midpoint list: ")
outputFilename4 = input("Enter the name of the output file for interim chrXVII midpoint list: ")
with open(inputFilename) as inputFile, open(outputFilename1, 'w') as outputFile1, open(outputFilename2, 'w') as outputFile2, open(outputFilename3, 'w') as outputFile3, open(outputFilename4, 'w') as outputFile4:
    totalCounts = {}
    seventeenCounts = {}
    for line in inputFile:
        splitLine = line.split()
        chromosome = splitLine[0]
        meanValue = math.ceil((float(splitLine[1]) + float(splitLine[2])) / 2)
        if chromosome != "chrM" and chromosome != "chrXVII":
            if chromosome not in totalCounts:
                totalCounts[chromosome] = {}
            if meanValue in totalCounts[chromosome]:
                totalCounts[chromosome][meanValue] = totalCounts[chromosome][meanValue] + 1
            else:
                totalCounts[chromosome][meanValue] = 1

        if chromosome == "chrXVII" and (int(splitLine[1]) > 3910) and (int(splitLine[2]) < 21879):
            if meanValue in seventeenCounts:
                seventeenCounts[meanValue] = seventeenCounts[meanValue] + 1
            else:
                seventeenCounts[meanValue] = 1
    print("In all chromosomes excluding M and XVII there are " + str(
        sum(len(chrDict.items()) for chrDict in totalCounts.values())) + " distinct mid points")
    print("In chromosome XVII there are " + str(len(seventeenCounts.items())) + " distinct mid points")
    # intermediary counting of each midpoint, per chromosome
    multipleCounts = {}
    for chromosome, chromosomeDict in totalCounts.items():
        for meanValue, count in chromosomeDict.items():
            outputFile3.write(chromosome + ' ' + str(meanValue) + ' ' + str(count) + '\n')
            if count in multipleCounts:
                multipleCounts[count] = multipleCounts[count] + 1
            else:
                multipleCounts[count] = 1
    totalCounts = {}
    # counts the number of overlapping intervals in chrXVII
    multipleCountsSeventeen = {}
    for meanValue, count in seventeenCounts.items():
        outputFile4.write(str(meanValue) + ' ' + str(count) + '\n')
        if count in multipleCountsSeventeen:
            multipleCountsSeventeen[count] = multipleCountsSeventeen[count] + 1
        else:
            multipleCountsSeventeen[count] = 1
    for count, value in multipleCounts.items():
        outputFile1.write(str(count) + ' ' + str(value) + '\n')
    for count, value in multipleCountsSeventeen.items():
        outputFile2.write(str(count) + ' ' + str(value) + '\n')
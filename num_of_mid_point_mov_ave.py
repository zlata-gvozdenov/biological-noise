# THIS IS MODIFICATION OF NUM_OF_MIDPOINTS.PY - NUMBER OF MIDPOINTS AT THE LOCATIONS WITH AND WITHOUT MOVING AVERAGE (BELOW SPECIFIED)
# input file should be bed file from fragment_location.py
#number of total distinct (non-overlapping) midpoints will be displayed in console (no moving average)
#3rd and 4th outputs are genomic/chrXVII midpoint lists with chromosome- and position-specific midpoints rounded up (no moving average)
#3rd and 4th outputs format: (1st column) chromosome, (2nd column) midpoint position rounded up, (3rd column) number of midpoints at that position
#1st and 2nd outputs are midpoint frequency distributions for genomic and chrXVII AFTER applying moving average (number of midpoints (column 1), number of times it occurs (column 2))
#5th and 6th outputs are the lists of midpoints (similarly to the 3rd and the 4th outputs) but AFTER moving average is applied
from __future__ import division


def getSafeValue(dictionary, key):
    if key in dictionary:
        return float(dictionary[key])
    return 0.0


def getSlidingAverage(dictionary, key, slidingWindowLength):
    key = int(key)
    slidingWindowLength = int(slidingWindowLength)
    end = key + slidingWindowLength - 1
    slidingSum = 0.0
    while key <= end:
        slidingSum = slidingSum + getSafeValue(dictionary, str(key))
        key = key + 1
    #if round(slidingSum / slidingWindowLength) != 0:
        #print(str(end - int(slidingWindowLength/2)) + ' ' + str(round(slidingSum / slidingWindowLength)) + '\n')
    return round(slidingSum / slidingWindowLength)


inputFilename = input("Enter the name of the input file: ")
outputFilename1 = input("Enter the name of the output file for genomic midpoint distribution count: ")
outputFilename2 = input("Enter the name of the output file for chromosome 17 midpoint distribution count: ")
outputFilename3 = input("Enter the name of the output file for genomic midpoints list: ")
outputFilename4 = input("Enter the name of the output file for chrXVII midpoints list: ")
outputFilename5 = input("Enter the name of the genomic interim sliding window: ")
outputFilename6 = input("Enter the name of the chrXVII interim sliding window: ")
slidingWindowLength = int(input("Enter the length of the sliding window: "))

inputFile = open(inputFilename)
outputFile1 = open(outputFilename1, 'w')
outputFile2 = open(outputFilename2, 'w')
outputFile3 = open(outputFilename3, 'w')
outputFile4 = open(outputFilename4, 'w')
outputFile5 = open(outputFilename5, 'w')
outputFile6 = open(outputFilename6, 'w')

totalCounts = {}
seventeenCounts = {}
for line in inputFile:
    splitLine = line.split()
    chromosome = splitLine[0]
    meanValue = round((float(splitLine[1]) + float(splitLine[2])) / 2 + 0.1)
    if chromosome != "chrM" and chromosome != "chrXVII":
        if chromosome not in totalCounts:
            totalCounts[chromosome] = {}
        if meanValue in totalCounts[chromosome]:
            totalCounts[chromosome][meanValue] = totalCounts[chromosome][meanValue] + 1
        else:
            totalCounts[chromosome][meanValue] = 1

    if chromosome == "chrXVII" and (int(splitLine[1]) > 3910) and (int(splitLine[2]) < 21879):
        meanValue = str(meanValue)
        if meanValue in seventeenCounts:
            seventeenCounts[meanValue] = seventeenCounts[meanValue] + 1
        else:
            seventeenCounts[meanValue] = 1
print("In all chromosomes excluding M and XVII there are " + str(
    sum(len(chrDict.items()) for chrDict in totalCounts.values())) + " distinct mid points")
print("In chromosome XVII there are " + str(len(seventeenCounts.items())) + " distinct mid points")
# intermediary counting of each midpoint, per chromosome
for chromosome, chromosomeDict in totalCounts.items():
    for meanValue, count in chromosomeDict.items():
        outputFile3.write(chromosome + ' ' + str(meanValue) + ' ' + str(count) + '\n')
totalCounts = None
outputFile3.close()
# counts the number of overlapping intervals in the genomic
lines = sorted(open(outputFilename3).readlines(), key=lambda line: float(line.split()[1]))
genomicDict = {}
for line in lines:
    line = line.split()
    if line[0] not in genomicDict:
        genomicDict[line[0]] = {}
    genomicDict[line[0]][line[1]] = line[2]
lines = None
genomicCounts = {}
for chromosome, chromosomeDict in genomicDict.items():
    minValue = int(min(chromosomeDict, key=int))
    maxValue = int(max(chromosomeDict, key=int))
    for i in range(minValue - int(slidingWindowLength/2), maxValue - int(slidingWindowLength/2) + 2):
        slidingSum = getSlidingAverage(chromosomeDict, i, slidingWindowLength)
        outputFile5.write(chromosome + ' ' + str(i) + ' ' + str(slidingSum) + '\n')
        if slidingSum != 0:
            if slidingSum in genomicCounts:
                genomicCounts[slidingSum] = genomicCounts[slidingSum] + 1
            else:
                genomicCounts[slidingSum] = 1
for count, value in genomicCounts.items():
    outputFile1.write(str(count) + ' ' + str(value) + '\n')
genomicCounts = None
# counts the number of overlapping intervals in chrXVII
for meanValue, count in seventeenCounts.items():
    outputFile4.write(str(meanValue) + ' ' + str(count) + '\n')
multipleCountsSeventeen = {}
minValue = int(min(seventeenCounts, key=int))
maxValue = int(max(seventeenCounts, key=int))
for i in range(minValue - int(slidingWindowLength/2), maxValue - int(slidingWindowLength/2) + 2):
    slidingSum = getSlidingAverage(seventeenCounts, i, slidingWindowLength)
    outputFile6.write("chrXVII " + str(i) + ' ' + str(slidingSum) + '\n')
    if slidingSum != 0:
        if slidingSum in multipleCountsSeventeen:
            multipleCountsSeventeen[slidingSum] = multipleCountsSeventeen[slidingSum] + 1
        else:
            multipleCountsSeventeen[slidingSum] = 1
outputFile4.close()
for count, value in multipleCountsSeventeen.items():
    outputFile2.write(str(count) + ' ' + str(value) + '\n')
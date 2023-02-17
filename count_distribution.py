#This code calculates distribution of counts present within 3rd column (specified in line 11)
import math
inputFilename=input("Enter the name of the input file: ")
outputFilenameOne = input("Enter the name of genomic distribution: ")
outputFilenameTwo = input("Enter the name of chrXVII distribution: ")
with open(inputFilename) as inputFile, open(outputFilenameOne, 'w') as outputFileOne, open(outputFilenameTwo, 'w') as outputFileTwo:
    largeMeasurements = {}
    smallMeasurements = {}
    for line in inputFile:
        line = line.split()
        count = int(float(line[2]))
        if line[0] != "chrM" and line[0] != "chrXVII":
            if count in largeMeasurements:
                largeMeasurements[count] = largeMeasurements[count] + 1
            else:
                largeMeasurements[count] = 1
        if line[0] == "chrXVII" and int(line[1]) > 3910 and int(line[1]) < 21879:
            if count in smallMeasurements:
                smallMeasurements[count] = smallMeasurements[count] + 1
            else:
                smallMeasurements[count] = 1
    for count, numberOfTimes in largeMeasurements.items():
        outputFileOne.write(str(count) + ' ' + str(numberOfTimes) + '\n')
    for count, numberOfTimes in smallMeasurements.items():
        outputFileTwo.write(str(count) + ' ' + str(numberOfTimes) + '\n')

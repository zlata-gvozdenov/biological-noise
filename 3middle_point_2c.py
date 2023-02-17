#input file should be bed file from fragment_location.py
#this code delivers midpoint locations, so only chr and midpoint location (x.5 values are rounded up)

inputFilename=input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the output file: ")
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile:
    for line in inputFile:
        line = line.split()
        meanValue = (float(line[1]) + float(line[2]))/2
        meanValueInt = int(meanValue)
        if meanValue > meanValueInt:
            meanValueInt = meanValueInt + 1
        outputFile.write(line[0] + ' ' + str(meanValueInt) + '\n')

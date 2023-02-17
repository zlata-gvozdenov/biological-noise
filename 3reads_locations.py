# input file should be "preppedWithoutTrimming_TruePolyAReads.out"
inputFilename = input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the output file: ")
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile:
    for line in inputFile:
        line = line.split()
        if line[2] == '-' or '+':
            #column5 = int(line[4]) + 1
            outputFile.write(line[3] + '\t' + line[4] + '\t' + line[4] + '\t' + 'x' + '\t' + 'y' + '\t' + line[2] + '\n')

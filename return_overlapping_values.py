# This code excludes file 2 coordinates (lines) not present in file 1
# File 2 has chr, position, and count; file 1 has chr, start position and end position

inputFilename1 = input("Enter the name of the selective regions file: ")
inputFilename2 = input("Enter the name of the count file: ")
outputFilename = input("Enter the name of the filtered output count file: ")
dictionary = {}
with open(inputFilename2) as inputFile2: #the one with the counts
    for line2 in inputFile2:
        line2 = line2.split()
        chromosome2 = line2[0]
        start2 = int(line2[1])
        count = int(line2[2])
        if chromosome2 not in dictionary:
            dictionary[chromosome2] = {}
        dictionary[chromosome2][start2] = count
with open(inputFilename1) as inputFile1, open(outputFilename, 'w') as outputFile:
    lineDict = {}
    for line1 in inputFile1:
        line1 = line1.split()
        chromosome1 = line1[0]
        start1 = int(line1[1])
        end1 = int(line1[2])
        if chromosome1 in dictionary:
            chrDict = dictionary[chromosome1]
            for i in range(start1, end1 + 1):
                if i in chrDict:
                    lineDict[chromosome1 + '\t' + str(i) + '\t' + str(chrDict[i]) + '\n'] = '' # '\t' + line1[3] + '\t' + line1[4] + '\t' + line1[5] + '\t' + line1[6] + '\t' + line1[7] + '\t' + line1[8] + '\n')
    for line in lineDict.keys():
        outputFile.write(line)

#This code counts values in file 1 if those are within the interval specified in file 2
#Output is file 1 count per defined file 2 interval
inputFilename1 = input("Enter the name of the input file 1: ")
inputFilename2 = input("Enter the name of the input file 2: ")
outputFilename = input("Enter the name of the output file: ")
dictionary = {}
with open(inputFilename1) as inputFile1:
    for line1 in inputFile1:
        line1 = line1.split()
        chromosome1 = line1[0]
        start1 = int(line1[1])
        number = float(line1[2])
        if chromosome1 not in dictionary:
            dictionary[chromosome1] = {}
        dictionary[chromosome1][start1] = number
with open(inputFilename2) as inputFile2, open(outputFilename, 'w') as outputFile:
    for line2 in inputFile2:
        line2 = line2.split()
        chromosome2 = line2[0]
        start2 = int(line2[1])
        end2 = int(line2[2])
        count = 0
        if chromosome2 in dictionary:
            chrDict = dictionary[chromosome2]
            for i in range(start2, end2 + 1):
                if i in chrDict:
                    count = count + chrDict[i]
            outputFile.write(chromosome2 + '\t' + str(start2) + '\t' + str(end2) + '\t' + str(count) + '\n')




#Fragments are converted to single position (chr, start, end is converted to chr, position, coverage)
inputFilename = input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the output file: ")
dictionary = {}
with open(inputFilename) as inputFile:
    for line in inputFile:
        line = line.split()
        chromosome = line[0]
        start = int(line[1])
        end = int(line[2])
        sense = line[3] #can be line[5] too
        if sense not in dictionary:
            dictionary[sense] = {}
        if chromosome not in dictionary[sense]:
            dictionary[sense][chromosome] = {}
        chrDict = dictionary[sense][chromosome]
        for i in range(start, end + 1):
            if i in chrDict:
                chrDict[i] = chrDict[i] + 1
            else:
                chrDict[i] = 1
with open(outputFilename, 'w') as outputFile:
    for sense, chrDict in dictionary.items():
        for chromosome, counts in chrDict.items():
            for start, count in counts.items():
                outputFile.write(chromosome + '\t' + str(start) + '\t' + str(count) + '\t' + str(sense) + '\n')

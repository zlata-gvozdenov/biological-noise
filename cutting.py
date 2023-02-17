#input file should be bed file from fragment_location.bed
#this code calculates the occurrence of fragment ends, i.e. counts the number of cuts per bp position
#1st output file is the list with the number of cuttings per each bp position
#2nd and 3rd output are cutting frequency distributions for genomic and chrXVII (1st column is the number of cuts, 2nd column is the occurrence of these cuts)

inputFilename = input("Enter the name of the fragment input file: ")
outputFilenameList = input("Enter the name of the output cutting list: ")
outputFilenameGenomicCount = input("Enter the name of the output genomic cutting count: ")
outputFilename17Count = input("Enter the name of the output chrXVII cutting count: ")
with open(inputFilename) as inputFile, open(outputFilenameList, 'w') as outputFileList, open(outputFilenameGenomicCount, 'w') as outputFileGenomic, open(outputFilename17Count, 'w') as outputFile17:
    chrDict = {}
    for line in inputFile:
        line = line.split()
        if not line[0] in chrDict:
            chrDict[line[0]] = {}
        if line[1] in chrDict[line[0]]:
            chrDict[line[0]][line[1]] = chrDict[line[0]][line[1]] + 1
        else:
            chrDict[line[0]][line[1]] = 1
        if line[2] in chrDict[line[0]]:
            chrDict[line[0]][line[2]] = chrDict[line[0]][line[2]] + 1
        else:
            chrDict[line[0]][line[2]] = 1
    countsGenomic = {}
    counts17 = {}
    for chromosome, countDict in chrDict.items():
        for point, count in countDict.items():
            outputFileList.write(chromosome + ' ' + point + ' ' + str(count) + '\n')
            if chromosome != 'chrXVII' and chromosome != 'chrM':
                if count in countsGenomic:
                    countsGenomic[count] = countsGenomic[count] + 1
                else:
                    countsGenomic[count] = 1
            if chromosome == 'chrXVII':
                if count in counts17:
                    counts17[count] = counts17[count] + 1
                else:
                    counts17[count] = 1
    for count, numTimes in countsGenomic.items():
        outputFileGenomic.write(str(count) + ' ' + str(numTimes) + '\n')
    for count, numTimes in counts17.items():
        outputFile17.write(str(count) + ' ' + str(numTimes) + '\n')

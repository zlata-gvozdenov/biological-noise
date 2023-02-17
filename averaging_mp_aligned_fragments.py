#This code generates meta-points for plotting.
#It aligns all test midpoints to the same reference point and then averages midpoint counts 1000 bp up- and downstream of defined/reference midpoint position.
#Input files 1 and 2 are per bp midpoint counts (chr (column 1), position (column 2), midpoint count (column 3)).
#Input files 3 and 4 are to be aligned midpoint positions for which meta-plot needs to be generated.

def getSafeKey(chrDict, point):
    if point in chrDict:
        return chrDict[point]
    return 0


inputFilename = input("Enter the name of entire genomic mp list file: ")
#inputFilename17 = input("Enter the name of entire XVII mp list file: ")
testFileName1 = input("Enter the name of the genomic test file ie target mp list: ")
#testFileName2 = input("Enter the name of chrXVII test file ie target mp list: ")
outputFileName = input("Enter the name of the genomic output file: ")
#outputFileName17 = input("Enter the name of the chrXVII output file: ")
outputFile = open(outputFileName, 'w')
#outputFile17 = open(outputFileName17, 'w')
with open(inputFilename) as inputFile, open(testFileName1) as testFile1:
    chromosomes = {}
    for line in inputFile:
        line = line.split()
        if line[0] not in chromosomes:
            chromosomes[line[0]] = {}
        chromosomes[line[0]][int(line[1])] = float(line[2])
    #for line in inputFile17:
        #line = line.split()
        #if line[0] not in chromosomes:
            #chromosomes[line[0]] = {}
        #chromosomes[line[0]][int(line[1])] = int(line[2])
    values = []
    for line in testFile1:
        line = line.split()
        values.append((line[0], int(line[1])))
    for i in range(-500, 501):
        average = 0
        for chromosome, value in values:
            chrDict = chromosomes[chromosome]
            average = average + getSafeKey(chrDict, value + i)
        outputFile.write(str(average/len(values)) + '\n')
    values = []
    #for line in testFile2:
        #line = line.split()
        #values.append((line[0], int(line[1])))
    #for i in range(-999, 1001):
        #average = 0
        #for chromosome, value in values:
            #chrDict = chromosomes[chromosome]
            #average = average + getSafeKey(chrDict, value + i)
        #outputFile17.write(str(average/len(values)) + '\n')
outputFile.close()
#outputFile17.close()

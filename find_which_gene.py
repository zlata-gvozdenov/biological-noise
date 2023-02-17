#This code aims to identify directionality i.e gene associated with genomic position
#It is needed as an input for max_midpoint_count.py (finding +2, +3, etc. nucleosomes)
#Here, nucleosomal midpoint positions and gene directionality input files are needed

#Location file (e.g. nucleosomal midpoint positions) specifies chromosomes and positions (start end end of e.g. 10 bo interval)
# chrI 2082 2091
# chrI 14481 14490
# chrI 21418 21427
#
#sacCer3_directionality.bed file contains gene coordinates and directionalities
# chrI	334	649	+
# chrI	537	792	+
# chrI	1806	2169	-

locationsFilename = input("Enter the name of the location file for which associated gene directionality needs to be found: ")
genesFilename = input("Enter the name of the genes file: ")
outputFilename = input("Enter the name of the output file: ")
locationsFile = open(locationsFilename)
genesFile = open(genesFilename)
outputFile = open(outputFilename, 'w')
chrDict = {}
for line in genesFile:
    splitLine = line.split()
    chromosome = splitLine[0]
    if chromosome not in chrDict:
        chrDict[chromosome] = {}
    start = splitLine[1]
    if splitLine[3] == '-':
        start = splitLine[2]
    chrDict[chromosome][int(start)] = splitLine[3]
for line in locationsFile:
    line = line.split()
    genesDict = chrDict[line[0]]
    start = int(line[1]) + 5
    outputLine = min(genesDict.keys(), key=lambda x: abs(x - start))
    outputFile.write(line[0] + ' ' + line[1] + ' ' + line[2] + ' ' + genesDict[outputLine] + '\n')
outputFile.close()

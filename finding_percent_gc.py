#input is fasta file (e.g. 100 bp intervals of the genome)
#the code will output those coordinates whose GC content criteria (specified in console as lower and higher GC threshold) is fulfilled
inputFileName = input("Enter the name of the input file: ")
outputFileName = input("Enter the name of the output file: ")
inputFile = open(inputFileName)
outputFile = open(outputFileName, 'w')
percentageStart = input("From which GC percentage?: ")
percentageEnd = input("To which GC threshold?: ")
percentageStart = int(percentageStart)
percentageEnd = int(percentageEnd)
hasLines = True
while hasLines:
    chrLine = inputFile.readline()
    sequenceLine = inputFile.readline()
    if not chrLine or not sequenceLine:
        hasLines = False
        continue
    chrLine = chrLine.split(':')
    chromosome = chrLine[0][1:]
    coordinates = chrLine[1].split('-')
    start = int(coordinates[0]) + 1
    end = int(coordinates[1])
    count = sequenceLine.count('G') + sequenceLine.count('C')
    if percentageStart <= count <= percentageEnd and not (chromosome == "chrXVII" and (start < 3910 or 21879 < end)):
        outputFile.write(chromosome + ' ' + str(start) + ' ' + str(end) + '\n')
outputFile.close()

#This code identifies interval with differential read levels between pseudo-replicates
#Threshold is specified under while getDivision(wtDict, mtDict, wtScale, mtScale, intervalEnd) >= 2.0:

def getReads(bedFileName):
    chromosomeReads = {}
    bedFile = open(bedFileName)
    oldChromosome = ""
    posReads = {}
    negReads = {}
    fileHasLines = True
    while fileHasLines:
        line = bedFile.readline()
        if line == "":
            fileHasLines = False
        data = line.split()
        if len(data) > 0:
            chromosome = data[0]
        else:
            chromosome = ""
        if oldChromosome == "":
            oldChromosome = chromosome
        if chromosome == oldChromosome:
            start = int(data[1])
            end = int(data[2])
            reads = None
            if data[5] == "+":
                reads = posReads
            else:
                reads = negReads
            for i in range(start, end+1):
                if i not in reads:  # first read
                    reads[i] = 1
                else:  # at least one other read
                    reads[i] = reads[i] + 1
        elif (not fileHasLines) or len(posReads) > 0 or len(negReads) > 0:
            chromosomeReads[oldChromosome + '1'] = posReads
            chromosomeReads[oldChromosome + '0'] = negReads
            posReads = {}
            negReads = {}
            print(oldChromosome)
            oldChromosome = chromosome
    return chromosomeReads


def getSafeKey(rawDict, index):
    if index in rawDict:
        return float(rawDict[index])
    return 1


def getDivision(wtDict, mtDict, wtScale, mtScale, intervalEnd):
    wtKey = getSafeKey(wtDict, intervalEnd)
    mtKey = getSafeKey(mtDict, intervalEnd)
    if wtKey < 10.0 and mtKey < 10.0:
        return 0
    return (wtKey * wtScale) / (mtKey * mtScale)


def compareDicts(wtDict, mtDict, wtScale, mtScale, start, end, chromosome, outputFile):
    sense = chromosome[-1]
    if sense == '1':
        sense = '+'
    else:
        sense = '-'
    chromosome = chromosome[:-1]
    intervalStart = start
    while intervalStart < end:
        intervalEnd = intervalStart + 1
        foldValue = 0.0
        while getDivision(wtDict, mtDict, wtScale, mtScale, intervalEnd) >= 2.0:
            foldValue = foldValue + getDivision(wtDict, mtDict, wtScale, mtScale, intervalEnd)
            intervalEnd = intervalEnd + 1
        if intervalEnd - intervalStart > 1:
            foldValue = foldValue / (intervalEnd - intervalStart - 1)
            outputFile.write(chromosome + ' ' + str(intervalStart + 1) + ' ' + str(intervalEnd - 1) + ' ' + str(foldValue) + ' ' + sense + '\n')
        intervalStart = intervalEnd


# start point of the execution
# first, the reads
wtBedFileName = input("Enter the name of the wild type reads file: ")
mtBedFileName = input("Enter the name of the mutant reads file: ")
outputFileName = input("Enter the name of the output file: ")
outputFile = open(outputFileName, 'w')
wtScale = float(input("Enter the scale factor for wild type: "))
mtScale = float(input("Enter the scale factor for mutant: "))
wildTypeChromosomeReads = getReads(wtBedFileName)
mutantChromosomeReads = getReads(mtBedFileName)
for chromosome, wtDict in wildTypeChromosomeReads.items():
    mtDict = mutantChromosomeReads[chromosome]
    start = min(min(wtDict, key=int), min(mtDict, key=int))
    end = max(max(wtDict, key=int), max(mtDict, key=int))
    compareDicts(wtDict, mtDict, wtScale, mtScale, start, end, chromosome, outputFile)
    wtDict = None
    mtDict = None

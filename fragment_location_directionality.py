#Input file should be bed file that stems/is converted from bam file (paired-end sequencing bowtie alignment)
inputFilename=input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the output file: ")
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile:
    measurements = {}
    for line in inputFile:
        line = line.split()
        thirdcolumn = line[3].split('/')[0]
        thirdcolumn1 = line[3].split('/')[1]
        directionality = '' # start as empty by default
        if thirdcolumn1 == '1':
            directionality = line[5]
        qualityscore = thirdcolumn.split(':')
        hashvalue = line[0] + qualityscore[4] + qualityscore[5] + qualityscore[6]
        if hashvalue in measurements:
            value = measurements[hashvalue].split()
            if directionality == '': # if it's not populated, that means we had a '1' the first time around
                directionality = value[1]
            outputFile.write(line[0] + '\t' + value[0] + '\t' + line[2] + '\t' + 'x' + '\t' + 'y' + '\t' + directionality + '\n')
            del measurements[hashvalue]
        else:
            value = line[1]
            if directionality != '':
                value = value + ' ' + directionality # instead of storing only the 'start', we also store the directionality
            measurements[hashvalue] = value


#Input file should be bed file that stems/is converted from bam file for paired-end sequencing bowtie alignment
inputFilename=input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the output file: ")
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile:
    measurements = {}
    for line in inputFile:
        line = line.split()
        thirdcolumn = line[3].split('/')[0]
        qualityscore = thirdcolumn.split(':')
        hashvalue = line[0] + qualityscore[4] + qualityscore[5] + qualityscore[6]
        if hashvalue in measurements:
            outputFile.write(line[0] + ' ' + measurements[hashvalue] + ' ' + line[2] + '\n')
            del measurements[hashvalue]
        else:
            measurements[hashvalue] = line[1]

# input file should be bed obtained from bowtie-aligned bam
inputFilename = input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the output file: ")
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile:
    for line in inputFile:
        line = line.split()
        if line[5] == '+':
        #if line[5] == '-':
            #column5 = int(line[4]) + 1
            outputFile.write(line[0] + '\t' + line[2] + '\t' + line[2] + '\t' + line[3] + '\t' + line[4] + '\t' + '-' + '\n')
            #outputFile.write(line[0] + '\t' + line[2] + '\t' + line[2] + '\t' + line[3] + '\t' + line[4] + '\t' + line[5] + '\n')

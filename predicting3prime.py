#This code gives a 3'isoform nucleotide score for given (isoform) positions
#3'isoform file is a 3-column format with chromosome, position, and isoform count per position
#Mind that sacCer3_pCC1random_nochrM.fa or sacCer3_pCC1random_nochrM_complement.fa
#and score_matrix.bed and score_matrix_complement.bed are used depending on the strand
import math


def getSafeKey(chrDict, point):
    if point in chrDict:
        return chrDict[point]
    return 0


chrFileName = input("Enter the name of the chromosomes file; like sacCer3_pCC1random_nochrM.fa: ")
matricsFileName = input("Enter the name of the matrices file; like score_matrix.bed: ")
isoformFileName = input("Enter the name of the 3'isoform file: ")
outputFileName = input("Enter the name of the output file: ")
chrFile = open(chrFileName)
matricsFile = open(matricsFileName)
isoformFile = open(isoformFileName)
outputFile = open(outputFileName, 'w')
chromosomes = {}
chrValues = {}
chromosomeLengths = {}
chromosome = ''
for line in chrFile:
    line = line.rstrip()
    if line.startswith(">"):
        chromosome = line[1:]
        chromosomes[chromosome] = ''
    else:
        chromosomes[chromosome] = chromosomes[chromosome] + line
matrix = {'A': {}, 'C': {}, 'G': {}, 'T': {}}
for line in matricsFile:
    line = line.split()
    offset = int(line[0])
    matrix['A'][offset] = int(line[2])
    matrix['C'][offset] = int(line[3])
    matrix['G'][offset] = int(line[4])
    matrix['T'][offset] = int(line[5])
for chromosome, sequence in chromosomes.items():
    for position in range(25, len(sequence) - 25 - 1):
        product = 1
        for i in range(-25, 26):
            character = sequence[position + i]
            product = product * matrix[character][i]
        if chromosome not in chrValues:
            chrValues[chromosome] = {}
        chrValues[chromosome][position] = math.log10(product)
for line in isoformFile:
    line = line.split()
    chromosome = line[0]
    position = int(line[1])
    predictedScore = getSafeKey(chrValues[chromosome], position)
    actualScore = line[2]
    outputFile.write(chromosome + ' ' + str(position) + ' ' + str(predictedScore) + ' ' + actualScore + '\n')
outputFile.close()

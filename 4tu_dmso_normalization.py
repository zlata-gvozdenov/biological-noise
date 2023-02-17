#Input files are 3-column files (chromosome, nt position, and count per position)
#This code is run separately for plus and minus strand
#Normalization factor is specified in line 29 (an exemplary normalization constant here is 2.5)
import math

inputFilename1 = input("Enter the name of the 4tu file: ")
inputFilename2 = input("Enter the name of the dmso file: ")
#outputFilename = input("Enter the name of the output file that combines 4tu and dmso count columns: ")
outputFilename2 = input("Enter the name of the subtracted and norm file: ")
dictionary = {}
with open(inputFilename2) as inputFile2:
    for line2 in inputFile2:
        line2 = line2.split()
        chromosome2 = line2[0]
        start2 = int(line2[1])
        end2 = int(line2[2])
        if chromosome2 not in dictionary:
            dictionary[chromosome2] = {}
        dictionary[chromosome2][start2] = end2
with open(inputFilename1) as inputFile1, open(outputFilename, 'w') as outputFile, open(outputFilename2, 'w') as outputFile2:
    for line1 in inputFile1:
        line1 = line1.split()
        chromosome1 = line1[0]
        start1 = int(line1[1])
        end1 = int(line1[2])
        #score = float(line1[3])
        if chromosome1 in dictionary and start1 in dictionary[chromosome1]:
            end2 = dictionary[chromosome1][start1]
            value = float(end1-(end2/2.5))
            if value < 0:
                value = end1 #value = 0
            #outputFile.write(chromosome1 + '\t' + line1[1] + '\t' + str(end2) + '\t' + str(end1) + '\n')
            outputFile2.write(chromosome1 + '\t' + line1[1] + '\t' + str(value) + '\n')
        else:
            #outputFile.write(chromosome1 + '\t' + line1[1] + '\t' + str(end1) + '\t' + str(end1) + '\n')
            outputFile2.write(chromosome1 + '\t' + line1[1] + '\t' + str(end1) + '\n')


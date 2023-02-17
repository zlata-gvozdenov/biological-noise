#This code combines RNA-seq count and 4tU-seq count files to create an input file for tpm.py.
#Each file has chromosomal location, start position, end position, and nt coverage count per defined start-end interval. It is run for each strand separately.

inputFilename1 = input("Enter the name of the input file 1: ")
inputFilename2 = input("Enter the name of the input file 2: ")
outputFilename = input("Enter the name of the output file with coordinates from file 1 and counts from file 1 and 2: ")
dictionary = {}
with open(inputFilename2) as inputFile2:
    for line2 in inputFile2:
        line2 = line2.split()
        chromosome2 = line2[0]
        start2 = int(line2[1])
        #end2 = int(line2[2])
        count2 = float(line2[3])
        if chromosome2 not in dictionary:
            dictionary[chromosome2] = {}
        dictionary[chromosome2][start2] = count2
with open(inputFilename1) as inputFile1, open(outputFilename, 'w') as outputFile:
    for line1 in inputFile1:
        line1 = line1.split()
        chromosome1 = line1[0]
        start1 = int(line1[1])
        end1 = int(line1[2])
        count1 = float(line1[3])
        if chromosome1 in dictionary:
            chrDict = dictionary[chromosome1]
            for start2, count2 in chrDict.items():
                if start1 == start2:
                    outputFile.write(chromosome1 + '\t' + line1[1] + '\t' + line1[2] + '\t' + str(count1) + '\t' + str(count2) + '\n')
                    break

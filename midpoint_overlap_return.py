# input file should be midpoint list file from num_of_mid_pints.py
# 3rd column is count (this is not a classical bed file but chr, position, count per position)
# it finds whether midpoint regions defined in file1 (sample input) are found within the intervals defined in file2 (e.g. intergenic)
inputFilename1 = input("Enter the name of the sample input file: ")
inputFilename2 = input("Enter the name of the intergenic input file: ")
outputFilename = input("Enter the name of the output file for midpoints within intergenic intervals: ")
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
with open(inputFilename1) as inputFile1, open(outputFilename, 'w') as outputFile:
    for line1 in inputFile1:
        line1 = line1.split()
        chromosome1 = line1[0]
        start1 = int(line1[1])
        end1 = int(line1[2])
        if chromosome1 in dictionary:
            chrDict = dictionary[chromosome1]
            for start2, end2 in chrDict.items():
                if start2 <= start1 <= end2 and end1 <= end2:
                #if start1 in range(start2, end2) and chromosome1 == chromosome2:
                #line1.append(line1[1])
                    outputFile.write(chromosome1 + '\t' + line1[1] + '\t' + line1[2] + '\n')
                    break

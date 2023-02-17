#This file removes duplicates considering both pairs of the paired end sequencing reads and the alignment location
#first input file - fastq for pair 1
#second input file - fastq for pair 2
#third input file - bed file generated from bowtie-aligned bam (with bamtobed)
#first output file - filtered (duplicate-free) fastq for pair 1
#second output file - filtered (duplicate-free) fastq for pair 2
#The length of the sequence to match is the length of the fastq reads for duplicate consideration
#This code needs 16 GB RAM

inputFilename1 = input("Enter the name of the first file: ")
inputFilename2 = input("Enter the name of the second file: ")
inputFilename3 = input("Enter the name of the third file: ")
outputFilename1 = input("Enter the name of the first output file: ")
outputFilename2 = input("Enter the name of the second output file: ")
seqLength = int(input("Enter the length of the sequence to match: "))
inputFile1 = open(inputFilename1)
inputFile2 = open(inputFilename2)
inputFile3 = open(inputFilename3)
outputFile1 = open(outputFilename1, 'w')
outputFile2 = open(outputFilename2, 'w')
hasLines = True
identifierDict = {}
for line in inputFile3:
    line = line.split()
    hashValue = line[0] + ' ' + line[1] + ' ' + line[2]
    value = [None] * 2
    line[3] = line[3].split('/')
    if line[3][0] not in identifierDict:
        identifierDict[line[3][0]] = value
    # store chromosome and position in the array
    if line[3][1] == '1':
        identifierDict[line[3][0]][0] = hashValue
    else:
        identifierDict[line[3][0]][1] = hashValue
file1dict = {}
lines = [None] * 4
while True:
    lines[0] = inputFile1.readline()
    if not lines[0]:
        break
    lines[1] = inputFile1.readline()
    lines[2] = inputFile1.readline()
    lines[3] = inputFile1.readline()
    identifier = lines[0][1:].split()[0]
    sequence = lines[1][:seqLength]
    if 'N' in lines[1]:
        continue
    hashValue = lines[0] + lines[1] + lines[2] + lines[3]
    if identifier in identifierDict:
        file1dict[identifier] = (sequence, hashValue)
file2dict = {}
while True:
    lines[0] = inputFile2.readline()
    if not lines[0]:
        break
    lines[1] = inputFile2.readline()
    lines[2] = inputFile2.readline()
    lines[3] = inputFile2.readline()
    identifier = lines[0][1:].split()[0]
    sequence = lines[1][:seqLength]
    if 'N' in lines[1]:
        continue
    hashValue = lines[0] + lines[1] + lines[2] + lines[3]
    if identifier in identifierDict:
        file2dict[identifier] = (sequence, hashValue)
# same sequence and same position
locationsDict1 = {}
locationsDict2 = {}
for identifier, hashValues in identifierDict.items():
    # both entries should have an identifier in the .bed file
    if identifier in file1dict and identifier in file2dict:
        # combine the sequence and the location to check for duplicates
        hashValue1 = file1dict[identifier][0] + ' ' + hashValues[0]
        hashValue2 = file2dict[identifier][0] + ' ' + hashValues[1]
        if hashValue1 not in locationsDict1 and hashValue2 not in locationsDict2:
            locationsDict1[hashValue1] = ''
            locationsDict2[hashValue2] = ''
            outputFile1.write(file1dict[identifier][1])
            file1dict[identifier] = (file1dict[identifier][0], '')
            outputFile2.write(file2dict[identifier][1])
            file2dict[identifier] = (file2dict[identifier][0], '')
outputFile1.close()
outputFile2.close()

#input file should be bed file from fragment_location.py
#this code calculates distribution of fragment sizes i.e lengths
#output: lenght, number of times it occurs

inputFilename=input("Enter the name of the input file: ")
outputFilenameOne = input("Enter the name of genomic fragment distribution: ")
outputFilenameTwo = input("Enter the name of chrXVII fragment distribution: ")
with open(inputFilename) as inputFile, open(outputFilenameOne, 'w') as outputFileOne, open(outputFilenameTwo, 'w') as outputFileTwo:
    largeMeasurements = {}
    smallMeasurements = {}
    for line in inputFile:
        line = line.split()
        difference = int(line[2]) - int(line[1])
        if line[0] != "chrM" and line[0] != "chrXVII":
            if difference in largeMeasurements:
                largeMeasurements[difference] = largeMeasurements[difference] + 1
            else:
                largeMeasurements[difference] = 1
        if line[0] != "chrM" and line[0] == "chrXVII" and int(line[1]) > 3910 and int(line[2]) < 21879:
            if difference in smallMeasurements:
                smallMeasurements[difference] = smallMeasurements[difference] + 1
            else:
                smallMeasurements[difference] = 1
    for difference, count in largeMeasurements.items():
        outputFileOne.write(str(difference) + ' ' + str(count) + '\n')
    for difference, count in smallMeasurements.items():
        outputFileTwo.write(str(difference) + ' ' + str(count) + '\n')

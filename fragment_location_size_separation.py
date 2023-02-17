#input file should be bed file from fragment_location.py
#this code delivers fragments that satisfy length criteria, specified under min and max, and delivers results in the same bed format as fragment_location.py output
inputFilename=input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the output file: ")
minLength = int(input("Enter the minimum length: "))
maxLength = int(input("Enter the maximum length: "))
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile:
    measurements = {}
    for line in inputFile:
        line = line.split()
        chromosome = line[0]
        start = int(line[1])
        end = int(line[2])
        if (chromosome != 'chrM') and ((chromosome != 'chrXVII') or (chromosome == 'chrXVII' and start > 3910 and end < 21879)):
            length = end - start
            if minLength <= length <= maxLength:
                outputFile.write(chromosome + ' ' + line[1] + ' ' + line[2] + '\n')

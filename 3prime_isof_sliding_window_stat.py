#This code calculates various 3'isoforms features by applying sliding window tactics
#Input file is a simple isoform file (chromosome, location, count of the isoforms per location)
#Done for each strand separately
#Ouput: chromosome, position, count, percent of the total maximum isoform signal within the sliding window, number of distinct isoforms within the window, position of the leftmost isoform, position of the rightmost isoform, distance between the leftmost and rightmost, middle position of the window

def getSafeKey(chrDict, point):
    if point in chrDict:
        return chrDict[point]
    return 0


inputFilename = input("Enter the name of the input file: ")
outputFilename = input("Enter the name of output file: ")
offset = int(input("Input the offset i.e. 1/2 of desired sliding window size (nt): "))
threshold = int(input("Input the threshold i.e. minimum % for the maximum isoform signal fraction per window: "))
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile:
    dictionary = {}
    isPositive = True
    for line in inputFile:
        line = line.split()
        chromosome = line[0]
        position = int(line[1])
        count = float(line[2])
        if chromosome not in dictionary:
            dictionary[chromosome] = {}
        dictionary[chromosome][position] = count
        if line[3] == '-':
            isPositive = False
    for chromosome, chrDict in dictionary.items():
        start = min(chrDict, key=int) - 2 * offset
        end = max(chrDict, key=int) + 2 * offset
        iterator = start
        while iterator <= end:
            highest = 0
            totalSum = 0
            numCoordinates = 0
            position = start
            for i in range(iterator - offset, iterator + offset + 1):
                safeKey = getSafeKey(chrDict, i)
                totalSum = totalSum + safeKey
                if highest <= safeKey:
                    highest = safeKey
                if safeKey != 0:
                    numCoordinates = numCoordinates + 1
            for i in range(iterator - offset, iterator + offset + 1):
                if highest == getSafeKey(chrDict, i):
                    position = i
                    break
            if totalSum > 0:
                leftMost = iterator - offset
                while getSafeKey(chrDict, leftMost) == 0:
                    leftMost = leftMost + 1
                rightMost = iterator + offset
                while getSafeKey(chrDict, rightMost) == 0:
                    rightMost = rightMost - 1
                distance = rightMost - leftMost
                if not isPositive:
                    temp = leftMost
                    leftMost = rightMost
                    rightMost = temp
                percentage = round(highest * 100.0 / totalSum, 1)
                if percentage >= threshold:
                    outputFile.write(chromosome + ' ' + str(position) + ' ' + str(getSafeKey(chrDict, position)) + ' ' + str(percentage) + ' ' + str(numCoordinates) + ' ' + str(leftMost) + ' ' + str(rightMost) + ' ' + str(distance) + ' ' + str(iterator) + '\n')
            iterator = iterator + 1
outputFile.close()

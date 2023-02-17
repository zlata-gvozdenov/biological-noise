# input file should be chrall_length_modified as below (start i.e. 1 is added as the 2nd column, and end is modified with +1 (python thing))
# chrI	1	230219
# chrII	1	813185
# chrIII	1	316621
# chrIV	1	1531934
# chrIX	1	439889
# chrV	1	576875
# chrVI	1	270162
# chrVII	1	1090941
# chrVIII	1	562644
# chrX	1	745752
# chrXI	1	666817
# chrXII	1	1078178
# chrXIII	1	924432
# chrXIV	1	784334
# chrXV	1	1091292
# chrXVI	1	948067
# chrXVII	3911	21879

# output is 10 bp interval for every genomic position (overlapping, +1 sliding intervals)

inputFilename = input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the output file: ")
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile:
    count = 0
    for line in inputFile:
        line = line.split()
        chromosome = line[0]
        start = int(line[1])
        end = int(line[2])
        for i in range(start, end):
            count = i + 9
            if count < end:
                outputFile.write(chromosome + '\t' + str(i) + '\t' + str(count) + '\n')

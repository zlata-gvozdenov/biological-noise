#this code needs midpoints for the treated sample (MNased chromatin) and midpoints for the control sample (MNased genomic DNA)
#these files are generated in 3middle_point_corrected_2c.py
#this code counts the number of midpoints in control and treated sample, retaining the information about the location
#it then scales all counts with a normalization factor (*10000000/total#reads for that sample), which is specified in console
#1st and 2nd outputs are bed-like files with chr (column 1), location (column 2) and number of midpoints at location (column 3) in treated sample after control subtraction
#3rd file is frequency distribution count of midpoints after subtraction (number of midpoints, number of times it occurs)


treatFilename = input("Enter the name of the treated file: ")
controlFilename = input("Enter the name of the control file: ")
genomicOutputFilename = input("Enter the name of the genomic output file: ")
chr17OutputFilename = input("Enter the name of the chr17 output file: ")
genomicOutputCountFileName = input("Enter the name of the genomic count output file: ")
normalizationTreat = float(input("Enter the normalization factor for the treated: "))
normalizationControl = float(input("Enter the normalization factor for the control: "))

with open(treatFilename) as treatFile, open(controlFilename) as controlFile, open(genomicOutputFilename, 'w') as genomicOutputFile, open(chr17OutputFilename, 'w') as chr17OutputFile, open(genomicOutputCountFileName, 'w') as genomicOutputCountFile:
    genomicTreat = {}
    chr17Treat = {}
    genomicControl = {}
    chr17Control = {}
    genomicDict = {}
    chr17Dict = {}
    for line in treatFile:
        line = line.split()
        value = int(line[1])
        if line[0] != 'chrM' and line[0] != 'chrXVII':
            if line[0] not in genomicTreat:
                genomicTreat[line[0]] = {}
            if value in genomicTreat[line[0]]:
                genomicTreat[line[0]][value] = genomicTreat[line[0]][value] + 1
            else:
                genomicTreat[line[0]][value] = 1
        if line[0] == 'chrXVII' and 3910 < value < 21879:
            if value in chr17Treat:
                chr17Treat[value] = chr17Treat[value] + 1
            else:
                chr17Treat[value] = 1
    for line in controlFile:
        line = line.split()
        value = int(line[1])
        if line[0] != 'chrM' and line[0] != 'chrXVII':
            if line[0] not in genomicControl:
                genomicControl[line[0]] = {}
            if value in genomicControl[line[0]]:
                genomicControl[line[0]][value] = genomicControl[line[0]][value] + 1
            else:
                genomicControl[line[0]][value] = 1
        if line[0] == 'chrXVII' and 3910 < value < 21879:
            if value in chr17Control:
                chr17Control[value] = chr17Control[value] + 1
            else:
                chr17Control[value] = 1
    for chromosome, chromosomeDict in genomicTreat.items():
        for k, v in chromosomeDict.items():
            if chromosome in genomicControl and k in genomicControl[chromosome]:
                difference = round(v * normalizationTreat - genomicControl[chromosome][k] * normalizationControl)
                if chromosome not in genomicDict:
                    genomicDict[chromosome] = {}
                if difference in genomicDict[chromosome]:
                    genomicDict[chromosome][difference] = genomicDict[chromosome][difference] + 1
                else:
                    genomicDict[chromosome][difference] = 1
    genomicTreat = {}
    genomicControl = {}
    for k, v in chr17Treat.items():
        if k in chr17Control:
            difference = round(v * normalizationTreat - chr17Control[k] * normalizationControl)
            if difference in chr17Dict:
                chr17Dict[difference] = chr17Dict[difference] + 1
            else:
                chr17Dict[difference] = 1
    differenceCounts = {}
    for chromosome, chromosomeDict in genomicDict.items():
        for difference, count in chromosomeDict.items():
            genomicOutputFile.write(chromosome + ' ' + str(difference) + ' ' + str(count) + '\n')
            if difference in differenceCounts:
                differenceCounts[difference] = differenceCounts[difference] + count
            else:
                differenceCounts[difference] = count
    for difference, count in differenceCounts.items():
        genomicOutputCountFile.write(str(difference) + ' ' + str(count) + '\n')
    for difference, count in chr17Dict.items():
        chr17OutputFile.write('chrXVII ' + str(difference) + ' ' + str(count) + '\n')

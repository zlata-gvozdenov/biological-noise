#Input file looks as following (without headline)
# chr  	start   	end     	rna-seq 4tu-seq
# chrI	57945	58944	112266	14649.75385865153
# chrI	57962	58961	113473	16626.40861088549
# chrI	57972	58971	113200	16877.983753046337
# chrI	57974	58973	113079	16908.21933387493
#RNA-seq and 4tU-seq columns represent the sum of the nt coverages per defined interval (between start and end, i.e. columns 2 and 3)
#This input file can be generated with return_colvalues_rna-seq_4tu-seq.py and count_per_defined_interval.py
#Plus and minus strand values can be unified in one file before running tpm.py.

inputFilename = input("Enter the name of the input file: ")
outputFilename = input("Enter the name of the output file: ")
sumRna = 0.0
sum4tu = 0.0
with open(inputFilename) as inputFile:
    for line in inputFile:
        line = line.split()
        distance = int(line[2]) - int(line[1])
        sumRna = sumRna + (float(line[3])/distance)
        sum4tu = sum4tu + (float(line[4])/distance)
with open(inputFilename) as inputFile, open(outputFilename, 'w') as outputFile:
    for line in inputFile:
        line = line.split()
        rna_seq = float(line[3])
        tu4 = float(line[4])
        distance = int(line[2]) - int(line[1])
        tpmRna = ((float(line[3]) / distance) * 1000000) / sumRna
        tpm4tu = ((float(line[4]) / distance) * 1000000) / sum4tu
        if tpm4tu == 0.0: #if tpm4tu <= 0.0:
            tpm4tu = 1.0
        if tpmRna == 0.0:
            tpmRna = 1.0
        tpm = tpmRna / tpm4tu
        outputFile.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\t' + line[3] + '\t' + line[4] + '\t' + str(tpm) + '\n')

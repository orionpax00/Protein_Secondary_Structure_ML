import os
import sys

with open(sys.argv[1],'r') as gadbadfile:
    lines = gadbadfile.readlines()
    with open('seq.sec_str','w') as file_to_write:
        for line in lines :
            if line[:4] == 'Pred':
                file_to_write.write(line[6:])
            else:
                continue
        file_to_write.close()

with open('d_tmp.fasta','w') as d_tmp:
    with open('seq.sec_str', "rb") as infile:
        ini = infile.read().replace('H','G').replace('E','A')
        d_tmp.write(ini)

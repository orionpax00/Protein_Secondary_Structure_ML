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

with open('./svm_fasta','w') as svm_fas:
    with open(sys.argv[2], "rb") as infile:
        ini = infile.read().replace('H','G').replace('E','A')
        svm_fas.write(ini)
    svm_fas.write(">query.d\n")
    with open("seq.sec_str", "rb") as infile:
        ini = infile.read().replace('H','G').replace('E','A')
        svm_fas.write(ini)

os.system('/home/deepak/durgeshapi/Protein_Secondary_Structure_ML/clustalo'+' -i ./svm_fasta -o'+ ' ./output.txt'+ ' --outfmt'+ ' vie' + ' --force')

with open('svm_secondary_structure.train','w') as svm_sec_str:
    string = ""
    with open('output.txt','r') as clastalo_out:
        lines = clastalo_out.readlines()
        super_string = ""
        for counter,line in enumerate(lines):
            if counter == 0:
                continue
            elif (counter) % 2 != 0:
                if lines[counter-1][1:lines[counter-1].index('.')+2] in positive_fasta:
                    sub_string = "+1 "
                else:
                    sub_string = "-1 "
                line = line.replace('A','C').replace('G','H')
                for counter2,letter in enumerate(line):
                    if letter == 'H':
                        sub_string += str(counter2+1) + ":4 "
                        # svm_sec_str.write(str(counter3) + ":4 ")
                    elif letter == 'E':
                        sub_string += str(counter2+1) + ":3 "
                        # svm_sec_str.write(str(counter3) + ":3 ")
                    elif letter == 'C':
                        sub_string += str(counter2+1) + ":2 "
                        # svm_sec_str.write(str(counter3) + ":2 ")
                    elif letter == '-':
                        sub_string += str(counter2+1) + ":0 "
                super_string += sub_string+"\n"
        svm_sec_str.write(super_string)


with open('svm_secondary_structure.train','rb') as semi_train:
    lines = semi_train.readlines()
    with open('svm.train','w') as train:
        for line in lines[:-1]:
            train.write(line)
    with open('svm.predict','w') as predict:
        predict.write("0 ")
        predict.write(lines[-1][3:])

with open('svm_secondary_structure.train','a') as svm_sec_str:
    string = ""
    super_string = ""
    svm_sec_str.write("0 ")
    with open('seq.sec_str','r') as sec_str:
        lines = sec_str.readlines()
        length = len(lines)
        counter = 0
        for counter1, line in enumerate(lines):
            string += line[0:-1]

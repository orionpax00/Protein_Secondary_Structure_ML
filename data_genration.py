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

    string.replace('\n','')
    sub_string = ""
    for counter3,letter in enumerate(string):
        if letter == 'H':
            sub_string += str(counter3) + ":4 "
            # svm_sec_str.write(str(counter3) + ":4 ")
        elif letter == 'E':
            sub_string += str(counter3) + ":3 "
            # svm_sec_str.write(str(counter3) + ":3 ")
        elif letter == 'C':
            sub_string += str(counter3) + ":2 "
            # svm_sec_str.write(str(counter3) + ":2 ")
        elif letter == '-':
            sub_string += str(counter3) + ":0 "
            # svm_sec_str.write(str(counter3) + ":0 ")
    super_string+= sub_string+"\n"
    svm_sec_str.write(super_string)

with open('./svm_fasta','w') as svm_fas:
    with open(sys.argv[2], "rb") as infile:
        ini = infile.read().replace('H','G').replace('E','A')
        svm_fas.write(ini)
    svm_fas.write(">query.d\n")
    with open("seq.sec_str", "rb") as infile:
        ini = infile.read().replace('H','G').replace('E','A')
        svm_fas.write(ini)

# os.system('/home/primus/durgeshppi/tools/blast/clustalo'+' -i ./svm_fasta -o'+ ' ./output.txt'+ ' --outfmt'+ ' vie' + ' --force')

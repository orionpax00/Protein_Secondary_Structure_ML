import os
import math

files = sorted(os.listdir("../../hprd_fasta"))
fasta_list = []
for file_ in files:
    if file_[-3:]  == 'out':
        continue
    elif file_[0]  == '.':
        continue
    elif file_[-3:]  == 'ali':
        continue
    else:
        fasta_list.append(file_)
for counter,file_ in enumerate(fasta_list[2229+492+3558+1679+1043:]):
    positive_fasta = []
    negative_fasta = []
    print(counter)
    print(file_)
    os.system('blastp -db hprdfasta.fasta -query ../../hprd_fasta/'+file_+' -out jev_blast.out')

    fasta_list = []
    with open('./jev_blast.out','r') as query_blast:
        lines = query_blast.readlines()
        for line in lines:
            if line[0] == ">":
                fasta_list.append(line[2:line.index('|')])
    if len(fasta_list) >= 20:
        positive_fasta = fasta_list[0:10]
        negative_fasta = fasta_list[-10:]

    else:
        positive_len = int(math.ceil(len(fasta_list)/2))
        negative_len = int(math.floor(len(fasta_list)/2))
        positive_fasta = fasta_list[0:positive_len]
        negative_fasta = fasta_list[-negative_len:]

    with open("./positive_negative_data/"+file_,'w') as svm_fas:
        for hprd_fasta in fasta_list:
            if hprd_fasta in positive_fasta:
                svm_fas.write("> +"+hprd_fasta+"\n")
            else:
                svm_fas.write("> -"+hprd_fasta+"\n")
            if hprd_fasta[0]  == 'O' or hprd_fasta[0]  == 'P' or hprd_fasta[0]  == 'Q' :
                with open("../promals/secondary_structures/"+hprd_fasta, "rb") as infile:
                    ini = infile.read().replace('H','G').replace('E','A')
                    svm_fas.write(ini)
            else:
                with open("../promals/secondary_structures/"+hprd_fasta[0:-2], "rb") as infile:
                    ini = infile.read().replace('H','G').replace('E','A')
                    svm_fas.write(ini)

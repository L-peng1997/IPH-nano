#Writen by Liuzhe
#Use : python mapping.py path/sample.fa path/sequence_name_file 
import os
import sys
from Bio import SeqIO
import pandas as pd

# 接收命令行指定的数量
count_ = int(sys.argv[3])
fasta_list = []
ref_name_list= []
for record in SeqIO.parse(sys.argv[1] , "fasta") :
    fasta_list.append(record)
    SeqIO.write(fasta_list , "temp.fa" ,"fasta")
    os.system("minimap2 -x asm20 -t 24 -c --secondary=no -z 8000,100 temp.fa /home/admin1/IPH-nano/Database/gisaid/gisaid.align.fa -o temp.paf")
    table1 = pd.read_csv("temp.paf" , names = ["ref_name" , "a2" , "a3" , "a4" , "a5" , "sample_name" , "a7" , "a8" , "a9" , "a10" , "a11" , "a12" , "a13" , "a14" ,"a15", "a16", "a17", "a18", "a19", "a20", "a21", "a22", "a23" ] , sep = "\t")
    table1 = table1[table1["a10"]>25000]
    table1["diff"] = table1["a11"] - table1["a10"]
    table2 = table1.sort_values(by = ["diff" , "a10"] , ascending=[True, False] )
    count = 1
    for i in table2["ref_name"]:
        if count >count_ : break
        ref_name_list.append(i)
        count+=1
    fasta_list = []
ref_name_set = set(ref_name_list)
with open(sys.argv[2] , "w") as ww:
    ww.write("strain" + "\n")
    for i in ref_name_set:
        ww.write(str(i) + "\n")
#os.system("rm temp.fa")
#os.system("rm temp.paf")
os.system("cat /home/admin1/IPH-nano/Database/gisaid/lineagestrain >>%s" %(sys.argv[2]))

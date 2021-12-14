import pandas as pd
import os
import argparse
parser = argparse.ArgumentParser(description="Use BLAST find the most similar ref sequence")
parser.add_argument("-q", type=str , help="Raw fastq file")
parser.add_argument("-o", type=str , help = "output path of ref sequences")
parser.add_argument("-db", type=str , help="Reference Database")
parser.add_argument("-num", type=int , help="number of reference output")
args = parser.parse_args()
fastq_name = args.q.split("/")[-1]
sample_name = fastq_name.split(".")[0]
os.system("seqkit fq2fa %s > temp.fa" %(args.q))
os.system("seqtk sample temp.fa 4000 > temp2.fa")
os.system("blastn -query temp2.fa -db %s -out %s/%s.blastn -outfmt \"6 qaccver saccver bitscore stitle\" -max_target_seqs 1 -num_threads 16" %(args.db,args.o,sample_name))
table1 = pd.read_csv("%s/%s.blastn" %(args.o,sample_name) , names = ["qseqid" , "sseqid" ,"bitscore" , "stitles"] , sep = "\t")
table2 = table1.sort_values(by = "bitscore" , ascending= False )
table2.drop_duplicates(subset = "sseqid" , inplace = True)
table2 = table2.reset_index(drop=True)
for i in range(0,args.num):
    seqname = table2.loc[i ,"sseqid"]
    cmd = "seqkit grep -p %s %s -o %s/%s_%s_%d.fasta"%(seqname,args.db,args.o,sample_name,seqname,i)
    os.system(cmd)

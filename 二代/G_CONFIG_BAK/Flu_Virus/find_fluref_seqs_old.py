import pandas as pd
import os
import argparse
parser = argparse.ArgumentParser(description="Use BLAST find the most similar ref sequence")
parser.add_argument("-o", type=str , help = "output ref sequence file")
parser.add_argument("-db", type=str , help="Reference Database")
args = parser.parse_args()
os.system("blastn -query temp2.fa -db %s -out temp2.blastn -outfmt \"6 qaccver saccver bitscore stitle\" -max_target_seqs 1 -num_threads 16" %(args.db))
table1 = pd.read_csv("temp2.blastn" , names = ["qseqid" , "sseqid" ,"bitscore" , "stitles"] , sep = "\t")
table2 = table1.sort_values(by = "bitscore" , ascending= False )
seqname = table2["sseqid"].iloc[1]
cmd = "seqkit grep -p \"%s\" %s.fasta -o %s"%(seqname,args.db,args.o)
os.system(cmd)


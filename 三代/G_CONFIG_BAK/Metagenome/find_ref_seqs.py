import pandas as pd
import os
import argparse
parser = argparse.ArgumentParser(description="Use BLAST find the most similar ref sequence")
parser.add_argument("-q", type=str , help="Raw fastq file")
parser.add_argument("-o", type=str , help = "output ref sequence file")
parser.add_argument("-db", type=str , help="Reference Database")
args = parser.parse_args()
os.system("seqkit fq2fa %s > temp.fa" %(args.q))
os.system("seqtk sample temp.fa 4000 > temp2.fa")
os.system("blastn -query temp2.fa -db %s -out %s.blastn -outfmt \"6 qaccver saccver bitscore stitle\" -max_target_seqs 1 -num_threads 16" %(args.db,args.q))
table1 = pd.read_csv("%s.blastn" %(args.q) , names = ["qseqid" , "sseqid" ,"bitscore" , "stitles"] , sep = "\t")
table2 = table1.sort_values(by = "bitscore" , ascending= False )
seqname = table2["sseqid"].iloc[1]
cmd = "seqkit grep -p \"%s\" %s -o %s"%(seqname,args.db,args.o)
os.system(cmd)

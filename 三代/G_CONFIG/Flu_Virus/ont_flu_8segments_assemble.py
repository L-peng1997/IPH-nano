import os
import argparse
import sys
parser = argparse.ArgumentParser(description="Assemble Influenza Virus 8 segments")
parser.add_argument("-d", type=str , help = "Raw fastq path")
parser.add_argument("-o", type=str , help="Result path")
parser.add_argument("-db", type=str , help="Reference database path")
parser.add_argument("-s", type=str , help="Sample name")
args = parser.parse_args()
fastq_path = args.d
sample_name = args.s
result_path = args.o
fludb_path = args.db
os.system("seqkit fq2fa %s > temp.fa" %(fastq_path))
os.system("seqtk sample temp.fa 4000 > temp2.fa")
os.system("mkdir %s/%s" %(result_path,sample_name))
os.system("mkdir %s/%s/ref" %(result_path,sample_name))
for genes in ["HA" , "NA" , "PB1" , "PB2" , "PA" , "M" , "NP" , "NS1"]:
    os.system("mkdir %s/%s/%s" %(result_path,sample_name,genes))
    os.system(f'python {sys.path[0]}/find_fluref_seqs.py -o {result_path}/{sample_name}/ref/{sample_name}_{genes}.fasta -db {fludb_path}/flu_{genes}')
    if os.path.exists(f'{result_path}/{sample_name}/ref/{sample_name}_{genes}.fasta'): 
        os.system(f'python {sys.path[0]}/ont_flu_assemble.py {sample_name} {fastq_path} {result_path}/{sample_name}/ref/{sample_name}_{genes}.fasta {result_path}/{sample_name}/{genes}')
        os.system("artic_fasta_header %s/%s/%s/%s.consensus.fasta %s_%s" %(result_path,sample_name,genes,sample_name,sample_name,genes))
os.system("rm temp*")
os.system("cat %s/%s/*/*.consensus.fasta>%s/%s.fasta" %(result_path,sample_name,result_path,sample_name))

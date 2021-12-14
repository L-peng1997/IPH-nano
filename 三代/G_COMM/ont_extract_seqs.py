import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser(description='extract sequences from rawdata by kraken2 classify files, output fastq and fasta file')
parser.add_argument("-kraken", type=str,  help="kraken2 classify detail file")
parser.add_argument("-fastq", type=str, help="Nanopore merged raw fastq file")
parser.add_argument("-taxid", type=str, help="taxid of the pathogen wants to extract")
parser.add_argument("-name", type=str, help="sample name")
parser.add_argument("-out", type=str,  help="path of the result output")
args = parser.parse_args()
if args.taxid.isdigit():
    os.system("taxonkit list --ids %s > list" %(args.taxid))
    table1 = pd.read_csv("./list", names=["id"])
else:
    table1 = pd.read_csv(args.taxid, names=["id"])
table2 = pd.read_csv(args.kraken, names=["comfirm", "readsid", "id", "length", "detail"], sep="\t")
table3 = pd.merge(table2, table1, on="id", how="inner")
with open("temp_seqlist.txt", "w") as ww:
    for name in table3["readsid"]:
        ww.write(name + "\n")
os.system("seqkit grep -f temp_seqlist.txt %s>%s/%s.fastq"%(args.fastq, args.out, args.name))
os.system("seqkit fq2fa %s/%s.fastq -o %s/%s.fa" %(args.out, args.name, args.out, args.name))

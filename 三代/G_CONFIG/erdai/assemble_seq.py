import os
import argparse
import pandas as pd
from Bio import SeqIO
parser = argparse.ArgumentParser(description="assemble sequences from fastq file with reference")
parser.add_argument("-type", type=str, help="single reads or pair end reads input PE or SE")
parser.add_argument("-ref", type=str, help="Reference file")
parser.add_argument("-sample_name", type=str, help="file name of analyze sample")
parser.add_argument("-threads", type=int, help="threads used for assemble")
parser.add_argument("-depth", type=int, help="seq depth for consensus")
parser.add_argument("-quality", type=int, help="missing data 20-40 int")
parser.add_argument("-snp_cutoff", type=float, help="call snp cut off value 0-1 float")
parser.add_argument("-sec_file", type=str, help="Second step result file of intermediate file")
parser.add_argument("-thi_file", type=str, help="Third step result file of intermediate file")
args = parser.parse_args()
snp = args.snp_cutoff
bwa_threads = args.threads
samtools_threads = abs(args.threads/4)
reference_file = args.ref
sample_name = args.sample_name
# 第二步结果文件夹名称:1.cutadapt
sec_file = args.sec_file
# 第三步结果文件夹名称:2.mapping
thi_file = args.thi_file

# 检测index文件是否存在
if not os.path.exists("%s.bwt"%(reference_file)):
    os.system("bwa index %s"%(reference_file))
# 比对reads到参考序列 命令里的1.cutadapt,2.mapping以及.fp_1.fq.gz字符替换为config文件里对应的内容
if args.type == "SE":
    os.system(f"bwa mem -t {bwa_threads} -a {reference_file} {sec_file}/{sample_name}.fp_1.fq.gz | samtools view -@ {samtools_threads} -bS -F 4 | samtools sort -@ {samtools_threads} -o {thi_file}/{sample_name}.bam")
if args.type == "PE":
    os.system(f"bwa mem -t {bwa_threads} -a {reference_file} {sec_file}/{sample_name}.fp_1.fq.gz {sec_file}/{sample_name}.fp_2.fq.gz | samtools view -@ {samtools_threads} -bS -F 4 | samtools sort -@ {samtools_threads} -o {thi_file}/{sample_name}.bam")
os.system(f"samtools index {thi_file}/{sample_name}.bam")
# 生成一致性序列
os.system(f"samtools mpileup {thi_file}/{sample_name}.bam | ivar consensus -p {thi_file}/{sample_name}.fa -q {args.quality} -t 0 -n N -m {args.depth}")
# 生成SNP位点列表
if snp != '-':
    os.system(f"samtools mpileup --reference {reference_file} {thi_file}/{sample_name}.bam | ivar variants -p {thi_file}/{sample_name}.tsv -t {args.snp_cutoff}")
# 生成测序深度列表
os.system(f"samtools depth {thi_file}/{sample_name}.bam > {thi_file}/{sample_name}.depth")

# 生成测序报告
with open(f"{thi_file}/{sample_name}.report", "w") as output_file:
    ref_record = SeqIO.read(reference_file, "fasta")
    ref_len = len(ref_record.seq)
    sample_record = SeqIO.read(f"{thi_file}/{sample_name}.fa", "fasta")
    sample_N_counts = sample_record.seq.count("N")
    coverage = (ref_len - sample_N_counts) / ref_len
    output_file.write(f"sample {sample_name} sequence coverage = {coverage}" + "\n")
    table1 = pd.read_csv(f"{thi_file}/{sample_name}.depth", sep="\t", names=["ref_name", "pos", "depth"])
    depth_mean = table1["depth"].mean()
    output_file.write(f"sample {sample_name} sequence mean depth = {abs(depth_mean)}" + "\n")

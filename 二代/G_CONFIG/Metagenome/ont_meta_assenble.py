import sys
import os
sample_name = sys.argv[1]
fastq_file = sys.argv[2]
ref_file = sys.argv[3]
result_path = sys.argv[4]
depth = sys.argv[5]

make_depth_mask_path = sys.path[0].replace('Metagenome', 'Flu_Virus')

os.system("minimap2 -a -x map-ont -t 16 %s %s | samtools view -bS -F 4 - | samtools sort -o %s/%s.bam -" %(ref_file,fastq_file,result_path,sample_name))
os.system("samtools index %s/%s.bam" %(result_path,sample_name))
os.system("medaka consensus %s/%s.bam %s/%s.hdf" %(result_path,sample_name,result_path,sample_name))
os.system("medaka variant %s %s/%s.hdf %s/%s.vcf" %(ref_file,result_path,sample_name,result_path,sample_name))
os.system("bgzip %s/%s.vcf" %(result_path,sample_name))
os.system("tabix -p vcf %s/%s.vcf.gz" %(result_path,sample_name))
os.system("longshot -P 0 -F -A --no_haps --bam %s/%s.bam --ref %s --out %s/%s.longshot.vcf --potential_variants %s/%s.vcf.gz" %(result_path,sample_name,ref_file,result_path,sample_name,result_path,sample_name))
os.system("artic_vcf_filter --longshot %s/%s.longshot.vcf %s/%s.pass.vcf %s/%s.fail.vcf" %(result_path,sample_name,result_path,sample_name,result_path,sample_name))
os.system(f'python {make_depth_mask_path}/make_depth_mask.py {result_path}/{sample_name}.bam {result_path}/{sample_name}.coverage_mask.txt {ref_file} {depth}')
os.system("bgzip -f %s/%s.pass.vcf" %(result_path,sample_name))
os.system("tabix -p vcf %s/%s.pass.vcf.gz" %(result_path,sample_name))
os.system("artic_mask %s %s/%s.coverage_mask.txt %s/%s.fail.vcf %s/%s.preconsensus.fasta" %(ref_file,result_path,sample_name,result_path,sample_name,result_path,sample_name))
os.system("bcftools consensus -f %s/%s.preconsensus.fasta %s/%s.pass.vcf.gz -m %s/%s.coverage_mask.txt -o %s/%s.consensus.fasta" %(result_path,sample_name,result_path,sample_name,result_path,sample_name,result_path,sample_name))
os.system("artic_fasta_header %s/%s.consensus.fasta %s" %(result_path,sample_name,sample_name))



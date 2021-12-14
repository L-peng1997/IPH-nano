#use global wildcard make sample list# 
#raw sequencing data should be in the format as: $sample_1/2.fq.gz#
import sys

path = str(config['path'])
SAMPLE_LIST, = glob_wildcards(path + "/0.rawdata/{sample}_1.fq.gz")
##database file; $PATH to the norovirus sequences blastn database###
db = "/home/admin1/IPH-nano/Database/ngsdb/noronet/norovp1"
usearchdb="/home/admin1/IPH-nano/Database/ngsdb/noronet/usearchdb/norovp1.udb"
re_path = path

rule all:
    input:
        expand("{re_path}/03.cluster/{sample}_unique.fa",re_path=re_path,sample=SAMPLE_LIST),
        expand("{re_path}/03.cluster/{sample}_cluster.fa",re_path=re_path,sample=SAMPLE_LIST),
        expand("{re_path}/03.cluster/{sample}_uparse.txt",re_path=re_path,sample=SAMPLE_LIST),
        expand("{re_path}/03.cluster/{sample}_cluster.csv",re_path=re_path,sample=SAMPLE_LIST),
        expand("{re_path}/04.annotation/{sample}_annotation.csv",re_path=re_path,sample=SAMPLE_LIST),
        expand("{re_path}/05.combined/{sample}_finalcb.csv",re_path=re_path,sample=SAMPLE_LIST),
        expand("{re_path}/05.combined/{sample}_annocut.csv",re_path=re_path,sample=SAMPLE_LIST),
        expand("{re_path}/06.seq/{sample}.seq.csv",re_path=re_path,sample=SAMPLE_LIST),
        expand("{re_path}/06.seq/{sample}_final.seq.csv",re_path=re_path,sample=SAMPLE_LIST)

rule qc_cutadapter:
    input:
        raw1="{re_path}/0.rawdata/{sample}_1.fq.gz",

        raw2="{re_path}/0.rawdata/{sample}_2.fq.gz"

    output:
        ca1="{re_path}/01.cutadp/{sample}_1_ca.fq.gz",
        ca2="{re_path}/01.cutadp/{sample}_2_ca.fq.gz",
        rep="{re_path}/01.cutadp/report/{sample}_ca.report.html"


    shell:
        "fastp -i {input.raw1} -I {input.raw2} -o {output.ca1} -O {output.ca2} -q 30 -5 -3 -M 10 -h {output.rep}"

rule pair_assemble:
    input:
        ca1=rules.qc_cutadapter.output.ca1,
        ca2=rules.qc_cutadapter.output.ca2
    output:
        assemble="{re_path}/02.assemble/{sample}_assemble.fa"
    shell:
#####-m:mini overlaps ; -c standardoutput; -x maxmismatch; -d dir;  :
        "flash {input.ca1} {input.ca2} -m 20 -x 0.2 -c -d 02.assemble|seqkit seq -m 300 -M 400|seqkit fq2fa -o {output.assemble}"
rule cutprimer:
        input:
            assemble=rules.pair_assemble.output.assemble
        output:
            caleft=temp("{re_path}/02.assemble/{sample}_leftca.fa"),
            caright=temp("{re_path}/02.assemble/{sample}_assemble_rightca.fa"),
            caprimer="{re_path}/02.assemble/{sample}_assemble_cut.fa",
            orient="{re_path}/02.assemble/{sample}_cut_orient.fa"
        log:
        	logfile="{re_path}/02.assemble/{sample}.cutprimer.log"
        params:
        	dir="/home/admin1/IPH-nano/Database/ngsdb/noronet"

        shell:
#######using cutadapt to cut the amplication primer G1SKF/G1SKR; G2SKF/G2SKR; the primer sequence files were stored in {params.dir}        
            """
            cutadapt -g file:{params.dir}/primerF.fa \
             --rc -e 0.1 -n 5 \
             -o {output.caleft} {input} -j 8 | tee {log.logfile}; 
            cutadapt -a file:{params.dir}/primerR-RC.fa \
             --rc -e 0.1 -n 5 \
             -o {output.caright} {output.caleft} -j 8 | tee -a {log.logfile};
             cat {output.caright}|seqkit seq -m 250 -M 350 > {output.caprimer};
             usearch -orient {output.caprimer} -db {usearchdb} -fastaout {output.orient} 
             """
rule cluster:
    input:
        orient=rules.cutprimer.output.orient
    output:
        uniseq="{re_path}/03.cluster/{sample}_unique.fa",
        clusterseq="{re_path}/03.cluster/{sample}_cluster.fa",
        uparlog="{re_path}/03.cluster/{sample}_uparse.txt",
        clustertab="{re_path}/03.cluster/{sample}_cluster.csv"
    shell:
        ##Generating unique sequences for the next clustering##
        "usearch -fastx_uniques {input.orient}  -fastaout {output.uniseq} -strand both -sizeout;"
        #Generating the clustering information: otu number the sequence belong to and its relative identity#
        "usearch -cluster_otus {output.uniseq} -otus {output.clusterseq} -uparseout {output.uparlog} -relabel Otu -minsize 2;"
        #relative reads number in each otu cluster#
        "usearch -usearch_global {input.orient} -db {output.clusterseq} -strand both -id 0.987 -otutabout {output.clustertab}"

rule annotation:
    ##Genotype annotation by alignment with local Norovirus seqs dataset#
    input:
        clusterseq=rules.cluster.output.clusterseq
    output:
        annotation="{re_path}/04.annotation/{sample}_annotation.csv"
    shell:
        "blastn -query {input.clusterseq} -db {db} -max_target_seqs 1 -outfmt 6  -out {output.annotation}"

rule combineInf:
###Calculating reads number in each otus###
    input:
        annotation=rules.annotation.output.annotation,
        clustertab="{re_path}/03.cluster/{sample}_cluster.csv"
    output:
        anntab="{re_path}/05.combined/{sample}_annocut.csv",
        clutab="{re_path}/05.combined/{sample}_clusort.csv",
        finaltab="{re_path}/05.combined/{sample}_finalcb.csv"
    params:
        date="{sample}"
    shell:
        "awk -v FS='[\\t_]' -v OFS=',' '{{print x, $1, $3}}' x={params.date} {input.annotation}|csvtk add-header -n sample,OTU,type > {output.anntab};"
        "cat {input.clustertab}|csvtk tab2csv|csvtk add-header -n OTU,reads >{output.clutab};"
        "csvtk join -f OTU {output.anntab} {output.clutab}>{output.finaltab}"
rule combineSeq:
##paste consensus seq of each otu for further phylogenetic analysis#
    input:
        "{re_path}/03.cluster/{sample}_cluster.fa",
        "{re_path}/05.combined/{sample}_finalcb.csv"
    output:
        "{re_path}/06.seq/{sample}.seq.csv",
        "{re_path}/06.seq/{sample}_final.seq.csv"
    shell:
        "seqkit fx2tab {input[0]} | csvtk tab2csv | csvtk add-header -n OTU,Seq,NA|csvtk cut -f 1,2 > {output[0]};"
        "csvtk join -f OTU {input[1]} {output[0]} > {output[1]}"

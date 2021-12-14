#use global wildcard make sample list#
datadir="/home/admin1/IPH-nano/Database/"
path = str(config['path'])
count = str(config['count'])
rule all:
    input:
        expand("{path}/0.data/strainname", path=path),
        expand("{path}/02.nextdata/nextclade.fa", path=path),
        expand("{path}/02.nextdata/nextclade.tsv", path=path)

rule mapping:
    input:
        seq="{path}/0.data/sample.fa",
        gisaid="/home/admin1/IPH-nano/Database/gisaid/gisaid.align.fa",#########以wuhan1为参考基因组align后的序列；
        reflineage="/home/admin1/IPH-nano/Database/gisaid/lineagestrain"########根据pangolin lingeage每个lineage选取0.5%条序列，并加入Hu01和Wuhan1的序列名；
    output:
        relstrain="{path}/0.data/strainname"

    shell:
        """
		python /home/admin1/IPH-nano/G_CONFIG/mapping.py {input.seq} {output.relstrain} {count};
        """
#rm 0.data/*.$$

rule select_clade:
    input:
        gisaidseq="/home/admin1/IPH-nano/Database/gisaid/gisaid.align.fa",
        gisaidepi="/home/admin1/IPH-nano/Database/gisaid/gisaid.tsv",
        relstrain=rules.mapping.output.relstrain
    output:
        gisaidtab="{path}/01.filter/gisaid.seq.tsv",
        seltab="{path}/01.filter/clade.tsv",
        selstrain="{path}/01.filter/filstrain.tsv",       
        selseq="{path}/01.filter/clade.fa"


    shell:
        #change to tsv format seq#######
        "cat {input.gisaidseq}|seqkit fx2tab |cut -f 1,2|csvtk -t add-header -n strain,seq>{output.gisaidtab};"
        #filter sepcific clade epi#######
        "csvtk -t join -f 'strain' {input.relstrain} {input.gisaidepi} --left-join >{output.seltab};"
        ###filtered strain name with collection date and epi inf####
        "cat {output.seltab}|cut -f 1 >{output.selstrain};"
        #filter sepcific clade seq#######
        "cat {output.gisaidtab}|csvtk -t grep -f strain -P {output.selstrain}|csvtk -t cut -f 1,2|csvtk -t del-header|seqkit tab2fx>{output.selseq}"

rule combineseq:
    input:
        sampleseq="{path}/0.data/sample.fa",####include your seqs and ref Wuhan/Hu-1/2019###
        selseq="{path}/01.filter/clade.fa",
        sampletab="{path}/0.data/sample.tsv",####include epi inf of your seqs and ref Wuhan/Hu-1/2019###
        seltab="{path}/01.filter/clade.tsv"
    output:
        finalseq="{path}/02.nextdata/nextclade.fa",
        tempfil=temp("{path}/0.data/sample_ref.head.del.tsv"),
        finaltab="{path}/02.nextdata/nextclade.tsv"
    params:
        dir="/home/admin1/IPH-nano/ncov"
        #dir="/Volumes/T7/software/Bioinf_software/ncov/"
    shell:
        #combine sequences data
        "cat {input.sampleseq} {input.selseq} |seqkit rmdup -n >{output.finalseq};"
        "cat {input.sampletab}|csvtk -t del-header>{output.tempfil};"
        "cat {input.seltab} {output.tempfil} |csvtk -t uniq -f 1 >{output.finaltab};"
        "cp {output.finalseq} {output.finaltab} {params.dir}/data;"#####copy generated file to nextstrain data folder#
        "seqkit seq -n {output.finalseq}>{params.dir}/defaults/include.txt"

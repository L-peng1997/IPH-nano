import pandas as pd
import os
import sys
bam_file = sys.argv[1]
mask_file = sys.argv[2]
ref_file = sys.argv[3]
depth = sys.argv[4]
depth = int(depth)
with open(ref_file , "r") as ref_f:
    for line in ref_f:
        if line[0] == ">" :
            ref_name = line.split(" ")[0][1::]
os.system("samtools depth -a %s > depth.txt"  %(bam_file))
table1 = pd.read_csv("./depth.txt" , names = ["ref" , "pos" , "depth"] , sep = "\t")
table2 = table1[table1["depth"] < depth]
ww= open(mask_file , "w")
pos_list = [i for i in table2["pos"]]
if pos_list:
    j = pos_list[0]
    ww.write(ref_name.strip() + "\t" + str(j) + "\t")
    for i in pos_list[1::]:
        if i - j > 1:
            ww.write(str(j) + "\n")
            ww.write(ref_name.strip() + "\t" + str(i) + "\t")
        j = i
    ww.write(str(pos_list[-1]))
os.system("rm depth.txt")
ww.close()

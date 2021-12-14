#二代测序从头拼接（spades）
import pandas as pd
import argparse
import os
parser = argparse.ArgumentParser(description='denovo assemble NGS reads to contigs ')
parser.add_argument("-list_file", type=str , help="the list file separate with tab")
parser.add_argument("-raw_path", type=str , help="raw data directory")
parser.add_argument("-result_path", type=str , help="result file path ")
parser.add_argument("-meta", action="store_true" , help="whether meta data")
parser.add_argument("-type", type=str , help="Sequence type PE or SE")
parser.add_argument("-threads", type=int , help="number of threads ")
args = parser.parse_args()


print (args.list_file + "\n")
print(args.raw_path + "\n")
print(args.result_path + "\n")
if args.meta :
    print ("True")
else:
    print('False')
print(args.type + "\n")
print(str(args.threads) + "\n")


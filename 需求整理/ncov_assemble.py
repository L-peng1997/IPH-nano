# -*- coding: utf-8 -*- 
#基于artic流程拼接新冠病毒序列
import pandas as pd
import argparse
import os
parser = argparse.ArgumentParser(description='assemble ncov consensus sequence from list file ')
parser.add_argument("-list_file", type=str , help="the list file separate with tab")
parser.add_argument("-raw_path", type=str , help="raw data directory")
parser.add_argument("-result_path", type=str , help="result file path ")
parser.add_argument("-max_length", type=int ,default = 700 , help="max reads length default 700 ")
parser.add_argument("-min_length", type=int , default = 400 ,  help="result file path default 400")
parser.add_argument("-model", type=str , help="medaka model")
parser.add_argument("-primmer_schemes", type=str , default = "/home/admin1/IPH-nano/artic-ncov2019/primer_schemes" , help="primmer schemes ")
parser.add_argument("-primmer_detail", type=str , default = "nCoV-2019/V3" , help="primmer schemes detail ")
args = parser.parse_args()

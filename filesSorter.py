import pandas as pd 
import os
import shutil 


path = os.getcwd()
doc_path = path + "\\levaniTxts\\"

categories = {'E12':'_MP', 'E01':'AC_','E02':'OF_', 'E03':'NP_', 'E04':'FI_', 'E05':'NR_', 
                'E06':'SU_','E07':'HP_', 'E08':'CP_', 'E09':'PC_', 'E99':'AR_',
                'E13':'TB'}
categories2 = {'E01':'HL_', 'E04':'DW_', 'E05':'NO_', 'E06':'IB_', 'E99':'DC_'}
categories3 = {'E01':'8W_', 'E04':'AQ_', }

def SortFiles(key, value):
        for item in os.listdir(doc_path):
                if value in item:
                        if not os.path.isdir(doc_path+key):
                                os.mkdir(doc_path+key)
                        shutil.move(doc_path+item, doc_path+key+"\\")

dicts = [categories, categories2, categories3]
for dictionary in dicts:
        for key, value in dictionary.items():
                SortFiles(key, value)

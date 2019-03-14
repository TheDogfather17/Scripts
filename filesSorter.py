import pandas as pd 
import os
import shutil 


path = os.getcwd()
doc_path = path + "\\levaniTxts\\"

categories = {'E12':'_MP', 'E1':'AC_','E2':'OF_', 'E3':'NP_', 'E4':'FI_', 'E5':'NR_', 
                'E6':'SU_','E7':'HP_', 'E8':'CP_', 'E9':'PC_', 'E99':'AR_',
                'E13':'TB'}
categories2 = {'E1':'HL_', 'E4':'DW_', 'E5':'NO_', 'E6':'IB_', 'E99':'DC_'}
categories3 = {'E1':'8W_', 'E4':'AQ_', }

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

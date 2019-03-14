import re, string 
import os 
import random


file_names = [] 

path_= os.getcwd() 
path_ = path_+"\\RFI\\"
print(path_)
number = 1
rand_max = 9
for file in os.listdir(path_):
    print(file)
    f=open(path_+file,  encoding='utf-8')
    filedata = f.read()
    f.close()

    filedata = re.sub("BKT","REF",filedata)
    filedata = re.sub("\d",lambda x:str(random.randint(1,rand_max)),filedata)
    #filedata = re.sub("\d","0",filedata)
    f = open(path_+file,'w', encoding = 'utf-8')
    f.write(filedata)
    f.close()

# file_ = "\\horrible Halifax OCR.txt"
# path = os.getcwd()

# f = open(path+file_,'r', encoding='utf-8')
# filedata = f.read()
# f.close()

#newdata = filedata.replace('/[0-9]/',"0")
# filedata = re.sub("\d","0",filedata)

# f = open(path+file_,'w', encoding = 'utf-8')
# f.write(filedata)
# f.close()
import difflib 
import itertools 
import filecmp
import os 
import shutil
import fileinput

current_path = os.getcwd()

file_names = []
for file in os.listdir(current_path):
    file_names.append(file)

# # #print(file_names)

# with open('acks_combined.txt','w', encoding='utf-8') as wfd:
#     for f in file_names:
#         with open(f, 'r') as fd:
#             shutil.copyfileobj(fd, wfd)

# with open(current_path+'\\'+'acks_combined.txt', 'w', encoding='utf-8') as fout:
#     fin = fileinput.input(file_names)
#     for line in fin:
#         fout.write(line)
#     fin.close()


import glob

read_files = glob.glob("*.txt")

with open("noppi_combined.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
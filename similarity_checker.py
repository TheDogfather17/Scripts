import os 
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
import pprint 
import itertools 
import shutil
import time
import concurrent.futures
import glob
pp = pprint.PrettyPrinter(indent=4)

cwd = os.getcwd()
text_directory = cwd + '//ALL//'

text_files = {}

for item in os.listdir(text_directory):
    text_files.update({item : os.path.getsize(text_directory+item)})

count = 0
ratio = 0
text_files_list = sorted(text_files.items(), key=lambda kv: kv[1])
text_files = dict(text_files_list)

def Find_Similar_Text(text_files, count):
    #count = count
    tic = time.process_time()
    for a, b in itertools.combinations(text_files, 2):
        if text_files[a] - 100 < text_files[b] < text_files[a] + 100:
            file1 = open(text_directory + a, 'rb')
            file1_data = file1.read()
            file1.close()

            file2 = open(text_directory + b, 'rb')
            file2_data = file2.read()
            file2.close()
            if (-200 < len(file1_data) - len(file2_data) < 200):
                ratio = fuzz.ratio(file1_data, file2_data)
                if ratio > 70:
                    #count+=1
                    print(count, 'Ratio:', ratio, a, text_files[a], 'kb', b, text_files[b], 'kb')
                    shutil.move(text_directory + a, text_directory + '//SimilarFiles//')
                    text_files.pop(a)
                    toc = time.process_time()
                    print('Elapsed time:', toc - tic)
                    break


while ratio != None: 
    count+=1
    Find_Similar_Text(text_files, count)

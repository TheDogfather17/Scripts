import pandas as pd 
import os
import shutil 

df = pd.read_csv("FullList.csv", encoding = "utf-8")
df['File Name'] = df['File Name'].astype(str)# + '.txt'
#print(df['File Name'])

#print(df['File Name'])
path = os.getcwd()
doc_path = path + "\\all files\\"
#aldoPath = path + "\\NonTest\\"
levani_path = path + "\\levaniTxts\\"
#print(doc_path)
count = 1 
for item in os.listdir(doc_path):
    if item in list(df['File Name']):
        shutil.move(doc_path+item, levani_path)
        #os.remove(doc_path+item)
        print(count, item) 
        count+=1



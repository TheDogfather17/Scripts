import os 
import pandas as pd 

df = pd.read_csv('extractions.csv')

path = os.getcwd()
path = path+'//InputFiles//'

for item in df['FileName']:
     if item not in os.listdir(path):
         df.drop[[df['FileName']]]
         #df.drop(df.index[], inplace=True)



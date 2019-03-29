import pandas as pd 
from lxml import etree as etree
import numpy as np
import copy
import os
#import xml.etree.ElementTree as xml
df = pd.read_csv('extractions.csv', encoding='utf-8')
#df.replace('', np.nan, inplace=True)

def GenerateXML(index, row):
    NKN_count = CountElements('nkn', row) 
    product_count = CountElements('Product', row)  
    #print(product_count)
    

    FileName = row.FileName
    FileData = GetText(FileName)
    Date = row.Date
    Provider = row.Provider
    Debtor = row.DebtorName
    category = row.Category0

    

    parser = etree.XMLParser(strip_cdata=False)
    with open('target.xml', "rb") as source:
        tree = etree.parse(source, parser=parser)
    
    dupes = []
   # multple nkns generating their own FIELD
    for i in range(0, NKN_count):
        dupes.append(copy.deepcopy(tree.find('//FIELD[@NAME = \'NKN\']')))
        node = tree.find('//FIELD[@NAME = \'NKN\']')
        node.append(dupes[i])
        NKN = row['NKN'+str(i)]
        tree.findall('ETARGET/FIELD')[i].attrib['BASE'] = NKN

#     dupes = []
#    # multple nkns generating their own FIELD
#     for i in range(0, product_count):
#         dupes.append(copy.deepcopy(tree.find('//FIELD[@NAME = \'ProductNumber\']')))
#         node = tree.find('//FIELD[@NAME = \'ProductNumber\']')
#         node.append(dupes[i])
#         Product = row['Product'+str(i)]
#         tree.findall('ETARGET/FIELD')[i].attrib['BASE'] = Product


    tree.find('SECTION').text = FileData
    tree.find('SECTION').text = etree.CDATA(tree.find('SECTION').text)    


    tree.find('//FIELD[@NAME = \'CorrespondenceDated\']').attrib['BASE'] = Date
    tree.find('//FIELD[@NAME = \'ProviderName\']').attrib['BASE'] = Provider
    tree.find('//FIELD[@NAME = \'DebtorName\']').attrib['BASE'] = Debtor
    tree.find('CTARGET').attrib['NAME'] = category

    for item in tree.findall('//FIELD'):
        if item.attrib['BASE']=='' or item.attrib['BASE']==' ':
            item.getparent().remove(item)


    if not os.path.isdir('Output'):
        os.mkdir('Output')
    tree.write('Output//output'+str(index)+'.xml', encoding='utf-8')

    #xml.dump(tree)
    return FileName
def CountElements(item, row):
    row = row.drop(['FileName'])
    count = 0
    
    # if item == 'Product': 
    #     product_columns = 0
    #     print(row.items)
    #     if 'Product' in row.items():
    #         product_columns+=1
    #     print('number of prod columns', product_columns)
    #     for i in range(0, product_columns-1):
    #         if row['Product'+str(i)] is not None:
    #             count+=1
    
    if item.lower() == 'nkn': 
        for cell in row:
            if item in str(cell).lower():
                count+=1
    return count

def GetText(FileName):
    File = open('InputFiles//'+FileName, 'r', encoding='utf-8')
    FileData = File.read()
    return FileData
    
for index, row in df.iterrows():
    print(GenerateXML(index, row), " done")


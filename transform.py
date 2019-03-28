import pandas as pd 
from lxml import etree as etree
#import xml.etree.ElementTree as xml


df = pd.read_csv('extractions.csv', encoding='utf-8')

def GenerateXML(index, row):
    FileName = row.FileName
    FileData = GetText(FileName)
    NKN = row.NKN
    category = row.Category1


    parser = etree.XMLParser(strip_cdata=False)
    with open('target.xml', "rb") as source:
        tree = etree.parse(source, parser=parser)

    tree.find('SECTION').text = FileData
    tree.find('SECTION').text = etree.CDATA(tree.find('SECTION').text)    
    tree.find('CTARGET').attrib["NAME"] = category
    tree.find('ETARGET/FIELD').attrib['BASE'] = NKN
    tree.write('output'+str(index)+'.xml', encoding='utf-8')

    #xml.dump(tree)
    return FileName
  
def GetText(FileName):
    File = open(FileName, 'r', encoding='utf-8')
    FileData = File.read()
    return FileData
    
for index, row in df.iterrows():
    print(GenerateXML(index, row), " done")




    
    #tree = xml.parse('target.xml')
    #xml.dump(tree)
    #root = tree.getroot()
    #print(etree.tostring(tree, pretty_print=True))
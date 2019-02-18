import os 


path_= os.getcwd() 
path_ = path_+"/RFI"

number = 1
for file in  os.listdir(path_):
    os.rename(str(path_)+"/"+file, "RFI"+str(number)+".txt")
    number = number +1
    #print(str(path_)+"/"+file)

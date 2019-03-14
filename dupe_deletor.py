import difflib 
import itertools 
import filecmp
import os 

# category_to_clean = "no ppi 2\\"

current_path = os.getcwd()

# current_path = current_path+"\\"+category_to_clean

# print(current_path)

file_names = []
files_delete = []
for file in os.listdir(current_path):
    file_names.append(file)
#print(file_names)

for a, b in itertools.combinations(file_names, 2):
    if (filecmp.cmp(a,b, shallow=False)==True):
        print(a, " same as ", b)
        files_delete.append(a)
      #file_names.append(a, b)
print(files_delete)
def RemoveFiles(list_):
    for item in list_:
        print("File removed: ", current_path+"\\" +str(item))
        os.remove(current_path + "\\" + str(item))


#RemoveFiles(files_delete)
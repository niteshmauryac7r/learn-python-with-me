import os
path = "/Users/niteshmaurya/python projects/Python_basics/Bill 2025 - 2026"
folder  = os.listdir(path)

def Rename(old_name,path):
    j=0
    for i in old_name:
        print(i)
        if i.endswith(".docx"):
            os.rename(f"{path}/{i}",f"{path}/{j}.docx")
        j +=1


Rename(folder,path)
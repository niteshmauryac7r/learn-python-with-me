import os
import shutil
'''
if (not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,101):
    os.mkdir(f"data/Tutorial {i}")
    i = i+1


for i in range(0,101):
    os.rename(f"data/Tutorial {i}", f"data/ Day {i}")
    i = i+1
'''
folder = os.listdir("data")

print(os.getcwd())

for i in folder:
    print(i)
    print(os.listdir(f"data/{i}"))

shutil.rmtree("data")


    

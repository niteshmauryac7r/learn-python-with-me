import subprocess

l = ["Nitesh","Dharmesh","Nilesh","Pritish","Shantu"]

for i in l:
    subprocess.call(["say",f"Hello!{i}"])

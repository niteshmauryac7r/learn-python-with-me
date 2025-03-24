# Reading a File
# f = open("myfile.txt","r")
# file = f.read()
# print(file)
# f.close()

# Writing a file
# f = open("myfile.txt", 'w')
# file = f.write("Hello World")
# print(file)
# f.close()

# Appending to a file
# f = open("myfile.txt", 'a')
# file = f.write("Hello World")
# print(file)
# f.close()

# a = [1,2,3,4,5]

# with open("myfile.txt", 'a') as f:
#     f.write(str(a))

# f = open("myfile.txt","r")
# i=0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks in maths is {m1} of student{i}")
#     print(f"Marks in science is {m2} of student{i}")
#     print(f"Marks in Geography is {m3} of student{i}")

# f = open("myfile2.txt","w")
# marks = ['12\n','34\n','67\n','78\n']
# file = f.writelines(marks)
# f.close()


with open("myfile2.txt",'r') as f:
    f.seek(5)
    print(f.tell())
    data = f.read(4)
    print(data)

with open("myfile3.txt","w") as f:
    f.write("Hello World")
    f.truncate(5)

with open("myfile3.txt","r") as f:
    print(f.read())
emp = {
    12: "Nitesh",
    13: "Dharmesh",
    16: "Nilesh",
    18: "Shantu",
    20 : "Pritish"
}

print(emp[12])
print(emp.get(20))
print(emp.keys())
print(emp.values())

for name in emp.keys():
    print(f"The value coresponding to {name} is {emp[name]}")


print(emp.items())

for key, value in emp.items():
    print(f"The value coresponding to {key} is {value}")
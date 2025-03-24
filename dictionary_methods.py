emp = {
    12: "Nitesh",
    13: "Dharmesh",
    16: "Nilesh",
    18: "Shantu",
    20 : "Pritish"
}

emp_mgr = {
    21: "Mahima",
    23: "Shweta"
}

emp_ceo = {
    12: "Nitesh",
    13: "Dharmesh",
    16: "Nilesh",
    18: "Shantu",
    20 : "Pritish"
}

emp1 = {
    12: "Nitesh",
    13: "Dharmesh",
}

emp_ceo.clear()
print(emp_ceo)
emp.update(emp_mgr)
print(emp)

emp.pop(20)
print(emp)

emp.popitem() # removes the last item
print(emp)

#del emp1[12]
#print(emp1)

class Employee:
    companyName = "Golden Neons"
    No_of_emp = 0
    def __init__(self, name):
        self.name = name
        self.raise_ammount = 0.02
        Employee.No_of_emp += 1

    def showDetails(self):
        print(f"The name of employee is {self.name} and the raise amount "
              f"in {self.No_of_emp} sized {self.companyName} is {self.raise_ammount}")

emp1 = Employee("Nitesh")
emp1.companyName = "Apple"
emp1.showDetails()
emp2  = Employee("Dharmesh")
emp2.raise_ammount = 0.3

emp2.showDetails()
#Employee.showDetails(emp1)

Employee.companyName = "Google"
print(Employee.companyName)




# 🔹 Problem 1: Track Total Objects Created (Beginner)
# Create a class Student with a class variable total_students that tracks how many student objects have been created.

# Requirements:

# Every time a new student is created, increment total_students.
# Each student should have instance variables name and grade.

class Student:
    total_students = 0
    
    def __init__(self,name):
        self.name = name
        Student.total_students += 1
        
a = Student("Nitesh")

b = Student("Dharmesh")


print(Student.total_students)


# 🔹 Problem 2: Library Book Tracker (Intermediate)
# Create a class Library with:

# A class variable total_books_issued.
# Instance variables book_name, issued_to.
# Every time a book is issued (object is created), increment the class variable.
# Bonus: Add a method to display how many total books have been issued so far.


class Library:
    total_books_issued = 0
    
    def __init__(self,book_name,issued_to):
        self.book_name = book_name
        self.issued_to = issued_to
        Library.total_books_issued +=1
    
    @staticmethod  
    def TotalBookIssued():
        return Library.total_books_issued
        
a = Library("Alice in wonderland","Nilesh")
b = Library("Oliver Twist", "Pritish")

print(Library.TotalBookIssued())


# 🔹 Problem 3: Count of Instances by Type (Advanced)
# Create a class Animal:

# Class variables: total_animals, dog_count, cat_count.
# Subclasses: Dog and Cat that update the counters on creation.
# Test:

# d1 = Dog()
# c1 = Cat()
# d2 = Dog()
# print(Animal.total_animals)  # 3
# print(Animal.dog_count)      # 2
# print(Animal.cat_count)      # 1

class Animals:
    dog_count = 0
    cat_count = 0
    total_animals = 0
    
    
class Dog(Animals):
    def __init__(self,dog_name):
        self.dog_name = dog_name
        Animals.dog_count +=1
        Animals.total_animals +=1
        
class Cat(Animals):
    def __init__(self,cat_name):
        self.cat_name = cat_name
        Animals.cat_count +=1
        Animals.total_animals +=1
        
        
d1 = Dog("Oscar")
c1 = Cat("Mike")
d2 = Dog("Walter")
print(Animals.total_animals)  # 3
print(Animals.dog_count)      # 2
print(Animals.cat_count)      # 1

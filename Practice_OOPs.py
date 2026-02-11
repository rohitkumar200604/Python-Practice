# Create a class Car with attribute brand = "Scorpio".

class Car:
    brand = "Scorpio"

car = Car()
print(car.brand)

# Create a class Laptop with attributes: brand, RAM, price. Create 2 objects 
# with different values. 

class Laptop:
    brand = ""
    RAM = ""
    price = ""

Lap1 = Laptop()
Lap1.brand = "HP"
Lap1.RAM = "8GB"
Lap1.price = "28K"

Lap2 = Laptop()
Lap2.brand = "Lenovo"
Lap2.RAM = "16GB"
Lap2.price = "40K"

# Create a class FoodItem with class attribute category = "Snacks" and instance 
# attribute name (“Samosa”, “GulabJamun”).
 
class FoodItem:
    category = "Snacks"

    def __init__(self,item):
        self.item = item


food1 = FoodItem("Samosa")
food2 = FoodItem("GulabJamun")
print(food1.item)
print(food2.item)

# Create class Student that takes 3 marks and has a method average().

class Student:
    def __init__(self, name, ListMarks):
        self.name = name
        self.ListMarks = ListMarks
    def average(self, name, ListMarks):
        sum = 0
        for marks in ListMarks:
            sum += marks
        avg = sum/3
        print(f"{self.name} marks average is {avg}") 

ListMarks = []
name = input("Enter name of student: ")
for i in range(0,3):
    marks = float(input(f"Enter mark {i+1}: "))
    ListMarks.append(marks)
stud = Student(name, ListMarks)
stud.average(name, ListMarks)

# Create static method to validate if a number is even. 

class isEven:
    def __init__(self,num):
        self.num = num;
    def even(self,num):
        if num%2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

num = int(input("Enter number: "))
check_even = isEven(num)
check_even.even(num)

# Create class Student with name, class, marks. Add method get_percentage(). 

class Student:
    def __init__(self,name,clas,marks):
        self.name = name
        self.clas = clas
        self.marks = marks
    def get_percentage(self,marks):
        percent = (marks/80)*100
        print("Percentage of Marks [Out of 80]:",percent)


# Create class Creator with attributes (name, username). Add method bio(). 
class Creator:
    def __init__(self,name,uname):
        self.name = name
        self.uname = uname
    def bio(self,name,uname):
        print("Name:",name)
        print("User name:",uname)

# Create class FoodOrder with item name, quantity, price. Add method to calculate 
# bill. 

class FoodOrder:
    def __init__(self,item_name,quantity,price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
    def bill_calc(self,quantity,price):
        bill = quantity*price
        print("Bill Generated:",bill)

# Add method to increase salary by a percentage. 
class Increment:
    def __init__(self,salary,increment):
        self.salary = salary
        self.increment = increment
    def Increase(self,salary,increment):
        new_Salary = salary + ((increment/100)*salary)
        print(f"New Salary after {increment}% hike:",new_Salary)

sal = float(input("Enter present Salary: "))
per = float(input("Enter the percentage of increment: "))
increase = Increment(sal,per)
increase.Increase(sal,per)



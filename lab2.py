#while Loop
c = 0
while (c<2):
    print("You are my fvt")
    c = c+1

print("Printing the list using for in loop")
list = ['Mohsin','CR',3.98,"He is a good boy"]
for i in list:
    print(i)

print("\nTuple iteration")
list1 = ("I am very cute","Dont be jealous yr","You are my desh")
for i in list1:
    print(i)

print("\nString iteration")
s = "GoodDay"
for i in s:
    print(i)

print("\nindex of elements, using range")
l=["Saad","Moodser","GM","Adrees"]
for index in range(len(l)):
    print(l[index])

for i in range(5):
    print(i)

print("\nCONTINUE")
#Continue-->returns the control to the beginning of the loop
for i in 'Iamveryhappytoday':
    if i == 'y' or i == 'a':
        continue
    print('Current letter',i)

print("\nBREAK")
#break-->bring control out of the loop
for i in 'Iamveryhappytoday':
    if i == 'p':
        break
    print("Current letter",i)

print("\nFunction and passing parameters")
def firstone(fname):
    print(fname," is my first name")

firstone("Mohsin")

print("\n Using Default parameter value, if no value is passed to the function")
def Cname(country = "Pakistan"):
    print("I am from " + country)

Cname("India")
Cname()
Cname("America")

print("\nPassing a list,string,number as parameter")
def traverse(hobby):
    for i in range(len(hobby)):
        print("My hobbies are " + hobby[i])

hobby = ["Cycling","Cricket","Study"]
traverse(hobby)

print("\nReturn values from function")
def add(a,b):
    return a + b
print("Sum of 5 and 7 is ",add(5,7))
print("Concatenating my name ",add("Mohsin"," Saleem"))

print("\nSending Arguments using key=value syntax")
def show(address,fname,sname):
    print("Student name is " + sname + " ,Father name is " + fname + " ,Address is " + address)

show(sname="Mohsin",fname="Saleem",address="Gujranwala")

print("\nCreating Objects, and defining class")
#class-->blueprint or template for creating objects
class student:
    name = "Mohsin"
    age = 20

O1 = student()
print("Student name is " + O1.name + ",age is " + str(O1.age))

print("\nUsing the __init__ method to initialize the object")
class parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_parent = parent("Amir Khan", 54)
print("Parent name is " + my_parent.name) 
print(f"Parent age is {my_parent.age}")

print("\nConstructor Example using a function in the class")
class Dog:
    def __init__(self, name, age):
        self.name = name  # Initialize the name attribute
        self.age = age    # Initialize the age attribute

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)
# Accessing attributes and methods
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
my_dog.bark()








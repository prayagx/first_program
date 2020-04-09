name=input("enter your name: ")
age=input("enter your age: ")
print("hello "+name+" your age is "+age)
print("a simple calculator")
num2=input("enter a number: ")
num3=input("enter the 2nd number: ")
def addition (num2,num3):
    result=int(num2)+int(num3)
    print(result)
def subtraction (num2,num3):
    result = int(num2) - int(num3)
    print(result)
def multiply (num2,num3):
    result = int(num2)*int(num3)
    print(result)
def divide (num2,num3):
    result = float(num2)/float(num3)
    print(result)
print("select an operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
number=input("enter a character between(1-4):  ")
if number=='1':
    addition(num2,num3)
elif number=='2':
    subtraction(num2,num3)
elif number=='3':
    multiply(num2,num3)
elif number=='4':
    divide(num2,num3)
else:
    print("wrong input")



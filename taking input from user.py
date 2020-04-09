#taking user information
name=input("enter your name: ")
age=input("enter your age: ")
print("hello "+name+" your age is "+age)
print("a simple calculator")
#creating a function for add,sub,multiply and division.
def addition (num2,num3):
    num2=input("enter a number: ")
    num3=input("enter the 2nd number: ")
    result=int(num2)+int(num3)
    return result
def subtraction (num2,num3):
    num2 = input("enter a number: ")
    num3 = input("enter the 2nd number: ")
    result = int(num2) - int(num3)
    return result
def multiply (num2,num3):
    num2 = input("enter a number: ")
    num3 = input("enter the 2nd number: ")
    result = int(num2)*int(num3)
    return result
def divide (num2,num3):
    num2 = input("enter a number: ")
    num3 = input("enter the 2nd number: ")
    result = float(num2)/float(num3)
    return result
number=input("enter a character between(1-4):  ")
print("select an operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
#calling of function
if number=='1':
    print(addition(num2,num3))
elif number=='2':
    print(subtraction(num2,num3))
elif number=='3':
    print(multiply(num2,num3))
elif number=='4':
    print(divide(num2,num3))
else:
    print("wrong input")



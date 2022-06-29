# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# first I imported essential modules



try:
    num1= float(input("Enter nubmer: "))
    op = input("Enter operator type")
    num2= float(input("Enter another number: "))
except:
    print("Invalid Input, please input a number")



if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "-":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else :
    print("Invalid Operator, please pick one of the following  + - / *")










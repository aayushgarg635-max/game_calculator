def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

while True:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # print("sum: ",add(a,b))
    # print("subtract: ",subtract(a,b))
    # print("multiply: ",multiply(a,b))
    # print("divide: ",divide(a,b))

    operation = input("choose operations(+,-,*./): ")

    if operation == "+":
        print("sum: ",add(a,b))

    elif operation == "-":
     print("subtract: ",subtract(a,b))

    elif operation == "*":
     print("multiply: ",multiply(a,b))

    elif operation =="/" and b == 0:
     print(" the second number is zero leading to absurd result")

    elif operation == "/":
     print("divide: ",divide(a,b))
     
    else:
     print("Invlid Input")

    choice = input("do you want to calculate again:{yes} or {no}")

    if choice == "no":
      print("calculator closed. Goodbye!")
      break




     
     
     

    
 
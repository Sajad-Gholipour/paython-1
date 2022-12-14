import math

op = input( "please enter your operation: ")

if op == "+" or op == "-" or op == "*" or op == "/":

    a = float(input( "please enter your first number: "))
    b = float(input( "please enter your second number: "))
    if op == "+": 
        result = a + b
        print(result)
    if op == "-": 
        result = a - b
        print(result)
    if op == "*": 
        result = a * b
        print(result)
    if op == "/":
        if b == 0:
            result = "error"
        if b != 0:
            result = a / b  
            print(result)

elif op == "radical" or op == " factorial" or op == "sin" or op == "cos" or op == "tan" or op == "cot":
    a = float(input("please enter your number: "))

    if op == "sin":
        result = math.sin(math.radians(a))
        print(result)
    if op == "cos":
        result = math.cos(math.radians(a))
        print(result)
    if op == "tan":
        result = math.tan(math.radians(a))
        print(result)
    if op == "cot":
        if math.sin(math.radians(a)) != 0:
            result = 1/(math.tan(math.radians(a))) 
        else:    
            result = "Error"
        print(result)
    
    if op == "radical":
        if a >= 0:
            result = math.radical(a)
            print(result)

    if op == "factorial":
        result = math.factorial(int(a))    
        print(result)             
name = input(" please enter your name: ")
family = input(" please enter your family: ")
A = float(input("please enter your first lesson: "))
B = float(input("please enter your second lesson: "))
C = float(input("please enter your third lesson: "))

if A <=20>=0 and B <=20>=0 and C <=20>=0:
    average = ( A + B + C ) / 3
    if average >= 17:
        print("greate")
    if average <17>=12:
        print("normal")        
    if average <12:
        print("fail")
else:
    print("Error") 
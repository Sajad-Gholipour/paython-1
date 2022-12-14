a = float(input("please enter first number: "))
b = float(input("please enter second number: "))
c = float(input("please enter third number: "))

if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        print("می توان مثلث رسم کرد")
    else:
        print("نمی توان مثلت رسم کرد") 
else:
    print("Error")
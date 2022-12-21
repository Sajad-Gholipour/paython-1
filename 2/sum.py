box = []

while True:
    a = (input("enter your number\nWhen you need to see your result type exit :) "))

    if a == "Exit":
        result = sum(box)
        print("result:", result)
        break
    
    box.append(float(a))

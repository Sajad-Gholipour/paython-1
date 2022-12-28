r = int(input("enter a value for number of rows: "))
c = int(input("enter a value for number of columns: "))
s = 1

for i in range(1 , r+1):
    for j in range(1 , c+1):
        if s == 1:
            print(end=("*"))
        else:
            print(end=("#"))
        s = -s
    if c % 2 == 0:
        s*= -1
    print()
    

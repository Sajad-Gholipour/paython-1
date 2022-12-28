import numpy
import math
print("moadele daraje 2 = ax^2 + bx + c")
a = int(input("please enter a: "))
b = int(input("please enter b: "))
c = int(input("please enter c: "))
delta = b * b -4 * a * c
if delta == 0:
    x = -b + math.sqrt(delta)
    print("moadele yek javab darad, x=", x)

elif delta < 0:
    print("moadele javab haghighi nadarad :< ")
else :
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("moadele 2 javab darad.\nx1 = ",x1,"\nx2 = ",x2)
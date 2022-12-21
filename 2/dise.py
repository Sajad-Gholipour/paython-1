import random

dise = random.randint(1, 6)
prize = random.randint(1, 6)


while True:
    if dise != 6:
        print("dise :", dise)
        break
            
    elif dise == 6:
        print("dise :", dise)
        print("lucky, you win a prize\nprize :", prize)
        break
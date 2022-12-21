import random
count = 0

pc_number = random.randint(0, 20)
while True:
    user_number = int(input("enter number: "))

    if pc_number < user_number:
        print("decrease")
        count = count + 1
    elif pc_number > user_number:
        print("increase")
        count = count + 1
    elif pc_number == user_number:
        print("win")
        print(count)
        break

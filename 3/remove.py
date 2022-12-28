a = [8,0,3,0,4,1,8,8,10,7]

def remove_duplicate(group):
    b = []
    for number in group :
        if number not in b :
            b.append(number)
    return b
print(remove_duplicate(a))





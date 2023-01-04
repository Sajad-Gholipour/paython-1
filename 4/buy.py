products = []
def read_file():
    f = open("database.txt", "r")
    for line in f:
        result = line.split(",")
        my_dic = {"id":result[0],"name":result[1],"price":result[2],"count":result[3]}
        products.append(my_dic)
       


def show_menu():
    print("1- add")
    print("2- remove")    
    print("3- search")
    print("4- edit")
    print("5- show_list")
    print("6- buy")
    print("7- exit")

def add():
    id = input("id: ")
    name = input("name: ")
    price = input("price: ")
    count = input("count: ")  

    new_dic = {"id":id,"name":name,"price":price,"count":count}
    products.append(new_dic)
    print(products)


def remove():
    key = input("Enter the product key: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            products.remove(product)
            print(products)
            show_list()
            break
def search():
    key = input("enter your key: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            print(product)
            break
    else:
        print("not found")    

def show_list():
    print("id\tname\tprice\tcount")
    for product in products:
        print(product["id"],product["name"],product["price"],product["count"] )
def buy():
    read_file()
    buy_list = []
    key = input("Enter the id key of name key of the product: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            print(product)
            number = int(input("How many do wanna purchase? : "))
            count = int(product["count"])
            price = int(product["price"])
            print(price)
            print(count)
            if count == 0:
                price("Eror")
                break
            if number > count:
                print("there isnt enough product")
                break
            else:
                print("available")
                
                b = input("Do you want to buy: ")
                if b == "yes":
                    Total_price = number * price
                    print("Total price is: ", Total_price)
                    buy_list.append(product["name"])
                    buy_list.append(count)
                    buy_list.append(Total_price)
                    print(buy_list)
                    show_list()
                    break
            

def save_to_database():
    q = input("save to database? ")
    if q == "yes":
        q = open("database.txt", "a")
        for product in products:
            q.write(str(product))
            q.write("")
        print(product)
    else:
        print("Not saved")
read_file() 
while True:
    show_menu()

read_file()

while True:
    show_menu()

    user_choice = int(input("enter your choice: "))

    if user_choice == 1:
        add()
    elif  user_choice == 2: 
        remove()
    elif  user_choice == 3:
        search()
    elif  user_choice == 4:
        edit() 
    elif  user_choice == 5: 
        show_list() 
    elif  user_choice == 6:
        buy()
    elif  user_choice == 7:
        save_to_database()
        exit(0)  

    else:
        print("please select another")    
     
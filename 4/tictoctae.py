import pyfiglet
count =0
def show():
    for row in game_board:
        for cell in row:
            print(cell, end="")
        print() 

def check_game():
    if( game_board[0][0]=="X " and game_board[0][1]=="X " and game_board[0][2]=="X " or 
        game_board[1][0]=="X " and game_board[1][1]=="X " and game_board[1][2]=="X " or
        game_board[2][0]=="X " and game_board[2][1]=="X " and game_board[2][2]=="X " or
        game_board[2][0]=="X " and game_board[1][1]=="X " and game_board[0][2]=="X " or
        game_board[0][0]=="X " and game_board[1][1]=="X " and game_board[2][2]=="X " or
        game_board[0][0]=="X " and game_board[1][0]=="X " and game_board[2][0]=="X " or
        game_board[0][1]=="X " and game_board[1][1]=="X " and game_board[2][1]=="X " or
        game_board[0][2]=="X " and game_board[1][2]=="X " and game_board[2][2]=="X "):
        
        print("pleyer1 wins")

    
    if( game_board[0][0]=="O " and game_board[0][1]=="O " and game_board[0][2]=="O " or 
        game_board[1][0]=="O " and game_board[1][1]=="O " and game_board[1][2]=="O " or
        game_board[2][0]=="O " and game_board[2][1]=="O " and game_board[2][2]=="O " or
        game_board[2][0]=="O " and game_board[1][1]=="O " and game_board[0][2]=="O " or
        game_board[0][0]=="O " and game_board[1][1]=="O " and game_board[2][2]=="O " or
        game_board[0][0]=="O " and game_board[1][0]=="O " and game_board[2][0]=="O " or
        game_board[0][1]=="O " and game_board[1][1]=="O " and game_board[2][1]=="O " or
        game_board[0][2]=="O " and game_board[1][2]=="O " and game_board[2][2]=="O "):

        print("pleyer2 wins")



title = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
print (title)

game_board = [["- ", "- ", "- "],
               ["- ", "- ", "- "],
               ["- ", "- ", "- "]] 

show()

while True :

    print("player1")
  
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <=2 and 0 <= col <= 2 :
        
            if game_board[row][col] == "- ":
                game_board[row][col] ="X "
                count = count +1
                show()
                break
            else:
                print("select another cell")
        else:
            print("enter row and col between 0 and 2")

        check_game()


    print ("player2")
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <=2 and 0 <= col <= 2 :        
            if game_board[row][col] == "- ":
                game_board[row][col] ="O "
                count = count +1
                show()
                break
            else:
                print("select another cell") 
        else:
            print("enter row and col between 0 and 2")

        check_game()


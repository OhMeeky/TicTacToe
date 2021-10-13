#@OhMeeky :)

bos = [[], [], [],
      [], [], [],
      [], [], []]

Game = True
System = True

def print_board(bo=bos, slot=0):
    #print(f"{bo[slot]} - {bo[slot]} - {bo[slot]}\n{bo[slot]} - {bo[slot]} - {bo[slot]}\n{bo[slot]} - {bo[slot]} - {bo[slot]}\n")
    print(f"{bo[0]} - {bo[1]} - {bo[2]}\n{bo[3]} - {bo[4]} - {bo[5]}\n{bo[6]} - {bo[7]} - {bo[8]}\n")
    
def update_board(bos, action, player_sym, P1):
    new_sym = bos[int(action)] = player_sym
    print_board(bos, new_sym)
    check(P1, bos)
    
def clear_board():
    bos = [[], [], [],
      [], [], [],
      [], [], []]
    
def stop_game(P1):
    print(P1, " Has Won")
    decision = input("Would you like to continue? Y/N: ")
    if decision == 'Y':
        System = True
        clear_board()
    if decision == 'N':
        System == False
        
        
        
def check(P1, bo):
    if bo[0] == "O" and bo[3] == "O" and bo[6] == "O":
        stop_game(P1)
    elif bo[1] == "O" and bo[4] == "O" and bo[7] == "O":
        stop_game(P1)
    elif bo[2] == "O" and bo[5] == "O" and bo[8] == "O":
        stop_game(P1)
    elif bo[0] == "O" and bo[1] == "O" and bo[2] == "O":
        stop_game(P1)
    elif bo[3] == "O" and bo[4] == "O" and bo[5] == "O":
        stop_game(P1)
    elif bo[6] == "O" and bo[7] == "O" and bo[8] == "O":
        stop_game(P1)
    elif bo[0] == "O" and bo[4] == "O" and bo[8] == "O":
        stop_game(P1)
    elif bo[2] == "O" and bo[4] == "O" and bo[6] == "O":
        stop_game(P1)
    elif bo[0] == "X" and bo[3] == "X" and bo[6] == "X":
        stop_game("X")
    elif bo[1] == "X" and bo[4] == "X" and bo[7] == "X":
        stop_game("X")
    elif bo[2] == "X" and bo[5] == "X" and bo[8] == "X":
        stop_game("X")
    elif bo[0] == "X" and bo[1] == "X" and bo[2] == "X":
        stop_game("X")
    elif bo[3] == "X" and bo[4] == "X" and bo[5] == "X":
        stop_game("X")
    elif bo[6] == "X" and bo[7] == "X" and bo[8] == "X":
        stop_game("X")
    elif bo[0] == "X" and bo[4] == "X" and bo[8] == "X":
        stop_game("X")
    elif bo[2] == "X" and bo[4] == "X" and bo[6] == "X":
        stop_game("X")   

        
def game():
    while System:
        symbol = False
        symbol_list = ["X","O"]
        Player1_sym = False
        #Current_player = Player1_sym
        
        action_list = [0,1,2,3,4,5,6,7,8]
        
        while Player1_sym not in symbol_list:
            
            Player1_sym = input("What symbol would you like to choose? X or O : ")
            
            if Player1_sym not in symbol_list:
                print("Please choose either X or O: ")
                
            if Player1_sym == "O":
                #Current_player = Player1_sym
                Player2_sym = "X"
                P1 = Player1_sym
                P2 = Player2_sym
            if Player1_sym == "X":
                #Current_player = Player1_sym
                Player2_sym = "O"
                P1 = Player1_sym
                P2 = Player2_sym
                
        while Game:
            print("Turn: ", P1)
            action = input("Input a number between 0 - 8: ")
            
            if action not in action_list:
                print("Number must be int 0 - 9 or Number already selected")
            update_board(bos, int(action), P1, P1)
            P1, P2 = P2, P1
            action_list.remove(int(action))
            
print_board(bos)
game()



class tictac():
    def __init__(self):
        self.user = []
        self.computer = []
        self.empty = [1,2,3,4,5,6,7,8,9]
        self.cells = [" "," "," "," "," "," "," "," "," "]

    def display(self):
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("---|---|---")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("---|---|---")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")

    def computerInsert(self):
        y = 0
        for i in range(0, len(self.user),1):
            for j in range(i,len(self.user),1):

                if self.user[i] == None:
                    x = random.choice(self.empty)
                    self.empty.remove(x)
                    y = 1
                    break
                    

                if self.user[i] != None and self.user[j] == None:
                    x = random.choice(self.empty)
                    self.empty.remove(x)
                    y = 1
                    break
                
                if self.user[i] == 1 and self.user[j] == 2:
                    if 3 in self.empty :
                        x = 3
                        self.empty.remove(x)
                        y = 1
                        break
                
                if self.user[i] == 1 and self.user[j] == 5:
                    if 9 in self.empty :
                        x = 9
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 1 and self.user[j] == 4:
                    if 7 in self.empty :
                        x = 7
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 2 and self.user[j] == 3:
                    if 1 in self.empty :
                        x = 1
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 2 and self.user[j] == 5:
                    if 8 in self.empty :
                        x = 8
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 3 and self.user[j] == 6:
                    if 9 in self.empty :
                        x = 9
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 3 and self.user[j] == 5:
                    if 7 in self.empty :
                        x = 7
                        self.empty.remove(x)
                        y = 1
                        break

                if self.user[i] == 4 and self.user[j] == 5:
                    if 6 in self.empty :
                        x = 6
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 4 and self.user[j] == 7:
                    if 1 in self.empty :
                        x = 1
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 5 and self.user[j] == 6:
                    if 4 in self.empty :
                        x = 4
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 5 and self.user[j] == 8:
                    if 2 in self.empty :
                        x = 2
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 5 and self.user[j] == 9:
                    if 1 in self.empty :
                        x = 1
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 5 and self.user[j] == 7:
                    if 3 in self.empty :
                        x = 3
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 6 and self.user[j] == 9:
                    if 3 in self.empty :
                        x = 3
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 7 and self.user[j] == 8 :
                    if 9 in self.empty :
                        x = 9
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 8 and self.user[j] == 9:
                    if 7 in self.empty :
                        x = 7
                        self.empty.remove(x)
                        y = 1
                        break
                
                
            if(y == 1):
                break

        if( y == 1):
            return x

                
        else:
            x = (random.choice(self.empty))
            self.empty.remove(x)
            return x
        
                        


    def checkWin(self, player_list: list):
        if (len(self.empty) > 4):
            return
        for i in range(0, 7, 3):
            if(i+1 in player_list and i+2 in player_list and i+3 in player_list):
                print("Game won")
                return
        for j in range(1, 4):
            if (j in player_list and j+3 in player_list and j+6 in player_list):
                print("Game won")
                return
        if ((1 in player_list and 5 in player_list and 9 in player_list) or (3 in player_list and 5 in player_list and 7 in player_list)):
            print("Game won")
            return
        
    def playGame(self):
        while True:
            while self.empty:
                move = input("Enter the position where you want to place your move")
                move = int(move)
                while(move not in self.empty):
                    print("Invald Choice. The space has already been occupied.")
                    move = input("Enter the position where you want to place your move")
                    move = int(move) 
                    #add a loop here to reenter the choice

                #remove move from the empty array
                self.empty.remove(move)
                self.empty.sort()
                self.user.append(move)
                self.user.sort()
                self.checkWin(self.user)  #this will have a break thingy if there is a win
                if not self.empty:
                    print("There are no more spaces to be filled, it's a tie.")
                    break
                #there should be exit statements in the check win function that exit the loop incase there's a win
                cmove = int(self.computerInsert())
                self.cells[cmove - 1 ] = "O"
                #remove cmove from the empty array
                self.computer.append(cmove)
                self.empty.sort()
                self.computer.sort()
                self.checkWin(self.computer)  #this will have a break thingy if there is a win
                if not self.empty:
                    print("There are no more spaces to be filled, it's a tie.")
                    break
                
            choice = input("Would you like to play another game?")
            if choice == 'No': #no podanum da yes illa :)
                break
            
            return


Tc= tictac()

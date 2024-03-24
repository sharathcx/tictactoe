
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
            self.cells[x - 1 ] = "O"
            self.computer.append(x)
            self.empty.sort()
            self.computer.sort() 

                
        else:
            x = (random.choice(self.empty))
            self.empty.remove(x)
            self.cells[x - 1 ] = "O"
            self.computer.append(x)
            self.empty.sort()
            self.computer.sort() 
                        


    def checkWin(self):
        empty_count = len([x for x in self.cells if x == " "])
        if (empty_count > 4): #To check if the minimum number of moves have been played. Minimum of 5 moves is required, hence max no. of " " will be 9-5 = 4.
            return False
        for i in range(0, 7, 3):
            if((self.cells[i] == self.cells[i+1] == self.cells[i+2] == "X") or (self.cells[i] == self.cells[i+1] == self.cells[i+2] == "O")): #Checking horizontal rows
                return True
        for i in range(0, 3):
            if((self.cells[i] == self.cells[i+3] == self.cells[i+6] == "X") or (self.cells[i] == self.cells[i+3] == self.cells[i+6] == "O")): #Checking vertical columns
                return True
        if((self.cells[0] == self.cells[4] == self.cells[8] == "X") or (self.cells[0] == self.cells[4] == self.cells[8] == "O") or (self.cells[2] == self.cells[4] == self.cells[6] == "X") or (self.cells[2] == self.cells[4] == self.cells[6] == "X")): #Checking diagonals
            return True
        return False
        
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
                
                if not self.empty:
                    print("There are no more spaces to be filled, it's a tie.")
                    break
                
            choice = input("Would you like to play another game?")
            if choice == 'No': #no podanum da yes illa :)
                break
            
            return


Tc= tictac()

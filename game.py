import random


class tictac():
    def __init__(self):
        self.user = []
        self.computer = []
        self.empty = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print("Tic Tac Toe")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")
        print("---|---|---")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("---|---|---")
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")

    def computerInsert(self):
        y = 0
        for i in range(0, len(self.user), 1):
            for j in range(i, len(self.user), 1):

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
                    if 3 in self.empty:
                        x = 3
                        self.empty.remove(x)
                        y = 1
                        break

                if self.user[i] == 1 and self.user[j] == 5:
                    if 9 in self.empty:
                        x = 9
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 1 and self.user[j] == 4:
                    if 7 in self.empty:
                        x = 7
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 2 and self.user[j] == 3:
                    if 1 in self.empty:
                        x = 1
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 2 and self.user[j] == 5:
                    if 8 in self.empty:
                        x = 8
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 3 and self.user[j] == 6:
                    if 9 in self.empty:
                        x = 9
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 3 and self.user[j] == 5:
                    if 7 in self.empty:
                        x = 7
                        self.empty.remove(x)
                        y = 1
                        break

                if self.user[i] == 4 and self.user[j] == 5:
                    if 6 in self.empty:
                        x = 6
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 4 and self.user[j] == 7:
                    if 1 in self.empty:
                        x = 1
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 5 and self.user[j] == 6:
                    if 4 in self.empty:
                        x = 4
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 5 and self.user[j] == 8:
                    if 2 in self.empty:
                        x = 2
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 5 and self.user[j] == 9:
                    if 1 in self.empty:
                        x = 1
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 5 and self.user[j] == 7:
                    if 3 in self.empty:
                        x = 3
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 6 and self.user[j] == 9:
                    if 3 in self.empty:
                        x = 3
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 7 and self.user[j] == 8:
                    if 9 in self.empty:
                        x = 9
                        self.empty.remove(x)
                        y = 1

                        break

                if self.user[i] == 8 and self.user[j] == 9:
                    if 7 in self.empty:
                        x = 7
                        self.empty.remove(x)
                        y = 1
                        break

            if (y == 1):
                break

        if (y == 1):
            self.cells[x - 1] = "O"
            self.computer.append(x)
            self.empty.sort()
            self.computer.sort()


        else:
            x = (random.choice(self.empty))
            self.empty.remove(x)
            self.cells[x - 1] = "O"
            self.computer.append(x)
            self.empty.sort()
            self.computer.sort()

    def checkWin(self):
        empty_count = len([x for x in self.cells if x == " "])
        if (
                empty_count > 4):  # To check if the minimum number of moves have been played. Minimum of 5 moves is required, hence max no. of " " will be 9-5 = 4.
            return False
        for i in range(0, 7, 3):
            if ((self.cells[i] == self.cells[i + 1] == self.cells[i + 2] == "X") or (
                    self.cells[i] == self.cells[i + 1] == self.cells[i + 2] == "O")):  # Checking horizontal rows
                return True
        for i in range(0, 3):
            if ((self.cells[i] == self.cells[i + 3] == self.cells[i + 6] == "X") or (
                    self.cells[i] == self.cells[i + 3] == self.cells[i + 6] == "O")):  # Checking vertical columns
                return True
        if ((self.cells[0] == self.cells[4] == self.cells[8] == "X") or (
                self.cells[0] == self.cells[4] == self.cells[8] == "O") or (
                self.cells[2] == self.cells[4] == self.cells[6] == "X") or (
                self.cells[2] == self.cells[4] == self.cells[6] == "X")):  # Checking diagonals
            return True
        return False

    def playGame(self):
        while True:
            while True:
                player = input("Single or Multiplayer?")
                if player != "Single" or player != "Multiplayer":
                    break

            while self.empty:

                if player == "Single":
                
                    user_inp = int(input("Enter the index you want to insert"))  # user input given in playgame fun. since there's no separate function
                    if user_inp in self.empty:
                        self.empty.remove(user_inp)
                        self.cells[user_inp - 1] = "X"
                        self.display()
                    else:
                        print("Enter a valid position")
                        continue
                   
                    if self.checkWin():
                        print("The player wins!")
                        break
                    self.computerInsert()
                    self.display()
                    if self.checkWin():
                        print("The computer wins!")
                        break

                elif player == "Multiplayer":

                    user_1 = int(input("Player 1, enter the index you want to insert"))
                    if user_1 in self.empty:
                        self.empty.remove(user_1)
                        self.cells[user_1 - 1] = "X"
                        self.display()
                    else:
                        print("Enter a valid position")
                        continue
                    
                    if self.checkWin():
                        print("Player 1 wins!")
                        break

                    if not self.checkWin() and len(self.empty)==0:
                        print("The match is a draw!") 
                        break

                    user_2 = int(input("Player 2, enter the index you want to insert"))
                    if user_2 in self.empty:
                        self.empty.remove(user_2)
                        self.cells[user_2 - 1] = "O"
                        self.display()
                    else:
                        print("Enter a valid position")
                        continue

                    if self.checkWin():
                        print("Player 2 wins!")
                        break
           
                    if not self.checkWin() and len(self.empty)==0:
                        print("The match is a draw!") 

            again = input("Would you like to play another game?")
            if again == "yes":
                self.cells = [" " for x in range(9)]
                self.user = []
                self.computer = []
                self.empty = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                continue
            else:
                break

        return


Tc = tictac()
Tc.playGame()

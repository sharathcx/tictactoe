import random


class TicTacToe:

    def __init__(self):
        self.param = [" " for x in range(10)]
        self.status = None

    def board(self):
        print(f" ------ TicTacToe ------ ")
        print(f" |  {self.param[7]}  |   {self.param[8]}  |   {self.param[9]}  |")
        print(f" |  {self.param[4]}  |   {self.param[5]}  |   {self.param[6]}  |")
        print(f" |  {self.param[1]}  |   {self.param[2]}  |   {self.param[3]}  |")
        print(" ----------------------- ")

    def win(self):
        if " " not in self.param:
            print("Draw")
            return True
        if self.param[7] != " " and (self.param[7] == self.param[8] == self.param[9]):
            print(f"Player {self.param[7]} wins")
            return True
        elif self.param[4] != " " and (self.param[4] == self.param[5] == self.param[6]):
            print(f"Player {self.param[4]} wins")
            return True
        elif self.param[1] != " " and (self.param[1] == self.param[2] == self.param[3]):
            print(f"Player {self.param[1]} wins")
            return True
        elif self.param[1] != " " and (self.param[1] == self.param[4] == self.param[7]):
            print(f"Player {self.param[1]} wins")
            return True
        elif self.param[3] != " " and (self.param[3] == self.param[6] == self.param[9]):
            print(f"Player {self.param[3]} wins")
            return True
        elif self.param[1] != " " and (self.param[1] == self.param[5] == self.param[9]):
            print(f"Player {self.param[1]} wins")
            return True
        elif self.param[3] != " " and (self.param[3] == self.param[5] == self.param[7]):
            print(f"Player {self.param[3]} wins")
            return True
        return False

    def game(self):
        print("Player 1: O")
        print("Player 2: X")
        self.param = [" " for x in range(10)]
        self.board()
        while True:
            o = int(input("Player 1 input position :"))
            if self.param[o] == " ":
                self.param[o] = "O"
                self.board()
            else:
                print("Foul")
                pass
            if self.win():
                break
            x = int(input("Player 2 input position"))
            if self.param[x] == " ":
                self.param[x] = "X"
                self.board()
            else:
                print("Foul")
                pass
            if self.win():
                break

    # computer is player 2 and is X
    def computer(self):
        while True:
            if self.win():
                return
            o = int(input("Player 1 input position :"))
            if self.param[o] == " ":
                self.param[o] = "O"
                self.board()
            else:
                o = 99
                print("Foul")
                pass
            if o == 5:
                if self.win():
                    return
                choice = random.choice([2, 4, 8, 6])
                while self.param[choice] != " ":
                    choice = random.choice([2, 4, 8, 6])
                self.param[choice] = "X"
            elif o == 7:
                if self.win():
                    return
                choice = random.choice([4, 8, 5])
                while self.param[choice] != " ":
                    choice = random.choice([4, 8, 5])
                self.param[choice] = "X"
            elif o == 9:
                if self.win():
                    return
                choice = random.choice([6, 8, 5])
                while self.param[choice] != " ":
                    choice = random.randint(0, 9)
                self.param[choice] = "X"
            elif o == 3:
                if self.win():
                    return
                choice = random.choice([6, 2, 5])
                while self.param[choice] != " ":
                    choice = random.randint(0, 9)
                self.param[choice] = "X"
            elif o == 1:
                if self.win():
                    return
                choice = random.choice([4, 2, 5])
                while self.param[choice] != " ":
                    choice = random.randint(0, 9)
                self.param[choice] = "X"

            elif o == 4:
                if self.win():
                    return
                choice = random.choice([1, 7, 5])
                while self.param[choice] != " ":
                    choice = random.randint(0, 9)
                self.param[choice] = "X"

            elif o == 8:
                if self.win():
                    return
                choice = random.choice([9, 7, 5])
                while self.param[choice] != " ":
                    choice = random.randint(0, 9)
                self.param[choice] = "X"

            elif o == 6:
                if self.win():
                    return
                choice = random.choice([9, 3, 5])
                while self.param[choice] != " ":
                    choice = random.randint(0, 9)
                self.param[choice] = "X"

            elif o == 2:
                if self.win():
                    return
                choice = random.choice([1, 3, 5])
                while self.param[choice] != " ":
                    choice = random.randint(0, 9)
                self.param[choice] = "X"
            else:
                if self.win():
                    return
                choice = random.randint(1, 9)
                while self.param[choice] != " ":
                    choice = random.randint(0, 9)
                self.param[choice] = "X"
            self.board()
            if self.win():
                return


obj = TicTacToe()
chocie = int(input("Enter the mode\n1 : Multiplayer\n2 : Computer\n"))
if chocie == 1:
    obj.game()
else:
    obj.computer()
    

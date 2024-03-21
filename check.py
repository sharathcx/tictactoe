def CheckC_Row_Col(ttc: list[list]): #Function to check the result conditionality
    for i in range(3):
        if(ttc[i][0] == ttc[i][1] == ttc[i][2] == 'X' or ttc[i][0] == ttc[i][1] == ttc[i][2] == 'O' or 
           ttc[0][i] == ttc[1][i] == ttc[2][i] == 'X' or ttc[0][i] == ttc[1][i] == ttc[2][i] == 'O'):
            return True
    if(ttc[0][0] == ttc[1][1] == ttc[2][2] == 'X' or ttc[0][0] == ttc[1][1] == ttc[2][2] == 'O' or
       ttc[0][2] == ttc[1][1] == ttc[2][0] == 'X' or ttc[0][2] == ttc[1][1] == ttc[2][0] == 'O'):
        return True
    return False

def printBoard(ttc: list[list]): #Function to print out the elements
    for i in range(3):
        for j in range(3):
            print(ttc[i][j], end=" ")
        print("\n")

def result(ttc: list[list], c:int): #Function to determine the result after each input
    if(5 <= c < 9):
        if(CheckC_Row_Col(ttc)):
            print("Player", (c%2), "won") if c %2 !=0 else print("Player", (c%2 + 2), "won")
            return False
            
    elif(c == 9):
        if(CheckC_Row_Col(ttc)):
            print("Player", (c%2), "won") if c %2 !=0 else print("Player", (c%2 + 2), "won")
            return False
        print("Match drawn")
        return False
    

def checkDup(ll: list[list], r:int, j:int): #Function to check if there already exists an element in the space specified by the input. Here 'r' is the row no. and 'j' is the column no.
    if ll[r][j] == "X" or ll[r][j] == "O":
        return False
        
        
l1 = ['-' for i in range(3)]
l2 = ['-' for i in range(3)]
l3 = ['-' for i in range(3)]
list_of_l = [l1, l2, l3]
print(list_of_l)
p1 = 'X'
p2 = 'O'
inp_list = [p1, p2]
c = 0 #Count of inputs

while True:
    num = int(input()) #Location number which can take a value in the range 1 to 9
    if(num < 1 or num > 9):
        print("Invalid input. Try again.")
    else:
        if(1 <= num <= 3):
            y = checkDup(list_of_l, 2, num - 1)
            if y is False:
                continue
            list_of_l[2][num - 1] = inp_list[c%2]
            c += 1
        elif(4 <= num <=6):
            y = checkDup(list_of_l, 1, (num % 3) - 1)
            if y is False:
                continue
            list_of_l[1][(num % 3) - 1] = inp_list[c%2]
            c += 1
        else:
            y = checkDup(list_of_l, 0, (num % 3) - 1)
            if y is False:
                continue
            list_of_l[0][(num % 3) - 1] = inp_list[c%2]
            c += 1
        printBoard(list_of_l)
        x = result(list_of_l, c)
        if x is False:
            break   
            
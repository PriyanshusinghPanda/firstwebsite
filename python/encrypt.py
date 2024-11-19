def printBoard(li):
    for i in li:
        print(i[0],i[1],i[2],sep="|")
def checkGame(li):
    li0 = li[0]
    li1 = li[1]
    li2 = li[2]
    for i in range(3):
        if li0[i]==li1[i]==li2[i]=="x" or li0[i]==li1[i]==li2[i]=="o":
            return li0[i]
        elif li[i][0]==li[i][1]==li[i][2]=="x" or li[i][0]==li[i][1]==li[i][2]=="o":
            return li[i][0]
    if li0[0]==li1[1]==li2[2]=="x" or li0[0]==li1[1]==li2[2]=="o" or li0[2]==li1[1]==li2[0]=="x" or li0[2]==li1[1]==li2[0]=="o":
        return li1[1]
    if "_" not in li0 and "_" not in li1 and "_" not in li2:
        return "DRAW"
    return "NO WINNER"
def markUserOption(li,pos,turn):
    index = pos//3
    posindex = pos%3
    if li[index][posindex]=="_":
        li[index][posindex]=turn
        return li
    return li[index][posindex]


li = [["_","_","_"],["_","_","_"],["_","_","_"]]
# the X will be represented by x
# the O will be represent by o
print("the oponent will place x and o in the lowercase")
print("the oponent need to give the input of the field in which they want to place 'x' or 'o'")

printBoard(li)

turn = "x"
while True:
    pos = int(input(f"where you want to place the {turn}:-"))
    templi = markUserOption(li,pos,turn)
    if templi=="x" or templi=="o":
        print(f"invalid operatin:- the {templi} already present")
    else:
        li = templi
    win = checkGame(li)
    printBoard(li)
    if win=="x" or win=="o":
        print(f"the player with {turn} won the game")
        break
    elif win=="DRAW":
        print("the game has been drawed")
        break
    if turn=="x":
        turn="o"
    else:
        turn="x"

import random

def won()


def easyComputer(li):
    while True:
        compMove = random.choices(li)
        humanMove = input("Enter your choice human (stone,paper,scissors):-")
        if 

    






print("1:- play with computer")
print("2:- play with human")
print("3:- play with computer(hard)")
print("4:- play with computer(extreme hard)(don't play alone BRAT!!)")
level = int(input("whats your choice"))
li = ["stone","paper","scissors"]

if level == 1:
    easyComputer(li)



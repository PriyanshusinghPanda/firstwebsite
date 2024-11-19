d = list(map(int,input().split()))
# ind = -1
# for i in range(len(d)):
#     if d[i] % 3 == 0:
#         ind=d[i]
#         break
# print(ind)
def divisibleByThree(ar):
    tu = []
    for i in ar:
        if i%3==0:
            tu.append(i)
    return tuple(tu)
            


# ind = -1
# for i in range(len(d)):
#     if d[i] % 3 == 0:
#         ind=d[i]
print(divisibleByThree(d))
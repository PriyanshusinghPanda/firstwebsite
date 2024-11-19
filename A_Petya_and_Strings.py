first=input()
second=input()
first=first.lower()
second=second.lower()

# if first>second:
#     print(1)
# elif first<second:
#     print(-1)
# elif first==second:
#     print(0)
c = 0
for i in range(len(first)):
    if first[i]>second[i]:
        c = 1
        break
    elif first[i]<second[i]:
        c = -1
        break
print(c)
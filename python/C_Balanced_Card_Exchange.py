n , m = map(int,input().split())
li = list(map(int,input().split()))
d = set(li)
odd , even = 0,0
i = 0
new = list(d)
if n%2!=0:
    print(-1)
else:
    while i<len(new):
        if new[i]%2==0:
            even+=1
        else:
            odd+=1
        i += 1
        if odd==n//2 or even==n//2:
            break

    if odd==even==n//2:
        print(0)
        print(*sorted(new))
    else:
        j = 1
        a = odd+even
        
        while odd!=n//2:
            if j not in new:
                new.append(j)
                odd+=1
            j+=2
        j = 2
        while even!=n//2:
            if j not in new:
                new.append(j)
                even+=1
            j+=2
        print(odd+even-a)
        print(*sorted(new))
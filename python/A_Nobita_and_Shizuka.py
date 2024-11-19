width, length = map(int,input().split())
w_cut, l_cut = map(int,input().split())
wcuts = list(map(int,input().split()))
lcuts = list(map(int,input().split()))
maxwidth = wcuts[0]
for i in range(w_cut-1):
    if wcuts[i+1]-wcuts[i]>=maxwidth:
        maxwidth = wcuts[i+1]-wcuts[i]
if width-wcuts[-1]>maxwidth:
    maxwidth = width-wcuts[-1]

maxheight = lcuts[0]
for i in range(l_cut-1):
    if lcuts[i+1]-lcuts[i]>=maxheight:
        maxheight = lcuts[i+1]-lcuts[i]

if length-lcuts[-1]>maxheight:
    maxheight = length-lcuts[-1]  
print(maxwidth*maxheight)


# n, m = map(int, input().split()) 
# x, y = map(int, input().split()) 
# arr_x = list(map(int, input().split()))
# arr_y = list(map(int, input().split()))

# umm_x = [arr_x[0]] 
# for i in range(x - 1):  
#     umm_x.append(arr_x[i+1] - arr_x[i])

# umm_x.append(n - arr_x[-1]) 

# umm_y = [arr_y[0]]  
# for i in range(y - 1): 
#     umm_y.append(arr_y[i+1] - arr_y[i])
# umm_y.append(m - arr_y[-1])  

# max_area = max(umm_x) * max(umm_y)
# print(max_area)
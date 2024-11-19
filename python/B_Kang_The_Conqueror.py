# # def subsets(s):  
# #     if len(s) == 0:  
# #         return [[]]  
# #     x = subsets(s[:-1])  
# #     return x + [[s[-1]] + y for y in x]  

# # t = int(input())
# # for _ in range(t):
# #     n = int(input())
# #     li = list(map(int,input().split()))
# #     subset = subsets(li)
# #     ans = 0
# #     for i in subset:
# #         if i==[]:
# #             pass
# #         else:
# #             ans += max(i)
# #     print(ans)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     m = 1000000007
#     li = sorted(list(map(int,input().split())))
#     ans = 0 
#     p = 1
#     for i in range(n):
#         ans = (ans+p* li[i])%m
#         p = (p*2)%m
#     print(ans)


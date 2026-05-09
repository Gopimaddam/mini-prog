d={'M':1000,'D':500,'C':100,'L':50,'X':10,'I':1}
# s="MLXII"
# res=0
# last_digit=0
# for ch in s[::-1]:
#     if(d[ch]>=last_digit):
#         res+=d[ch]
#         last_digit=d[ch]
#     else:
#         res-=d[ch]
# print(res)   


s="MCDXLII"
res=0
last_digit=10000
for ch in s:
    if(d[ch]<=last_digit):
        res+=d[ch]
    else:
        res=d[ch]-last_digit
print(res)



    
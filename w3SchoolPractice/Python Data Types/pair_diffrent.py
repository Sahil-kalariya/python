
def two_sum(lis):
    dic = {}
    ans = []
    for i in lis:
        if 3 - abs(i) in dic:
            ans.append([i , 3-abs(i)])
        dic[i] = 1          
    print(ans)

lis = [0, 3, 4, 7, 9]
lis2 = [0, -3, -5, -7, -8]
two_sum(lis)
two_sum(lis2)



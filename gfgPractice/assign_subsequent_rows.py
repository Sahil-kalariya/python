from my_module import list_input

def assign_row(lis):
    res= {}
    for i in range(0,n-1):
       res[lis[0][i]] = lis[i+1] 
    return res    

if __name__ == "__main__":
    lis = list_input()
    n = len(lis)
    print(lis)
    res = assign_row(lis)
    print(res)
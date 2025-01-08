from my_module import list_input

def add_matrix(lis1 , lis2):
    n = len(lis1)
    print(f"lenght {n}")
    sum_list = []
    sum = []
    for i in range(0,n):
        for j in range(0,len(lis1[i])):
            sum.append(lis1[i][j] + lis2[i][j])
        sum_list.append(sum)
        sum = [] 
    return sum_list       

def sub_matrix(lis1 , lis2):
    n = len(lis1)
    print(f"lenght {n}")
    sum_list = []
    sum = []
    for i in range(0,n):
        for j in range(0,len(lis1[i])):
            sum.append(lis1[i][j] - lis2[i][j])
        sum_list.append(sum)
        sum = [] 
    return sum_list       

if __name__ == "__main__":
    lis1 = list_input()
    lis2 = list_input()
    print(lis1)
    print(lis2)
    lis_sum = add_matrix(lis1 , lis2)
    lis_sub = sub_matrix(lis1 , lis2)
    print(f"sum of list is {lis_sum}")
    print(f"sub of list is {lis_sub}")
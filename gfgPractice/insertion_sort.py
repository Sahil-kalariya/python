from my_module import list_input


def InsertionSort(lis):
    n = len(lis)

    for i in range(1,n):
        tmp = lis[i]
        j = i
        while j > 0:
            if tmp < lis[j-1]:
                lis[j] = lis[j-1] 
            else:
                break
            j-=1      
        lis[j] = tmp


if __name__ == "__main__":
    lis = list_input()
    print(lis)
    InsertionSort(lis)
    print(lis)

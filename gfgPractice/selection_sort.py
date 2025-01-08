from my_module import list_input

def SelectionSort(lis):
    n = len(lis)
    for i in range(0,n):
        mini = i
        for j in range(i+1,n):
            if lis[j] < lis[mini]:
                mini = j
        lis[i] , lis[mini] = lis[mini] , lis[i]        
                

if __name__ == "__main__":
    lis = list_input()
    print(lis)
    SelectionSort(lis)
    print(lis)
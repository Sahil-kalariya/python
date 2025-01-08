
from my_module import list_input

def bubbleSort(lis):
    n = len(lis)
    cnt = 0
    for i in range(0,n):
        for j in range(0,n-i-1):
            if lis[j] > lis[j+1]:
                cnt+=1
                lis[j] , lis[j+1] = lis[j+1] , lis[j]
        if cnt == 0:
            print("already sorted")
            break        

if __name__ == "__main__":
    lis = list_input()
    print(lis)
    bubbleSort(lis)
    print(lis)
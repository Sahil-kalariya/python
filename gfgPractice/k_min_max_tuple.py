from my_module import tuple_input , print_tuple , print_list


def k_min_max(tup , k):
    sorted_list = sorted(tup)
    n = len(tup)
    lis = []
    for i in range(0,k):
        lis.append(sorted_list[i])
        
    for i in range(n-1,n-k-1,-1):
        lis.append(sorted_list[i])

    return lis

if __name__ == "__main__":
    tup = tuple_input()
    k = int(input("enter k "))
    lis = k_min_max(tup,k)

    print_list(lis)

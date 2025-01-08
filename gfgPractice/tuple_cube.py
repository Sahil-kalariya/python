from my_module import list_input , print_tuple

def tup_cube(lis):
    tup = ()

    for i in lis:
        tup += (i , i**3)
    return tup
if __name__ == "__main__":
    lis = list_input()
    tup = tup_cube(lis)
    print_tuple(tup)
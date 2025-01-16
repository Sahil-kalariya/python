
def CubeRootRduce(n):
    cnt = 0
    while n >= 3:
        n = n ** (1/3)
        cnt += 1
    return cnt    

if __name__ == "__main__":
    n = int(input("enter integer"))
    print(CubeRootRduce(n))
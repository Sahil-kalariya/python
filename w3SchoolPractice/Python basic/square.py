# 149. NxN Square of Integer


def Square(n):
    res = []
    for i in range(n):
            res.append([n]*n)  
    return res

if __name__ == "__main__":
    n = int(input("enter integer"))
    print(Square(n))
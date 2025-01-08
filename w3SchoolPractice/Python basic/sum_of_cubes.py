# 149. Cube Sum of Smaller Integers

if __name__ == "__main__":
    n = int(input("enter number "))
    sum = 0
    n-=1
    while n > 0:
        sum += n**3
        n -= 1

    print(sum)    




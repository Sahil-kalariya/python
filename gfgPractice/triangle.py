
def print_triangle(num):

    for i in range(1,num+1):

        for j in range(1,num-i+1):
            print(" " , end = "")
        for j in range(1,i*2):
            print("*" , end="")    

        print("")


if __name__ == "__main__":
    num = int(input("enter a number"))
    print_triangle(num)
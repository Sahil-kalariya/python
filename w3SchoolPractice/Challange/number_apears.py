def find_num(lis):
    ans = 0
    for i in lis:
        ans = ans ^ i

    return ans

if __name__ == "__main__":
    lis = [2,2,3,3,5,4,5]
      


    print(find_num(lis))
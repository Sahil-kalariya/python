number = int(input("enter a number"))
print("1 = 1")
for i in range(2,number+1):
    sum = 0
    for j in range(1,i):
        sum += j
        print(f"{j} + " , end = "")
    j+=1
    sum += j    
    print(f"{j} = {sum}")
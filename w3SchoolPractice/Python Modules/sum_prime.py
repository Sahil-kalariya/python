
def isPrime(num):
    for i in range(2,num//2+1):
        if (num % i == 0):
            print(num)
            return False
    return True

def sum_of_prime(lis):
    sum = 0
    for num in lis:
        if num == 1:
            continue
        if isPrime(num):
            sum += num

    return sum

if __name__ == "__main__":
    lis = [11, 37, 444]
    print(sum_of_prime(lis))

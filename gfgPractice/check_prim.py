

def is_prime(num):
    for i in range(2 , int(num**0.5)+1):
        print(num , i)
        if(num%i == 0):
            return False

    return True


if(__name__ == "__main__"):
  num = int(input("enter a number"))
  if is_prime(num):
     print("number is prime")
  else:
     print("number is not prime")   



def pow(n ,ans , p):
    if p > 0:
         ans = pow(n , ans*n , p-1)
    return ans     


if __name__ == "__main__":
     n = int(input("enter n "))
     p = int(input("enter p "))
     ans = 1
     print(pow(n , ans , p)) 





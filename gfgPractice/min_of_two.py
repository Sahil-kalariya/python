def find_min(num1 , num2):
   return min(num1, num2)


if __name__ == "__main__":
   num1 = int(input("enter number 1 "))
   num2 = int(input("enter number 2 "))
   print(f"{find_min(num1,num2)} is smaller of {num1} and {num2}")
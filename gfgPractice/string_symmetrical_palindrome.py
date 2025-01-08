from my_module import string_input

def string_symmetrical(str):
    n = len(str)
    return str[0:n//2] == str[n//2:n]

def string_palindrome(str):
    n = len(str)
    return str == str[::-1]

if __name__ == "__main__":
    str = string_input()
    if string_symmetrical(str):
        print(f"{str} is symmetrical")
    else:
        print(f"{str} is nor symmertrical")
    if string_palindrome(str):
        print(f"{str} is palindrome")
    else:
        print(f"str is not palindrome")       

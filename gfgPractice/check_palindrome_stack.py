def IsPalindrome(stack , st):
    for i in st:
        stack.append(i)

    for i in st:
        if stack.pop() != i:
            return False
        
    return True

if __name__ == "__main__":
    st = input("enter string ")
    stack = []
    if IsPalindrome(stack , st):
        print("string is palindrome")
    else:
        print("not palindrome")    
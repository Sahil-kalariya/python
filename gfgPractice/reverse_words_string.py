from my_module import string_input

def reverse_word(str):
    lis = str.split()
    str= ""
    for i in range(len(lis)-1 , -1 , -1):
        str += lis[i] + " "
    return str     

if __name__ == "__main__":
    str = string_input()
    print(f"string with reversed word {reverse_word(str)}") 
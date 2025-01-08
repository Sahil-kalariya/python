from my_module import string_input


def even_length_word(str):
    li = str.split()
    str = ""
    for s in li:
       if(len(s)%2 == 0):
          print(s)
    return str      

if __name__ == "__main__":
  str = string_input()
  {even_length_word(str)}
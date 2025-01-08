# def print_list(my_list):    
#     print(my_list)

# def print_tuple(tup):    
#     for i in tup:
#        print(f"{i} " , end = "")
#     print("")

# def print_dict(dict):
#    print(dict)

def tuple_input():
    tup = ()
    size = int(input("enter size of tuple "))
    for i in range(0,size):
       num = ((int(input("enter number to append in tuple "))))
       tup += (num,)
    return tup

def list_input():
    my_list = []
    size = int(input("enter size of list "))
    for i in range(0,size):
       num  = input("enter number to append in list ")
       my_list.append(eval(num))
    return my_list

def string_input():
    str = input("enter string ")
    return str

def dict_input():
    dict = {}
    size = int(input("enter size of dict "))
    for i in range(0,size):
       key = (input("enter key "))
       value = (input("enter value "))
       
       try:
          value = int(value)
       except:
           pass    

       dict[key] = value
    return dict
def swap(n1 , n2):
    n1 = n1 + n2 
    n2 = n1 - n2
    n1 = n1 - n2
    return (n1,n2)
    
def print_list(my_list):    
    for i in my_list:
       print(f"{i} " , end = "")
    print("")

def list_input():
    my_list = []
    size = int(input("enter size of list "))
    for i in range(0,size):
       my_list.append(int(input("enter number to append in list ")))
    return my_list

if __name__ == "__main__":
     my_list =  list_input() 
     print_list(my_list)
     my_list[0] , my_list[len(my_list)-1] = swap(my_list[0],my_list[len(my_list)-1])   
     print_list(my_list)
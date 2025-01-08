from my_module import dict_input

def sum_values(dict):
    sum = 0
    for i in dict.values():
        sum += i    
    return sum 

if __name__ == "__main__":
    dict = dict_input()
    sum = sum_values(dict)

    print(f"sum of all values {sum}")
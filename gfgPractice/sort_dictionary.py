from my_module import dict_input 



if __name__ == "__main__":
    dict = dict_input()
    print(f"dictionary befor sorting {dict}")
    lis = sorted(dict)
    for i in lis:
        print(f"{i} : {dict[i]} " , end="")
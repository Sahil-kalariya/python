from my_module import list_input

def group_list_element(lis):
    dict = {
    }
    for i in lis:
        if(i in dict):
            dict[i] += 1
        else:
            dict[i] = 1    
    return dict

if __name__ == "__main__":
    lis = list_input()
    dict = group_list_element(lis)

    ans = []
    for i in dict:
        temp = []
        for j in range(0,dict[i]):
            temp.append(i)
        ans.append(temp)

    print(ans)        

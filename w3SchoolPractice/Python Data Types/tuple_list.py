def test(lst_tuples):
    result = []
    for i in lst_tuples:
        result.append(list(i))  
    return result


lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]


print(lst_tuples)


print(test(lst_tuples)) 

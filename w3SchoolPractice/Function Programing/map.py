def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result


colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

print("Original list of tuples:")

print(colors)

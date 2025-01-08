def test(text):
    data = text.split(' ')
    result = []
    char = sorted([i[0] for i in data])
    for i in char:
        for j in data:
            if i == j[0] and j not in result:
                result.append(j)
    
    return ' '.join(result)


word = "Calculate the sum of two said numbers given as strings."
print(test(word))


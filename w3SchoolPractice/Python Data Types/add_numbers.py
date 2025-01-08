def test(x, y):
    
    if (x == "" or y == ""):
        return False
    
    return str(int(x) + int(y))

n1 ="234242342341"
n2 ="2432342342"
print("Original string numbers:", n1, n2)
print(test(n1, n2))

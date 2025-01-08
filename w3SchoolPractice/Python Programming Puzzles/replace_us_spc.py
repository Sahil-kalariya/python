# 99. Replace Spaces with Underscore and Hyphen

def replace(n):
    n = n.replace("-", " " * 3).replace("_", " ")
    print(n)
if __name__ == "__main__":
    n = (input("enter string "))
    print(replace(n))
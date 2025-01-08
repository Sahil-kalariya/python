
class my_class:
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def __str__(self):
            return str((self.a , self.b))

if __name__ == "__main__":
    g = [my_class(2,4),
         my_class(1,2),
         my_class(2,4),
         my_class(4,2)]

    (sorted(g , key=lambda x : x.b))
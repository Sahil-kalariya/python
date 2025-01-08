def fun(*args):
    for i in args:
        print(i)

def fun1(**kwargs):
    for i , j in kwargs.items():
        print(i , j)

if __name__ == "__main__":
    fun("astring" , 2  ,  " ")
    fun1(a = "2" , b = "3")

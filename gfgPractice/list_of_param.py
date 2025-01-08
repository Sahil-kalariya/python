
import inspect
import collections

def fun(a , b):
    return a+b

if __name__ == "__main__":
    print(inspect.getfullargspec(collections.Counter))
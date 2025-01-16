class UpperAttrMeta(type):
    def __new__(cls, name, bases, dct):
        uppercase_attr = {}
        for name, value in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = value
            else:
                uppercase_attr[name] = value
        return super().__new__(cls, name, bases, uppercase_attr)

class MyClass(metaclass=UpperAttrMeta):
    foo = 'bar'
    baz = 'qux'

print(hasattr(MyClass, 'foo')) 
print(hasattr(MyClass, 'FOO'))  
print(MyClass.FOO) 
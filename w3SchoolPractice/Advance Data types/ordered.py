from collections import OrderedDict

ordered_dict = OrderedDict([
    ('Laptop', 40),
    ('Desktop', 45),
    ('Mobile', 35),
    ('Charger', 25)
])

print("Original OrderedDict:")
print(ordered_dict)

print("\nRemove the first key-value pair of the said OrderedDict:")
ordered_dict.popitem(last=False)

print("\nUpdated OrderedDict:")
print(ordered_dict)

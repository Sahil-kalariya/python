def test(d):
    return max(d, key=d.get), min(d, key=d.get)

students = {
    'Theodore': 19,
    'Roxanne': 22,
    'Mathew': 21,
    'Betty': 20
}

print("maximum and minimum value of dictionary:")
print(test(students))
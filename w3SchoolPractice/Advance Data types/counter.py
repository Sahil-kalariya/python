from collections import Counter

def main():
    items = ['Red', 'Green', 'Black', 'Black', 'Red', 'Red', 'Orange', 'Pink', 'Pink', 'Red', 'White']
    counter = Counter(items)
    print(counter)
    counter['Red'] += 2
    counter['Orange'] -= 1
    print(counter)
if __name__ == "__main__":
    main()

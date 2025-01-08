def test(memory_view):
    for element in memory_view:
        print(hex(element))

def main():
    nums = [8, 16, 42, 92, 128]
    print("Original list values:",nums)

    memory_view = memoryview(bytearray(nums))

    print("Hex Values of said list elements:")
    test(memory_view)

if __name__ == "__main__":
    main()

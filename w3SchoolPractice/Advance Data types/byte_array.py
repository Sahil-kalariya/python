def bytearray_to_bytes(bytearray_obj):
    bytes_obj = bytes(bytearray_obj)
    return bytes_obj

def main():
    try:
        original_bytearray = bytearray([12, 51, 10, 15, 95, 102, 132, 117])
        
        bytes_result = bytearray_to_bytes(original_bytearray)
        
        print("Original Bytearray:", original_bytearray)
        print("Bytes Object:", bytes_result)
        print("Decoded String:", bytes_result.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

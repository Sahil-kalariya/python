def replace_substr(original_string, old_substring, new_substring):
    if original_string:
        return original_string.replace(old_substring, new_substring)
    else:
        return None

def main():
    try:
        input_string = "Java Exercises!"
        old_substr = "Java"
        new_substr = "Python"
        
        result = replace_substr(input_string, old_substr, new_substr)
        
        if result is None:
            print("Original string is empty.")
        else:
            print("Original String:", input_string)
            print("New String:", result)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

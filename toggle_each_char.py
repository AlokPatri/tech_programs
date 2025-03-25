def toggle_each_char(input_string):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in input_string])

# Example usage:
if __name__ == "__main__":
    test_string = "Hello World!"
    toggled_string = toggle_each_char(test_string)
    print(toggled_string)  # Output: hELLO wORLD!
    
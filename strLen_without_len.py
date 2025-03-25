def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

# Example usage
input_string = "Hello, World!"
print(f"The length of the string is: {string_length(input_string)}")

def calculate_char_frequency(text):
    """Calculate the frequency of each character in the given text."""
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

text = input("Enter a text: ")  
print(f"Frequency of each character in the text: {calculate_char_frequency(text)}") 

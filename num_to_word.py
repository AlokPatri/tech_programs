'''from num2words import num2words
def num_to_word(n):
    return num2words(n)
num=int(input("enter a number"))
print("in words",num_to_word(num))'''

# Dictionary for number words
ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

# Function to convert a number below 1000 to words
def num_to_words_under_1000(n):
    if n == 0:
        return ""
    elif n < 10:
        return ones[n]
    elif n < 20:
        return teens[n - 10]
    elif n < 100:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    else:
        return ones[n // 100] + " Hundred" + (" " + num_to_words_under_1000(n % 100) if n % 100 != 0 else "")

# Main function to convert a full number to words
def number_to_words(n):
    if n == 0:
        return "Zero"
    
    words = ""
    chunk_index = 0

    while n > 0:
        chunk = n % 1000
        if chunk > 0:
            words = num_to_words_under_1000(chunk) + (" " + thousands[chunk_index] if thousands[chunk_index] else "") + (" " + words if words else "")
        n //= 1000
        chunk_index += 1

    return words.strip()

# Example usage
num = int(input("Enter a number: "))
print("In words:", number_to_words(num))

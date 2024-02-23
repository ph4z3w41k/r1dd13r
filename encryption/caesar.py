def caesar_cipher(input: str, increment: int) -> str:
    lower_char_bound = 97
    upper_char_bound = 122
    chars_in_alphabet = 26
    
    input = input.lower()
    solution = ""

    for char in input:
        # Ignore syntax
        if ord(char) < lower_char_bound or ord(char) > upper_char_bound:
            solution += char
            continue 
        
        # Get new char, handling overflows
        new_char = chr(((ord(char) - lower_char_bound) + increment % chars_in_alphabet) + lower_char_bound)
        
        solution += new_char

    return solution

def caesar_cipher(input: str, increment: int) -> str:
    lower_char_bound = 97
    upper_char_bound = 122
    
    input = input.lower()
    solution = ""

    for char in input:
        solution += char

    return solution

if __name__ == '__main__':
    print(caesar_cipher("HeLlO, WoRlD", 1))
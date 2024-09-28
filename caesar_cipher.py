def caesar_cipher(text, shift, encrypt=True):
    shift = shift if encrypt else -shift
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65  # 'A' starts at 65 in ASCII
            else:
                ascii_offset = 97  # 'a' starts at 97 in ASCII
            
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char

    return result

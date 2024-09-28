from caesar_cipher import caesar_cipher

def encrypt_file(input_file, output_file, shift=8):
    with open(input_file, 'r') as file:
        text = file.read()
    
    encrypted_text = caesar_cipher(text, shift, encrypt=True)
    
    with open(output_file, 'w') as file:
        file.write(encrypted_text)

def decrypt_file(input_file, output_file, shift=8):
    with open(input_file, 'r') as file:
        text = file.read()
    
    decrypted_text = caesar_cipher(text, shift, encrypt=False)
    
    with open(output_file, 'w') as file:
        file.write(decrypted_text)

from operations import encrypt_file, decrypt_file

def main_menu():
    print("Choose an action:")
    print("1. File encryption")
    print("2. File decryption")
    print("3. Exit")

    choice = input("Your choice: ")

    if choice == '1':
        input_file = input("Enter a name for the input file: ")
        output_file = input("Enter the name of the file to save the result: ")
        encrypt_file(input_file, output_file, 8)
        print(f"The file '{input_file}' is encrypted and saved to '{output_file}'.")
    elif choice == '2':
        input_file = input("Enter the name of the encrypted file: ")
        output_file = input("Enter a file name to save the result: ")
        decrypt_file(input_file, output_file, 8)
        print(f"The file '{input_file}' has been decrypted and saved to '{output_file}'.")
    elif choice == '3':
        print("Exit the program.")
        exit()
    else:
        print("Wrong choice. Try again.")
        main_menu()

while True:
    main_menu()

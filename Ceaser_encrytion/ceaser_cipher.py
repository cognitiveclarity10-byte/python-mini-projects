# Function to encrypt the message using a Caesar Cipher
def encryption(message_to_encrypt, user_key):
    encrypted_message = ""  # Initialize the encrypted message as an empty string

    # Loop through each character in the input message
    for i in message_to_encrypt:
        encrypted_num = ord(i)  # Get the ASCII value of the character
        new_num = encrypted_num + user_key  # Shift the character by the user key
        new_letter = chr(new_num)  # Convert the new number back to a character
        encrypted_message += new_letter  # Append the new character to the encrypted message

    print(f"Encrypted message: {encrypted_message}")  # Output the encrypted message

# Function to decrypt the message using the reverse of the Caesar Cipher
def decryption(message_to_decrypt, user_key):
    decrypted_message = ""  # Initialize the decrypted message as an empty string

    # Loop through each character in the encrypted message
    for j in message_to_decrypt:
        decrypted_num = ord(j)  # Get the ASCII value of the encrypted character
        old_num = decrypted_num - user_key  # Reverse the shift by subtracting the user key
        old_letter = chr(old_num)  # Convert the new number back to a character
        decrypted_message += old_letter  # Append the decrypted character to the decrypted message

    print(f"Decrypted message: {decrypted_message}")  # Output the decrypted message

# Function to handle user input for the key and the message
def user_data():
    # Input loop for a valid key (between 1 and 26)
    while True:
        try:  
            user_key = int(input("Enter a number between 1 and 26 for key: "))
            if 1 <= user_key <= 26:
                break  # Break out of loop when valid key is provided
            else:
                print("The number must be between 1 and 26.")
        except ValueError:
            print("Invalid entry. Please enter an integer.")

    # Input loop for a valid message
    while True:
        user_message = input("Enter a message to encrypt: ")
        if user_message:
            break 
        else:
            print("Please enter some text to encrypt.")
    
    return user_key, user_message  # Return the key and the message

# Main function to run the program
def main():
    while True:
        user_key, user_message = user_data()  # Get user data (key and message)
        
        # Ask if the user wants to encrypt or decrypt
        ask_user = input("Enter (e) for Encrypt and (d) for Decrypt: ").lower()

        if ask_user == "e":
            encryption(user_message, user_key)  # Encrypt the message
        elif ask_user == "d":
            decryption(user_message, user_key)  # Decrypt the message
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        
        # Ask if the user wants to perform another operation
        to_user = input("Do you want to do it again? (Yes / No): ").lower()
        if to_user != "yes":
            break  # Exit the loop if the user doesn't want to continue


if __name__ == "__main__":
    main()

# Caesar Cipher - Python Encryption and Decryption

This Python project implements a basic **Caesar Cipher** encryption and decryption algorithm. The Caesar Cipher is a simple encryption technique where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

## Features

- **Encryption**: Encrypt a message using a Caesar Cipher with a user-defined key.
- **Decryption**: Decrypt a previously encrypted message using the same key.

## Requirements

- Python 3.x (Tested with Python 3.8+)

## Getting Started

### 1. Clone the Repository

You can copy or Download the file 

## Run the Program

To run the program, simply execute the caesar_cipher.py script:
```bash
ceaser_cipher.py
```

## Example

Encryption 
```bash
Enter a number between 1 and 26 to for key: 3
Enter a message to encrypt: Hello World
Encrypted message: Khoor Zruog

```

Decryption
```bash
Enter a number between 1 and 26 for key: 3
Enter a message to encrypt: Khoor Zruog
Enter (e) for Encrypt and (d) for Decrypt: d
Decrypted message: Hello World

```
## How It Works

Encryption: The program converts each character of the message into its corresponding ASCII code using ord(), adds the key to the ASCII value, and then converts it back to a character using chr().

Decryption: The reverse process is done to recover the original message by subtracting the key from each character's ASCII value

## License

This project is licensed under the MIT License - see the LICENSE


## Acknowledgments

This project was inspired from the book ** The Big Book of Small Python Projects ** 


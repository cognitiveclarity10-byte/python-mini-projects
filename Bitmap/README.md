# Bitmap Text Printer

This Python script prints a custom message in the shape of a predifined bitmap heart-like pattern. It replaces the * characters in the btmap with letters form the user,s input message, cycling through the message as needed

## How it Works

* The script contains a multi_line string called ```bitmap``` which is a pattern of '*' and spaces 
* When run the script prompts the user to enter a text message.
* Then it prints the bitmap pattern to the console replacing each '*' in the pattern with a character from the user's message.
* Spaces in the bitmap remain spaces
* If the message is shorter than thenumber of '*' in a line the message repeats cyclically 

## Usage

* Run the script
```
 python3 bitmap.py
 ```
 * Enter the desired message when prompted 
* See your message in Heart shape


## 📄 License

This project is open-source and free to use under the MIT License

## 🙌 Credits

Inspired by the classic Bagels game from Al Sweigart's Invent Your Own Computer Games with Python.

# 🧠 Bagels - A Number Guessing Game

**Bagels** is a simple number logic game where the computer thinks of a random 3-digit number with unique digits, and your job is to guess it. After each guess, the game gives you clues to help you figure out the secret number.

---

## 🎮 How to Play

1. The computer generates a secret 3-digit number (digits are unique and randomly chosen).
2. You have a limited number of guesses (default: 3).
3. After each guess, you'll receive clues:
   - 🟢 **Pico** – One digit is correct and in the right position.
   - 🟡 **Farmi** – One digit is correct but in the wrong position.
   - ❌ **Bagels** – No digits are correct.
4. Use these clues to make your next guess.
5. If you guess the number correctly, you win!
6. If you run out of guesses, the game reveals the secret number.

---

## 📦 Features

- Random 3-digit number with unique digits.
- Up to 3 guesses per round.
- Clue-based feedback after each guess.
- Option to play again after finishing a game.
- Input validation to prevent invalid guesses.

---

## Run the Game

```
python3 bagels.py

```
## Example Gameplay

```
Welcome to Bagels!

This is a Guessing Game. I will think of a 3-digit number.
You have to guess the number. I will give you some clues:

Pico  : one digit is correct and in the correct position.
Farmi : one digit is correct but in the wrong position.
Bagels: no digits are correct.

You have 3 guesses left.
Enter a 3-digit number: 123
Clues: Pico Farmi

You have 2 guesses left.
Enter a 3-digit number: 456
Clues: Bagels

You have 1 guess left.
Enter a 3-digit number: 321
Clues: You got it!

Do you want to play again? (yes/no): no
Thank you for playing Bagels!
```

## 📄 License

This project is open-source and free to use under the MIT License

## 🙌 Credits

Inspired by the classic Bagels game from Al Sweigart's Invent Your Own Computer Games with Python.

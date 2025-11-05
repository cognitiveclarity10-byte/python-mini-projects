# Deep Cave

## Description
This Python program simulates a "dice-based" width adjustment for a dynamic pattern on the console. The screen is divided into three parts:
- A left section of `#` characters (`leftwidth`).
- A fixed gap of spaces (`gapwidth`).
- A right section of `#` characters (`rightwidth`).

The program will continuously adjust the width of the left and right sections based on random dice rolls. The left width can either increase or decrease depending on the outcome of the dice roll, while ensuring the total width remains constant at 70 characters.

## Features

- The total width of the output is always 70 characters.
- The left section (`leftwidth`) starts at 20 characters.
- The middle gap section (`gapwidth`) is fixed at 10 spaces.
- The right section (`rightwidth`) adjusts automatically based on the size of the left section.
- The `leftwidth` can increase or decrease based on random dice rolls, simulating a dynamic pattern.
- The program continues to run in an infinite loop until manually stopped (e.g., `Ctrl+C`).

## How It Works

- The program uses Python's `random.randint(1, 6)` to simulate a dice roll.
- When the dice rolls `1`, the `leftwidth` decreases by 1 (if greater than 1).
- When the dice rolls `2`, the `leftwidth` increases by 1 (if there is enough space for both the `leftwidth` and `gapwidth`).
- For any other dice rolls (`3`, `4`, `5`, `6`), the width remains unchanged.
  
The pattern of `#` characters is printed to the console with a gap between the left and right sections. The left section's width changes dynamically based on the dice rolls.

## Requirements

- Python 3.x
- No additional libraries are needed (uses `random`, `sys`, and `time` modules which are part of Python's standard library).

## How to Run

1. Clone or download this repository.
2. Open a terminal window.
3. Run the script:
   ```bash
   python3 deep_cave.py

## Notes

The program will continue running indefinitely unless you stop it manually.

The dice roll results in either an increase or decrease of the left width, keeping the total width at 70 characters.

## License

This project is licensed under the MIT License - see the LICENSE
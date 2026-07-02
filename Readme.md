# Guessing a Number

## Overview

This project is a simple Python-based guessing game that consists of two interactive parts.

In the first game, the computer randomly generates a number between 1 and 100, and the user has to guess it. After each guess, the program provides hints such as "Too Low" or "Too High" to help the user reach the correct number. It also counts only valid attempts and uses exception handling to prevent the program from crashing when invalid input, such as letters or symbols, is entered.

In the second game, the roles are reversed. The user thinks of a number between 1 and 100, and the computer attempts to guess it. The computer uses the Binary Search algorithm by always selecting the middle value of the current range and adjusting the range according to the user's feedback ("High", "Low", or "Correct"). This strategy allows the computer to find the correct number efficiently.

The project also includes a scoreboard that records the number of attempts taken in both games and displays the final results after both games are completed.

## Features

- Random number generation
- User Guessing Game
- Computer Guessing Game
- High and Low hints
- Scoreboard
- Input validation using try-except
- Attempt counter

## Programming Concepts Used

This project demonstrates the following Python concepts:

- Variables
- While loops
- Conditional statements (if, elif, else)
- User input using input()
- Output using print()
- Exception handling using try-except
- Lists for storing scores
- f-strings for formatted output
- Random number generation

## Mathematical Concepts

### User Guessing Game

The first game follows the concept of Linear Search, where guesses are made one at a time until the correct number is found. The total number of attempts depends on the player's guessing strategy and therefore cannot be predetermined.

### Computer Guessing Game

The second game uses the Binary Search algorithm. After every guess, the search range is divided into two halves based on the user's feedback ("Too High" or "Too Low"). This gives the algorithm a time complexity of O(log₂ n), making it much more efficient than linear search.

## Scoreboard

The program displays a final scoreboard showing:

- User Guessing Game attempts
- Computer Guessing Game attempts

This allows the performance of both games to be compared easily.

## How to Run

Run the following command in the terminal:

```bash
python Guess_Number.py
```

## Conclusion

This project demonstrates beginner-level Python programming concepts through an interactive guessing game. It combines user interaction, exception handling, loops, conditional statements, and searching algorithms to provide a simple and engaging learning experience.
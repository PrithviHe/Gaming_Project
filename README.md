This project is a simple Python-based guessing game that contains two interactive parts. In the first part, the computer randomly generates a number between 1 and 100, and the user has to guess it. The program guides the user by giving hints such as “too low” or “too high” after each guess. It also keeps track of the number of valid attempts and uses error handling to manage invalid inputs like letters or symbols so that the program does not crash.

In the second part of the project, the roles are reversed. The user thinks of a number between 1 and 100, and the computer tries to guess it. The computer uses an efficient strategy called binary search, where it always guesses the middle value of the current range and then adjusts the range based on user feedback. This makes the guessing process very fast and reduces the number of attempts significantly.

The project also includes a scoreboard feature that stores the number of attempts taken in both games. It helps track performance and shows how many attempts were needed in each round. Additionally, it displays the best score achieved, which is the minimum number of attempts across games.

Programming Insight:

This project demonstrates important Python concepts such as loops, conditional statements, functions like input and print, exception handling using try-except, and list operations for storing scores. It also introduces basic algorithmic thinking through linear search (user guessing game) and binary search (computer guessing game).

Mathematical Insight:

Mathematically, the user guessing game behaves like a linear search with an average of about 50 attempts in a 1–100 range, while the computer guessing game uses binary search, which requires only about log₂(100) ≈ 7 attempts in the worst case.

Overall, we thought this project is a good demonstration of beginner-level Python programming combined with simple algorithms and user interaction.

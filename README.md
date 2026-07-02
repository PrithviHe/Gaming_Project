                                          **Guessing a Number**

This project is a simple Python-based guessing game that contains two interactive parts. In the first part, the computer randomly generates a number between 1 and 100, and the user has to guess it. The program guides the user by giving hints such as “too low” or “too high” after each guess. It also keeps track of the number of valid attempts and uses error handling to manage invalid inputs like letters or symbols so that the program does not crash.

In the second part of the project, the roles are reversed. The user thinks of a number between 1 and 100, and the computer tries to guess it. The computer uses an efficient strategy called binary search, where it always guesses the middle value of the current range and then adjusts the range based on user feedback. This makes the guessing process very fast and reduces the number of attempts significantly.

The project also includes a scoreboard feature that stores the number of attempts taken in both games. It helps track performance and shows how many attempts were needed in each round. Additionally, it displays the best score achieved, which is the minimum number of attempts across games.

**Programming Thought**:

This project demonstrates important Python concepts such as **loops, conditional statements, functions like input and print, exception handling using try-except, and list operations** for storing scores. It also introduces basic algorithmic thinking through linear search (user guessing game) and binary search (computer guessing game).

**Mathematical Thought:**

User Guessing Game: The game follows a **linear search** approach because the player makes guesses one at a time until the correct number is found. The number of attempts depends on the player's guessing strategy and cannot be predetermined.

Computer Guessing Game: The game uses the **binary search algorithm**. After each guess, the search range is divided into two halves based on the user's feedback ("too high" or "too low"). The mathematical complexity is O(log₂ n), where n is the size of the search range, making it much more efficient than linear search.

Overall, we thought this project is a good demonstration of beginner-level Python programming combined with simple algorithms and user interaction.

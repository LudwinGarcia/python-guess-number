# Guess the number

      The Goal this project uses the random module in Python. The program will first randomly 
      generate a number unknown to the user. The user needs to guess what that number is. 
      (In other words, the user needs to be able to input information.) If the user’s guess 
      is wrong, the program should return some sort of indication as to how wrong (e.g. The 
      number is too high or too low). If the user guesses correctly, a positive indication should
      appear. You’ll need functions to check if the user input is an actual number, to see the 
      difference between the inputted number and the randomly generated numbers, and to then 
      compare the numbers. The program must be able to handle an error if the input is not an 
      integer (e.g. a letter).

## Concepts required

      1. Funciones aleatorias
      2. Variables
      3. Numeros enteros
      4. Input/Output
      5. Print
      6. While Loops
      7. If/Else statements
      8. Try

## I/O

### Input Values
      1. Should accept: ints and floats
      2. Should not accept: string, other types of values.

### Output messages
      "Wrong. Try again."
      "Wrong. Game over."
      "Correct. You win."

## Before starting

Install:
```
sudo apt-get install python-pip
sudo pip install -U nose
```

then:
```
sudo pip install -U pylint
```

## Running tests

When inside the project directory, run `nosetests` in the terminal. Your code
should work perfectly.

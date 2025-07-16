### 1. What I build ?

- A simple text-based game where:
  - The computer picks a secret password (word)
  - The user keeps guessing the word.
  - After each guess, the program gives a hint about how close the guess word is (How many letters are correct and incorrect in place wise)
  - The game counts how many guesses it took

### 2. How does it work ?

- Steps by steps

  - The program chooses a secret word.
  - The user is told how many letters the word has
  - The program asks the user isto guess the word.
  - After each guess :-
    - If correct, the user wins and the program shows the number of attempts.
    - If not, the program gives a hint
  - The game continues until the user guess correctly.

- Bonus :-
  - Easy:- 3 letters words
  - medium :-
  - hard :-

### Pseudocode :-

```
start

show a welcome message and rules

Let user choose difficulty level

Randomly select a secret word from the list

Tell the user how many letters the word has

Set attempt count as 0

While the user has not guessed the word:
  a - Ask user to enter a guess
  b - Increment attempt counter
  c - If guess equals secret word
    - print congrats you guessed right
    - break
  d - else
    - compare each letter in guess to the secret word
    - count how many letters are correct and in the correct place


```

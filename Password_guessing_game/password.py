import random as rd

three_letter_words = [
    "cat", "dog", "sun", "bat", "hat",
    "run", "fan", "pen", "box", "car",
    "man", "map", "cap", "bag", "bed",
    "net", "lip", "pot", "rat", "jam",
    "bug", "cow", "log", "top", "egg"
]
five_letter_words = [
    "apple", "table", "chair", "grape", "plant",
    "house", "light", "cloud", "brush", "green",
    "clock", "bread", "stone", "flame", "water",
    "mouse", "train", "glass", "river", "truck",
    "shelf", "beach", "crown", "lemon", "spoon"
]
seven_letter_words = [
    "picture", "teacher", "journey", "kingdom", "diamond",
    "monster", "blanket", "airport", "balloon", "cabinet",
    "battery", "musical", "station", "library", "freedom",
    "tractor", "plastic", "justice", "bedroom", "organic",
    "visitor", "glasses", "network", "payment", "country"
]

print("Welcome to the game and try your luck...")
print("Choose your level:- easy, medium and hard")
level = input("Enter difficult level:- ").lower()

if level == 'easy':
  secret = rd.choice(three_letter_words)
elif level == 'medium':
  secret = rd.choice(five_letter_words)
elif level == 'hard':
  secret = rd.choice(seven_letter_words)
else:
  print("Invalid choice")
  secret = rd.choice(three_letter_words)


attempts = 0
print("Guess the secret password !!!")
while True:
  guess = input("Enter your guess:-").lower()
  hintGiven = 0
  attempts += 1
  if guess == secret:
    print(f"7 karod, Badhayi ho😀😀, you guessed it in {attempts}th time")
    break
  else:
    hint = ""
    for i in range(len(secret)):
      if i < len(guess) and guess[i] == secret[i]:
        hint += guess[i]
      else:
        hint += "_"
    needHint = input("Kya vai tujhe hint chahiye ? yes/no ").lower()
    if needHint == 'yes':
      if hintGiven == 1:
        print("Hint already given")
      else:
        hintGiven = 1
        print("Hint: ", hint)
    else:
      continue
  
print("Game over !!!")
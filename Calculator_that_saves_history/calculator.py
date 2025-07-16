import os
history_file = "history.txt"


def open_history_file():
  file = open(history_file, "r")
  lines = file.readlines()

  if len(lines) == 0:
    print("No history found !!!")
  else:
    for line in reversed(lines):
      print(line)
  # file.close()

def clear_history():
  file = open(history_file, "w")
  file.close()

  print("History cleared...")

def save_history(equation, result):
  file = open(history_file, "a")
  file.write(equation + " = " + str(result) + "\n") 
  file.close()


def calculate(user_input):
  parts = user_input.split()
  if len(parts) < 3:
    print("Invalid")
    return
  
  num1 = float(parts[0])
  operator = parts[1]
  num2 = float(parts[2])

  if operator == "+":
    result = num1 + num2
  elif operator == '-':
    result = num1 - num2
  elif operator == '*':
    result = num1 * num2
  elif operator == '/':
    if num2 == '0':
      print("0 can not be denominator")
      return
    result = num1 / num2
  elif operator == '%':
    if num2 == '0':
      print("0 can not be denominator")
      return
    result = num1 % num2
  else:
    print("This is not an operator")
  
  if int(result) == result:
    result = int(result)
  print("Result: ", result)
  save_history(user_input, result)


def main():
  print("Hey I am Your calcultor that saves history")
  while True:
    user_input = input("Enter calculation(+ - * / %) or command (history, clear, exit): ")
    if user_input == 'exit':
      break
    elif user_input == 'history':
      open_history_file()
    elif user_input == 'clear':
      clear_history()
    else:
      calculate(user_input)


main()
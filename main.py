import random
from stages_file import stages
import os

print("Welcome to Hangman")

data = open("Countries.txt")
list = data.read()

words = list.split()

word = random.choice(words).lower()

#print(word)

new_list = ['_' for i in word]
lives=6
won = False

print(stages[lives])

while '_' in new_list and lives>0:
  guess = input("Guess a letter: ")
  for i in range(len(word)):
    if guess == word[i]:
      new_list[i]=guess
  if guess not in word:
    lives-=1
    
  os.system('clear')
  print(stages[lives])
  print(" ".join(new_list))
if lives>0:  
  print("\nYou Win!")
else:
  print("\nYou lose!")
  print(f"\n{word} is your answer.")

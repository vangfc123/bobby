import random
import urllib
import time
import os

wordLen = 0   

def removeLetter(word, letterRem):
  global wordLen
  newStr = word
  leftStr = ''
  rightStr = ''

  while newStr.find(letterRem) is not -1: 
      wordLen = wordLen - 1
      location = newStr.find(letterRem)
      leftStr = newStr[:location]
      rightStr = newStr[location+1:]
      newStr = leftStr+rightStr

      print("left: "+leftStr)
      print("\n")
      print("right: "+rightStr)
      print("\n")
      print("How many letters left (CLUE): " + str(wordLen))
      time.sleep(3)

  return newStr
 
wrongTries = 0
art = [ '.....\n' \
        '.....\n' \
        '.....\n' \
        '.....\n',
        '..0..\n' \
        '.....\n' \
        '.....\n' \
        '.....\n',
        '..0..\n' \
        '.-|-.\n' \
        '.....\n' \
        '.....\n',
        '..0..\n' \
        '.-|-.\n' \
        './...\n' \
        '.....\n',
        '..0..\n' \
        '.-|-.\n' \
        './.\.\n' \
        '.....\n' 
       ]
defeatMsg = ['Fuchee is disappointed in you Bobby!', \
             'Try harder next time you almost got it!', \
             'Come on Bobby, concentrate!']
tries = 0
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)

print '\nWelcome to Hangman 1.0'
time.sleep(1.5)
print('Get ready to play hangman!')
time.sleep(1.2)

wordLen = len(secret)
guessedLetters = ''
correctLetters = ''

freader = open("tries","r")
numberTries = freader.readline()
# print numberTries
# time.sleep(2)
numberConv = int(numberTries)

# print numberConv
freader.close()

# time.sleep(2) 

while 1:
  os.system("clear")
  print art[wrongTries]
  print "\nYour correct letters so far: " + correctLetters 
  print "\n"

  if wordLen == 0:
      print("You win!\n")
      numberConv = numberConv + 1
      fwriter = open("tries","w")
      fwriter.write(str(numberConv))
      fwriter.close()
      break

  if wrongTries == 4:
      print(random.choice(defeatMsg))
      numberConv = numberConv + 1
      fwriter = open("tries","w")
      fwriter.write(str(numberConv))
      fwriter.close()
      print('\n')
      break 

  ans = raw_input("Guess a letter: ")

  if ans in guessedLetters:
      print('You already guessed that letter! Try a different one...')
      time.sleep(1)
  else:
      if ans in secret: 
        guessedLetters = guessedLetters + ans
        correctLetters = correctLetters + ans + '-'
        secret = removeLetter(secret, ans) 
      else:	
        wrongTries = wrongTries + 1
        guessedLetters = guessedLetters + ans


import random, math, time
from unittest import result

#made by Alex and Gleb

dict = []

file = open('english.txt', 'r')
dictionary = {}
for word in file:
  dictionary[word.strip().upper()] = True
file.close()

file = open('english2.txt', 'r')
dictionary2 = {}
for word in file:
  dictionary2[word.strip().upper()] = True
file.close()

file = open('english3.txt', 'r')
dictionary3 = {}
for word in file:
  dictionary3[word.strip().upper()] = True
file.close()

file = open('english4.txt', 'r')
dictionary4 = {}
for word in file:
  dictionary4[word.strip().upper()] = True
file.close()

file = open('english5.txt', 'r')
dictionary5 = {}
for word in file:
  dictionary5[word.strip().upper()] = True
file.close()

dict = [dictionary, dictionary2, dictionary3, dictionary4, dictionary5];

def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


class Tray:
  def __init__(self):
    self.dice = [['R', 'I', 'F', 'O', 'B', 'X'],
                 ['I', 'F', 'E', 'H', 'E', 'Y'],
                 ['D', 'E', 'N', 'O', 'W', 'S'],
                 ['U', 'T', 'O', 'K', 'N', 'D'],
                 ['H', 'M', 'S', 'R', 'A', 'O'],
                 ['L', 'U', 'P', 'E', 'T', 'S'],
                 ['A', 'C', 'I', 'T', 'O', 'A'],
                 ['Y', 'L', 'G', 'K', 'U', 'E'],
                 ['Qu', 'B', 'M', 'J', 'O', 'A'],
                 ['E', 'H', 'I', 'S', 'P', 'N'],
                 ['V', 'E', 'T', 'I', 'G', 'N'],
                 ['B', 'A', 'L', 'I', 'Y', 'T'],
                 ['E', 'Z', 'A', 'V', 'N', 'D'],
#                 ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'],
                 ['R', 'A', 'L', 'E', 'S', 'C'],
                 ['U', 'W', 'I', 'L', 'R', 'G'],
                 ['P', 'A', 'C', 'E', 'M', 'D']]

  def shift(self):
    random.shuffle(self.dice)

    self.tray = [[],[],[],[]]

    for row in range(4):
      for col in range(4):
        index = row*4 + col
        i = random.randint(0, 5)
        self.tray[row].append(self.dice[index][i])

  def display(self):
    print("┌------------┐")
    for row in range(4):
      print("|", end='')
      for col in range(4):
        if (len(self.tray[row][col]) == 2):
          spacer = ''
        else:
          spacer = ' '
        print(' ' + self.tray[row][col] + spacer, end='')
      print('|')
    print("└------------┘")


def valid(row, col):
  if (row < 0): return False
  if (row > 3): return False
  if (col < 0): return False
  if (col > 3): return False
  return True

def getIndex(row, col):
  return row*4 + col

def makeAllCombos2(tray, depth, row, col, word):

  actualWord = ""
  for index in word:
    rr = math.floor(index / 4)
    cc = index - rr*4
    actualWord += tray.tray[rr][cc]

  if (len(actualWord) < 6):
    for i in range(1, 6):
      if (len(actualWord) == i+1 and actualWord not in dict[i]):
        return
    
  if (checkIfDuplicates(word) == True):
    return
  #print(word)
  
  if (depth == 1): 
    if (actualWord in dict[0]):
      results.append(actualWord)
    return
    
  if (valid(row-1, col-1)): 
    newWord = word.copy()
    newWord.append(getIndex(row-1,col-1))
    #print("newWord: " + str(newWord))
    makeAllCombos2(tray, depth-1, row-1, col-1, newWord)
  if (valid(row  , col-1)): 
    newWord = word.copy()
    newWord.append(getIndex(row  ,col-1))
    #print("newWord: " + str(newWord))
    makeAllCombos2(tray, depth-1, row  , col-1, newWord)
  if (valid(row+1, col-1)): 
    newWord = word.copy()
    newWord.append(getIndex(row+1,col-1))
    #print("newWord: " + str(newWord))
    makeAllCombos2(tray, depth-1, row+1, col-1, newWord)
  if (valid(row-1, col  )): 
    newWord = word.copy()
    newWord.append(getIndex(row-1,col  ))
    #print("newWord: " + str(newWord))
    makeAllCombos2(tray, depth-1, row-1, col  , newWord)
  if (valid(row+1, col  )): 
    newWord = word.copy()
    newWord.append(getIndex(row+1,col  ))
    #print("newWord: " + str(newWord))
    makeAllCombos2(tray, depth-1, row+1, col  , newWord)
  if (valid(row-1, col+1)): 
    newWord = word.copy()
    newWord.append(getIndex(row-1,col+1))
    #print("newWord: " + str(newWord))
    makeAllCombos2(tray, depth-1, row-1, col+1, newWord)
  if (valid(row  , col+1)): 
    newWord = word.copy()
    newWord.append(getIndex(row  ,col+1))
    #print("newWord: " + str(newWord))
    makeAllCombos2(tray, depth-1, row  , col+1, newWord)
  if (valid(row+1, col+1)): 
    newWord = word.copy()
    newWord.append(getIndex(row+1,col+1))
    #print("newWord: " + str(newWord))
    makeAllCombos2(tray, depth-1, row+1, col+1, newWord)
  
def findAllWords(length):
  results = []
  for i in range(4):
    for j in range(4):
      makeAllCombos2(tray, length, i, j, [getIndex(i, j)])
  return results

def countdown(t):
 while t:
    time.sleep(1)
    t -= 1

def guessing(used):
  global scoretotal

  guess = input("Word: ")
  guess = guess.upper()
  if guess in results and guess not in used:
    multiplyer = 100 * len(guess)
    #print(score)
    scoretotal += multiplyer
    print("Nice! You earned " + str(multiplyer) + " points!")
    used.append(guess)
    print("score: " + str(scoretotal))
  elif guess in results and guess in used:
    print("Already Found")
  elif guess not in results:
    print("Not a Word")
    print("score: " + str(scoretotal))
  tray.display()


class Timer:
  def __init__(self):
    self.sec = 10

  def rundown(self):
    print("\nTime Remaining:")
    while (self.sec>0):
      time.sleep(1)
      #timer = "{:02d}".format(self.sec) 
      timer = "{:03d}".format(self.sec) # correct format
      #print(str(timer // 60) + ":" + str(timer % 60), end = "\r")
      print(timer, flush=True, end="\r")
      self.sec -= 1 
    print("Out of time!")
    
  def reset(self):
    a = input("Successfully reset. Press 'c' to continue or ANY KEY to go back: ")
    if a == "c":
      self.sec = 1
      timer.rundown()
    elif a != "c":
      return False
  def remaining(self):
    #print("hello")
    return self.sec

timer = Timer()
tray = Tray()

tray.shift()
tray.display()

used = []

results = []
for length in range(3, 8):
 findAllWords(length)

global scoretotal 
scoretotal = 0
timeout = 20 #timeout
prompt = "\nYou have %d seconds to choose the correct answer...\n" % timeout
print(prompt)

while True:
  #tray = Tray()
  #tray.shift()
  results = set(results)
  #print(results)
  #print(scoretotal)
  #print(timeout)

  from threading import Timer
  import threading

 # timeout = 10 #timeout
  
  #guessing(used, scoretotal)
  t = Timer(timeout, print, ['\nSorry, times up - Press ENTER to end this round'])
  t.start()
  threading.Thread(target=guessing(used)).start()
  #print(totalscore)
  #guessing(used, scoretotal)
 

  #prompt = "You have %d seconds to choose the correct answer...\n" % timeout
  #answer = input(prompt)
  t.cancel()
  if t.is_alive() == False:
    print("All possible Words:")
    print(results)
    while True:
      answer = str(input('Run again? (y/n): '))
      if answer in ('y', 'n'):
        break
      else:
        print("invalid input.")
    if answer == 'y':
      tray.shift()
      tray.display()
      results = []
      for length in range(3, 8):
        findAllWords(length)
      results = set(results)
      scoretotal = 0
      #print(results)
      #print(results)
      used = []
      #print("hello")
      continue
    else:
        print("Goodbye")
        break
'''
    ui = input("Do you wanna restart? y/N")
    if ui == 'y':
      continue
      #timeout = 2
      #print(prompt)
      t = Timer(timeout, print, ['Sorry, times up - Press ENTER to end this round'])
      print("restarted.")
      guessing(used, score)
    if ui == 'n':
      break
'''

print("Exit complete.")
t.cancel()

 # import threading
#  threading.Thread(target=guessing(used, score)).start()

'''
while True:
  doAgain = input("Reset? y/N ")
  if doAgain == "y":
    timer.reset()
  elif doAgain != "y":
    print("Done.")
    break
'''
    
#timer = Timer()
#tray = Tray()
'''
global results
results = []
for length in range(3, 8):
 findAllWords(length)

results = set(results)

used = []
score = 0
'''
'''
import threading
threading.Thread(target=countdown(10)).start()
while countdown.t is True:
#  threading.Thread(target=guessing(used, score)).start()
  #while True:
  #guessing(used, score)

#print(results)

#tray.display()
#here you go
'''

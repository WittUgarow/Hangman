import random
import turtle

screen = turtle.Screen()
screen.setup(width=500, height=500)
t = turtle.Turtle()
t.hideturtle()

def try0():
  t.goto(0,0)
  t.setheading(90)
  t.pendown()
  t.forward(100)
  t.right(90)
  t.forward(50)
  
def try1():
  t.pencolor("red")
  try0()
  
def try2():
  t.pencolor("orange")
  try0()

def try3():
  t.pencolor("green")
  try0()
  
def try4():
  t.pencolor("blue")
  try0()
  
def try5():
  t.pencolor("purple")
  try0()
  
def try6():
  t.pencolor("black")
  try0()

def draw(number):
  t.penup()
  if number==6:
    try0()
  if number==5:
    try1()
  if number==4:
    try2()
  if number==3:
    try3()
  if number==2:
    try4()
  if number==1:
    try5()
  if number==0:
    try6()

words = [
    "apple", "banana", "orange", "grape", "melon", "peach", "cherry", "lemon", "pear", "plum",
    "table", "chair", "couch", "bed", "door", "window", "lamp", "mirror", "carpet", "shelf",
    "house", "garden", "river", "mountain", "forest", "beach", "desert", "valley", "island", "ocean",
    "dog", "cat", "horse", "sheep", "cow", "rabbit", "mouse", "tiger", "lion", "bear",
    "school", "teacher", "student", "pencil", "paper", "book", "notebook", "desk", "chalk", "clock",
    "computer", "keyboard", "mousepad", "screen", "phone", "camera", "speaker", "charger", "battery", "cable",
    "happy", "sad", "angry", "sleepy", "funny", "brave", "smart", "strong", "quiet", "loud",
    "walk", "run", "jump", "climb", "swim", "dance", "laugh", "smile", "cry", "think",
    "music", "movie", "game", "story", "dream", "cloud", "rain", "snow", "wind", "storm",
    "bread", "cheese", "pizza", "burger", "cookie", "candy", "sugar", "salt", "butter", "milk"
]

drawing=[
  """
       _________
      ||
      ||
      ||
      ||
      ||
      ||
      ||
  ==============
  
  """,
  """
       _________
      ||        |
      ||       (O)
      ||      
      ||      
      ||      
      ||
      ||
  ==============
  
  """,
  """
       _________
      ||        |
      ||       (O)
      ||        |
      ||        |\
      ||        | \
      ||
      ||
  ==============
  
  """,
  """
       _________
      ||        |
      ||       (O)
      ||        |
      ||       /|\
      ||      / | \
      ||
      ||
  ==============
  
  """,
  """
       _________
      ||        |
      ||       (O)
      ||        |
      ||       /|\
      ||      / | \
      ||         \
      ||          \
  ==============
  
  """,
  """
       _________
      ||        |
      ||       (O)
      ||        |
      ||       /|\
      ||      / | \
      ||       / \
      ||      /   \
  ==============
  
  """
  ]


index = random.randint(0, len(words))
word = words[index]
workingWord = ""
letterBank=""

for i in range(0, len(word)):
  workingWord+="*"

tries=6
won=False

while tries>0:
  print("\n\n\n")
  draw(tries)
  print(drawing[6-tries])
  print(workingWord)
  print("Guessed Letters: "+letterBank)
  print("You have "+str(tries)+" left\n")
  
  letter = input("Enter a letter:")
  correct=False
  for i in range(0, len(word)):
    if word[i]==letter:
      workingWord = workingWord[:i] + letter + workingWord[i+1:]
      correct=True
  if not correct:
    tries-=1
    letterBank+=" "+letter
  if workingWord==word:
    print("You Win!!!")
    won=True
    break
  
if not won:
  print("You Lose :(")
print("The word was "+word)

turtle.done()

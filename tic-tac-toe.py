from tkinter import *

def next():
  global player

  if player == "O":
    player = "X"
  else:
    player = "O"

def winner(player):
  win = True

  for flag in winnerFlag:
    for elem in flag:
      win = True
      button = list[elem]
      if button["text"] != player:
        win = False
        break
    if win:
      break

  return win

def disable():
  for button in list:
    button["state"] = "disabled"

def checked(i):
  global player
  button = list[i]

  if button["text"] != "     ":
   return

  button["text"] = player

  if player == "O":
    button["bg"] = "lightgreen"
  else:
    button["bg"] = "yellow"

  if winner(player):
    print("Player " + player + " is win!")
    disable()

  next()

window = Tk()
player = "X"
winnerFlag = [
  [0, 1, 2], [3, 4, 5], [6, 7, 8],
  [0, 3, 6], [1, 4, 7], [2, 5, 8],
  [0, 4, 8], [2, 4, 6]
]
list = []

for i in range(9):
  b = Button(window, text="     ", command=lambda k=i: checked(k))
  b.grid(row=i//3, column=i%3)
  list.append(b)

window.mainloop()




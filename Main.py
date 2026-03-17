import random
import time
import keyboard
import threading
import os
#this makes the board function

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def placefruit():
    x = random.randint(0, 9)
    y = random.randint(0, 9)

    board[x][y] = 1

    for i in board:
         print(i)

#movement

movement = [
     0, -1
]

position = [
     5, 4
]

def controls():
     global movement
     while True:
          try: 
               if keyboard.is_pressed('w'):
                    movement = [-1, 0]
          except:
               break

          
          try: 
               if keyboard.is_pressed('a'):
                    movement = [0, -1]
          except:
               break

          
          try: 
               if keyboard.is_pressed('s'):
                    movement = [1, 0]
          except:
               break

          
          try: 
               if keyboard.is_pressed('d'):
                    movement = [0, 1]
          except:
               break


thread = threading.Thread(target=controls)
thread.start()

while True:
     time.sleep(0.5)
     position[0] += movement[0]
     
     position[1] += movement[1]
     print(position)

     if position[0] == 10: 
          break
     if position[0] == -1:
          break
     if position[1] == 10:
          break
     if position[1] == -1:
          break

     board[position[0]][position[1]] =2
     
     os.system("cls")

     for i in board:
         print(i)
     
thread.join()
placefruit()

#controls working now and somewhat functional
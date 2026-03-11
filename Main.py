import random
import time
import keyboard
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
     
     for i in board:
         print(i)
     
     try: 
          if keyboard.is_pressed('w'):
               movement = [1, 0]
     except:
          break
placefruit()

#Controls broken because of sleep line. Need fixing at later date.
from time import sleep
import pyautogui as pg
sleep(10)
#full path of the animal .txt file
txt= open('E:\Collage Work\Programming\Python/animals.txt', 'r')
a = '(Your firend Name) is a '
for i in txt:
  pg.write(a+i)
  #to press enter button
  pg.press('Enter')

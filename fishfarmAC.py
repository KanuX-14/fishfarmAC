## Script made by KanuX for Fish Farm tutorial ##
## Follow me: twitch.tv/kanux14 ##

from pynput.mouse import Button, Controller
import keyboard
from time import sleep
from random import uniform
bool = False

while True:
  if keyboard.is_pressed('f4'):
    bool = not bool
    sleep(1)
    Controller().click(Button.right, 1)
  if bool == True:
    Controller().press(Button.right)
    sleep(uniform(0,0.47))
  if keyboard.is_pressed('f12'):
    break
  sleep(0.03)

from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()
sleep(5)
keyboard.type ("Hello World")

sleep(3)
keyboard.press(Key.left)
sleep(2)
keyboard.press(Key.left)
sleep(2)
keyboard.press(Key.left)
sleep(2)
keyboard.press(Key.left)
sleep(2)
keyboard.release(Key.left)
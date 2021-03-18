from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()
sleep(5)
keyboard.type ("Hello World")
Hello World
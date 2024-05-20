import pyautogui
import time

time.sleep(5)  # Tempo que irei deixar o mouse sobre o item que desejo saber a posição
print(pyautogui.position())  # Mostra a posição

# print(pyautogui.KEYBOARD_KEYS) # Mostra as teclas do teclado

pyautogui.scroll(200)

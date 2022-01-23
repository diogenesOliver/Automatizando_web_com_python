from time import time
import pyautogui

pyautogui.alert('Clique em OK para executar o código! [Atenção] Durante a execução do codigo não mexa no seu computador!')
pyautogui.PAUSE = 3

pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.write('https://github.com/')
pyautogui.press('enter')

pyautogui.moveTo(1849, 104)
pyautogui.mouseDown()
pyautogui.mouseUp()

pyautogui.moveTo(1769, 251)
pyautogui.mouseDown()
pyautogui.mouseUp()

""" pyautogui.alert('Código executado com sucesso! Pode voltar a mexer no computador normalmente!') """
from time import time
import pyautogui

pyautogui.alert('Clique em OK para executar o código! [Atenção] Durante a execução do codigo não mexa no seu computador!')
pyautogui.PAUSE = 0.7

pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.write('https://www.youtube.com/')
pyautogui.press('enter')

pyautogui.moveTo(905, 89)
pyautogui.mouseDown()

pyautogui.write('Kali Uchis - Telepatía (TikTok Remix) [Lyrics]')
pyautogui.press('enter')

pyautogui.moveTo(704, 299)
pyautogui.mouseDown()
pyautogui.mouseUp()

pyautogui.alert('Código executado com sucesso! Pode voltar a mexer no computador normalmente!')
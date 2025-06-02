import pyautogui
import time # pyautogui é uma biblioteca que permite controlar o mouse e o teclado


# pyautogui.click -> clica em uma posição específica da tela
# pyautogui.press -> pressiona uma tecla específica
# pyautogui.write - > escreve um texto como se fosse digitado
# pyautogui.hotkey -> pressiona uma combinação de teclas

pyautogui.PAUSE = 1  # Define um tempo de pausa entre os comandos

#  Abre o navegador Opera e acessa uma URL específica

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')

time.sleep(3)  # Espera 5 segundos para a página carregar

pyautogui.click(500, 500)  # Clica na posição (500, 500) da tela
pyautogui.write('hashtagtreinamentos')  # Digita o nome de usuário

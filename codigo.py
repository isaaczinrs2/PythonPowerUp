import pyautogui
import time # pyautogui é uma biblioteca que permite controlar o mouse e o teclado
import pandas

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

pyautogui.click(1000, 500)  # Clica na posição (1000, 500) da tela
pyautogui.write('python1impressionar@gmail.com')  # Digita o nome de usuário

pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o próximo campo
pyautogui.write('minhasenhasupersecreta')  # Digita a senha
pyautogui.press('enter')  # Pressiona Enter para fazer login
time.sleep(3)  # Espera 3 segundos para o login ser processado

tabela = pandas.read_csv("produtos.csv")  # Lê o arquivo CSV com os produtos

print (tabela)  # Imprime a tabela no console

# cadastrar 1 produto

for linha in tabela.index:
    pyautogui.click(1039, 361)  # Clica no botão de cadastro
    time.sleep(1)  # Espera 1 segundo para o formulário abrir
    
    codigo = tabela['codigo'][linha]  # Obtém o código do produto atual
    pyautogui.write(str(codigo))  # Digita o código do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    marca = tabela['marca'][linha]  # Obtém a marca do produto atual
    pyautogui.write(marca)  # Digita a marca do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    tipo = tabela['tipo'][linha]  # Obtém o tipo do produto atual
    pyautogui.write(tipo)  # Digita o tipo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    categoria = tabela['categoria'][linha]  # Obtém a categoria do produto atual
    pyautogui.write(str(categoria))  # Digita a categoria do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    preco = tabela['preco_unitario'][linha]  # Obtém o preço do produto atual
    pyautogui.write(str(preco))  # Digita o preço do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    custo = tabela['custo'][linha]  # Obtém o custo do produto atual
    pyautogui.write(str(custo))  # Digita o custo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    obs = ""  # Observação vazia
    pyautogui.write(obs)  # Digita a observação (vazia)
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    pyautogui.press('enter')  # Pressiona Enter para finalizar o cadastro   25.0


pyautogui.scroll(10000)




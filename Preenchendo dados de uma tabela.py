import time
import pyautogui

# pyautogui.press – Serve para pressionar uma tecla do seu teclado
# pyautogui.write – Serve para escrever com o teclado (como se fosse você digitando)
# pyautogui.click – Serve para clicar com o mouse

pyautogui.PAUSE = 0.5  # Tempo de execução dos comandos

# Abrir o sistema (Chrome) e entrar no site
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Tempo para carregar
time.sleep(2)

# Fazer o login
pyautogui.click(x=916, y=406)
pyautogui.write('teste123@gmail.com')
pyautogui.press('tab')
pyautogui.write('suasenha')
pyautogui.press('tab')
pyautogui.press('enter')

# Tempo para carregar
time.sleep(2)

import pandas as pd

# Abrir/Importar a base de dados dos produtos para cadastrar
tabela = pd.read_csv('produtos.csv')

# Cadastrar os produtos
for linha in tabela.index:           # columns = colunas / index = linha
    pyautogui.click(x=874, y=298)    # Peguei a posição do primeiro campo

    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)          # Código
    pyautogui.press('tab')           # Pula
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)           # Marca
    pyautogui.press('tab')           # Pula
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)            # Tipo
    pyautogui.press('tab')           # Pula
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)       # Categoria
    pyautogui.press('tab')           # Pula
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)  # Preço
    pyautogui.press('tab')           # Pula
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)           # Custo
    pyautogui.press('tab')           # Pula
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)             # Observação

    pyautogui.press('tab')           # Pula
    pyautogui.press('enter')         # Confirma
    pyautogui.scroll(5000)           # Rola pra cima

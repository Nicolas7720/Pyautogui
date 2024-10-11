import pyautogui
import time

time.sleep(5)
print(pyautogui.position())

pyautogui.PAUSE = 2.5
# abrir o navegador (chrome)
pyautogui.press("win") #abrir o iniciar
pyautogui.write("chrome") #digitar chrome

pyautogui.press("enter") #apertar enter

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=685, y=451)
# escrever o seu email
pyautogui.write("nkblabla@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("10201030")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")

# Passo 3: Importar a base de produtos pra cadastrar
pyautogui.click(x=696, y=319)
pyautogui.PAUSE = 0.2

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
linha = 0

for linha in tabela.index:

    # clicar no campo de código
    pyautogui.click(x=696, y=319)

    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]

    # preencher o campo
    pyautogui.write(str(codigo))

    # passar para o proximo campo
    pyautogui.press("tab")

    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    if not pd.isna(obs):

        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")

    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima

    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim

    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim

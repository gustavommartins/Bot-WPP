import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def montaMensagem(valor):
    print("\nVocê selecionou enviar apenas uma mensagem!\n")
    numero = input("Digite o numero/nome do contato ou grupo: ")
    mensagem = input("Digite a sua mensagem: ")
    validaLoop = valor
    enviaMensagem(numero, mensagem, validaLoop)


def switch(comando):
    if comando == 0:
        validador = False
        return validador
    elif comando == 1:
        montaMensagem(False)
        validador = True
        return validador
    elif comando == 2:
        montaMensagem(True)
        validador = True
        return validador


def loopMensagens(mensagem, numeroMensagens, driver):
    campo_mensagem = driver.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    for i in range(int(numeroMensagens) - 1):
        campo_mensagem[1].send_keys(mensagem)
        campo_mensagem[1].send_keys(Keys.ENTER)


def mensagemFunction(numero, mensagem, numeroMensagens):
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.get('https://web.whatsapp.com/')
    campo_pesquisa = True

    while campo_pesquisa:
        campo_pesquisa = procuraCampo(driver)
    time.sleep(5)
    campo = driver.find_element(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    campo.click()
    campo.send_keys(numero)
    campo.send_keys(Keys.ENTER)
    time.sleep(5)
    loopMensagens(mensagem, numeroMensagens, driver)
    time.sleep(5)


def procuraCampo(driver):
    elements = driver.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    element = False

    if not elements:
        element = True

    return element


def enviaMensagem(numero, mensagem, multiplaMensagens):
    if multiplaMensagens:
        numeroMensagens = input("Digite quantas vezes será enviada a mensagem:  ")
        mensagemFunction(numero, mensagem, numeroMensagens)
    else:
        numeroMensagens = "1"
        mensagemFunction(numero, mensagem, numeroMensagens)

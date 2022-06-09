import time
from selenium import webdriver
from msedge.selenium_tools import EdgeOptions, Edge
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


def loopMensagens(mensagem, numeroMensagens, browser):
    campo_mensagem = browser.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    for i in range(int(numeroMensagens) - 1):
        campo_mensagem[1].send_keys(mensagem)
        campo_mensagem[1].send_keys(Keys.ENTER)


def mensagemFunction(numero, mensagem, numeroMensagens):
    options = EdgeOptions()
    options.use_chromium = True
    options.binary_location = r"/usr/bin/microsoft-edge"
    options.set_capability("platform", "LINUX")

    webdriver_path = r"/home/gummart/webdrivers/msedgedriver"

    browser = Edge(options=options, executable_path=webdriver_path)
    browser.get('https://web.whatsapp.com/')
    campo_pesquisa = True

    while campo_pesquisa:
        campo_pesquisa = procuraCampo(browser)
    time.sleep(5)
    campo = browser.find_element(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    campo.click()
    campo.send_keys(numero)
    campo.send_keys(Keys.ENTER)
    time.sleep(5)
    loopMensagens(mensagem, numeroMensagens, browser)
    time.sleep(5)
    browser.quit()


def procuraCampo(browser):
    elements = browser.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
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

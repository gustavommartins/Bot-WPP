import functions as bot

print("Bem vindo ao BOT de envio de mensagens no WhatsApp!\n")

validador = True

while validador:
    print("Opções de entrada", end="\n\n")
    print("0 - SAIR DO BOT")
    print("1 - ENVIAR APENAS UMA MENSAGEM")
    print("2 - ENVIAR VARIAS MENSAGENS", end="\n\n")
    comando = input("O que você deseja fazer? \n")
    validador = bot.switch(int(comando))
else:
    print("Você decidiu sair, até logo!")
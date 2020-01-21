#!/usr/bin/python3
#Codado por badc

import urllib.request
import urllib.parse
import urllib.error
import time

vapotest = input("Insira a url:\nExemplo ----> https://www.facebook.com/usuariofb\n") # Url Facebook Perfil
status = ()
tempo = input("\nDeseja efetuar uma verificação a cada quanto tempo?\n \nDigite em segundos!\n\n")

while True:
    try:
        print ("\nVerificando status...")
        teste = urllib.request.urlopen(vapotest)
        status = (1)
        print ("Facebook Status: Ativado!")
    except urllib.error.HTTPError as desativado:
        status = (2)
        print("Facebook Status: Desativado!\n")
        print("Aguardando", tempo, "segundos para verificar novamente!")
        print("Para abortar pressione Ctrl+C\n")
    except KeyboardInterrupt:
        print ("\nEncerrando...")
        time.sleep(3)
        print ("Desligado! :)")
    if status == 2:
        try:
            time.sleep (int(tempo))
            continue
        except KeyboardInterrupt:
            print ("\nEncerrando...")
            time.sleep(3)
            print ("Desligado! :)")
            break
    else:
        break

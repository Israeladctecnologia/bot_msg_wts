import pyautogui
import webbrowser
from time import sleep
import pyperclip
import cv2 #Necessário para que o pyautogui utilize a funcionalidade de confiança

#Funçao enviar texto
def texto(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

#Comando integra contatos
telefones = []

with open('telefones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n') [0])

#Repetições de envio 
for telefone in telefones:
    webbrowser.open(f'https://wa.me/{telefone}')
    sleep(5)
    
 
    #Laço de repetição
    try:
        while True:
        #Tentar localizar na tela
            iniciar_conversa = pyautogui.locateCenterOnScreen('iniciar.png', confidence=0.8)
                        
            if iniciar_conversa is not None:
                pyautogui.click(iniciar_conversa)
                break
            else:
                print('Iniciar não localizado, tentando novamente...')
    except pyautogui.ImageNotFoundException:
            print('Iniciar não localizado, tentando novamente...')
            sleep(5)

    sleep(5)
    try:
        while True:
            #Tentar localizar na tela
            usar_wts = pyautogui.locateOnScreen('usar_wts.png', confidence=0.51)
                            
            if usar_wts is not None:
                pyautogui.click(usar_wts)
                break
            else:
                print('Usar Wts não localizado, tentando novamente...')
    except pyautogui.ImageNotFoundException:
            print('Usar Wts não localizado, tentando novamente...')
            sleep(5)

    sleep(16)

    pyautogui.click(1162,677, duration=3)
    sleep(22)

    texto(' Oi, essa msg foi enviada por um robo kkk')
    sleep(10)

    pyautogui.press('enter')
    sleep(300)
    
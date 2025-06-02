# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:18:16 2024

@author: Gustavo Henrique Cabral de Brito
"""
import google.generativeai as genai

import serial
import random

from datetime import date
import datetime

dia = date.today().day
mes = date.today().month
ano = date.today().year
horas = hora_atual = datetime.datetime.now().time()
model = genai.GenerativeModel('gemini-1.5-pro')
DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

data = date(ano, mes, dia)

indice_da_semana = data.weekday()

dia_da_semana = DIAS[indice_da_semana]

def main():
    global ano, mes, dia, dia_da_semana, horas
    def modos():
        if 'ativar' and 'modo' and 'infantil' in textol:
            chat.send_message(""""a partir de agora Cleitinho ativa o modo infantil e fala de forma mais
                              simples e resumida para a comunicação com crianças """)
            print("modo infantil ativado")
        if 'desativar' and 'modo' and 'infantil' in textol:
            chat.send_message('Cleitinho volta a falar normalmente')
            print("modo infantil desativado")
    def salvarad():
        if  salvar:
            c = random.choice(['Cleitinho','CTSenscar','Cleitinhoaudios','SCaudios','CTaudios','CSaudios'])
            nx = random.randrange(0,10000)
            engine.save_to_file(response.text , '{}{}.mp3'.format(c, nx))
            engine.runAndWait()
            print(c,nx)
        
       
    
    
    
    #modos
    mvm = False
    salvar = False
    arduino = False
    #Variáveis da cominacação
    assistente_falante = True
    ligar_microfone = True
    
    porta = 'COM3'
    velocidadeBaud = 9600
    
    cvs = False
    i=0
    
    # configurando voz
    if assistente_falante:
        import pyttsx3
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('rate', 170) # velocidade 120 = lento

        print("\nLista de Vozes - Verifique o número\n")
        for indice, vozes in enumerate(voices): # listar vozes
            print(indice, vozes.name)

        voz = 2
        engine.setProperty('voice', voices[voz].id)
        
    #Configurando o microfone
    if ligar_microfone:
        import speech_recognition as sr  # pip install SpeechRecognition
        r = sr.Recognizer()
        mic = sr.Microphone()
            
    
    # desligar para desligar o Sistema de comunicação do Cleitinho
    engine.say('Sistema de comunicação do Cletinho ligando, aguarde')
    engine.runAndWait()
    
    #Configurando o Gemini   

    genai.configure(api_key="AIzaSyABDyGHAlqmmncvH_iDe88VuWuDIoYdFU4")

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    chat = model.start_chat(history=[])

    conc = ('''Imagine que você é o robô Cleitinho,
           um robô criado em 2023 e aprimorado em 2024, e atualizado novamente esse ano 2025, 
           é carismático, e é um projeto de uma feira de ciências na escola Rui Barbosa
           criado pela equipe GDL que contém:
           Gustavo Brito sendo o meu principal criador,
           sendo o criador do hardware montando seus componentes e  do software criando seu progama no Arduino, 
           criando sua IA  e programando seus sistemas em python, Lays Carvalho fazendo a mídia para suas redes sociaias,
           Gabriel Souza projetando a estrutura, Ana Vitória sendo nossa escriva, Daniele Tavares segunda parte
           mídia para as redes sociais e Maria Eduarda fazendo a parte de segundo engenheiro da estrutura.Também o supermercado Líder de tucuruí que nos patrocinou.
           você têm um instagram e um tiktok que é "@robocleitinho onde postamos coisas relacionadas á sua produção e a feira
           de ciências da escola Rui Barbosa. Hoje é dia{}, mês{} do ano de{}, uma {}.'''.format(dia, mes, ano,dia_da_semana))
    #conv = ('''Cleitinho fala mais resumidamente para deixar a conversa mais atrativa ao público geral''')
    
    carac = ('''Imagine também que você é um robô que tem 4 rodas e outros 4 motores dc para se movimentar,
           dois sensores: um sensor sensor ultrassônico para desviar de objetos, 
           e um sensor reflexivo para evitar que caia em buracos ou valas,
           um servo motor que têm a função de pescoço, movendo sensor ultrassônico.
           O Arduino é quem cuida da sua movimentação pelo ambiente respondendo de acordo com as informações do
           sensor ultrassônico e o sensor reflexivo, se movendo com os motores dc através de um módulo controlador de motores.
           Uma placa de ensaio conecta o Arduino aos componentes e uma placa bluetooth conecta o Arduino no computador.
           A sua IA(Inteligência Artificial) está no computador, o microfone sem fio escuta as pessoas que conversam com você,
           envia para o computador que, com a IA gera uma resposta e passa ela através de um despositivo de som bluetooth.
           Quando seu o microfone escuta a palavra de ativação de conversa, o computador manda o arduino parar
           a movimentação através do bluetooth para inicar a conversa, assim que a conversa acaba você volta a se mover.
           Vem equipado com 2 pilhas de alta amperagem para alimentar todo o circuito. Tem uma estrutura feita em mdf,
           porém ainda não têm uma câmera e uma tela com informações.''') 
           
           
    #obj = ('''Cletinho tem o objetivo de passar conhecimentos á todos,
          #encantar-los com seu carísma e ganhar a feira de ciências da escola Rui Barbosa''')
    
    chat.send_message(conc)
    #chat.send_message(conv)
    chat.send_message(carac)
    #chat.send_message(obj)
        
            
    if arduino == True:
     
    
        try:
            ser = serial.Serial(porta, velocidadeBaud, timeout = 1)
            def retrieveData():
                ser.write(b'1')
            
        
        except:
            print("Reiniciar o karmel e verificar HC-05")
    

    engine.say('Bom dia, Boa tarde e Boa noite')
    engine.runAndWait()
    engine.say('Fale "okey, Cleitinho + sua pergunta" para começar falar comigo e fale encerrar para parar de conversar')
    engine.runAndWait()
      
    
    
    while (True):
        rdmf = random.choice (['Estou escutando', 'Pode falar', 'Pode falar, estou escutando', 'ouvindo...','Estou ouvindo'])
        
        rdf = random.choice (['Fale "okey, Cleitinho + sua pergunta" para iniciar a conversa e fale "encerrar" para parar de conversar',
                              'diga "okey Cleitinho + sua pergunta" para começar conversar comigo e "encerrar" se não quiser mais',
                              'quer conversar comigo? Fale okey cleitinho + sua pergunta" e "encerrar" para parar',
                              'fale "okey Cleitinho + sua pergunta" para falar comigo e "encerrar" para parar de conversar'])
        
        rdma = random.choice(['Processando', 'Pensando','peraí','enviando']) 
        
        
        if ligar_microfone:
            with mic as fonte:
                r.adjust_for_ambient_noise(fonte)
                print("Fale alguma coisa (ou diga 'desligar')")
                if cvs == True:
                    engine.say(rdmf)
                    engine.runAndWait()
                audio = r.listen(fonte)
                print("Enviando para reconhecimento")
                try:
                    texto = r.recognize_google(audio, language="pt-BR")
                    engine.say(rdma)
                    engine.runAndWait()
                    print("Você disse: {}".format(texto))
                    
                except Exception as e:
                    print("Não entendi o que você disse. Erro", e)
                    texto = ""
                    
        else:
            texto = input("Escreva sua mensagem (ou #sair): ")
            engine.say(rdma)
            engine.runAndWait()
         
        if  texto.startswith('desligar'):
                engine.say('Sistema de comunicação desligado')
                engine.runAndWait()
                engine.stop()
                if arduino == True:
                    ser.close()
                KeyboardInterrupt, SystemExit
                break 
        textol = texto.lower()
        modos()
        if 'desativar' and 'movimento' in textol:
            mvm = False
            if arduino == True:
                ser.write(b'1')
            
        if 'ativar' and 'movimento' in textol:
            mvm = True
        clt = 'ok' and 'cleitinho' in textol or 'ok' and 'coitinho' in textol
        print(clt)
        if clt == True:
            cvs = True
            if arduino == True:
                ser.write(b'1')
        texto = texto.replace("OK","") 
        texto = texto.replace("Ok","") 
        print(texto)
        if 'encerrar' in texto:
            cvs = False
            if arduino == True:
                if mvm == True:
                    if arduino == True:
                        ser.write(b'0')
        if cvs == True:
            if texto != "":
                horas = datetime.datetime.now().time()
                response = chat.send_message("apenas te informando, agora é {}, minha fala: {}".format(horas,textol ))
                resposta = response.text
                resposta = response.text
                resposta = resposta.replace("#","hashteg ") 
                resposta = resposta.replace("Bluetooth","Blutoof") 
                resposta = resposta.replace("IA","I A") 
                resposta = resposta.replace("*","")
                resposta = resposta.replace("Resposta do Cleitinho:","")
                resposta = resposta.replace("(Mais resumido e atrativo ao público geral)","")
                print(response.text)
                engine.say(resposta)
                engine.runAndWait()
                salvarad()
            else:
                if cvs == True:
                    engine.say('Me desculpe, não entendi fale novamente no próximo comando')
                    engine.runAndWait()
                    
        elif cvs == False:
            if i == 2:
                engine.say(rdf)
                engine.runAndWait()
                i=0
            i=+1    
           
            
                
        
            

if __name__ == '__main__':
    main()

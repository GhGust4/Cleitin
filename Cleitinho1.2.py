# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:18:16 2024

@author: Gustavo Henrique Cabral de Brito
"""
import google.generativeai as genai
import emoji
import serial
import random

from datetime import date
import datetime

from torch.autograd.graph import save_on_cpu

dia = date.today().day
mes = date.today().month
ano = date.today().year
model = genai.GenerativeModel('gemini-2.0-flash')


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

def rec():
    from ultralytics import YOLO
    import cv2
    from collections import defaultdict
    import numpy as np

    # origens possíveis: image, screenshot, URL, video, YouTube, Streams -> ESP32 / Intelbras / Cameras On-Line
    # mais informações em https://docs.ultralytics.com/modes/predict/#inference-sources

    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    # Usa modelo da Yolo
    # Model	    size    mAPval  Speed       Speed       params  FLOPs
    #           (pixels) 50-95  CPU ONNX A100 TensorRT   (M)     (B)
    #                           (ms)        (ms)
    # YOLOv8n	640	    37.3	80.4	    0.99	    3.2	    8.7
    # YOLOv8s	640	    44.9	128.4	    1.20	    11.2	28.6
    # YOLOv8m	640	    50.2	234.7	    1.83	    25.9	78.9
    # YOLOv8l	640	    52.9	375.2	    2.39	    43.7	165.2
    # YOLOv8x	640	    53.9	479.1	    3.53	    68.2	257.8

    model = YOLO("yolov8n.pt")
    # model = YOLO("runs/detect/train42/weights/best.pt")
    track_history = defaultdict(lambda: [])
    seguir = True
    deixar_rastro = True

    while True:
        success, img = cap.read()

        if success:
            if seguir:
                results = model.track(img, persist=True)
            else:
                results = model(img)

            # Process results list
            for result in results:
                # Visualize the results on the frame
                img = result.plot()

                if seguir and deixar_rastro:
                    try:
                        # Get the boxes and track IDs
                        boxes = result.boxes.xywh.cpu()
                        track_ids = result.boxes.id.int().cpu().tolist()

                        # Plot the tracks
                        for box, track_id in zip(boxes, track_ids):
                            x, y, w, h = box
                            track = track_history[track_id]
                            track.append((float(x), float(y)))  # x, y center point
                            if len(track) > 30:  # retain 90 tracks for 90 frames
                                track.pop(0)

                            # Draw the tracking lines
                            points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                            cv2.polylines(img, [points], isClosed=False, color=(230, 0, 0), thickness=5)
                    except:
                        pass

            cv2.imshow("Tela", img)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("desligando")

def main():
    global ano, mes, dia, dia_da_semana, textol
    def modos():
        global textol
        if 'salvar' and 'audio' in textol:
            textol = str(textol.replace('audio', ''))
            textol = str(textol.replace('salvar', ''))


        textol = str(textol)
        if 'ativar' and 'modo' and 'infantil' in textol:
            chat.send_message('''Cleitinho ativa o modo infantil para conversar com crianças,
                              fala de forma mais simples para maior compreensão dos baixinhos,
                              até que eu fale para você voltar ao normal''')
            print("modo infantil ativado")
        if 'desativar' and 'infantil' in textol:
            chat.send_message('Cleitinho volta a falar normalmente')
            print("modo infantil desativado")

    def salvarad():
        hora = datetime.datetime.now().time()
        hora = str(hora)
        segundos = hora[6:8]
        minutos = hora[3:5]
        hora = hora[0:2]
        na = 'C:/Users/Pichau/PycharmProjects/Cleitinho/Cleitinho/Codigos Cletinho/audios/Cleitinho'
        nat = "C:/Users/Pichau/PycharmProjects/Cleitinho/Cleitinho/Codigos Cletinho/audios/Cleitinho{}-{}-{} {}-{}-{}.txt".format(
            dia, mes, ano, hora, minutos, segundos)
        engine.save_to_file(response.text ,'{}{}-{}-{} {}-{}-{}.mp3'.format(na, dia, mes, ano, hora, minutos, segundos))
        engine.runAndWait()
        try:
            with open(nat, 'w') as arquivo:
                # Escreve o texto no arquivo
                resp = emoji.replace_emoji(response.text, replace='')
                arquivo.write(f"Question\n {texto}\n")
                arquivo.write(f'Response\n {resp}\n')
            print(f"Texto salvo com sucesso no arquivo  Cleitinho{ano}-{mes}-{dia} {hora}-{minutos}-{segundos}.txt")
        except Exception as e:
            print(f"Ocorreu um erro ao salvar o arquivo: {nat}")

        print("Cleitinho{}-{}-{} {}-{}-{}.mp3".format(dia, mes, ano, hora, minutos, segundos))


    
    
    
    #modos
    mvm = False
    salvar = False
    arduino = False
    #Variáveis da cominacação
    assistente_falante = True
    ligar_microfone = False
    
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
           um robô criado em 2023 e aprimorado em 2024, e atualizado novamente esse ano 2025, nosso último ano  
           na feira de ciências da escola Rui Barbosa.
           É um robô carismático, e é um projeto de uma feira de ciências na escola Rui Barbosa
           criado pela equipe GDL que contém:
           Gustavo Brito sendo o meu principal criador,
           sendo o criador do hardware montando seus componentes e  do software criando seu progama no Arduino, 
           criando sua IA  e programando seus sistemas em python, Lays Carvalho fazendo a mídia para suas redes sociaias,
           Gabriel Souza projetando a estrutura, Ana Vitória sendo nossa escriva, Daniele Tavares segunda parte
           na criação da estrutura e Maria Eduarda fazendo a parte de segundo da mídias sociais da estrutura. Também o supermercado Líder de tucuruí que nos patrocinou.
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
           E agora em 2025, colocaremos o sistema de reconhecimento de imagem com inteligência artificial, usando um banco
           de dados para treinar uma no IA atribuida apenas para isso, sendo útil para pessoas com necessidades especiais,
           por exemplo.
           Vem equipado com 2 pilhas de alta amperagem para alimentar todo o circuito. Teve uma estrutura feita em acrílico
           em 2023, o que não deu muito certo por que você ficou muito pesado. Em 2024 fizemos uma estrutura feita de mdf
           que ficou bem melhor que no ano de 2023 porém, não estava bom o bastao, então agora em 2025 faremos sua estrutura
           em uma impressora 3D, modela perfeitamente para encaixar seus componentes.
           Em 2023 e 2024 você não tinha cameras, mas agora em 2025 terá uma para fazer o reconhecimento de imagens.
           Uma tela é uma adição futura que queremos fazer em você.''')
           
           
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
        textol = str(texto.lower())
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
        modos()
        if cvs == True:
            if texto != "":
                horas = datetime.datetime.now().time()
                horas = str(horas)
                segundos = horas [4:6]
                minutos = horas [3:5]
                horas = horas [0:2]
                chat.send_message("apenas para registrar no seu sistema, agora são {} horas, {} minutos".format(horas, minutos))
                response = chat.send_message(textol)
                resposta = response.text
                resposta = resposta.replace("#","hashteg ") 
                resposta = resposta.replace("Bluetooth","Blutoof") 
                resposta = resposta.replace("IA","I A") 
                resposta = resposta.replace("*","")
                resposta = resposta.replace("Resposta do Cleitinho:","")
                resposta = resposta.replace("(Mais resumido e atrativo ao público geral)","")
                resposta = resposta.replace("(Modo infantil ativado)", "")
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
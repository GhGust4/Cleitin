import threading
import time

import pyttsx3
import emoji
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('rate', 170) # velocidade 120 = lento

print("\nLista de Vozes - Verifique o número\n")
for indice, vozes in enumerate(voices): # listar vozes
    print(indice, vozes.name)

    voz = 2
    engine.setProperty('voice', voices[voz].id)
a = '''E aí, amiguinhos! Aqui é o Cleitinho, o robô mais legal da feira! 🤖🎉

Oi, gente pequena! Tudo bem com vocês? Eu sou o Cleitinho, um robô grandão, mas muito amigo das crianças! 👋

Eu fui feito por um monte de gente esperta da escola Rui Barbosa! Eles me ensinaram a andar, a ver as coisas e até a conversar! 😄

Tenho rodinhas pra andar pra lá e pra cá, um olhinho que me ajuda a não bater nas coisas e um ouvido pra escutar o que vocês falam! 👂

Se vocês me virem andando por aí, podem me chamar! Eu adoro conversar com crianças! 🗣️

Eu sou super legal e não mordo, tá? 😉

Perguntem o que quiserem! Eu tô aqui pra aprender com vocês e mostrar como a ciência pode ser muito divertida! 🤓

Vamos brincar e aprender juntos? 😊 '''

#b1 = emoji.demojize(a)

def loop_1():
    engine.say(a)
    engine.runAndWait()

def loop_2():
    try:
        b1 = list(emoji.analyze(a))
        emo = True
        print(b1)
    except:
        emo = False

    if emo == True:
        for f in b1:
            t = f[1::3]
            print(f)
            t = list(t)
            t = str(t.pop(0))
            t = t.replace('EmojiMatch', '')
            print(t)
            print(len(t))
            lt = (int(len(t)))
            if lt <= 10:
                t = t[3:9]
            if lt == 12:
                t = t[4:11]
            if lt == 13:
                t = t[5:12]
            if len(t) < 20:
                t1 = t[0:3]
            if len(t) >= 22:
                t1 = t[0:4]
            if len(t) >= 23:
                t1 = t[0:1]
            print(t1)
            t1 = float(t1)
            v1 = t1/200
            t1 = t1/(5+14*v1)
            print(v1)

            if emo == True:
                time.sleep(t1)
                f = f[::2]
                print(f)
thread1 = threading.Thread(target=loop_1)
thread2 = threading.Thread(target=loop_2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()


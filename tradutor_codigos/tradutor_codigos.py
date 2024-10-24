import keyboard, json, pyperclip, pyttsx3
from pygame import mixer
mixer.init()
pytts = pyttsx3.init()


#///////////////////////#

type_hotkey = "/"

translate_hotkey = ';'

#///////////////////////#

tts_letter = ""
tts_str = ""


with open("tradutor_codigos/tabela.json", "r") as f:
    table = json.load(f)

while True:
    tp = input("bin / morse?: ")
    if (tp != "morse" and tp != "bin"):
        print("inválido")
    else:
        break

while True:
    keyboard.release(type_hotkey)
    tts = mixer.Sound("tradutor_codigos/audios/comecar.WAV")
    tts.play()
    print("Pressione a tecla de atalho para começar")

    while True:
        read = keyboard.read_hotkey(False)
        
        if (read == type_hotkey):
            keyboard.send('backspace')
            break
        if (read == translate_hotkey):
            cb = pyperclip.paste()
            
            try:
                teste = int(cb[0])
                data = table['bin']
            except:
                data = table['morse']

            tts_str = ""

            for char in cb:
                if (char != " "):
                    tts_letter += char
                else:
                    tts_letter += " "
                    for a in data:
                        if (tts_letter == data[a]):
                            if(a == "space"):
                                tts_str += " "
                            else:
                                tts_str += a
                            break
                    tts_letter = ""
            tts.stop()
            print(tts_str)
            pytts.say(tts_str)
            pytts.runAndWait()

    tts.stop()
    tts = mixer.Sound("tradutor_codigos/audios/traduzindo.WAV")
    tts.play()
    print("traduzindo")

    while True:   
        tecla = keyboard.read_event(True)
        try:
            if (tecla.event_type == 'down'):
                if (tp == "bin"):
                    keyboard.write(table[tp][tecla.name])
                else:
                    keyboard.write(table[tp][(tecla.name).lower()])
            else:
                tp += table #forçar um erro
        except:
            if (tecla.name == 'backspace' and tecla.event_type == 'down'):
                keyboard.send('backspace')
            elif (tecla.name == type_hotkey and tecla.event_type == 'up'):
                break
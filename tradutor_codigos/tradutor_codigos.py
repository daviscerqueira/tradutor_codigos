import keyboard, json, pyperclip


# /////////////////////// #

type_hotkey = "/"

translate_hotkey = ';'

# /////////////////////// #


with open("tabela.json", "r") as f:
    data = json.load(f)

while True:
    tp = input("bin / morse?: ")

    if (tp != "morse" and tp != "bin"):
        print("Inválido\n")

    else:
        table = data[tp]
        break

while True:
    print("Pressione a tecla para começar ou traduzir\n")

    while True:
        read = keyboard.read_hotkey(False)
        
        if (read == type_hotkey):
            keyboard.send('backspace')
            break

        if (read == translate_hotkey):
            keyboard.send('backspace')
            cb = pyperclip.paste()
            
            if (cb[0].isnumeric()):
                cb_table = data['bin']
            else:
                cb_table = data['morse']

            tts_str = ""

            cb = cb.split()

            reverse_table = {v: k for k, v in cb_table.items()}

            for i in cb:
                i += " "
                try:
                    if (not reverse_table[i] == 'space'):
                        tts_str += reverse_table[i]
                    else:
                        tts_str += " "
                except:
                    continue
                
            print(f"Texto copiado: {tts_str}\n")


    print("traduzindo...\n")

    while True:   
        tecla = keyboard.read_event()

        if (tecla.event_type == 'down' and tecla.name in table):
            keyboard.send('backspace')
            keyboard.write(table[tecla.name])
        
        elif (tecla.name == type_hotkey and tecla.event_type == 'up'):
            keyboard.send('backspace')
            break
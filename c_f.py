import PySimpleGUI as sg

class c_f:
    def __init__(self):

        theme = sg.theme('BlueMono')

        layout = [

        [sg.Text("Digite o valor de Celsius")],
        [sg.Input(size=(10,0), key="input")],
        [sg.Text(" ", key="resultado", size=(0,1))],
        [sg.Button("Confirmar")]
        ]
        self.window = sg.Window("Celsius para Fahreinheit", layout)

    def init_cf(self):
        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED:
                break
            if event == "Confirmar":
                try:
                    # graus celsius recebido pelo usuário:
                    self.c = float(values["input"])
                    f = self.c * 1.8 + 32
                    self.window["resultado"].update(f"O resultado foi {f} (Fahreinheit)")
                except:
                    self.window["resultado"].update(
                f"Digite apenas números, ou troque a vírgula do número por um ponto final (.)")
                    
celsius_fahreinheit = c_f()

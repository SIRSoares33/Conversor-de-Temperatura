import PySimpleGUI as sg

class c_k:
    def __init__(self):

        theme = sg.theme('BlueMono')

        layout = [

        [sg.Text("Digite o valor de Celsius")],
        [sg.Input(size=(10,0), key="input")],
        [sg.Text(" ", key="resultado", size=(0,1))],
        [sg.Button("Confirmar")]
        ]
        self.window = sg.Window("Celsius para Kelvin", layout)

    def init_ck(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "Confirmar":

                try:
                    # graus celsius recebido pelo usuário:
                    self.c = float(values["input"])
                    k = self.c + 273.15
                    self.window["resultado"].update(f"O resultado foi {k} (Fahreinheit)")
                except:
                    self.window["resultado"].update(
                f"Digite apenas números, ou troque a vírgula do número por um ponto final (.)")
        


celsius_kelvin = c_k()

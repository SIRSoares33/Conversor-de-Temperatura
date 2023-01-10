import PySimpleGUI as sg

class k_c:
    def __init__(self):

        theme = sg.theme('BlueMono')

        layout = [

        [sg.Text("Digite o valor de Kelvin")],
        [sg.Input(size=(10,0), key="input")],
        [sg.Text(" ", key="resultado", size=(0,1))],
        [sg.Button("Confirmar")]
        ]
        self.window = sg.Window("Kelvin para Celsius", layout)

    def init_kc(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "Confirmar":
                try:
                    # Kelvin recebido pelo usuário:
                    self.k = float(values["input"])
                    c = self.k - 273.15
                    self.window["resultado"].update(f"O resultado foi {c} (Fahreinheit)")
                except:
                    self.window["resultado"].update(
                f"Digite apenas números, ou troque a vírgula do número por um ponto final (.)")

   
   

kelvin_celsius = k_c()

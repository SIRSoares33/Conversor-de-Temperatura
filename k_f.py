import PySimpleGUI as sg

class k_f:
    def __init__(self):

        theme = sg.theme('BlueMono')

        layout = [

        [sg.Text("Digite o valor de Kelvin")],
        [sg.Input(size=(10,0), key="input")],
        [sg.Text(" ", key="resultado", size=(0,1))],
        [sg.Button("Confirmar")]
        ]
        self.window = sg.Window("Kelvin para Fahreinheit", layout)

    def init_kf(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "Confirmar":

                try:
                    # Kelvin recebido pelo usuário:
                    self.k = float(values["input"])
                    f = 1.8 * (self.k - 273) + 32
                    self.window["resultado"].update(f"O resultado foi {f} (Fahreinheit)")
                except:
                    self.window["resultado"].update(
                f"Digite apenas números, ou troque a vírgula do número por um ponto final (.)")

   
   

kelvin_fahreiheit = k_f()

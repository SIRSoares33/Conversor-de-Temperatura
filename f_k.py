import PySimpleGUI as sg

class f_k:
    def __init__(self):

        theme = sg.theme('BlueMono')

        layout = [

        [sg.Text("Digite o valor de Fahreinheit")],
        [sg.Input(size=(10,0), key="input")],
        [sg.Text(" ", key="resultado", size=(0,1))],
        [sg.Button("Confirmar")]
        ]
        self.window = sg.Window("Fahreinheit para Kelvin", layout)

    def init_fk(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "Confirmar":

                try:
                    # graus Fahreinheit recebido pelo usuário:
                    self.f = float(values["input"])
                    k = (self.f + 459.67) * 5 / 9 
                    self.window["resultado"].update(f"O resultado foi {k} (Fahreinheit)")
                except:
                    self.window["resultado"].update(
                f"Digite apenas números, ou troque a vírgula do número por um ponto final (.)")

fahreiheit_kelvin= f_k()

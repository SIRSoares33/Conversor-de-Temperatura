import PySimpleGUI as sg


class f_c:
    def __init__(self):

        theme = sg.theme('BlueMono')

        layout = [

        [sg.Text("Digite o valor de Fahreinheit")],
        [sg.Input(size=(10,0), key="input")],
        [sg.Text(" ", key="resultado", size=(0,1))],
        [sg.Button("Confirmar")]
        ]
        self.window = sg.Window("Fahreinheit para Celsius", layout)

    def init_fc(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "Confirmar":

                try:
                    # graus Fahreinheit recebido pelo usuário:
                    self.f = float(values["input"])
                    c = (self.f - 32) / 1.8
                    self.window["resultado"].update(f"O resultado foi {c} (Fahreinheit)")
                except:
                    self.window["resultado"].update(
                f"Digite apenas números, ou troque a vírgula do número por um ponto final (.)")

   


fahreinheit_celsius = f_c()

import PySimpleGUI as sg
from c_f import celsius_fahreinheit
from f_c import fahreinheit_celsius
from c_k import celsius_kelvin
from k_c import kelvin_celsius
from k_f import kelvin_fahreiheit
from f_k import fahreiheit_kelvin

class interface:
    def __init__(self):
        # theme:
        theme = sg.theme('BlueMono')

        # layout:
        layout = [

        [sg.Text("Escolha a fórmula que deseja resolver", size=(30,0))], 
        [sg.Button("Celsius para Fahreinheit")],
        [sg.Button("Fahreinheit para Celsius")],
        [sg.Button("Celsius para Kelvin")],
        [sg.Button("Kelvin para Celsius")],
        [sg.Button("Kelvin para Fahreinheit")],
        [sg.Button("Fahreinheit para Kelvin")],
        [sg.Text("Para números com casas decimais troque a vírgula pelo ponto final", size=(50,0))]
        ]

        # window:
        self.window = sg.Window("Conversor de temperatura", layout)

    def iniciar(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "Celsius para Fahreinheit": # >
                celsius_fahreinheit.init_cf() 
                continue
            if event == "Fahreinheit para Celsius": # >
                fahreinheit_celsius.init_fc() 
                continue
            if event == "Celsius para Kelvin": # 
                celsius_kelvin.init_ck()
                continue
            if event == "Kelvin para Celsius": #
                kelvin_celsius.init_kc()
                continue
            if event == "Kelvin para Fahreinheit": #
                kelvin_fahreiheit.init_kf()
                continue
            if event == "Fahreinheit para Kelvin": #
                fahreiheit_kelvin.init_fk()
                continue

interface_inicial = interface()
interface_inicial.iniciar()

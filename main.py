from layout import layout
from aritméticas import *

while True:

    layout()

    formula = input('>>>').lower()

    if formula == 'c para f':
        c_f()
    elif formula == 'f para c':
        f_c()
    elif formula == 'c para k':
        c_k()
    elif formula == 'k para c':
        k_c()
    elif formula == 'k para f':
        k_f()
    elif formula == 'f para k':
        f_k()
    elif formula == 'sair':
        quit()
    else:
        continue
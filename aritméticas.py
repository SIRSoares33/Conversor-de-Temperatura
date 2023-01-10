# Celsius -> Fahrenheit:
def c_f():
    print('Digite o valor de Celsius (C)')
    c = float(input())

    f = c * 1.8 + 32
    
    print(f'F = {f}')
    
    input('press enter to pass')

# Fahrenheit -> Celsius:
def f_c():
    print('Digite o valor de Fahrenheit (F)')
    f = float(input())

    c = (f - 32) / 1.8
    
    print(f'C = {c}')

    input('press enter to pass')

# Celsius -> Kelvin
def c_k():
    print('Digite o valor de Celsius (C)')
    c = float(input())

    k = c + 273.15
    
    print(f'K = {k}')

    input('press enter to pass')

# Kelvin -> Celsius:
def k_c():
    print('Digite o valor de Kelvin (K)')
    k = float(input())

    c = k - 273.15
    
    print(f'C = {c}')

    input('press enter to pass')

# Kelvin -> Fahrenheit:
def k_f():
    print('Digite o valor de Kelvin (K)')
    k = float(input()) 

    f = 1.8 * (k - 273) + 32
     
    print(f'F = {f}')

    input('press enter to pass')

# Fahrenheit -> Kelvin:
def f_k():
    print('Digite o valor de Fahrenheit (F)')
    f = float(input())

    k = (f + 459.67) * 5 / 9 
    
    print(f'K = {k}')
    
    input('press enter to pass')
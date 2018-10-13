# ***************************************** Ejercicio **************************************************
# Diseñe una función que permita identificar si un número (que se le ingresa como parámetro de entrada) 
# es potencia de 2 y en caso afirmativo debe retornar el exponente

def findTwoPower(num):
    exponent = 0
    while num > 1 :
        num = num/2
        if num != int(num) :
            return None
        exponent = exponent + 1
    return exponent


while True :
    num = 0
    while num == 0 or num != int(num) :
        rawNum = input('Ingrese un numero entero mayor que cero: ')
        num = int(rawNum) if rawNum.isnumeric() else 0
    exponent = findTwoPower(num)
    if exponent != None :
        print('El numero es potencia de 2, el exponente es: %d' % (exponent))
    else:
        print('El numero no es potencia de 2')
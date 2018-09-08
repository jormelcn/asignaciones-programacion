# ***************************************** Ejercicio **************************************************
# Diseñar y codificar una función que tome como parámetro de entrada una cadena de caracteres y determine 
# si hay exactamente tres simbolos de interrogacion entre cada par de numeros que sumen exactamente 10

def analiceString(chain) :
    leftNumber = rightNumber = 0
    questionsCount = 0
    for char in chain :
        if char.isnumeric() :
            leftNumber = rightNumber
            rightNumber = int(char)
            if leftNumber + rightNumber == 10 and questionsCount != 3:
                return False
            questionsCount = 0
        elif char == '?' :
            questionsCount = questionsCount + 1
    return True

while True :
    chain = ''
    while len(chain) < 1 :
        chain = input('Ingrese una cadena de caracteres: ')
    print('Cumple: %s' % ( 'SI' if analiceString(chain) else 'No'))

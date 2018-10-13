
# ***************************************** Ejercicio **************************************************
# Diseñe una función que reciba como parámetro de entrada una cadena de caracteres cualquiera. 
# En particular cadenas de caracteres en las que se combinen letras con números y caracteres especiales ($%&@=!). 
# La función debe invertir el orden de los caracteres que sean exclusivamente letras, 
# los números y caracteres especiales no deben ser modificados en su posición original.


def swapAlpha(chain) :
    charList = list(chain)
    mid = int(len(charList)/2)
    end = len(charList) - 1
    for i in range(mid) :
        if charList[i].isalpha() and charList[end - i].isalpha() :
            charList[i], charList[end - i] = charList[end - i], charList[i]
        elif charList[i].isalpha() or charList[end - i].isalpha() :
            return None
    return ''.join(charList)


while True :
    chain = ''
    while len(chain) < 1 :
        chain = input('Ingrese una cadena de caracteres: ')
    swap = swapAlpha(chain)
    if swap != None :
        print('La cadena con letras invertida es: %s' % (swap))
    else:
        print('Las letras de la cadena no se pueden invertir')
    
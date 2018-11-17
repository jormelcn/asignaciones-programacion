# 1. Dados 3 enteros X, Y, Z que representan las dimensiones de un tetraedro. Y dado un número
# N. Imprima todas las posibles coordenadas dadas por (i,j,k) en una cuadricula tridimensional
# donde la suma de i+j+k no es igual a N. De modo que: 0 ≤ i ≤ X; 0 ≤ j ≤ Y; 0 ≤ k ≤ Z

def f1(X, Y, Z, N):
  return [(i, j, k) for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i + j + k != N]

print('Posibles Coordenadas: ', f1(1, 1, 1, 3))

# 2. Dada una lista de enteros separados por espacio. Determine si todos los números de la lista
# son positivos y si todos los números de la lista son números “palindromos”

def f2(nums):
  return all([num == num[::-1] for num in nums.split()])

nums = '3 565 1223221'
print('Son [%s] Palindromos? %s' % (nums, 'Si' if f2(nums) else 'No'))

# 3. Dada la siguiente lista de strings cuente cuántas veces se repite la palabra “Python” en toda
# la lista.

leest = [
  'We are learning Python', 
  'Functional programming in Python', 
  'What are this Python functions for?', 
  'Do we really need Python?', 
  'Python rulez!']

def f3(leest):
  return sum([True for string in leest for word in string.split() if 'Python' in word]) 

print('Veces que se repite Python en la lista: %d' % (f3(leest)))

# 4. ¿Cuál es la suma de los primeros 50 números positivos cuyo cuadrado es divisible por 5?

def f4(N, d):
  return sum([n for n in range(N+1) if (n**2)%d == 0])

print('Suma de los primeros 50 números positivos cuyo cuadrado es divisible por 5: %d' % (f4(50,5)))

# 5. Imprima una lista con los cubos de los primeros 30 números de Fibonacci

def fibo(n):
  if n == 1 : 
    return [1]
  elif n == 2 : 
    return [1, 1]
  else :
    f = fibo(n - 1)
    return f + [f[-1] + f[-2]]
  
print('cubos de los primeros 30 números de Fibonacci:')
print([f**3 for f in fibo(30)])

# 6. Suponga que recibe cadenas de caracteres de la siguiente forma: ‘12223311’, donde un
# carácter ‘c’ aparece consecutivamente x veces. Reemplace las ocurrencias consecutivas con
# tuplas de estilo (x, c), donde x es el número de ocurrencias y c el carácter. (Sugerencia: groupby)

def appendChar(char, grupo):
    if len(grupo) == 0:
        return  [char]
    elif char == grupo[-1][-1]:
        nuevoGrupo = grupo.copy()
        nuevoGrupo[-1] = nuevoGrupo[-1] + char 
        return nuevoGrupo
    else :
        return grupo + [char]


def groupby(chain, grupo = []):
    if len(chain) == 1:
        return appendChar(chain[0], grupo)
    else :
        return groupby(chain[1:], appendChar(chain[0], grupo))
    
recibido = '111116666677cc77777'
grupos = [(len(chain), chain[0]) for chain in groupby(recibido) ]
print('Tuplas:', grupos) 
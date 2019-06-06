'''
Esse código é uma adaptação do trecho do artigo entitulado "On the
performance of the Python programming language for serial and parallel
scientific computations" de Xing Caia,b, Hans Petter Langtangena,b
and Halvard Moea.
Seu principal objetivo é ilustrar uma array unidimensional, gerada através
de uma função trigonométrica. O método empregado para geração é o loop for
com a biblioteca numpy.
'''

import numpy as np
import time
from math import sin, cos

start = time.time()
#from Numeric import arange, zeros, Float

n = 100
dx = 1.0/(n-1)

'''cria um arranjo contendo uma sequência de valores em um intervalo com início
e fim, espaçados de maneira uniforme. De zero a 1 com espaçamentos conforme dx'''

x = np.arange(0, 1, dx)       #sequencia ([x = 0, dx, 2*dx,...])
y = np.zeros(len(x),float)    #sequencia de array unidimensional contendo zeros

for i in np.arange(len(x)):
    y[i] = sin(x[i]*cos(x[i] + x[i]**2))

end = time.time()
print('O tempo de execução do código é:',end - start)

print(x)
print(y)


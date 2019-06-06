import numpy as np
import time
start = time.time()

from math import sin, cos

n = 100
dx = 1.0/(n-1)

'''cria um arranjo contendo uma sequência de valores em um intervalo com início
e fim, espaçados de maneira uniforme. De zero a 1 com espaçamentos conforme dx'''

x = np.arange(0, 1, dx) # x = 0, dx, 2*dx, ...
y = np.sin(x)*np.cos(x) + x**2

end = time.time()
print('O tempo de execução do código é:',end - start)

print(x)
print(y)
#importar numpy para as operações com as arrays e matrizes
import numpy as np
#importar a biblioteca timeit para medição de tempo da função scheme
import timeit
import time
start = time.time()

#função scheme que retorna unew e inicielmente recebe os parâmetros
def scheme(unew, u, a, dx, dy, dz, dt):
        nx,ny,nz = u.shape
        nx -= 1 #nx = nx - 1
        ny -= 1
        nz -= 1
        dx2 = dx*dx
        dy2 = dy*dy
        dz2 = dz*dz

        for i in np.arange(1, nx):
            for j in np.arange(1, ny):
                for k in np.arange(1, nz):
                    a_c = 1.0/a[i, j, k]
                    a_ip = 2.0/(a_c + 1.0/a[i+1, j, k])
                    a_im = 2.0/(a_c + 1.0/a[i-1, j, k])
                    a_jp = 2.0/(a_c + 1.0/a[i, j+1, k])
                    a_jm = 2.0/(a_c + 1.0/a[i, j-1, k])
                    a_kp = 2.0/(a_c + 1.0/a[i, j, k+1])
                    a_km = 2.0/(a_c + 1.0/a[i, j, k-1])
                    unew[i,j,k] = u[i,j,k]+dt * \
                    ((a_ip*(u[i+1, j, k] - u[i , j, k]) - a_im*(u[i , j, k] - u[i-1, j, k]))/dx2 /
                    +(a_jp*(u[i, j+1, k] - u[i, j , k]) - a_jm*(u[i, j , k] - u[i, j-1, k]))/dy2 /
                    +(a_kp*(u[i, j, k+1] - u[i, j, k]) - a_km*(u[i, j, k] - u[i, j, k-1]))/dz2)
        return unew

u0=np.zeros((4,4,4))
#u=np.ones((6,6,6))
u=np.random.randint(5, size=(4,4,4))
a=np.ones((4,4,4))
print(u.shape)

dx=0.1;dy=0.1;dz=0.1;dt=0.01;
unew=scheme(u0, u, a, dx, dy, dz, dt)
print(unew)

#medir tempo da função (cabeçalho padrão da variável início e fim e ao centro a função com as variáveis)
inicio = timeit.default_timer()
scheme(unew, u, a, dx, dy, dz, dt)
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))

end = time.time()
print('O tempo de execução do código é:',end - start)
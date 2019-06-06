'importa as bibliotecas para arrays e medição de tempo da função'
import numpy as np
import timeit

'função com mesmos parãmetros'
def schemev(unew, u, a, dx, dy, dz, dt):
    nx, ny, nz = u.shape
    nx -= 1
    ny -= 1
    nz -= 1
    dx2 = dx*dx; dy2 = dy*dy; dz2 = dz*dz

    a_c = 1.0 / a[1:-1, 1:-1, 1:-1]
    a_ip = 2.0 / (a_c + 1.0 / a[2:, 1:-1, 1:-1])
    a_im = 2.0 / (a_c + 1.0 / a[:-2, 1:-1, 1:-1])
    a_jp = 2.0 / (a_c + 1.0 / a[1:-1, 2:, 1:-1])
    a_jm = 2.0 / (a_c + 1.0 / a[1:-1, :-2, 1:-1])
    a_kp = 2.0 / (a_c + 1.0 / a[1:-1, 1:-1, 2:])
    a_km = 2.0 / (a_c + 1.0 / a[1:-1, 1:-1, :-2])

    unew[1:-1, 1:-1, 1:-1] = u[1:-1, 1:-1, 1:-1] + dt * (
                (a_ip * (u[2:, 1:-1, 1:-1] - u[1:-1, 1:-1, 1:-1]) -
                 a_im * (u[1:-1, 1:-1, 1:-1] - u[:-2, 1:-1, 1:-1])) / dx2 +
                (a_jp * (u[1:-1, 2:, 1:-1] - u[1:-1, 1:-1, 1:-1]) - \
                 a_jm * (u[1:-1, 1:-1, 1:-1] - u[1:-1, :-2, 1:-1])) / dy2 +
                (a_kp * (u[1:-1, 1:-1, 2:] - u[1:-1, 1:-1, 1:-1]) -
                 a_km * (u[1:-1, 1:-1, 1:-1] - u[1:-1, 1:-1, :-2])) / dz2)
    return unew


u0=np.zeros((4,4,4))
u=np.random.randint(5, size=(4,4,4))
a=np.ones((4,4,4))
print(u.shape)

dx=0.1;dy=0.1;dz=0.1;dt=0.01;
unew=schemev(u0, u, a, dx, dy, dz, dt)
print(unew)

inicio = timeit.default_timer()
schemev(unew, u, a, dx, dy, dz, dt)
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
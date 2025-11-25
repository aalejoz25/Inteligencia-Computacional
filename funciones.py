import numpy as np

def trapezoidal(x, a, m, n, b):
    x = np.asarray(x)
    valor = np.zeros_like(x, dtype=float)
    if m != a:
        mascara_izq = (x >= a) & (x < m)
        valor[mascara_izq] = (x[mascara_izq] - a) / (m - a)
    else:
        mascara_izq = (x >= a) & (x <= m)
        valor[mascara_izq] = 1
    mascara_medio = (x >= m) & (x <= n)
    valor[mascara_medio] = 1
    if b != n:
        mascara_der = (x > n) & (x <= b)
        valor[mascara_der] = (b - x[mascara_der]) / (b - n)
    else:
        mascara_der = (x >= n) & (x <= b)
        valor[mascara_der] = 1
    valor[(x < a) | (x > b)] = 0
    return np.clip(valor, 0, 1)

def triangular(x, a, m, b):
    x = np.asarray(x)
    valor = np.zeros_like(x, dtype=float)
    if m != a:
        mascara_izq = (x >= a) & (x <= m)
        valor[mascara_izq] = (x[mascara_izq] - a) / (m - a)
    else:
        mascara_izq = (x == a)
        valor[mascara_izq] = 1
    if b != m:
        mascara_der = (x > m) & (x <= b)
        valor[mascara_der] = (b - x[mascara_der]) / (b - m)
    else:
        mascara_der = (x == b)
        valor[mascara_der] = 1
    valor[(x < a) | (x > b)] = 0
    return np.clip(valor, 0, 1)

def membresia_difusa(x, tipo, parametros):
    if tipo == 'triangular':
        return triangular(x, *parametros)
    elif tipo == 'trapezoidal':
        return trapezoidal(x, *parametros)
    raise ValueError('Tipo de función no soportado')
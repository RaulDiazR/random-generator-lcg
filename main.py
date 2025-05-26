import sys
from collections import defaultdict

def leer_entrada():
    entrada = sys.stdin.read().strip().split()
    x0 = int(entrada[0])
    a = int(entrada[1])
    c = int(entrada[2])
    m = int(entrada[3])
    n = int(entrada[4])
    return x0, a, c, m, n

def detectar_ciclo(x0, a, c, m):
    vistos = {}
    secuencia = []
    x = x0
    i = 0

    while x not in vistos:
        vistos[x] = i
        secuencia.append(x)
        x = (a * x + c) % m
        i += 1

    inicio_ciclo = vistos[x]
    cola = secuencia[:inicio_ciclo]
    ciclo = secuencia[inicio_ciclo:]
    periodo = cola + ciclo

    return cola, periodo, ciclo

def generar_para_estadisticas(x0, a, c, m, n):
    if n <= 0:
        return []
    secuencia = []
    x = x0
    for _ in range(n):
        secuencia.append(x)
        x = (a * x + c) % m
    return secuencia

def estadisticas(datos, m):
    n = len(datos)
    
    if n == 0:
        # Evita divisiones por cero y errores con listas vacías
        return 0.0, 0, "", 0.0, 0.0, [0.0] * 10

    # Media
    media = sum(datos) / n

    # Mediana
    sorted_vals = sorted(datos)
    mid = n // 2
    if n % 2 == 1:
        mediana = sorted_vals[mid]
    else:
        mediana = (sorted_vals[mid - 1] + sorted_vals[mid]) // 2

    # Moda
    freq = defaultdict(int)
    for x in datos:
        freq[x] += 1
    max_freq = max(freq.values())
    if max_freq == 1:
        moda = ""
    else:
        moda_vals = sorted([k for k, v in freq.items() if v == max_freq])
        moda = ', '.join(str(x) for x in moda_vals)

    # Varianza y desviación estándar
    if n > 1:
        varianza = sum((x - media) ** 2 for x in datos) / (n - 1)
        desviacion = varianza ** 0.5
    else:
        varianza = 0.0
        desviacion = 0.0

    # Porcentajes por intervalo
    normalizados = [x / m for x in datos]
    porcentajes = [0] * 10
    for x in normalizados:
        idx = min(int(x * 10), 9)
        if x == idx / 10 and idx > 0:
            idx -= 1
        porcentajes[idx] += 1
    porcentajes = [(c / n) * 100 for c in porcentajes]

    return media, mediana, moda, desviacion, varianza, porcentajes

def main():
    x0, a, c, m, n = leer_entrada()
    cola, periodo, ciclo = detectar_ciclo(x0, a, c, m)
    datos_estadistica = generar_para_estadisticas(x0, a, c, m, n)

    media, mediana, moda, desviacion, varianza, porcentajes = estadisticas(datos_estadistica, m)
    print(', '.join(str(x) for x in cola))
    print(', '.join(str(x) for x in periodo))
    print(', '.join(str(x) for x in ciclo))
    print(len(cola))
    print(len(periodo))
    print(len(ciclo))
    print(f"{media:.6f}")
    print(mediana)
    print(moda)
    print(f"{desviacion:.6f}")
    print(f"{varianza:.6f}")
    
    for porcentaje in porcentajes:
        print(f"{porcentaje:.2f}%")

if __name__ == "__main__":
    main()

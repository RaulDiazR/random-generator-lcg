import sys

def leer_entrada():
    entrada = sys.stdin.read().strip().split()
    x0 = int(entrada[0])
    a = int(entrada[1])
    c = int(entrada[2])
    m = int(entrada[3])
    n = int(entrada[4])
    return x0, a, c, m, n

def generar_congruencial(x0, a, c, m, n):
    vistos = {}
    secuencia = []
    x = x0

    for i in range(n):
        if x in vistos:
            break
        vistos[x] = i
        secuencia.append(x)
        x = (a * x + c) % m

    # Detectar cola y ciclo
    if x in vistos:
        i = vistos[x]
        cola = secuencia[:i]
        periodo = secuencia[i:]
    else:
        cola = []
        periodo = secuencia

    ciclo = cola + periodo
    return cola, periodo, ciclo

def estadisticas(ciclo, m):
    normalizados = [x / m for x in ciclo]
    n = len(normalizados)

    # Media
    media = sum(normalizados) / n

    # Mediana
    sorted_vals = sorted(ciclo)
    mid = n // 2
    mediana = sorted_vals[mid] if n % 2 == 1 else (sorted_vals[mid - 1] + sorted_vals[mid]) // 2

    # Moda
    frecuencias = {}
    for x in ciclo:
        frecuencias[x] = frecuencias.get(x, 0) + 1
    max_freq = max(frecuencias.values())
    if max_freq == 1:
        moda = "no hay moda"
    else:
        moda = ', '.join(str(k) for k in sorted([k for k, v in frecuencias.items() if v == max_freq]))

    # Varianza y desviación estándar muestral
    varianza = sum((x - media) ** 2 for x in normalizados) / (n - 1)
    desviacion = varianza ** 0.5

    # Porcentajes en intervalos [0.0, 0.1), ..., (0.9, 1.0]
    porcentajes = [0] * 10
    for x in normalizados:
        idx = min(int(x * 10), 9)
        porcentajes[idx] += 1
    porcentajes = [(c / n) * 100 for c in porcentajes]

    return media, mediana, moda, desviacion, varianza, porcentajes

def imprimir_resultados(cola, periodo, ciclo, media, mediana, moda, desviacion, varianza, porcentajes):
    print("cola = " + ', '.join(str(x) for x in cola))
    print("periodo = " + ', '.join(str(x) for x in periodo))
    print("ciclo = " + ', '.join(str(x) for x in ciclo))
    print("longitud de cola = " + str(len(cola)))
    print("longitud de periodo = " + str(len(periodo)))
    print("longitud de ciclo = " + str(len(ciclo)))
    print(f"media = {media:.6f}")
    print(f"mediana = {mediana}")
    print(f"moda = {moda}")
    print(f"desviación estándar = {desviacion:.6f}")
    print(f"varianza = {varianza:.6f}")

    for i, porcentaje in enumerate(porcentajes):
        a = i / 10
        b = (i + 1) / 10
        print(f"porcentaje en ({a:.1f} < x <= {b:.1f}) = {porcentaje:.2f}%")

def main():
    x0, a, c, m, n = leer_entrada()
    cola, periodo, ciclo = generar_congruencial(x0, a, c, m, n)
    media, mediana, moda, desviacion, varianza, porcentajes = estadisticas(ciclo, m)
    imprimir_resultados(cola, periodo, ciclo, media, mediana, moda, desviacion, varianza, porcentajes)

if __name__ == "__main__":
    main()

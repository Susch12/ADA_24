#!/usr/bin/env python3

import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    "Ascendente": {
        "Quicksort": [1.811981201171875e-05, 6.151199340820312e-05, 0.0004928112030029297, 0.007733821868896484, 0.07833528518676758],
        "Burbuja": [5.7220458984375e-06, 0.00012087821960449219, 0.012926340103149414, 1.44073486328125, 139.73975467681885]
    },
    "Descendente": {
        "Quicksort": [5.7220458984375e-06, 4.8160552978515625e-05, 0.0005817413330078125, 0.006435871124267578, 0.0785212516784668],
        "Burbuja": [4.5299530029296875e-06, 0.0002880096435546875, 0.029683828353881836, 3.1967051029205322, 367.33529019355774]
    },
    "Random": {
        "Quicksort": [7.152557373046875e-06, 7.62939453125e-05, 0.010535955429077148, 0.011089086532592773, 0.22864079475402832],
        "Burbuja": [3.814697265625e-06, 0.00020456314086914062, 2.425377368927002, 2.513603925704956, 307.5848286151886]
    }
}

# Tamaños de las listas
tamaños = [10, 100, 1000, 10000, 100000]

# Graficar
for tipo in data.keys():
    plt.figure(figsize=(10, 5))
    plt.title(f"Comparación de Quicksort y Burbuja para listas {tipo}")
    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo de ejecución (segundos)")
    
    for algoritmo, tiempos in data[tipo].items():
        plt.plot(tamaños, tiempos, marker='o', label=algoritmo)
    
    plt.xscale('log')  # Escala logarítmica en el eje x para mejor visualización
    plt.yscale('log')  # Escala logarítmica en el eje y para mejor visualización
    plt.xticks(tamaños, tamaños)
    plt.legend()
    plt.grid(True)
    plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 08:52:38 2025

@author: camic
"""

# Problema de la Mochila Fraccional - Algoritmo Voraz (Greedy)

def mochila_fraccional(objetos, capacidad):
    # Calculamos valor por unidad de peso y ordenamos de mayor a menor
    objetos.sort(key=lambda x: x['valor'] / x['peso'], reverse=True)

    peso_actual = 0
    valor_total = 0
    combinacion = []

    for obj in objetos:
        if peso_actual + obj['peso'] <= capacidad:
            # Tomamos el objeto completo
            peso_actual += obj['peso']
            valor_total += obj['valor']
            combinacion.append({
                'objeto': obj['nombre'],
                'fraccion': 1,
                'peso_tomado': obj['peso'],
                'valor_tomado': obj['valor']
            })
        else:
            # Tomamos solo la fracción que cabe
            fraccion = (capacidad - peso_actual) / obj['peso']
            valor_total += obj['valor'] * fraccion
            peso_actual += obj['peso'] * fraccion
            combinacion.append({
                'objeto': obj['nombre'],
                'fraccion': round(fraccion, 2),
                'peso_tomado': round(obj['peso'] * fraccion, 2),
                'valor_tomado': round(obj['valor'] * fraccion, 2)
            })
            break  # la mochila se llenó

    return valor_total, combinacion


# --- Datos del problema ---
objetos = [
    {'nombre': 'A', 'peso': 10, 'valor': 60},
    {'nombre': 'B', 'peso': 20, 'valor': 100},
    {'nombre': 'C', 'peso': 30, 'valor': 120}
]

capacidad = 50

# --- Ejecución ---
valor_maximo, combinacion_optima = mochila_fraccional(objetos, capacidad)

# --- Resultados ---
print("🔸 Combinación óptima que maximiza el valor total 🔸\n")
for item in combinacion_optima:
    print(f"Objeto {item['objeto']}: {item['fraccion']*100:.0f}% tomado "
          f"({item['peso_tomado']} kg, {item['valor_tomado']} monedas de oro)")

print(f"\n✅ Valor total máximo: {valor_maximo:.2f} monedas de oro")
print(f"⚖️ Peso total usado: {sum(x['peso_tomado'] for x in combinacion_optima):.2f} kg")

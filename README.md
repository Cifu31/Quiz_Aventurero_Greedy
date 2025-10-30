# 🧭 Problema de la Mochila Fraccional (Algoritmo Voraz en Python)

Este programa resuelve el **problema de la mochila fraccional** utilizando un **algoritmo voraz (greedy)**.  
El objetivo es **maximizar el valor total** de los objetos colocados en una mochila **sin exceder su capacidad máxima de peso**.

---

## 🎯 Objetivo del problema

Un aventurero tiene una mochila que puede soportar hasta **50 kg** y encuentra los siguientes objetos:

| Objeto | Peso (kg) | Valor (monedas de oro) |
|:-------|:-----------|:-----------------------|
| A | 10 | 60 |
| B | 20 | 100 |
| C | 30 | 120 |

Debe decidir **qué objetos tomar** (o qué fracción de ellos) para **maximizar el valor total** sin superar el límite de peso.

---

## ⚙️ Cómo funciona el algoritmo

El algoritmo sigue un **enfoque voraz (greedy)**, que consiste en tomar siempre la **mejor opción local** en cada paso:

1. **Calcular el valor por unidad de peso** de cada objeto  
   \[
   \text{valor/peso} = \frac{\text{valor}}{\text{peso}}
   \]
   Esto indica cuántas monedas de oro aporta cada kilogramo.

2. **Ordenar los objetos de mayor a menor valor/peso.**

3. **Agregar objetos completos** mientras haya capacidad disponible.

4. Si un objeto no cabe completo, **tomar solo la fracción que cabe** en la mochila.

5. **Calcular el valor total** obtenido con la combinación seleccionada.

---

## 💻 Ejecución del código

### 🔸 Requisitos
- Python 3 instalado (versión 3.7 o superior).

### 🔸 Ejecución
Guarda el siguiente código en un archivo llamado `mochila_fraccional.py` y ejecútalo desde tu terminal:


```bash
Quiz_Aventurero_Greedy.py
def mochila_fraccional(objetos, capacidad):
    objetos.sort(key=lambda x: x['valor'] / x['peso'], reverse=True)

    peso_actual = 0
    valor_total = 0
    combinacion = []

    for obj in objetos:
        if peso_actual + obj['peso'] <= capacidad:
            peso_actual += obj['peso']
            valor_total += obj['valor']
            combinacion.append({
                'objeto': obj['nombre'],
                'fraccion': 1,
                'peso_tomado': obj['peso'],
                'valor_tomado': obj['valor']
            })
        else:
            fraccion = (capacidad - peso_actual) / obj['peso']
            valor_total += obj['valor'] * fraccion
            peso_actual += obj['peso'] * fraccion
            combinacion.append({
                'objeto': obj['nombre'],
                'fraccion': round(fraccion, 2),
                'peso_tomado': round(obj['peso'] * fraccion, 2),
                'valor_tomado': round(obj['valor'] * fraccion, 2)
            })
            break

    return valor_total, combinacion

# lap_timer.py
# Libreria de funciones para registrar tiempos de vuelta en una carrera.
#
# Estructura del diccionario (timer):
#   - 'max':   numero maximo de vueltas permitidas (int)
#   - 'times': lista con los tiempos de cada vuelta (list)
#   - 'total': tiempo acumulado de todas las vueltas (float)


import itertools


def init(max_laps):
    return {
        'max': max_laps,
        'times': [],
        'total': 0.0
    }

def add_lap(timer, time):
    timer['times'].append(time)
    timer['total'] += time
    return timer


def count(timer):
    return len(timer['times'])
    pass


def cumulative_time(timer):
    return timer['total']
    pass


def format_laps(timer):
   return str(timer['times'])
   pass


def fastest_lap(timer):
    return min(timer['times'])
    pass


def fastest_multi_lap(timer, k):
    return sum(sorted(timer['times'])[:k])
    pass


def longest_decreasing_streak(timer):
    return max(len(list(group)) for _, group in itertools.groupby(timer['times'], lambda x: x < 0))
    pass


def main():
    # crear un cronometro para el record mundial de 100m de Usain Bolt,
    # dividiendo la carrera en 10 segmentos (o "vueltas")
    timer = init(10)
    timer = add_lap(timer, 1.85)
    timer = add_lap(timer, 1.02)
    timer = add_lap(timer, 0.91)
    timer = add_lap(timer, 0.87)
    timer = add_lap(timer, 0.85)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.83)
    timer = add_lap(timer, 0.90)

    # imprimir estadisticas
    print("numero de vueltas =", count(timer))                    # 10
    print("tiempo acumulado =", cumulative_time(timer))           # 9.69
    print("vuelta mas rapida =", fastest_lap(timer))              # 0.82
    print("50m mas rapidos =", fastest_multi_lap(timer, 5))       # 4.14
    print("racha mas larga =", longest_decreasing_streak(timer))  # 6

    # imprimir tiempos
    # [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.9]
    print(format_laps(timer))


if __name__ == "__main__":
    main()

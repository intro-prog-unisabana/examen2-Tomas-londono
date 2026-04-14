# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    name = input("Ingrese el nombre del archivo: ")
    
    with open(name, 'r') as f:
        n = int(f.readline().strip())
        timer = lap_timer.init(n)

        for _ in range(n):
            time = float(f.readline().strip())
            timer = lap_timer.add_lap(timer, time)
    
    print("Tiempos de vuelta:", lap_timer.longest_decreasing_streak(timer))
    
    pass

if __name__ == "__main__":
    main()

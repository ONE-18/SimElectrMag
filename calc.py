import numpy as np
import matplotlib.pyplot as plt
from clases.pnts import CargaPuntual

def ley_de_coulomb():
    print("Simulación de la Ley de Coulomb")
    q1 = float(input("Ingrese la carga q1 (en C): "))
    q2 = float(input("Ingrese la carga q2 (en C): "))
    r = float(input("Ingrese la distancia entre las cargas (en m): "))
    k = 8.99e9  # Constante de Coulomb en N·m²/C²
    F = k * (q1 * q2) / r**2
    print(f"La fuerza entre las cargas es: {F:.2e} N")

def ley_de_gauss():
    print("Simulación de la Ley de Gauss")
    q = float(input("Ingrese la carga encerrada (en C): "))
    epsilon_0 = 8.85e-12  # Permisividad eléctrica del vacío en F/m
    E = q / epsilon_0
    print(f"El flujo eléctrico es: {E:.2e} N·m²/C")

def ley_de_faraday():
    print("Simulación de la Ley de Faraday")
    print("Se calculará la FEM inducida en función de la variación del flujo magnético.")
    delta_flux = float(input("Ingrese el cambio en el flujo magnético (en Wb): "))
    delta_t = float(input("Ingrese el intervalo de tiempo (en s): "))
    fem = -delta_flux / delta_t
    print(f"La FEM inducida es: {fem:.2e} V")

def cargas_puntuales():
    print("Simulación de Cargas Puntuales")
    k = 1/(4*np.pi*8.85e-12)  # Constante de Coulomb en N·m²/C²

    # Ingreso de datos
    cargas = []
    if input("Desea ingresar las cargas manualmente? [s/n]: ") == "s":
        while(len(cargas)<1 or input("Desea agregar otra carga? [s/n]: ") != "n"):
            x, y = input("Ingrese la posición x, y [m]: ").split(",")
            q = float(input("Ingrese la carga [C]: "))
            cargas.append(CargaPuntual(q, float(x), float(y)))
    else:
        with open("cargasPnt.txt", "r") as f:
            for line in f:
                if line == "\n" or line[0] == "#":
                    continue
                x, y, q = line.split(",")
                cargas.append(CargaPuntual(float(q), float(x), float(y)))    
    
    # Manual fuerza eléctrica
    for _, carga in enumerate(cargas):
        fuerza_total_x = 0
        fuerza_total_y = 0
        for c in cargas:
            if c != carga:
                r = np.sqrt((carga.x - c.x)**2 + (carga.y - c.y)**2)
                fuerza = k * c.q / r**2
                fuerza_x = fuerza * (c.x - carga.x) / r
                fuerza_y = fuerza * (c.y - carga.y) / r
                fuerza_total_x += fuerza_x
                fuerza_total_y += fuerza_y
        fuerza_electr = np.sqrt(fuerza_total_x**2 + fuerza_total_y**2)
        print(f"La fuerza eléctrica sobre la carga {_} C es: {fuerza_electr:.2e} N en la dirección ({fuerza_total_x:.2e} i, {fuerza_total_y:.2e} j)")

    # Gráfica
    if input("Desea graficar el campo eléctrico? [s/n]: ") == "s":
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)
        Ex = np.zeros_like(X)
        Ey = np.zeros_like(Y)
        for carga in cargas:
            r = np.sqrt((X - carga.x)**2 + (Y - carga.y)**2)
            Ex += k * carga.q * (X - carga.x) / r**3
            Ey += k * carga.q * (Y - carga.y) / r**3

        plt.streamplot(X, Y, Ex, Ey)
        size_norm = np.array([abs(carga.q) for carga in cargas])
        plt.scatter([carga.x for carga in cargas], [carga.y for carga in cargas], s=[abs(carga.q)*100 for carga in cargas] / size_norm, c=[carga.q for carga in cargas])
        plt.show()      

def menu():
    t = True
    while t:
        print("\n--- Simulaciones Electromagnetismo ---")
        print("1. Cargas Puntuales")
        # print("1. Ley de Coulomb")
        # print("2. Ley de Gauss")
        # print("3. Ley de Faraday")
        print("x. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
             cargas_puntuales()
             t = False
        elif opcion == "x":
            t = False
            print("Saliendo...")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
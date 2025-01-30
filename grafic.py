import numpy as np
import matplotlib.pyplot as plt

def campo_electrico(q, r0, x, y):
    """
    Calcula el campo eléctrico debido a una carga q en la posición r0
    para un punto (x, y) en el plano.
    """
    k = 8.99e9  # Constante de Coulomb en N·m²/C²
    rx, ry = x - r0[0], y - r0[1]
    r = np.sqrt(rx**2 + ry**2)
    r[r == 0] = 1e-10  # Evitar divisiones por cero
    E = k * q / r**2
    Ex, Ey = E * (rx / r), E * (ry / r)
    return Ex, Ey

def graficar_campo():
    # Parámetros
    q1, q2 = 1e-9, -1e-9  # Cargas en Coulombs
    r1, r2 = (-0.5, 0), (0.5, 0)  # Posiciones de las cargas

    # Generar una cuadrícula
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)

    # Calcular el campo eléctrico de ambas cargas
    Ex1, Ey1 = campo_electrico(q1, r1, X, Y)
    Ex2, Ey2 = campo_electrico(q2, r2, X, Y)

    # Sumar los campos
    Ex, Ey = Ex1 + Ex2, Ey1 + Ey2

    # Crear el gráfico
    plt.figure(figsize=(8, 8))
    plt.streamplot(X, Y, Ex, Ey, color=np.sqrt(Ex**2 + Ey**2), cmap='viridis', linewidth=1)
    plt.scatter([r1[0], r2[0]], [r1[1], r2[1]], c=['red', 'blue'], s=100, label="Cargas")
    plt.text(r1[0], r1[1] + 0.1, "+q", color="red", fontsize=12, ha="center")
    plt.text(r2[0], r2[1] + 0.1, "-q", color="blue", fontsize=12, ha="center")
    plt.title("Campo Eléctrico de Dos Cargas Puntuales")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.axis("equal")
    plt.colorbar(label="Magnitud del Campo (N/C)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Ejecutar la gráfica
    graficar_campo()

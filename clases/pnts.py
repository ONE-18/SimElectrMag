class CargaPuntual:
    def __init__(self, q, x, y):
        self.q = q
        self.x = x
        self.y = y

    def __str__(self):
        return f'Carga_Puntual(k={self.q}, x={self.x}, y={self.y})'

    def __repr__(self):
        return f'Carga_Puntual(k={self.q}, x={self.x}, y={self.y})'

    def __eq__(self, other):
        return self.q == other.q and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.q, self.x, self.y))

    def __lt__(self, other):
        return self.q < other.q

    def __le__(self, other):
        return self.q <= other.q

    def __gt__(self, other):
        return self.q > other.q

    def __ge__(self, other):
        return self.q >= other.q

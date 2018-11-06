# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math
class triangle:
    def _init_(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        def _side1(topA, topB):
            return math.sqrt((topA[0] - topB[0]) ** 2 + (topA[1] - topB[1]) ** 2)
        def _side2(topB, topC):
            return math.sqrt((topB[0] - topC[0]) ** 2 + (topB[1] - topC[1]) ** 2)
        def _side3(topC, topA):
            return math.sqrt((topC[0] - topA[0]) ** 2 + (topC[1] - topA[1]) ** 2)

        self.AB = _side1(self.A, self.B)
        self.BC = _side2(self.B, self.C)
        self.CA = _side3(self.C, self.A)
#площадь (по формуле Герона)
    def areaABC(self):
        perimABC = self.perim(0) ** 0.5
        return math.sqrt (perimABC * (perimABC - self.AB) * (perimABC - self.BC) * (perimABC - self.CA))

#высота треугольника

    def altitudeABC(self):
        altitude = self.areaABC (0) / (self.AB [0] ** 0.5)
        return altitude

#периметр

    def perimABC(self):
        perim = self.AB [0] + self.BC [1] + self.CA [2]
        return perim

ABC = triangle((1, 2), (3, 5), (4, 1))

print(ABC.areaABC())
print(ABC.altitudeABC())
print(ABC.perimABC())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


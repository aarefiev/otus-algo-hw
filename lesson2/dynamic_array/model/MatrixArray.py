from model import *


class MatrixArray(IArray):
    def __init__(self, vector: int = 10):
        self.array = SingleArray()
        self.vector = vector
        self._size = 0

    def size(self) -> int:
        return self._size

    def add(self, item) -> None:
        if self._size == self.array.size() * self.vector:
            self.array.add(VectorArray(self.vector))

        self.array.get(int(self._size / self.vector)).add(item)
        self._size += 1

    def get(self, index: int):
        return self.array.get(int(index / self.vector)).get(index % self.vector)
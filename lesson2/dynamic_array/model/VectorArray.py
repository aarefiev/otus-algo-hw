from model import IArray


class VectorArray(IArray):
    def __init__(self, vector = 10):
        self.array = []
        self.vector = vector
        self._size = 0

    def size(self) -> int:
        return self._size

    def add(self, item) -> None:
        if self._size == len(self.array):
            self.resize()
        self.array[self._size] = item
        self._size += 1

    def get(self, index: int):
        return self.array[index]

    def resize(self) -> None:
        new_array = [None] * (len(self.array) + self.vector)
        index = 0
        total = len(self.array)

        while index < total:
            new_array[index] = self.array[index]
            index += 1

        self.array = new_array

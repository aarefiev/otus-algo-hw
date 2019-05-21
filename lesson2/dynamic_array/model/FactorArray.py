from model import IArray


class FactorArray(IArray):
    def __init__(self, factor: int = 50, init_length: int = 10):
        self.array = [None] * init_length
        self.factor = factor
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
        array_length = len(self.array)
        new_array = [None] * (array_length + int(array_length * self.factor / 100))
        index = 0

        while index < array_length:
            new_array[index] = self.array[index]
            index += 1

        self.array = new_array

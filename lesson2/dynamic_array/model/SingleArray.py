from model import IArray


class SingleArray(IArray):
    def __init__(self):
        self.array = []

    def size(self) -> int:
        return len(self.array)

    def add(self, item) -> None:
        self.resize()
        self.array[self.size() - 1] = item

    def get(self, index: int):
        return self.array[index]

    def resize(self) -> None:
        new_array = [None] * (self.size() + 1)
        index = 0
        total = self.size()

        while index < total:
            new_array[index] = self.array[index]
            index += 1

        self.array = new_array

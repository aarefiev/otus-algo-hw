from abc import ABCMeta, abstractmethod

class IArray:
    __metaclass__ = ABCMeta

    @abstractmethod
    def size(self) -> int:
        """Размер массива"""

    @abstractmethod
    def add(self, item) -> None:
        """Добавить элемент в массив"""

    @abstractmethod
    def get(self, index: int):
        """Получить элемент из массива по индексу"""

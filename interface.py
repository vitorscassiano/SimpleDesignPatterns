from abc import ABC, abstractmethod
from typing import List


class IHello(ABC):
    @abstractmethod
    def hello(self, word: str, bla: List):
        pass


class Hello(IHello):
    def hello(self, word):
        print(f"Hello {word}!")
        pass


# Main
Hello().hello("World")

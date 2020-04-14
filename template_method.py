from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.first()
        self.second()
        self.third()

    @abstractmethod
    def first(self):
        print("First")

    def second(self):
        print("Second")

    def third(self):
        print("Third")


class ConcreteClass(Abstract):
    def third(self):
        print("Other third")


if __name__ == "__main__":
    concrete = ConcreteClass()
    concrete.template_method()

from __future__ import annotations
from abc import ABC, abstractmethod


class Facade():
    def __init__(self, systemA: ConcreteSystemA, systemB: ConcreteSystemB):
        self._subsystemA = systemA or ConcreteSystemA()
        self._subsystemB = systemB or ConcreteSystemB()

    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystemA.operation1())
        results.append(self._subsystemB.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystemA.operation_n())
        results.append(self._subsystemB.operation_z())
        return "\n".join(results)


class ConcreteSystemA():
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class ConcreteSystemB():
    def operation1(self):
        return "Subsystem2: Get ready!"

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client(facade: Facade):
    print(facade.operation(), end="")


if __name__ == "__main__":
    systemA = ConcreteSystemA()
    systemB = ConcreteSystemB()
    facade = Facade(systemA, systemB)
    client(facade)

from abc import ABC, abstractmethod


class AbstractClass():
    def template_method(self) -> None:
        self.first_operation()
        self.required_operation_A()
        self.second_operation()
        self.hookA()
        self.required_operation_B()
        self.third_operation()
        self.hookB()

    def first_operation(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def second_operation(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def third_operation(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operation_A(self) -> None:
        pass

    @abstractmethod
    def required_operation_B(self) -> None:
        pass

    def hookA(self) -> None:
        pass

    def hookB(self) -> None:
        pass


class ConcreteClassA(AbstractClass):
    def required_operation_A(self):
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operation_B(self):
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClassB(AbstractClass):
    def required_operation_A(self):
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operation_B(self):
        print("ConcreteClass2 says: Implemented Operation2")

    def hookA(self):
        print("ConcreteClass2 says: Overridden Hook1")


def client(abstract: AbstractClass) -> None:
    abstract.template_method()

if __name__ == "__main__":
    concreteA = ConcreteClassA()
    client(concreteA)
    print("-------------------------------------")

    concreteB = ConcreteClassB()
    client(concreteB)

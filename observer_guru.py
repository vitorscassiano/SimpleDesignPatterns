from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):  # Notifier Interface
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):  # Notifier Implementation
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject attached an observer")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("Subject dettached an observer")
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Notifie list of observers")
        for observer in self._observers:
            observer.update(self)

    def business_logic(self) -> None:
        self._state = randrange(0, 10)
        self.notify()


class Observer(ABC):  # Observer Interface

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteObserverA(Observer):  # Observer Implementation
    def update(self, subject):
        if subject._state < 3:
            print("[ConcreteObserverA] React to an event")


class ConcreteObserverB(Observer):  # Observer Implementation
    def update(self, subject):
        if subject._state is 0 or subject._state >= 2:
            print("[ConcreteObserverB] React to an event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.business_logic()
    subject.business_logic()

    subject.detach(observer_a)

    subject.business_logic()

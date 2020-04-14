class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, *subscribers):
        for subscriber in subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, *subscribers):
        for subscribe in subscribers:
            self.subscribers.remove(subscribe)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update()


class Subscriber1():
    def update(self):
        print("subscriber1")


class Subscriber2():
    def update(self):
        print("subscriber2")


class Subscriber3():
    def update(self):
        print("subscriber3")


if __name__ == "__main__":
    publisher = Publisher()

    sub1 = Subscriber1()
    sub2 = Subscriber2()
    sub3 = Subscriber3()
    publisher.subscribe(sub1, sub2, sub3)

    publisher.notify()

    publisher.unsubscribe(sub2)
    publisher.notify()

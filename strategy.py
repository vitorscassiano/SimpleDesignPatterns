class RouteStrategy():
    def execute(self, sign: str, a: int, b: int):
        if sign is "+":
            return Plus().execute(a, b)
        elif sign is "-":
            return Minus().execute(a, b)
        elif sign is "*":
            return Multiply().execute(a, b)
        elif sign is "/":
            return Divide().execute(a, b)
        else:
            return


class Plus():
    def execute(self, a: int, b: int):
        return a + b


class Minus():
    def execute(self, a: int, b: int):
        return a - b


class Multiply():
    def execute(self, a: int, b: int):
        return a * b


class Divide():
    def execute(self, a: int, b: int):
        return a / b


if __name__ == "__main__":
    strategy = RouteStrategy()
    solution1 = strategy.execute("+", 1, 2)
    solution2 = strategy.execute("/", 1, 2)
    print(solution1)
    print(solution2)

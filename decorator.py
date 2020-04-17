from functools import wraps
from typing import Callable


def decorator(f: Callable):
    def wrapper(*args, **kwargs) -> None:
        print("Before")
        msg = f(args[0])
        print(msg)
        print("After")
    return wrapper

@decorator
def hello(name: str) -> str:
    return f"Hello {name}!"


# Main
if __name__ == "__main__":
    hello("Vitor")
from typing import Callable, List


class Obseverable:
    handlers: List = []

    def __init__(self, number: int):
        self.number = number

    def create_handlers(self, callback: Callable) -> List[Callable]:
        for step in range(self.number):
            self.handlers.append(lambda: callback())
        return self.handlers

    @staticmethod
    def execute_handlers(handlers: List[Callable]) -> None:
        for handler in handlers:
            handler()


if __name__ == '__main__':
    obsever = Obseverable(5)

    def func() -> None:
        print('Hello World')

    obsever.create_handlers(func)
    print(obsever.execute_handlers(obsever.handlers))

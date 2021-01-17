import threading

class Foo:
    def __init__(self):
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        for thread in threading.enumerate():
            if thread.name == 'first':
                thread.join()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

    def third(self, printThird: 'Callable[[], None]') -> None:
        for thread in threading.enumerate():
            if thread.name == 'second':
                thread.join()

        # printThird() outputs "third". Do not change or remove this line.
        printThird()

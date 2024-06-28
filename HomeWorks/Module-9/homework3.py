class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        current = self.i
        if self.i < self.end:
            self.i += 2
            return current
        else:
            raise StopIteration


if __name__ == '__main__':
    en = EvenNumbers(10, 25)
    for i in en:
        print(i)

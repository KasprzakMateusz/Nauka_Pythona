class Function:
    def __init__(self, earnings_one, earnings_two, expenses):
        self.ear_one = earnings_one
        self.ear_two = earnings_two
        self.exp = expenses
        self._check()

    def _check(self):
        if self.ear_one > self.ear_two:
            division = self.ear_two / self.ear_one
        elif self.ear_one < self.ear_two:
            division = self.ear_one / self.ear_two
        else:
            print(f'Musicie zapłacić po równo! \nPo: {self.exp / 2} zł')
            exit()
        return division

    def calc1(self):
        percent = self._check()
        s = self.ear_one * (1 - percent)
        return s

    def calc2(self):
        percent = self._check()
        s = percent * self.ear_two
        return s


x = Function(3500, 2100, 2100)
print(x.calc1())
print(x.calc2())





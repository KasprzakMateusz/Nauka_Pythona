class Function:
    def __init__(self, earnings_one, earnings_two, expenses):
        self.ear_one = earnings_one
        self.ear_two = earnings_two
        self.exp = expenses
        self._percent()

    def _percent(self):
        ear = self.ear_one + self.ear_two
        self.ear1 = self.ear_one / ear
        self.ear2 = self.ear_two / ear

    def first_person(self):
        xs = self.exp * self.ear1
        return xs

    def second_person(self):
        xs = self.exp * self.ear2
        return xs


# x = Function(3500, 3400, 2100)
# print(x.first_person())
# print(x.second_person())





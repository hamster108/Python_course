class fibonacci_sequence:
    def __init__(self, number):
        self.number = number
        self.lst = []
        self.first_digit = 1
        self.second_digit = 1

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lst) != self.number:
            remember_digit = self.second_digit
            self.second_digit = self.first_digit + self.second_digit
            self.lst.append(self.first_digit)
            self.first_digit = remember_digit
            return self.lst[-1]
        else:
            raise StopIteration

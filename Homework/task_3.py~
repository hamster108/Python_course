class fibonacci_sequence:
    def __init__(self, number):
        self.number = number
        self.first_digit = 0
        self.second_digit = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.number:
            remember_digit = self.second_digit
            self.second_digit = self.first_digit + self.second_digit           
            self.first_digit = remember_digit
            self.count += 1
            return remember_digit
            
        else:
            raise StopIteration

class main:
    def __init__(self):
        self.condition = 'A'

    def loop(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'B':
            self.condition = 'C'
            return 1
        elif self.condition == 'D':
            self.condition = 'E'
            return 4
        elif self.condition == 'F':
            self.condition = 'F'
            return 8
        else:
            raise KeyError

    def check(self):
        if self.condition == 'B':
            self.condition = 'B'
            return 2
        elif self.condition == 'C':
            self.condition = 'D'
            return 3
        elif self.condition == 'E':
            self.condition = 'F'
            return 6
        elif self.condition == 'F':
            self.condition = 'A'
            return 7
        elif self.condition == 'D':
            self.condition = 'A'
            return 5
        else:
            raise KeyError

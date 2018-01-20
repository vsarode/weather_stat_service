class CalCulator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def mul(self, num1, num2):
        return num1 * num2

    def sub(self, num1, num2):
        return num1 - num2

    def div(self, num1, num2):
        return num1 / num2


if __name__ == "__main__":
    c = CalCulator(10, 20)
    c.add()
    print c.mul(10, 20)

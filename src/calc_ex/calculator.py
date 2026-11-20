class Calculator:
    def __init__(self, op1: float, op2: float):
       self.op1 = op1
       self.op2 = op2
    def sum(op1: float, op2: float):
        return op1 + op2
    def sub(op1: float, op2: float):
        return op1 - op2
    def multiply(op1: float, op2: float):
        return op1 * op2
    def div(op1: float, op2: float):
        if op2 == 0:
            raise TypeError("Cannot divide by 0")
        return op1 / op2

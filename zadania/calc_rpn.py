class Expression():
    def __init__(self,expr):
        self.expr = expr
    def evaluate(self,stack):
        pass
class Add(Expression):
    def evaluate(self, stack):
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
class Sub(Expression):
    def sub():
        pass
class Print(Expression):
    def evaluate(self,stack):
        print(stack[-1])
class Integer(Expression):
    def evaluate(self, stack):
        stack.append(int(self.expr))
def evaluate(ops,stack):
    for each in ops:
        each.evaluate(stack)
stack = []

while True:
    ops = []
    expr = input()
    for each in expr.split():
        if each.isdigit():
            ops.append(Integer(each))
        elif each == '+':
            ops.append(Add(each))
        elif each == '-':
            ops.append(Sub(each))
        elif each == 'p':
            ops.append(Print(each))
        else:
            exit(1)
    evaluate(ops,stack)
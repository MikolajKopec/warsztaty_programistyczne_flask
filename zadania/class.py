class Basic:
    def __init__(self, field):
        self.field = field
    def __str__(self):
        return "basic: {x}".format(x=self.field)
    def __gt__(self,other):
        return self.field>other.field
    def print_field(self):
        print(self.field)
def print_field(x):
    print(x.field)
b = Basic(42)
c = Basic(100)

print(b)
b.print_field()
print_field(b)
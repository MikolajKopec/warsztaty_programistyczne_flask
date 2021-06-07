class Hello:
    def __init__(self,greeting = "Hello"):
        self.greeting=greeting
    def great(self,person):
        return print("{} {}".format(self.greeting,person))


def hello(person,greeting = "Hello"):
    return print("{} {}".format(greeting,person))
new = Hello("Yo")
new.great("me")
hello("me","yo")

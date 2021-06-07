class Swimmer():
    def swim(self):
        print("{} swims".format(self))
    def talk(self):
        print("something")
class Quaker():
    def talk(self):
        print("quak")
    def quak(self):
        print("{} quaks".format(self))
        self.swim()
class Duck(Quaker,Swimmer):
    pass
s = Swimmer()
q = Quaker()
s.swim()
#q.quak()
d = Duck()
d.swim()
d.quak()
d.talk()
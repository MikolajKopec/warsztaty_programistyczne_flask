class Shape:
    def __init__(self,n = None):
        self.n = n
    
    def draw(self,n = None):
        if n is None:
            n = self.n
        for i in range(1,n+1):
            self.draw_line(i,n)
    def scale(self,f):
        self.n=self.n*f
class Triangle(Shape):
    def draw_line(self,i,n):
        print("*"*i)

class Square(Shape):
    def draw_line(self,i,n):
        print("*"*n)
        
s = Shape()
#s.draw(4)
sq = Square(2)
sq.draw()
sq.scale(2)
sq.draw()
class Shape(object):
    def Area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__()
        self.width = width
        self.height = height

    def Area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self,width):
        super().__init__(width,width)

class Ellipse(Shape):
    pi=3.14
    def __init__(self,a,b):
        super().__init__()
        self.a=a
        self.b=b
    def Area(self):
        return self.a * self.b * self.pi
class Circle(Ellipse):
    def __init__(self,r):
        super().__init__(r,r)

shapes=[Ellipse(10,20),Square(15),Circle(5),
        Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]
Areas = [x.Area for x in shapes]
print('Areas:',Areas)

"""
    桥模式
    将一个事物的两个维度分离，使其都可以独立的变化(比如本例子中的形状和颜色)
"""
from abc import ABCMeta,abstractmethod
class Shape(metaclass=ABCMeta):
    def __init__(self,color):
        self.color=color
    @abstractmethod
    def draw(self):
        print("Shape")
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self,shape):
        print("Color")
class Recttangle(Shape):
    name="矩形"
    def draw(self):
        """矩形的逻辑"""
        self.color.paint(self)
class Circle(Shape):
    name="圆形"
    def draw(self):
        """圆形的逻辑"""
        self.color.paint(self)
class Line(Shape):
    def draw(self):
        self.color.paint(self)
class Red(Color):
    def paint(self,shape):
        print("红色的%s"%shape.name)
class Blue(Color):
    def paint(self,shape):
        print("蓝色的%s"%shape.name)
r=Recttangle(Red())
r.draw()

b=Circle(Blue())
b.draw()
"""
角色：
    抽象       Shape类
    细化抽象    Color类
    实现者      Recttangle类
    具体实现者   Red()等颜色类实现
    
本例子中形状是抽象，颜色是实现
优点：
    抽象和实现相分离
    优秀的扩展能力

"""
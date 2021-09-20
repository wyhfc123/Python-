"""
    建造者模式
"""
from abc import ABCMeta,abstractmethod
class Player:
    def __init__(self,face=None,body=None,arm=None,leg=None):
        self.face=face
        self.body=body
        self.arm=arm
        self.leg=leg
    def __str__(self):
        return "%s,%s,%s,%s"%(self.face,self.body,self.arm,self.leg)

"""玩家构造器"""
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexyGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player=Player()
    def build_face(self):
        self.player.face = "瓜子脸"
    def build_body(self):
        self.player.body = "苗条"
    def build_arm(self):
        self.player.arm="白皙"
    def build_leg(self):
        self.player.leg = "修长"




class Monster(PlayerBuilder):
    def __init__(self):
        self.player=Player()
    def build_face(self):
        self.player.face = "狰狞"
    def build_body(self):
        self.player.body = "肠肥脑满"
    def build_arm(self):
        self.player.arm="水桶粗"
    def build_leg(self):
        self.player.leg = "长毛"
class PlayerDirector: #控制组装顺序
    def build_player(self,builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player
#client
builder = SexyGirlBuilder()
director = PlayerDirector()

p=director.build_player(builder)
print(p)


"""
    将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
"""
"""
    角色
    抽象建造者
    具体建造者
    指挥者
    产品  
"""
"""
建造者模式与抽象工厂模式相似，也用来创建复杂对象。
主要区别是建造者模式着重一步步构造一个复杂对象，
而抽象工厂模式着重于多个系列的产品对象
"""
"""
隐藏了一个产品的内部结构和装配过程
将构造代码与表示代码分开
可以对构造过程进行更精细化的控制
"""

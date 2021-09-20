"""
    策略模式
    定义一系列的算法，把它们一个个封装起来，并且使它们可相互替换，本模式使
    得算法可独立使用它的客户而变化
"""
from abc import ABCMeta,abstractmethod
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self,data):
        pass
class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s" % data)


class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)
# Client

data = "[...]"
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()
"""
    角色
    抽象策略
    具体策略
    上下文
优点：
    定义了一系列可重用的算法和行为
    消除了一些条件语句
    可以提供相同行为的不同表现
缺点：
    客户必须了解不同的策略
    
"""
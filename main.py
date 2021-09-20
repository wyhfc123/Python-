"""
    1、创建型模式
"""

from abc import ABCMeta,abstractmethod
#接口，定义抽象类和抽象方法(子类必须实现父类的方法)
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass
#实现Payment接口
class Alipay(Payment):
    def pay(self,money):
        print(money)
class WeChat(Payment):
    def pay(self,money):
        print(money)

a=Alipay()
a.pay(200)


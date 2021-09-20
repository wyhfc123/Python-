"""

：简单工厂函数
"""
from abc import ABCMeta,abstractmethod
#接口，定义抽象类和抽象方法(子类必须实现父类的方法)
class Payment(metaclass=ABCMeta):   #抽象产品角色
    @abstractmethod
    def pay(self,money):
        pass
#实现Payment接口
#最底层
class Alipay(Payment):  #具体产品角色
    def __init__(self,huabei=False):  #增加花呗支付

        self.huabei=huabei
    def pay(self,money):
        if self.huabei:
            print("花呗支付了%s元" % money)
        else:
            print("支付宝支付了%s元"%money)

class WeChat(Payment): #具体产品角色
    def pay(self,money):
        print(" 微信支付了%s元" % money)
#简单工厂函数
class PayMentFactory():   #工厂角色
    def create_payment(self,method):
        if method == "alipay":
            return Alipay()
        if method == "wechat":
            return WeChat()
        elif method == "huabei":
            return Alipay(huabei=True)
        else:
            raise TypeError("%s：此方法没有"%method)
#最高层(client)
p=PayMentFactory()
c=p.create_payment("alipay")
c.pay(200)
c=p.create_payment("huabei")  #最高层不需要知道花呗参数以及具体的实现方法，只调用要实现的方法名就行了
c.pay(500)

"""
    :优点
    1、隐藏了对象创建实现的细节
    2、客户端不需要修改代码
    :缺点
    违反了单一职责原则，将创建逻辑集中到一个工厂类里
    当添加新产品时，需要修改工厂类代码，违反了开闭原则
"""

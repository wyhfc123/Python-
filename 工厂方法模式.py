

from abc import ABCMeta,abstractmethod
#接口，定义抽象类和抽象方法(子类必须实现父类的方法)
"""
    抽象产品角色
"""
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass
#实现Payment接口
#最底层
"""
    具体产品角色
"""
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
class Bank(Payment):
    def pay(self,money):
        print(" 银联支付了%s元" % money)

#定义工厂接口
"""
    抽象工厂角色
"""
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass
"""
    具体工厂角色
"""
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()
class WechatFactory(PaymentFactory):
    def create_payment(self):
        return WeChat()
class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(huabei=True)
class BankFactory(PaymentFactory): #新加的
    def create_payment(self):
        return Bank()
pf= HuabeiFactory()
p=pf.create_payment()
p.pay(200)
"""
    优点：
    1、每个具体产品都对应一个具体工厂类，不需要修改工厂代码
    2、隐藏了对象创建实现的细节
    缺点：
    1、每增加一个具体产品类，就必须增加一个相应的具体工厂类
    
"""
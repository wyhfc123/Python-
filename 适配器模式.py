"""
    适配器模式
"""
"""
    将一个类的接口转换成客户希望的另一个接口，适配器模式使得原本由于接口不兼容而不能一起工作的哪些类可以一起工作
    两种实现方式
        类适配器:使用多继承
        对象适配器:使用组合
"""
from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass
class Alipay(Payment):
    def __init__(self,huabei=False):  #

        self.huabei=huabei
    def pay(self,money):
        if self.huabei:
            print("花呗支付了%s元" % money)
        else:
            print("支付宝支付了%s元"%money)

class WeChat(Payment): #具体产品角色
    def pay(self,money):
        print(" 微信支付了%s元" % money)
#跟接口不兼容
class BankPay(object):
    def cost(self,money):
        print("银联支付了%s元"%money)
class ApplePay(object):
    def cost(self, money):
        print("苹果支付了%s元" % money)

#类适配器
# class NewBankPay(Payment,BankPay):
#     def pay(self,money):
#         self.cost(money)

# p=NewBankPay()
#对象适配器
class PaymentAdapter(Payment):
    def __init__(self,payment):
        self.payment=payment
    def pay(self,money):
        self.payment.cost(money)

p=PaymentAdapter(ApplePay())
p.pay(20)

"""
    角色
    1、目标接口
    2、待适配的类
    3、适配器
    使用场景
    想使用一个已经存在的类，而它的接口不符合你的要求
    (对象适配器) 想使用一些已经存在的子类,但不可能对每一个都进行子类化以匹配它们的接口，对象适配器
    可以适配它的父类接口
"""
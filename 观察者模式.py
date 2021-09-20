"""
    观察者模式
    定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时，所有依赖于它的对象都得到
    通知并被自动更新。观察者模式又称"发布-订阅"模式
"""
from abc import ABCMeta,abstractmethod
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self,notice):
        pass
class Notice:
    def __init__(self):
        self.obervers=[]
    def attach(self,obs):
        self.obervers.append(obs)
    def detach(self,obs):
        self.obervers.remove(obs)
    def notify(self):  #推送
        for obs in self.obervers:
            obs.update(self)
#具体发布者
class StaffNotice(Notice):
    def __init__(self,conpany_info = None):
        super(StaffNotice, self).__init__()
        self.__conpany_info=conpany_info
    @property
    def company_info(self):
        return self.__conpany_info
    @company_info.setter
    def company_info(self,info):
        self.__conpany_info = info
        self.notify()

class Staff(Observer):
    def __init__(self):
        self.company_info = None
    def update(self,notice):
        self.company_info = notice.company_info


notice = StaffNotice("初始公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司今年业绩非常好，给大家发奖金！！！"
print(s1.company_info)
print(s2.company_info)
notice.detach(s2)
notice.company_info = "公司明天放假！！！"
print(s1.company_info)
print(s2.company_info)
"""
角色：
    抽象主题
    具体主题      发布者
    抽象观察者
    具体观察者    订阅者
适用场景：
    当一个抽象模型有两方面，其中一方面依赖于另一个方面。将这两者封装在独立对象中以使它们可以各自独立地改变和复用。
    当一个对象的改变需要同时改变其他对象，而不知道具体有多少对象有待改变
    当一个对象必须通知其他对象，而它又不能假定其他的对象是谁。换言之，你不希望这些对象是紧密耦合的。
优点：
    目标和观察者之间的抽象耦合最小
    支持广播通信
    
    
    
    
    
    
     
"""
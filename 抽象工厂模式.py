"""
    抽象工厂模式
"""
from abc import ABCMeta,abstractmethod
"""抽象产品"""
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass
class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass
class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass
"""抽象工厂"""

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass
    @abstractmethod
    def make_cpu(self):
        pass
    @abstractmethod
    def make_os(self):
        pass
"""具体的产品"""
class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通手机小手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("普通手机大手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("高通骁龙cpu")


class MediaTaskCPU(CPU):
    def show_cpu(self):
        print("联发科cpu")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class Android(OS):
    def show_os(self):
        print("Android系统")


class IOS(OS):
    def show_os(self):
        print("ios系统")


"""具体工厂"""   #每个工厂生产一套对象

class MiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()
    def make_cpu(self):
        return SnapDragonCPU()
    def make_os(self):
        return Android()

class HuaWeiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()
    def make_cpu(self):
        return MediaTaskCPU()
    def make_os(self):
        return Android()
class IphoneFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()
    def make_cpu(self):
        return AppleCPU
    def make_os(self):
        return IOS()
#客户端
class Phone(object):
    def __init__(self,cpu,os,shell):
        self.cpu=cpu
        self.os=os
        self.shell=shell
    def show_info(self):
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()
def make_phone(factory):
    cpu=factory.make_cpu()
    os=factory.make_os()
    shell=factory.make_shell()
    return Phone(cpu,os,shell)


p1=make_phone(MiFactory())
p1.show_info()

"""
   角色
   抽象工厂角色
   具体工厂角色
   抽象产品角色
   具体产品角色
   客户端
"""

"""
   优点：
   1、将客户端与类的具体实现相分离
   2、每个工厂创建了一个完整的产品系列，使得易于交换产品序列
   3、有利于产品的一致性(即产品之间的约束关系)
   缺点：
   难以支持新种类的(抽象)产品
"""

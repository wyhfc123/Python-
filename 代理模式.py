"""

代理模式
为其他对象提供一种代理以控制对这个对象的访问。
应用场景：
    远程代理:为远程的对象提供代理
    虚代理：根据需要创建很大的对象
    保护代理：控制对原始对象的访问，用于对象有不同访问权限时
"""
from abc import ABCMeta,abstractmethod
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass
    @abstractmethod
    def set_content(self,content):
        pass

class RealSubject(Subject):
    def __init__(self,filename):
        self.filename = filename
        f = open(filename,"r")
        self.content= f.read()
    def get_content(self):
        return self.content
    def set_content(self,content):
        f = open(self.filename,'w')
        f.write(content)
        f.close()

#虚代理
class VirtualProxy(Subject):
    def __init__(self,filename):
        self.filename = filename
        self.subj = None
    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()
    def set_content(self,content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.set_content(content)

# subj = RealSubject("test.txt")   #创建对象时创建了f对象
# subj.get_content()
# subj = VirtualProxy("test.txt")  #创建对象时没有创建f对象
# print(subj.get_content())#调用时创建f对象


#保护代理
class ProtectedProxy(Subject):
    def __init__(self,filename):
        self.subj = RealSubject(filename=filename)
    def get_content(self):
        return self.subj.get_content()
    def set_content(self,content):
        raise PermissionError("无写入权限")

subj = ProtectedProxy("test.txt")  #创建对象时没有创建f对象
print(subj.get_content())#调用时创建f对象
print(subj.set_content("abc"))#调用时报错
"""
角色
    抽象实体
    实体
    代理
优点：
    远程代理:可以隐藏对象位于远程地址空间的事实
    虚代理：可以进行优化，例如根据要求创建对象
    保护代理：允许在访问一个对象时有一个附加的内务处理

"""
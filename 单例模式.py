"""
    单例模式
"""

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance
class MyClass(Singleton):
    def __init__(self,a):
        self.a=a
m=MyClass(20)
m1=MyClass(30)
print(m.a)
print(m1.a)
print(id(m),id(m1))

"""
    优点：
    1、对唯一的实例的受控访问
    2、单例相当于全局变量,但防止了命名空间被污染
"""
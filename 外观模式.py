"""

外观模式
为子系统中的一组接口提供一个一致地界面，外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用
"""

#子系统
class CPU:
    def run(self):
        print("CPU开始运行")

    def stop(self):
        print("CPU停止运行")
#子系统
class Disk:
    def run(self):
        print("Disk开始工作")

    def stop(self):
        print("Disk停止工作")
#子系统
class Memory:
    def run(self):
        print("内存通电")

    def stop(self):
        print("内存断电")
#外观
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()
    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()
    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()

computer = Computer()
computer.run()

computer.stop()


"""
角色:
    外观
    子系统类
优点：
    减少系统相互依赖
    提高了灵活性
    提高了安全性
"""
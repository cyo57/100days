'''
面向对象
'''

# 定义类
class Student(object):
    # 初始化, 绑定属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

# 创建和使用对象
def main():
    # 创建
    stu1 = Student('hxert', 38)
    # 发消息
    stu1.study('睡觉')

main()
# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def study(self, course_name):
#         print('%s正在学习%s.'%(self.name, course_name))

#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.'% self.name)
#         else:
#             print('%s只能观看《咳咳咳》.'% self.name)

# def main():
#     stu1 = Student('weishaodaren', 99)
#     stu1.study('Python')
#     stu1.watch_movie()
#     stu2 = Student('王大锤', 3)
#     stu2.study('时间简史')
#     stu2.watch_movie()

# if __name__ == '__main__':
#     main()

class Test:
    
    def __init__(self, foo):
        self.__foo = foo
    
    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    test.__bar()
    print(test.__foo)

if __name__ == "__main__":
    main()
#Напишите код, который выведет на экране все переменные объекта произвольного пользовательского класса.
class Student:
    def __init__(self):
        self.name = 'Elizaveta'
        self.last_name = 'Flera'
        self.age = 19

    def get_all_vars(self):
        return list(vars(self).keys())
#Напишите код, который по имени метода, заданному строкой, вызовет этот метод в объекте некоторого пользовательского класса.
    def f1(self):
        self.name = 'f1'
        print('Method f1')

    def f2(self):
        self.name = 'f2'
        print('Method f2')


student = Student()

# 1
print(student.get_all_vars())

# 2
func_name = input()
#возвращает значение атрибута объекта
func = getattr(student, func_name)
func()
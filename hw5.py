# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set
# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий

class Hamster:
    biological_class = 'Animal'
    biological_podclass = 'Gryzun'
    def __init__(self, name, weight, height):
        self.name = name
        self._age = 1
        self.weight = weight
        self.height = height
    #using the get function
    def get_age(self):
        #print('getter method')
        return self._age
    #using the set function
    def set_age(self, y):
        #print('setter method')
        self._age = y
    #using the del function
    def del_age(self):
        del self._age
    age = property(get_age, set_age, del_age)
    def say_hello(self):
        print(f'Hello! My name is {self.name}. I am {self.age} year(s) old, my weight is {self.weight} gramm and my height is {self.height} cm.')
siriyskiy = Hamster('Willy', 130, 12)
siriyskiy.age = 3
siriyskiy.say_hello()
dzyngarskiy = Hamster('Micro', 50, 5)
dzyngarskiy.age = 1
dzyngarskiy.say_hello()
robovsky = Hamster('Rob', 47, 4)
robovsky.age = float(0.5)
robovsky.say_hello()
robovsky.say_hello()

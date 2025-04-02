class Car:
    def __init__(self, brand, color):
        __slots__ = ['brand', 'color']
        self.brand = brand
        self.color = color #объявляем атрибуты self.brand и self.color
    #При создании объекта класса Car ему передается аргумент brand и color, который сохраняется в атрибуте self.brand и self.color
    def drive(self):
        print(self.color, self.brand, 'is driving')

my_car = Car('Kia', 'Yellow')
my_car.drive()
my_slovar = Car('Nigger','Black')
my_slovar.cock = 22
print(my_slovar.__dict__)
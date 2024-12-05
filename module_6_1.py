# Родительский класс для всех животных
class Animal:
    def __init__(self, name):
        self.name = name  # Имя животного
        self.alive = True  # Живой или нет
        self.fed = False  # Накормлен или нет

# Родительский класс для всех растений
class Plant:
    def __init__(self, name):
        self.name = name  # Имя растения
        self.edible = False  # Съедобное или нет

# Класс млекопитающих (унаследован от Animal)
class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может есть {food}, это не растение!")

# Класс хищников (унаследован от Animal)
class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может есть {food}, это не растение!")

# Класс цветов (унаследован от Plant)
class Flower(Plant):
    pass  # У цветов остаются атрибуты родительского класса

# Класс фруктов (унаследован от Plant)
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)  # Вызываем конструктор родителя
        self.edible = True  # У фруктов съедобность переопределена

# Тестируем:
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

print(a1.alive)  # True
print(a2.fed)  # False

a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Хатико съел Заводной апельсин

print(a1.alive)  # False
print(a2.fed)  # True

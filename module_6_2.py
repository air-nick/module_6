class Vehicle:
    # Атрибут класса: допустимые цвета
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color.lower()
        self.__engine_power = engine_power

    # Метод для получения модели транспорта
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод для получения мощности двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод для получения цвета транспорта
    def get_color(self):
        return f"Цвет: {self.__color.capitalize()}"

    # Метод для изменения цвета
    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    # Метод для вывода информации об автомобиле
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")


class Sedan(Vehicle):
    # Атрибут класса: лимит пассажиров
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Проверка работы программы
if __name__ == "__main__":
    # Создание объекта класса Sedan
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()
    print()

    # Меняем свойства
    vehicle1.set_color('Pink')  # Недопустимый цвет
    vehicle1.set_color('BLACK')  # Допустимый цвет
    vehicle1.owner = 'Vasyok'  # Меняем владельца
    print()

    # Проверяем, что изменилось
    vehicle1.print_info()

# Задача 1
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


# Создание спимска объектов и вывод результатов
rectangles: list[Rectangle] = [Rectangle(3, 4), Rectangle(5, 10), Rectangle(7, 2)]
for rect in rectangles:
    print(f"Площадь: {rect.area()}, Периметр: {rect.perimeter()}")


# Задача 2
class Math:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def addition(self) -> None:
        print(self.a + self.b)

    def multiplication(self) -> None:
        print(self.a * self.b)

    def division(self) -> None:
        if self.b != 0:
            print(self.a / self.b)
        else:
            print("Деление на ноль невозможно")

    def subtraction(self) -> None:
        print(self.a - self.b)


# Пример использования
math_obj = Math(10, 5)
math_obj.addition()
math_obj.multiplication()
math_obj.division()
math_obj.subtraction()


# Задача 3 (Если правильно понял что от меня требуется)
class SidebarButton:
    def __init__(self, text: str, button_type: str = "Кнопка", locator: str = ""):
        self.text = text
        self.button_type = button_type
        self.locator = locator

    def click(self) -> str:
        return f"Клик по кнопке {self.text}"


# Создание объектов и вывод результатов
buttons: list[SidebarButton] = [
    SidebarButton(text="Text Box"),
    SidebarButton(text="Check Box"),
    SidebarButton(text="Radio Button"),
]
for button in buttons:
    print(button.text)
    print(button.click())


# Доп Задача 4
class Car:
    def __init__(self, color: str, car_type: str, year: int):
        self.color = color
        self.type = car_type
        self.year = year

    def start(self) -> None:
        print("Автомобиль заведен")

    def stop(self) -> None:
        print("Автомобиль заглушен")

    def set_year(self, year: int) -> None:
        self.year = year

    def set_type(self, car_type: str) -> None:
        self.type = car_type

    def set_color(self, color: str) -> None:
        self.color = color


# Пример использования
car = Car("red", "sedan", 2020)
car.start()
car.stop()
car.set_year(2021)
car.set_type("SUV")
car.set_color("blue")

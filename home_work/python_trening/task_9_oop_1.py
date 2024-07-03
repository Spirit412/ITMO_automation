from task_9_checks import Checks

class Class1(Checks):
    def __init__(self, loc: str):
        super().__init__(loc)

class Class2(Checks):
    def __init__(self, loc: str):
        super().__init__(loc)

class Class3(Checks):
    def __init__(self, loc: str):
        super().__init__(loc)

class Class4(Checks):
    def __init__(self, loc: str):
        super().__init__(loc)

# Пример использования
obj1 = Class1("loc1")
obj2 = Class2("loc2")
obj3 = Class3("loc3")
obj4 = Class4("loc4")

print(obj1.check_text())
print(obj2.check_text())
print(obj3.check_text())
print(obj4.check_text())
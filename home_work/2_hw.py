def task_1() -> None:
    var_int: int = 10
    var_float: float = 3.14
    var_str: str = "Привет Мир!"
    var_list: list = [1, 2, 3, 4, 5]
    var_bool: bool = True

    print(type(var_int))
    print(type(var_float))
    print(type(var_str))
    print(type(var_list))
    print(type(var_bool))

# Вызов функции
task_1()


def task_2() -> None:
    a: list[int] = [1, 2, 3, 5, 8, 13, 21]  # * - Эта последовательность чисел называется "Последовательность Фибоначчи" ))
    print(a[:3])

# Вызов функции
task_2()


def task_3(number: int) -> int:
    return number ** 2

# Вызов функции и распечатка результата
print(task_3(5))  # Пример вызова функции с числом 5

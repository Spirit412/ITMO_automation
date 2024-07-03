def find_max(a: int, b: int) -> None:
    if a > b:
        print(a)
    else:
        print(b)


# Пример вызова функции
find_max(a=10, b=20)


def check_difference(a: int, b: int) -> None:
    if abs(a - b) == 135:
        print("yes")
    else:
        print("no")


# Пример вызова функции
check_difference(a=100, b=235)


def get_season(month: int) -> None:
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Неверный номер месяца")


# Пример вызова функции
get_season(month=7)


def check_numbers(a: int, b: int, c: int) -> None:
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")


# Пример вызова функции
check_numbers(a=11, b=12, c=13)


def count_positives(numbers: list[int]) -> None:
    count = sum(1 for num in numbers if num > 0)
    print(count)


# Пример вызова функции
count_positives([-1, 2, 3, -4, 5])


def calculate_days(years: int, months: int) -> None:
    days = (years * 12 + months) * 29
    print(days)


# Пример вызова функции
calculate_days(years=2, months=5)

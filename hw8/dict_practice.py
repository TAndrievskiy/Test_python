# 1. Объедните 2 словаря в 1 и выведите на экран
# Ожидаемый результат: {'Four': 4, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Sixty': 60}
dict1 = {"Four": 4, "Twenty": 20, "Thirty": 30}
dict2 = {"Thirty": 30, "Fourty": 40, "Sixty": 60}
dict3 = dict1 | dict2
print(dict3)

# 2. Создайте словарь из двух списков
# Ожидаемый результат: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
data = dict(zip(keys, values))
print(data)

# 3. Отобразите значение ключа 'math' на экран
# Ожидаемый результат: 92
data = {
    "class": {
        "student": {
            "name": "Max",
            "marks": {
                "math": 92,
                "history": 87,
            },
        }
    }
}
class_data = data.setdefault("class")
student_data = class_data.setdefault("student")
marks_data = student_data.setdefault("marks")
print(marks_data.setdefault("math"))


# 4. Создайте словарь с ключами из employees и дефолтными значениями defaults
# Ожидаемый результат: {'Max': {'role': 'developer', 'salary': 2000}, 'Ann':..}
employees = ["Max", "Ann", "John", "Jane"]
defaults = {"role": "developer", "salary": 2000}
data = dict()
for name in employees:
    data.update({name: defaults})
print(data)

# 5. Создайте словарь с элементами keys из словаря user_data
# Ожидаемый результат: {'name': 'Max', 'age': 21}
user_data = {
    "name": "Max",
    "email": "max@mail.com",
    "age": 21,
    "country": "Ukraine",
}
keys = ["name", "age"]
data = dict()
for key, value in user_data.items():
    for i in keys:
        if key == i:
            data.update({key: value})
print(data)


# 6. Переименуйте ключ 'country' на 'location' в словаре user_data
user_data = {
    "name": "Max",
    "email": "max@mail.com",
    "age": 21,
    "country": "Ukraine",
}
value = user_data.pop("country")
user_data.update({"location": value})
print(user_data)

# 7. Измените значение 'salary' у 'Jane' на 2500
user_data = {
    "Max": {"role": "developer", "salary": 2000},
    "Ann": {"role": "developer", "salary": 2000},
    "John": {"role": "developer", "salary": 2000},
    "Jane": {"role": "developer", "salary": 2000},
}
name_data = user_data.setdefault("Jane")
name_data.update({"salary": 2500})
print(user_data)

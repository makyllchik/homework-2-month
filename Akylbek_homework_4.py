# 1. Создать класс TimeDesk , в котором будет один атрибут seconds
# 2. Надо в методе продумать логику конвертера секунд на дни , часы ,
# минуты и секунды
# 3. Если было дано 70 секунд то вывод должен быть 0 дней, 0 часов , 1
# минута , 10 секунд
# 4. Если было дано 86401 секунда то вывод должен быть 1 день , 0 часов
# , 0 минут и 1 секунда


class TimeDesk:

    def convert(self, seconds, minutes, hours, days):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.days = days

    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60

    seconds = int(input("Enter a number of seconds: "))

    days = (seconds // seconds_in_day)
    seconds = seconds - (days * seconds_in_day)

    hours = (seconds // seconds_in_hour)
    seconds = seconds - (hours * seconds_in_hour)

    minutes = (seconds // seconds_in_minute)
    seconds = seconds - (minutes * seconds_in_minute)

    print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(days, hours, minutes, seconds))


# Задание № 2
# 1. Создать любой класс который вам по душе
# 2. Прописать Метод для @property  @staticmethod
# 3. Использовать декоратор @property и обратить метод в setter и deleter,
# также попробовать внести изменения
# 5. Использовать @staticmethod и прописать любую функцию
# независимого от класс

class Motorcicle:

    def __init__(self, name, model, engine, year_of_issue):
        self.name = name
        self.model = model
        self.engine = engine
        self.issue = year_of_issue

    @staticmethod
    def nickname(self):
        nickname = f"\"{self.name}\". {self.model}"
        return nickname

    @property
    def characteristics(self):
        properties = self.engine + " " + self.issue
        return properties

    @characteristics.setter
    def characteristics(self, properties):
        self.engine, self.issue = properties.split()

    @characteristics.deleter
    def characteristics(self):
        self.engine = None
        self.issue = None

    def __str__(self):
        return f"Nickname: \"{self.name}\" {self.model}\n" \
               f"Characteristics: {self.engine}, {self.issue} "


ural = Motorcicle("Ural", "M-72", "745cm^3", "1940")
print(ural)

print(ural.nickname)
print(ural.characteristics)
ural.year ="1946"
print(ural.nickname)

class Car:
    def __init__(self, brand, color, type_car, amount_passenger, max_speed, engine, country, year):

        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError("Brand should be string!")

        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError("Colour should be string")

        if isinstance(type_car, str):
            self.type_car = type_car
        else:
            raise ValueError("Type should be string")

        if isinstance(amount_passenger, int):
            self.amount_passenger = amount_passenger
        else:
            raise ValueError("amount_passenger should be int")

        if isinstance(max_speed, int):
            self.max_speed = max_speed
        else:
            raise ValueError("Max_speed should be int")

        if isinstance(engine, float):
            self.engine = engine
        else:
            raise ValueError("Engine should be float")

        if isinstance(country, str):
            self.country = country
        else:
            raise ValueError("Country should be string")

        if isinstance(year, int):
            self.year = year
        else:
            raise ValueError("Year should be int")

    def tunning(self, cost):
        car_cost = 1000
        summary = car_cost+cost
        return summary

    def __str__(self):
        return f"{self.year}, {self.country}, {self.color}, {self.engine}, {self.amount_passenger}, {self.max_speed}," \
               f"{self.type_car}, {self.brand}"

car_1 = Car(brand="BMW", country="Germany", year=2021, color="black", type_car="Crossover", amount_passenger=4,
            engine=3.5, max_speed=200)

print(car_1)
print(car_1.tunning(8000))

class Human:
    name = "Adilet"
    age = 24
    def __init__(self, name, age, height, gender):
        self.my_name = name
        self.age = age
        self.height = height
        self.gender = gender
    def __str__(self):
        return f"Name: {self.my_name}\n" \
               f"Age: {self.age}\n" \
               f"Height: {self.height}\n"\
                f"Gender: {self.gender}\n"
    def can_say_hello(self):
        return "Hello world"

    def can_calculate(self, number_1, number_2):
        summary = number_1+number_2
        return summary


human_1 = Human(name = "Adilet", age=24, height=189,gender= "male")
human_2 = Human("Aelin",20, 179,"female")
# print(human_1.can_say_hello())
# print(human_1.can_calculate(12,23))
# print(human_2)
# print(human_1)

class Programmer(Human):
    def __init__(self, name, age, height, gender, language, fast_typing, logic):
        super().__init__(name, age, height,gender)
        self.language = language
        self.fast_typing = fast_typing
        self.logic = logic

    def can_feely_use_laptop(self):
        print("Yes, I can freely use laptop like a God")

    def __str__(self):
        return f"Languages {self.language}\n" \
               f"Fast_typing {self.fast_typing}\n" \
                f"Logic {self.logic}\n"


proger = Programmer(language="Python", fast_typing=True, logic=True, name = "Adilet", age=24, height=189,gender= "male" )
print(proger)
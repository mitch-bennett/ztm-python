class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"my name is {self.name}")

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Tom", 20)

print(player1.adding_things(2, 3))

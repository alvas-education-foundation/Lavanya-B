#github repository- Lavanya-B


class As:
    def __init__ (self, a , b, c):
        self.name = a
        self.color = b
        self.pet = c
    def introduce (self):
        print("My name is " + self.name +".")
        print("My color is " + self.color +".")
        print("My pet is " + self.pet +".\n")
p1 = As("lavanya", "Fair", "Rabbit")
p1.introduce ()
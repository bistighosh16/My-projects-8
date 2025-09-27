class Car:
    def __init__(self, model, price, color, build_year):
        self.model = model
        self.price = price
        self.color = color
        self.build_year = build_year
    def display_info(self):
        print(f"Model: {self.model}, Price: ${self.price}, Color: {self.color}, Build Year: {self.build_year}")
car1 = Car("AAA", 10000, "Orange", 2015)
car2 = Car("BBB", 15000, "Blue", 2018)
car3 = Car("CCC", 45000, "Green", 2015)
car1.display_info()
car2.display_info()
car3.display_info()

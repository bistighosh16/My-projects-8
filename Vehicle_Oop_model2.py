class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"
class LoadingVehicle(Vehicle):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity 
    def display_info(self):
        return super().display_info() + f", Load Capacity: {self.load_capacity} tons"
class Truck(LoadingVehicle):
    def __init__(self, brand, model, year, load_capacity, wheels):
        super().__init__(brand, model, year, load_capacity)
        self.wheels = wheels
    def display_info(self):
        return super().display_info() + f", Wheels: {self.wheels}"
class LoadingVan(LoadingVehicle):
    def __init__(self, brand, model, year, load_capacity, fuel_type):
        super().__init__(brand, model, year, load_capacity)
        self.fuel_type = fuel_type
    def display_info(self):
        return super().display_info() + f", Fuel Type: {self.fuel_type}"
class PassengerVehicle(Vehicle):
    def __init__(self, brand, model, year, seating_capacity):
        super().__init__(brand, model, year)
        self.seating_capacity = seating_capacity
    def display_info(self):
        return super().display_info() + f", Seating Capacity: {self.seating_capacity}"
class Bike(PassengerVehicle):
    def __init__(self, brand, model, year, seating_capacity, type_of_bike):
        super().__init__(brand, model, year, seating_capacity)
        self.type_of_bike = type_of_bike
    def display_info(self):
        return super().display_info() + f", Type: {self.type_of_bike}"
class Car(PassengerVehicle):
    def __init__(self, brand, model, year, seating_capacity, fuel_type):
        super().__init__(brand, model, year, seating_capacity)
        self.fuel_type = fuel_type
    def display_info(self):
        return super().display_info() + f", Fuel Type: {self.fuel_type}"
truck = Truck("Volvo", "FH16", 2022, 20, 18)
van = LoadingVan("Ford", "Transit", 2021, 3, "Diesel")
bike = Bike("Yamaha", "YZF-R1", 2023, 2, "Sport")
car = Car("Tesla", "Model S", 2024, 5, "Electric")
def vehicle_details():
    print("Select a vehicle to view details:")
    print("1. Truck")
    print("2. Loading Van")
    print("3. Bike")
    print("4. Car")
    choice = int(input("Enter the number of your choice: "))
    match choice:
        case 1:
            print(truck.display_info())
        case 2:
            print(van.display_info())
        case 3:
            print(bike.display_info())
        case 4:
            print(car.display_info())
        case _:
            print("Invalid choice! Please select a number between 1 and 4.")
vehicle_details()
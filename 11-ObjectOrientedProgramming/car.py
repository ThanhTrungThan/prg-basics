class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")
    
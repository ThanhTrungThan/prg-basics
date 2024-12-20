class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    #adding a method print_receipt(self)
    def print_receipt(self):
        print("Taxi Ride Receipt")
        print("=================")
        print(f"Distance traveled: {self.distance} km")
        print(f"Rate per km: €{self.rate_per_km}")
        print(f"Total fare: €{self.fare:.2f}")
        print()

#main program
def main():
    #create 2 ride
    ride1 = TaxiRide(2)
    ride2 = TaxiRide(3)

    #calculate fare for 2 ride
    ride1.calculate_fare(13)
    ride2.calculate_fare(15)

    #print 2 ride
    ride1.print_receipt()
    ride2.print_receipt()


if __name__ == "__main__":
    main()

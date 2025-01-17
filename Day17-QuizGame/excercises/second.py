class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2
    

my_car = Car(5)

print(f"My car has {my_car.seats}")

my_car.enter_race_mode()

print(f"We are ready to race with {my_car.seats} seats")


################################################################
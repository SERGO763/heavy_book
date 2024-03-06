class HauntedBus:
    """Автобус, облюбованный пассажирами-призраками"""
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus_1 = HauntedBus(['Alice', 'Bill'])
print(bus_1.passengers)
bus_1.pick('Charlie')
bus_1.drop('Alice')
print(bus_1.passengers)
bus_2 = HauntedBus()
bus_2.pick('Carrie')
print(bus_2.passengers)
bus_3 = HauntedBus()
print(bus_3.passengers)
bus_3.pick('Dave')
print(bus_3.passengers)
print(bus_2.passengers is bus_3.passengers)
print(bus_1.passengers)

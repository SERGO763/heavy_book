import copy
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus_1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus_2 = copy.copy(bus_1)
bus_3 = copy.deepcopy(bus_1)
print(id(bus_1), id(bus_2), id(bus_3))
print(bus_1.drop('Bill'))
print(bus_2.passengers)
print(id(bus_1.passengers), id(bus_2.passengers), id(bus_3.passengers))
print(bus_3.passengers)
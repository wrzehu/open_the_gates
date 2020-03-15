class Vehicles:

    def __init__(self, num_of_wheels):
        self.num_of_wheels = num_of_wheels

    def repair(self):
        raise NotImplementedError("Subclass must implement this method")


class Bicycles(Vehicles):

    def repair(self):
        print('Repairing a bycycle with {} number of wheels'.format(self.num_of_wheels))


class Trucks(Vehicles):

    def repair(self):
        print('Repairing a truck with {} number of wheels'.format(self.num_of_wheels))


class Cars(Vehicles):

    def repair(self):
        print('Repairing a car with {} number of wheels'.format(self.num_of_wheels))


class Workshop:

    def accept(self, vehicle):
        vehicle.repair()



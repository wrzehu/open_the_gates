class IllegalCarError(Exception):
    """Raised when the attributes of Car class are wrong"""
    pass


class Car:

    def __init__(self, pax_count, car_mass, gear_count, ):

        self.__pax_count = pax_count
        self.pax_count_validation()

        self.__car_mass = car_mass
        self.car_mass_validation()

        self.__gear_count = gear_count

    @property
    def total_mass(self):
        avg_weight_of_person = 70
        return self.__car_mass + avg_weight_of_person * self.__pax_count

    def set_pax_count(self, pax_count):
        self.__pax_count = pax_count
        self.pax_count_validation()

    def set_car_mass(self, car_mass):
        self.__car_mass = car_mass
        self.car_mass_validation()

    def get_pax_count(self):
        return self.__pax_count

    def get_car_mass(self):
        return self.__car_mass

    def get_gear_count(self):
        return self.__gear_count

    def pax_count_validation(self):
        if self.__pax_count == 0:
            raise IllegalCarError('you need at least driver')
        elif self.__pax_count > 5:
            raise IllegalCarError('maximum 5 people in car')

    def car_mass_validation(self):
        if self.__car_mass > 2000:
            raise IllegalCarError('max weight of car can\'t be more than 2000 kg')

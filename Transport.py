class Transport:      # не ставим скобки, т.к. это главный класс
    '''transport description'''         # Transport.__doc__
    max_speed = None
    year = None
    type = None

    def __init__(self, type, max_speed, year):
        # метод инициализации
        # автоматически будет выполнять, когда создаем объект класса
        self.type = type
        self.max_speed = max_speed
        # self ссылка на объект на основе класса
        self.year = year

    def get_info(self):         # создаем метод вывода
        print('Type of transport:', self.type, 'Year:', self.year,
              'Max speed:', self.max_speed)


class Airplane(Transport):
    type_of_airplane = None
    flight_altitude = None

    def __lt__(self, other):
        if not isinstance(other, (int, Airplane)):
            raise TypeError("Операнд справа должен иметь тип int или Airplane")
        sc = other if isinstance(other, int) else other.flight_altitude
        return self.flight_altitude < sc

    def __str__(self) -> str:
        return "This object is Airplane"

    def __init__(self, type, type_of_airplane, flight_altitude,
                 max_speed, year):
        super().__init__(type, max_speed, year)
        # нужен self?
        # связываем с родителем и наследуем max_speed и year
        self.type_of_airplane = type_of_airplane
        self.flight_altitude = flight_altitude

    def get_info(self):
        super().get_info()
        print('Type of airplane:', self.type_of_airplane,
              'Flight altitude:', self.flight_altitude)

    def change_height(self, height_diff):  # add method for changing height
        '''Changing flight altitude'''
        self.flight_altitude += height_diff
        super().get_info()
        print('Type of airplane:', self.type_of_airplane,
              'Flight altitude:', self.flight_altitude)


class car(Transport):
    car_model = None
    drive_unit = None

    def __init__(self, type, car_model, drive_unit, max_speed, year):
        super().__init__(type, max_speed, year)
        self.car_model = car_model
        self.drive_unit = drive_unit

    def get_info(self):
        super().get_info()
        print('Car model:', self.car_model, 'Drive unit:', self.drive_unit)


airplane1 = Airplane('Airplane', 'Passenger', 10000, 450, 2005)
airplane2 = Airplane('Airplane', 'Passenger', 8000, 450, 2005)

print(airplane2 < airplane1)

# print(airplane1)
# airplane.get_info()     # delete if we want print only new height
# car = car('Car', 'BMW', 'four-wheel drive', 250, 2020)
# car.get_info()
airplane1.change_height(-3000)    # difference between altitudes
# print(airplane.change_height.__doc__)   # print docstring

print(airplane2 < airplane1)

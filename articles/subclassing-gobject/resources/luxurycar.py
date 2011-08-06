import pygtk
pygtk.require('2.0')
import gobject

from car4 import Car

class LuxuryCar(Car):
    def do_engine_started(self, remaining_fuel):
        Car.do_engine_started(self, remaining_fuel)
        print 'Welcome to the Luxury Car'


if __name__ == '__main__':
    luxuryCar = LuxuryCar()
    luxuryCar.start()

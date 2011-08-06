import pygtk
pygtk.require('2.0')
import gobject

from car4 import Car

def myCallback(obj, remaining_fuel, data=None):
    print '***** Beginning of User callback *****'
    print 'The engine is starting and we still have %f of fuel' % remaining_fuel
    print '***** End of User callback *****'

def lastCallback(obj, remaining_fuel, data=None):
    print '***** Callback connected with connect_after *****'
    obj.set_property('fuel', remaining_fuel - 10)
    print 'Now we have %f of fuel' % obj.get_property('fuel')
    print '***** End of this callback *****'

def test():
    aCar = Car()
    aCar.connect('engine-started', myCallback)
    aCar.connect_after('engine-started', lastCallback)

    aCar.start()

if __name__ == '__main__':
    test()

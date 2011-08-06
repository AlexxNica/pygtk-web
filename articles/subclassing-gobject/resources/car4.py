import pygtk
pygtk.require('2.0')
import gobject

from car1 import Car

def myCallback(obj, property):
    if obj.get_property('fuel') < 10:
        print 'we are running out of fuel!!'

def test():
    aCar = Car()
    aCar.connect('notify::fuel', myCallback)
    aCar.set_property('fuel', 5.0)

if __name__ == '__main__':
    test()

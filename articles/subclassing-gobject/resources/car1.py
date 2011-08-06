import pygtk
pygtk.require('2.0')
import gobject

class Car(gobject.GObject):
    __gproperties__ = {
        'fuel' : (gobject.TYPE_FLOAT,                        # type
                  'fuel of the car',                         # nick name
                  'amount of fuel that remains in the tank', # description
                  0,                                         # minimum value
                  60,                                        # maximum value
                  50,                                        # default value
                  gobject.PARAM_READWRITE)                   # flags
    }

    def __init__(self):
        gobject.GObject.__init__(self)
        self.fuel = 50

    def do_get_property(self, property):
        if property.name == 'fuel':
            return self.fuel
        else:
            raise AttributeError, 'unknown property %s' % property.name

    def do_set_property(self, property, value):
        if property.name == 'fuel':
            self.fuel = value
        else:
            raise AttributeError, 'unknown property %s' % property.name

gobject.type_register(Car)

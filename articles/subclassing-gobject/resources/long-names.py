import pygtk
pygtk.require('2.0')
import gobject

class Style(gobject.GObject):
    __gproperties__ = {
        'foreground_color' : (gobject.TYPE_STRING, 'foreground color',
                  'string that represents the foreground color',
                  'black', gobject.PARAM_READWRITE),
        'background_color' : (gobject.TYPE_STRING, 'background color',
                  'string that represents the background color',
                  'white', gobject.PARAM_READWRITE),
        }

    def __init__(self):
        gobject.GObject.__init__(self)
        self.foreground_color = 'black'
        self.background_color = 'white'

    def do_get_property(self, property):
        if property.name == 'foreground-color':
            return self.foreground_color
        elif property.name == 'background-color':
            return self.background_color
        else:
            raise AttributeError, 'unknown property %s' % property.name

    def do_set_property(self, property, value):
        if property.name == 'foreground-color':
            self.foreground_color = value
        elif property.name == 'background-color':
            self.background_color = value
        else:
            raise AttributeError, 'unknown property %s' % property.name

gobject.type_register(Style)

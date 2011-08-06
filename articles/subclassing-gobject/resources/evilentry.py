import pygtk
pygtk.require('2.0')
import gtk
import gobject

class EvilEntry(gtk.Entry):
    __gsignals__ = {
        'paste_clipboard' : 'override'
        }

    def __init__(self):
        gobject.GObject.__init__(self)

    def do_paste_clipboard(self):
        print "You tried to paste something but you can't!! muHAHAHA"

gobject.type_register(EvilEntry)

if __name__ == '__main__':
    win = gtk.Window()
    win.connect('destroy', lambda e: gtk.main_quit())

    entry = EvilEntry()
    entry.show()
    win.add(entry)
    win.show()

    gtk.main()

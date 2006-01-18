import gtk
import gtk.gdk
import math

class SemiCirculo(gtk.DrawingArea):
	def __init__(self):
		gtk.DrawingArea.__init__(self)
		self.connect("expose-event", self.expose)
	
	def expose(self, widget, event):
		pass

	def draw(self, context):
		pass

def main():
	window = gtk.Window()
	semicirculo = SemiCirculo()

	# Añadimos nuestro widget a la ventana
	window.add(semicirculo) 	
	# Conectamos el evento destroy con la salida del bucle de eventos
	window.connect("destroy", gtk.main_quit)
	# Dibujamos toda la ventana
	window.show_all()

	# Comenzamos el bucle de eventos
	gtk.main()

if __name__ == "__main__":
	main()

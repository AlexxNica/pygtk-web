import gtk
import gtk.gdk
import math

class SemiCirculo(gtk.DrawingArea):
	def __init__(self):
		gtk.DrawingArea.__init__(self)
		self.add_events(gtk.gdk.BUTTON_PRESS_MASK |
				gtk.gdk.BUTTON1_MOTION_MASK)
		
		self.connect("expose_event", self.expose)
		self.connect("button_press_event", self.pressing)
		self.connect("motion_notify_event", self.moving)
		
		#Desplazamiento
		self.desp = 0
	
	def pressing(self, widget, event):
		self.pressing_x = event.x
		
	def moving(self, widget, event):
		#Determinamos si nos movemos a la izquierda
		#o hacia la derecha
		if (self.pressing_x - event.x) > 1:
			self.desp = self.desp + 0.1
		else:
			self.desp = self.desp - 0.1
		
		self.pressing_x = event.x
		
		#Volvemos a dibujar el contexto
		self.draw(self.context)
		#Redibujamos el widget
		self.queue_draw()

	def expose(self, widget, event):
		self.context = widget.window.cairo_create()
		
		self.context.rectangle(event.area.x, event.area.y,
				event.area.width, event.area.height)
		self.context.clip()
	
		self.draw(self.context)
		return False

	def draw(self, context):
		rect = self.get_allocation()
		x = rect.x + rect.width / 2
		y = rect.y + rect.height / 2

		radius = min(rect.width / 2, rect.height / 2) - 5
		
		context.arc(x, y, radius, 0 + self.desp ,
				(1 * math.pi) + self.desp)
		
		context.set_source_rgb(0.7, 0.8, 0.1)
		context.fill_preserve()
		
		context.set_source_rgb(0, 0, 0)
		context.stroke()

	


def main():
	window = gtk.Window()
	clock = SemiCirculo()
	
	window.add(clock)
	window.connect("destroy", gtk.main_quit)
	window.show_all()
	
	gtk.main()

if __name__ == "__main__":
	main()

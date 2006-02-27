#!/usr/bin/env python
# clock_ex4.py

# a pygtk widget that implements a clock face
# porting of Davyd Madeley's
# http://www.gnome.org/~davyd/gnome-journal-cairo-article/clock-ex4.c

# author: Lawrence Oluyede <l.oluyede@gmail.com>
# date: 16 February 2005

import gtk
from gtk import gdk
import gobject

import math
from datetime import datetime

class EggClockFace(gtk.DrawingArea):
    # EggClockFace signals
    __gsignals__ = dict(time_changed=(gobject.SIGNAL_RUN_FIRST,
                                      gobject.TYPE_NONE,
                                      (gobject.TYPE_INT, gobject.TYPE_INT)))

    def __init__(self):
        super(EggClockFace, self).__init__()

        # gtk.Widget signals
        self.connect("expose_event", self.expose)
        self.connect("button_press_event", self.button_press)
        self.connect("button_release_event", self.button_release)
        self.connect("motion_notify_event", self.motion_notify)

        # make them private
        self._time = None # the time on the clock face
        self._minute_offset = 0 # the offset of the minutes hand
        self._dragging = False # true if the interface is being dragged

        # unmask events
        self.add_events(gdk.BUTTON_PRESS_MASK |
                        gdk.BUTTON_RELEASE_MASK |
                        gdk.POINTER_MOTION_MASK)

        self.update()
        # update the clock once a second
        gobject.timeout_add(1000, self.update)

    def expose(self, widget, event):
        context = widget.window.cairo_create()

        # set a clip region for the expose event
        context.rectangle(event.area.x, event.area.y,
                          event.area.width, event.area.height)
        context.clip()

        self.draw(context)

        return False

    def button_press(self, widget, event):
        minutes = self.time.minute + self._minute_offset

        # from
        # http://mathworld.wolfram.com/Point-LineDistance2-Dimensional.html
        px = event.x - widget.get_allocation().width / 2
        py = widget.get_allocation().height / 2 - event.y
        lx = math.sin(math.pi / 30 * minutes)
        ly = math.cos(math.pi / 30 * minutes)
        u = lx * px + ly * py

        # on opposite side of origin
        if u < 0:
            return False

        d2 = math.pow(px - u * lx, 2) + math.pow(py - u * ly, 2)

        if d2 < 25: # 5 pixels away from the line
            self._dragging = True
            print "got minute hand"

        return False

    def button_release(self, widget, event):
        if self._dragging:
            self._dragging = False
            self.emit_time_changed_signal(event.x, event.y)

        return False

    def motion_notify(self, widget, event):
        if self._dragging:
            self.emit_time_changed_signal(event.x, event.y)

    def emit_time_changed_signal(self, x, y):
        # decode the minute hand
        # normalize the coordinates around the origin
        x -= self.get_allocation().width / 2
        y -= self.get_allocation().height / 2

        # phi is a bearing from north clockwise, use the same geometry as we
        # did to position the minute hand originally
        phi = math.atan2(x, -y)
        if phi < 0:
            phi += math.pi * 2

        hour = self.time.hour
        minute = phi * 30 / math.pi

        # update the offset
        self._minute_offset = minute - self.time.minute
        self.redraw_canvas()

        self.emit("time_changed", hour, minute)

    def draw(self, context):
        rect = self.get_allocation()

        x = rect.x + rect.width / 2.0
        y = rect.y + rect.height / 2.0
        radius = min(rect.width / 2.0, rect.height / 2.0) - 5

        # clock back
        context.arc(x, y, radius, 0, 2.0 * math.pi)
        context.set_source_rgb(1, 1, 1)
        context.fill_preserve()
        context.set_source_rgb(0, 0, 0)
        context.stroke()

        # clock ticks
        for i in xrange(12):
            context.save()

            if i % 3 == 0:
                inset = 0.2 * radius
            else:
                inset = 0.1 * radius
                context.set_line_width(0.5 * context.get_line_width())

            context.move_to(x + (radius - inset) * math.cos(i * math.pi / 6.0),
                            y + (radius - inset) * math.sin(i * math.pi / 6.0))
            context.line_to(x + radius * math.cos(i * math.pi / 6.0),
                            y + radius * math.sin(i * math.pi / 6.0))
            context.stroke()
            context.restore()

        # clock hands
        hours = self.time.hour
        minutes = self.time.minute + self._minute_offset
        seconds = self.time.second

        # hour hand:
        # the hour hand is rotated 30 degrees (pi/6 r) per hour +
        # 1/2 a degree (pi/360) per minute
        context.save()
        context.set_line_width(2.5 * context.get_line_width())
        context.move_to(x, y)
        context.line_to(x + radius / 2 * math.sin(
            math.pi / 6 * hours + math.pi / 360 * minutes),
                        y + radius / 2 * -math.cos(
            math.pi / 6 * hours + math.pi / 360 * minutes))
        context.stroke()
        context.restore()

        # minute hand:
        # the minute hand is rotated 6 degrees (pi/30 r) per minute
        context.move_to(x, y)
        context.line_to(x + radius * 0.75 * math.sin(math.pi / 30 * minutes),
                        y + radius * 0.75 * -math.cos(math.pi / 30 * minutes))
        context.stroke()

        # seconds hand:
        # operates identically to the minute hand
        context.save()
        context.set_source_rgb(1, 0, 0) # red
        context.move_to(x, y)
        context.line_to(x + radius * 0.7 * math.sin(math.pi / 30 * seconds),
                        y + radius * 0.7 * -math.cos(math.pi / 30 * seconds))
        context.stroke()
        context.restore()

    def redraw_canvas(self):
        if self.window:
            alloc = self.get_allocation()
            #rect = gdk.Rectangle(alloc.x, alloc.y, alloc.width, alloc.height)
            #self.window.invalidate_rect(rect, True)
            self.queue_draw_area(alloc.x, alloc.y, alloc.width, alloc.height)
            self.window.process_updates(True)

    def update(self):
        # update the time
        self.time = datetime.now()

        return True # keep running this event

    # public access to the time member
    def _get_time(self):
        return self._time
    def _set_time(self, datetime):
        self._time = datetime
        self.redraw_canvas()
    time = property(_get_time, _set_time)

def time_changed_cb(widget, hours, minutes):
    print "::time-changed - %02i:%02i" % (hours, minutes)

def main():
    window = gtk.Window()
    clock = EggClockFace()

    window.add(clock)
    window.connect("destroy", gtk.main_quit)
    clock.connect("time_changed", time_changed_cb)
    window.show_all()

    gtk.main()

if __name__ == "__main__":
    main()

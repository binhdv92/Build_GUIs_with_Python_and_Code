import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def on_window_main_destroy(self, *args):
        Gtk.main_quit()

    #def onButtonPressed(self, button):
    #    print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("gui6.glade")
builder.connect_signals(Handler())

window = builder.get_object("window_main")
window.show_all()

Gtk.main()
# GUI_With_Gtk3_Glade_Python3

# Introduction

# This example have tested on the following version of components
Gtk 3.26.1
Glade 2.22.1

# Note
1. There is an issue with Glade 3.22.1 that the "GtkStatusbar" do not show on "Containers"
- The workaround is add ***<glade-widget-class-ref name="GtkStatusbar"\/>*** at below the ***<glade-widget-class-ref name="GtkToolbar"\/>*** line on the ***/usr/share/glade/catalogs/gtk+.xml*** file
- Folloing command is in order to open gtk+.xml file
> $ sudo gedit /usr/share/glade/catalogs/gtk+.xml


# GUI_With_Gtk3_Glade_Python3

# Introduction
- This repo is a example code to build a simple Graphic User Interface (GUI) that randomly show one by one image on a folder
- This repo is based on the youtube video tutorial [Build GUIs with Python and Glade](https://www.youtube.com/watch?v=9zDYCFWTbSw) by Terry Howald.


# This example have tested on the following version of components
- Python 3.6.9
- Gtk 3.26.1
- Glade 2.22.1


# Result
- Affer run the gui6.py file then you will be expected see the gui as below
![Reuslt](./media/result.PNG)

# Note
1. There is an issue with Glade 3.22.1 that the "GtkStatusbar" do not show on "Containers"
- The workaround is add ***<glade-widget-class-ref name="GtkStatusbar"\/>*** at below the ***<glade-widget-class-ref name="GtkToolbar"\/>*** line on the ***/usr/share/glade/catalogs/gtk+.xml*** file
- Folloing command is in order to open gtk+.xml file
> $ sudo gedit /usr/share/glade/catalogs/gtk+.xml


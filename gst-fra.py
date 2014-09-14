#!/usr/bin/env python

import gi, gi.repository
from gi.repository import Gst, Gtk

import sys

Gst.init(None)
Gtk.init(sys.argv)

class MainWindow(object):
    def __init__(self):
        self.builder = Gtk.Builder ()
        self.builder.add_from_file ('gstfra.ui')

        self.slider = self.builder.get_object('frequency')
        self.slider.connect ("value-changed", self.freq_cb)

        self.window = self.builder.get_object('MainWindow')
        self.window.connect ("destroy", lambda app: Gtk.main_quit())
        self.window.show_all()

        self.pipeline = Gst.parse_launch('audiotestsrc name=src volume=1 ! autoaudiosink')
        self.src = self.pipeline.get_by_name('src')
        self.src.props.freq = 100
        self.pipeline.set_state(Gst.State.PLAYING)

    def freq_cb(self, widget):
        self.src.props.freq = widget.get_value()


if __name__ == "__main__":
    w = MainWindow()
    sys.exit( Gtk.main() )



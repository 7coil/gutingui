# Copyright (c) 2013 David Holm <dholmster@gmail.com>
# This file is part of SimpleGUITk - https://github.com/dholm/simpleguitk
# See the file 'COPYING' for copying permission.

from __future__ import division

try:
    import Tkinter as tkinter
except ImportError:
    import tkinter

from PIL import ImageTk
from PIL import Image

import sys

from .canvas import Canvas
from .control_objects import Button
from .control_objects import Input
from .control_objects import Label
from .input import InputAdapter
from .timers import destroy as destroy_timers


class Frame(object):
    def _create_root(self, title):
        root = tkinter.Tk()
        root.wm_title(title)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.protocol('WM_DELETE_WINDOW', root.quit)
        return root

    def _background_init(self, image):
        background_image = ImageTk.PhotoImage(Image.open(image))
        background_label = tkinter.Label(self._root, image=background_image)
        background_label.image = background_image
        background_label.grid()
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def _canvas_init(self, width = None, height = None, padding = None, target_framerate = None, show_panel = None):
        canvas_frame = tkinter.Frame(self._root)
        self._canvas = Canvas(canvas_frame, width = width, height = height, target_framerate = target_framerate)
        if show_panel:
            canvas_frame.grid(row=0, column=1, rowspan=2, padx=padding, pady=padding, sticky=(tkinter.N, tkinter.S, tkinter.W, tkinter.E))
        else:
            canvas_frame.grid(padx=padding, pady=padding)

    def _control_frame_init(self, width):
        self._control_frame = tkinter.Frame(self._root, width=width)
        self._control_frame.grid(row=0, column=0, padx=5, pady=5)

    def _input_init(self):
        status_frame = tkinter.Frame(self._root, width=120, height=85)
        status_frame.pack_propagate(0)
        canvas_widget = self._canvas._get_widget()
        self._input = InputAdapter(status_frame, self._root, canvas_widget)
        status_frame.grid(row=1, column=0, sticky=(tkinter.W, tkinter.E),
                          padx=5, pady=5)

    def __init__(self,
        title = None,
        canvas_width = None,
        canvas_height = None,
        control_width = None,
        canvas_padding = None,
        show_panel = None,
        target_framerate = None,
        background_image = None):
        self._root = self._create_root(title)

        if background_image:
            self._background_init(background_image)

        self._canvas_frame = None
        self._canvas = None
        self._canvas_init(width = canvas_width, height = canvas_height, padding = canvas_padding, target_framerate = target_framerate, show_panel = show_panel)

        self._control_frame = None
        self._controls = []

        self._input = None
        self._key_label = None
        self._mouse_label = None

        if show_panel:
            self._control_frame_init(control_width)
            self._input_init()

    def _shutdown(self):
        destroy_timers()
        self._canvas.destroy()
        self._root.destroy()
        sys.exit(0)

    def start(self):
        try:
            self._root.mainloop()
        except KeyboardInterrupt:
            pass
        finally:
            self._shutdown()

    def set_draw_handler(self, draw_handler):
        self._canvas.set_draw_handler(draw_handler)

    def add_button(self, text, button_handler, width=None):
        button = Button(self._control_frame, text, button_handler, width)
        self._controls.append(button)
        return button

    def add_label(self, text):
        label = Label(self._control_frame, text)
        self._controls.append(label)
        return label

    def add_input(self, text, input_handler, width):
        inp = Input(self._control_frame, text, input_handler, width)
        self._controls.append(inp)
        return inp

    def set_keydown_handler(self, key_handler):
        self._input.set_keydown_handler(key_handler)

    def set_keyup_handler(self, key_handler):
        self._input.set_keyup_handler(key_handler)

    def set_mouseclick_handler(self, mouse_handler):
        self._input.set_mouseclick_handler(mouse_handler)

    def set_mousedrag_handler(self, mouse_handler):
        self._input.set_mousedrag_handler(mouse_handler)

    def set_canvas_background(self, color):
        self._canvas.set_background(color)

    def get_canvas_textwidth(self, text, size, face='serif'):
        return self._canvas.get_textwidth(text, size, face)


def create_frame(
    title = "GutinGUI",
    canvas_width = 800,
    canvas_height = 600,
    control_width = 200,
    *,
    canvas_padding = 5,
    show_panel = True,
    target_framerate = 60,
    background_image = None):
      return Frame(
        title = title,
        canvas_width = canvas_width,
        canvas_height = canvas_height,
        control_width = control_width,
        canvas_padding = canvas_padding,
        show_panel = show_panel,
        target_framerate = target_framerate,
        background_image = background_image
    )

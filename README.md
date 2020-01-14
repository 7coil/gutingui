# GutinGUI

**GutinGUI** is a wrapper for the [CodeSkulptor](http://www.codeskulptor.org/) *SimpleGUI* API using *TkInter*.
This is a fork of [`dholm/simpleguitk`](https://github.com/dholm/simpleguitk), with some changes to make it suitable for use in our CS1822 course.

*CodeSkulptor* is a browser-based Python interpreter used in the online
course "[An Introduction to Interactive Programming in Python](https://www.coursera.org/course/interactivepython)".

This wrapper makes it easier to work in the development environment of your
choice while still being able to quickly test your implementation without using
a web browser.

## Fork Additions
This fork adds three extra named arguments for `simplegui.create_frame`.
In addition, existing arguments can be called with named arguments.

New | Argument           | Default    | Description
--- | ------------------ | ---------- | ----------------------
No  | `title`            | "GutinGUI" | The title of the window
No  | `canvas_width`     | 800        | The width of the canvas
No  | `canvas_height`    | 600        | The height of the canvas
Yes | `canvas_padding`   | 5          | The padding around the canvas.
No  | `control_width`    | 200        | The width of the control panel. Note that the control panel is above the input panel (the one with Key and Mouse).
Yes | `show_panel`       | True       | Make the control frame and the input frame visible. When hidden, the canvas takes up the space of the entire window.
Yes | `target_framerate` | 60         | The frame rate the program runs at. May destroy your program if changed if you've tied the physics to the framerate. Whoopsiedaisy.


There's no way this horrible hack is going onto pypi, so you're going to have to set your `PYTHONPATH` environment variable.

## Requirements
- [Pillow](https://github.com/python-imaging/Pillow) in order to use images.
- [Pygame](http://www.pygame.org/) for sound support.
- [matplotlib](http://matplotlib.org/) for SimplePlot support.

None of these are strict requirements as SimpleGUITk will run without them as
long as you don't need to use the *SimpleGUI Images* or *SimpleGUI Sounds*
APIs.

## Usage
Although GutinGUI is a drop-in replacement, you should probably use a try-catch statement to utilise the new named arguments within `simplegui.create_frame`.

```py
import gutingui as simplegui
```

Assuming you intend to eventually run your code in CodeSkulptor make it a habit
to test it often. As of this writing some of Python's language features are
unavailable in CodeSkulptor and catching these early on makes it easier to make
sure your implementation works as expected.

One important difference between SimpleGUITk and CodeSkulptor is that due to
the design of TkInter the call to *frame.start()* is going to block until the
application terminates. Simply make sure that it is called as the last line of
the application.

To use SimplePlot just import it the same way as in CodeSkulptor.

```py
import simpleplot
```

## Versions
- Refer to https://github.com/dholm/simpleguitk#changes.

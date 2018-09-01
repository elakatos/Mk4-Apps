"""This is a simple hello world app in cat language. Also light up, because cats like lasers."""

___name___         = "Hello World"
___license___      = "MIT"
___dependencies___ = ["sleep", "app"]
___categories___   = ["EMF"]

import ugfx, os, time, sleep, app
from tilda import Buttons,LED


# initialize screen
ugfx.init()
ugfx.clear(ugfx.BLACK)

Buttons.enable_interrupt(Buttons.BTN_B, lambda button_id:app.restart_to_default(), on_press=True, on_release=False)

while True:
	ugfx.set_default_font(ugfx.FONT_TITLE)
	ugfx.set_default_font(ugfx.FONT_NAME)
	ugfx.text(20, 30, "Meow!", ugfx.WHITE)
	LED(LED.RED).on()

ugfx.clear()
app.restart_to_default()

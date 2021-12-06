import dearpygui.dearpygui as dpg
from sixth import sixth_misc

def sixth1():
    dpg.add_text("Determine the most accurate equation:")
    dpg.add_text("1)    √")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="n1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("=")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="x1", decimal=True)
    dpg.add_text("2) ")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="n2", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("/")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="n22", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("=")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="x2", decimal=True)

    dpg.add_button(label="Go!", callback=sixth_misc.save_callback, id="go")
    dpg.set_item_pos("go", [500, 170])
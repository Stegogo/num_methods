import dearpygui.dearpygui as dpg
from second import second_misc

def second1():
    dpg.add_text("Round the doubtful digits and \nleave the correct digits of the number:")
    dpg.add_input_text(width=100, id="a1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("(±")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="A1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text(")")
    dpg.add_button(label="Go!", callback=second_misc.save_callback, id="go2")
    dpg.set_item_pos("go2", [500, 165])
    dpg.add_input_text(width=100, id="b1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("(δ")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="B1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text(")")
    dpg.add_button(label="Go!", callback=second_misc.save_callback, id="go22")
    dpg.set_item_pos("go22", [500, 225])
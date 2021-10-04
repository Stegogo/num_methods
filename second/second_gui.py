import dearpygui.dearpygui as dpg
from second import second_misc

def add_buttons():
    global new_entry, new_entry2
    new_entry = dpg.add_input_text(width=40, decimal=True, id="new_button1")
    new_entry2 = dpg.add_input_text(width=40, decimal=True, id="new_button2")

def delete_buttons():
    dpg.delete_item("new_button1")
    dpg.delete_item("new_button2")

def second1():
    dpg.add_text("  x ")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=40, id="2x_1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=40, id="2x_2", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=40, id="2x_3", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=40, id="2x_4", decimal=True)
    
    dpg.add_text("f(x)")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=40, id="2fx_1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=40, id="2fx_2", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=40, id="2fx_3", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=40, id="2fx_4", decimal=True)

    dpg.add_button(label="Add Buttons", callback=add_buttons, id="add_button")
    dpg.add_button(label="Delete Buttons", callback=delete_buttons, id="delete_button")

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
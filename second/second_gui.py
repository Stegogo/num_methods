import dearpygui.dearpygui as dpg
from second import second_misc

"""def add_buttons():
    global new_entry, new_entry2
    new_entry = dpg.add_button(label="N", before="2x_4", id="new_button1")
    new_entry2 = dpg.add_button(label="M", before="2fx_4", id="new_button2")

def delete_buttons():
    dpg.delete_item("new_button1")
    dpg.delete_item("new_button2")
"""
def second1():
    dpg.add_text("Construct the Lagrange interpolating\npolynomial:")
    dpg.add_text("  x ")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2x_1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2x_2", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2x_3", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2x_4", decimal=True)
    
    dpg.add_text("f(x)")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2fx_1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2fx_2", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2fx_3", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2fx_4", decimal=True)

    dpg.add_text("And calculate values at given points:")
    dpg.add_text("  x ")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2dx_1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2dx_2", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2dx_3", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=70, id="2dx_4", decimal=True)


    dpg.add_button(label="Go!", callback=second_misc.save_callback, id="go2")
    dpg.set_item_pos("go2", [500, 180])
    
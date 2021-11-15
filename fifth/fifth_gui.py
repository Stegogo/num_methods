import dearpygui.dearpygui as dpg
from fifth import fifth_misc

def fifth1():
    dpg.add_text("Solve the nonlinear equation and\nspecify the roots with Newton\nand bisection methods.")
    dpg.add_input_text(width=450, id="5expr")
    dpg.add_same_line(spacing=10)
    dpg.add_button(label="Go!", callback=fifth_misc.save_callback, id="go5")
    dpg.set_item_pos("go5", [500, 195])
    
    
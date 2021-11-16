import dearpygui.dearpygui as dpg
from fifth import fifth_misc

def fifth1():
    dpg.add_text("Solve the nonlinear equation.\nSpecify the roots with Newton\nand bisection methods.")
    dpg.add_input_text(width=450, id="5expr")
    dpg.add_same_line(spacing=10)
    dpg.add_text("[")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=50, id="5_l_limit")
    dpg.add_same_line(spacing=10)
    dpg.add_text(";")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=50, id="5_r_limit")
    dpg.add_same_line(spacing=10)
    dpg.add_text("]")
    dpg.add_button(label="Go!", callback=fifth_misc.save_callback, id="go5")
    dpg.set_item_pos("go5", [540, 105])
    
    
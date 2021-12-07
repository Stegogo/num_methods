import dearpygui.dearpygui as dpg
from sixth import sixth_misc

def sixth1():
    dpg.add_text("Compose a solution of the Cauchy problem\n"
                 "for the ordinary first-order differential\n"
                 "equation on a segment with a step h=0.1\n"
                 "under the inital conditions:\n")
    dpg.add_radio_button(items=["Euler method", "Euler-Cauchy method"], callback=sixth_misc.switch_modes)
    dpg.add_text("y' = x +")
    dpg.add_same_line(spacing=10)
    dpg.add_combo(items=["sin", "cos"], callback=sixth_misc.expr.set_sin_or_cos, width=110, default_value="sin")
    dpg.add_same_line(spacing=10)
    dpg.add_text("(y/")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="6expr", default_value="1")
    dpg.add_same_line(spacing=10)
    dpg.add_text(")")
    
    dpg.add_text("Starting point: ")
    dpg.add_same_line(spacing=10)
    dpg.add_text("y(")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="6start_x", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text(") =")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="6start_y", decimal=True)
    
    dpg.add_text("Interval: ")
    dpg.add_same_line(spacing=10)
    dpg.add_text("[")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="6interval_begin", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text(";")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="6interval_end", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text(f"]")
    dpg.add_button(label="Go!", callback=sixth_misc.save_callback, id="go6")
    dpg.set_item_pos("go6", [630, 420])
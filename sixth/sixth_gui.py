import dearpygui.dearpygui as dpg
from sixth import sixth_misc

expr = sixth_misc.Expression("sin")

def sixth1():
    dpg.add_text("Compose a solution of the Cauchy problem\n"
                 "for the ordinary first-order differential\n"
                 "equation on a segment with a step h=0.1\n"
                 "under the inital conditions:\n")
    dpg.add_radio_button(items=["Euler method", "Euler-Cauchy method"], callback=sixth_misc.switch_modes)
    dpg.add_text("y' = x +")
    dpg.add_same_line(spacing=10)
    dpg.add_combo(items=["sin", "cos"], callback=expr.get_sin_or_cos, width=110, default_value="sin")
    dpg.add_same_line(spacing=10)
    dpg.add_text("(y/")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="6expr")
    dpg.add_same_line(spacing=10)
    dpg.add_text(")")
    dpg.add_button(label="Go!", callback=sixth_misc.save_callback, id="go6")
    dpg.set_item_pos("go6", [500, 360])
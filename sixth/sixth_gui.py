import dearpygui.dearpygui as dpg
from sixth import sixth_misc

def sixth1():
    dpg.add_text("Compose a solution of the Cauchy problem\n"
                 "for the ordinary first-order differential\n"
                 "equation on a segment with a step h=0.1\n"
                 "under the inital conditions:\n")
    dpg.add_radio_button(label="Radio A", items=["Euler method", "Euler-Cauchy method"], callback=sixth_misc.save_callback)
    dpg.add_button(label="Go!", callback=sixth_misc.save_callback, id="go6")
    dpg.set_item_pos("go6", [500, 170])
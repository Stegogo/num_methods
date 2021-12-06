import dearpygui.dearpygui as dpg
from sixth import sixth_misc

def sixth1():
    

    dpg.add_button(label="Go!", callback=sixth_misc.save_callback, id="go6")
    dpg.set_item_pos("go6", [500, 170])
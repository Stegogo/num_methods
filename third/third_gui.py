import dearpygui.dearpygui as dpg
from third import third_misc

def third3():
    dpg.add_text("Find the marginal absolute and relative\nerrors of numbers that have\nonly correct digits:")
    dpg.add_input_text(width=400, id="c1", decimal=True)
    dpg.add_button(label="Go!", callback=third_misc.save_callback, id="go3")
    dpg.set_item_pos("go3", [500, 200])
    dpg.add_collapsing_header(label="a")
    dpg.add_collapsing_header(label="b")
    with dpg.collapsing_header(label="i"):
        dpg.add_text("aaaaaa")
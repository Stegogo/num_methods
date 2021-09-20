import dearpygui.dearpygui as dpg
from first import first_misc

 

def first1():
    dpg.add_text("Determine the most accurate equation:")
    dpg.add_text("1)    √")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="n1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("=")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="x1", decimal=True)
    dpg.add_text("2) ")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="n2", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("/")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="n22", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("=")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="x2", decimal=True)

    dpg.add_button(label="Go!", callback=first_misc.save_callback, id="go")
    dpg.set_item_pos("go", [500, 130])

def first2():
    dpg.add_text("Round the doubtful digits and \nleave the correct digits of the number:")
    #dpg.add_radio_button("Radio1", items=["itemA", "itemB"], callback=first_misc.secondRadio)
    dpg.add_input_text(width=100, id="a1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("(±")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="A1", decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text(")")
    dpg.add_button(label="Go!", callback=first_misc.save_callback, id="go2")
    dpg.set_item_pos("go2", [500, 150])

def first3():
    dpg.add_text("Find the marginal absolute and relative\nerrors of numbers that have\nonly correct digits:")
    dpg.add_input_text(width=400, id="c1", decimal=True)
    dpg.add_button(label="Go!", callback=first_misc.save_callback, id="go3")
    dpg.set_item_pos("go3", [500, 180])
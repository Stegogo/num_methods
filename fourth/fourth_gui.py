import dearpygui.dearpygui as dpg
from fourth import fourth_misc

def fourth1():
    dpg.add_input_text(width=70, id="4integr_up", decimal=True)
    dpg.add_text("   ∫   ")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=250, id="4expr")
    dpg.add_same_line(spacing=10)
    dpg.add_text("dx")
    dpg.add_same_line(spacing=50)
    dpg.add_text("n =")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=50, id="4n", decimal=True)
    dpg.add_input_text(width=70, id="4integr_down", decimal=True)

    dpg.add_button(label="Go!", callback=fourth_misc.save_callback, id="go4")
    dpg.set_item_pos("go4", [590, 135])

    with dpg.collapsing_header(id="4rectangles", label="Rectangles method"):
        dpg.add_text("Left-hand rectangles method: ")
        dpg.add_same_line(spacing=50)
        dpg.add_text(" ",  id="4_lrect")
        dpg.add_text("Right-hand rectangles method: ")
        dpg.add_same_line(spacing=30)
        dpg.add_text(" ",  id="4_rrect")
        dpg.add_text("Mid-square method: ")
        dpg.add_same_line(spacing=200)
        dpg.add_text(" ",  id="4_mrect")
    with dpg.collapsing_header(id="4simpsons", label="Simpson's method"):
        dpg.add_text("Simpson's method: ")
        dpg.add_same_line(spacing=50)
        dpg.add_text(" ",  id="4_simpsons")
    with dpg.collapsing_header(id="4trapezoids", label="Trapezoids method"):
        dpg.add_text("Trapezoids method:")
        dpg.add_same_line(spacing=50)
        dpg.add_text(" ",  id="4_trapezoids")


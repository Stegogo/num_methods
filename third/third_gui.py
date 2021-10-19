import dearpygui.dearpygui as dpg
from third import third_misc

def third3():
    dpg.add_button(label="Go!", callback=third_misc.save_callback, id="go3")
    dpg.set_item_pos("go3", [590, 75])
    
    dpg.add_radio_button(["Odd task No.", "Even task No."], horizontal=True, callback=third_misc.show_contents, id="third_radio_buttons")
    
    dpg.add_text("  x ")
    dpg.add_same_line(spacing=150)
    dpg.add_text("f(x)")

    dpg.add_input_text(width=150, id="3x_1", decimal=True, default_value='2.4')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_1", decimal=True, default_value='3.526')

    dpg.add_input_text(width=150, id="3x_2", decimal=True, default_value='2.6')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_2", decimal=True, default_value='3.782')

    dpg.add_input_text(width=150, id="3x_3", decimal=True, default_value='2.8')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_3", decimal=True, default_value='3.945')
    dpg.add_same_line(spacing=40)#!-----------n1 button-----------
    dpg.add_text("x1 = ")
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=100, id="3x_x11", decimal=True, default_value='2.4')
    dpg.add_same_line(spacing=20)
    dpg.add_text("+ (")
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=100, id="3x_x12", decimal=True, default_value='0.05')
    dpg.add_same_line(spacing=20)
    dpg.add_text("*")
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=50, id="3x_n1", label=')', decimal=True)

    dpg.add_input_text(width=150, id="3x_4", decimal=True, default_value='3.0')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_4", decimal=True, default_value='4.043')
    dpg.add_same_line(spacing=40)#!-----------n2 button-----------
    dpg.add_text("x2 = ")
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=100, id="3x_x21", decimal=True, default_value='4.04')
    dpg.add_same_line(spacing=20)
    dpg.add_text("- (")
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=100, id="3x_x22", decimal=True, default_value='0.04')
    dpg.add_same_line(spacing=20)
    dpg.add_text("*")
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=50, id="3x_n2", label=')', decimal=True)

    dpg.add_input_text(width=150, id="3x_5", decimal=True, default_value='3.2')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_5", decimal=True, default_value='4.104')
    

    dpg.add_input_text(width=150, id="3x_6", decimal=True, default_value='3.4')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_6", decimal=True, default_value='4.155')
    dpg.add_same_line(spacing=40)#!-----------n1 results-----------
    dpg.add_text(f"y'(x1): ")
    dpg.add_same_line(spacing=20)
    dpg.add_text(f"     ", id="3result1")
    dpg.add_same_line(spacing=20)
    dpg.add_text(f"y''(x1): ")
    dpg.add_same_line(spacing=20)
    dpg.add_text(f"     ", id="3result2")
    
    dpg.add_input_text(width=150, id="3x_7", decimal=True, default_value='3.6')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_7", decimal=True, default_value='4.222')
    dpg.add_same_line(spacing=40)
    dpg.add_text(f"y'(x2): ")
    dpg.add_same_line(spacing=20)
    dpg.add_text(f"     ", id="3result3")
    dpg.add_same_line(spacing=20)
    dpg.add_text(f"y''(x2): ")
    dpg.add_same_line(spacing=20)
    dpg.add_text(f"     ", id="3result4")

    dpg.add_input_text(width=150, id="3x_8", decimal=True, default_value='3.8')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_8", decimal=True, default_value='4.331')

    dpg.add_input_text(width=150, id="3x_9", decimal=True, default_value='4.0')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_9", decimal=True, default_value='4.507')

    dpg.add_input_text(width=150, id="3x_10", decimal=True, default_value='4.2')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_10", decimal=True, default_value='4.775')

    dpg.add_input_text(width=150, id="3x_11", decimal=True, default_value='4.4')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_11", decimal=True, default_value='5.159')

    dpg.add_input_text(width=150, id="3x_12", decimal=True, default_value='4.6')
    dpg.add_same_line(spacing=20)
    dpg.add_input_text(width=150, id="3fx_12", decimal=True, default_value='5.683')


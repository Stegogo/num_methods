import dearpygui.dearpygui as dpg
import ctypes

got_res = False
handle = ctypes.CDLL("./libtest.so")     
handle.cppcalc1.argtypes = [ctypes.c_float]

def calc(n1, x1, n2, n22, x2):
    res = handle.cppcalc1(ctypes.c_float(n1), ctypes.c_float(x1), ctypes.c_float(n2), ctypes.c_float(n22), ctypes.c_float(x2))
    if res == 1:
        return f"√{int(n1)} is more accurate."
    elif res == 2:
        return f"{int(n2)}/{int(n22)} is more accurate."
    else:
        return "Calculation error."

def show_contents(sender, data):
    choice = dpg.get_value(sender)
    if(choice == "Odd task No."):
        dpg.configure_item("3x_1", default_value='2.4')
        dpg.configure_item("3fx_1", default_value='3.526')
        dpg.configure_item("3x_2", default_value='2.6')
        dpg.configure_item("3fx_2", default_value='3.782')
        dpg.configure_item("3x_3", default_value='2.8')
        dpg.configure_item("3fx_3", default_value='3.945')
        dpg.configure_item("3x_4", default_value='3.0')
        dpg.configure_item("3fx_4", default_value='4.043')
        dpg.configure_item("3x_5", default_value='3.2')
        dpg.configure_item("3fx_5", default_value='4.104')
        dpg.configure_item("3x_6", default_value='3.4')
        dpg.configure_item("3fx_6", default_value='4.155')
        dpg.configure_item("3x_7", default_value='3.6')
        dpg.configure_item("3fx_7", default_value='4.222')
        dpg.configure_item("3x_8", default_value='3.8')
        dpg.configure_item("3fx_8", default_value='4.331')

        dpg.configure_item("3x_x1", default_value='2.4 + (0.05')
        dpg.configure_item("3x_x2", default_value='4.04 - (0.04')

    elif (choice == "Even task No."):
        dpg.configure_item("3x_1", default_value='1.5')
        dpg.configure_item("3fx_1", default_value='10.517')
        dpg.configure_item("3x_2", default_value='2.0')
        dpg.configure_item("3fx_2", default_value='10.193')
        dpg.configure_item("3x_3", default_value='2.5')
        dpg.configure_item("3fx_3", default_value='9.807')
        dpg.configure_item("3x_4", default_value='3.0')
        dpg.configure_item("3fx_4", default_value='9.387')
        dpg.configure_item("3x_5", default_value='3.5')
        dpg.configure_item("3fx_5", default_value='8.977')
        dpg.configure_item("3x_6", default_value='4.0')
        dpg.configure_item("3fx_6", default_value='8.637')
        dpg.configure_item("3x_7", default_value='4.5')
        dpg.configure_item("3fx_7", default_value='8.442')
        dpg.configure_item("3x_8", default_value='5.0')
        dpg.configure_item("3fx_8", default_value='8.482')

        dpg.configure_item("3x_x1", default_value='1.6 + (0.08')
        dpg.configure_item("3x_x2", default_value='6.3 - (0.12')


def save_callback():
    global got_res
    n1 = dpg.get_value("n1")
    x1 = dpg.get_value("x1")
    n2 = dpg.get_value("n2")
    n22 = dpg.get_value("n22")
    x2 = dpg.get_value("x2")
    args = [n1, x1, n2, n22, x2]
    if '' in args:
        txt = "Incorrect input."
    else:
        args = [float(x) for x in args]
        txt = calc(args[0], args[1], args[2], args[3], args[4])
    
    if got_res == False:
        dpg.add_text(f"{txt}", before="go", id="result")
        got_res = True
    else:
        dpg.delete_item("result")
        dpg.add_text(f"{txt}", before="go", id="result")
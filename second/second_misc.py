import dearpygui.dearpygui as dpg
import ctypes

got_res = False
handle = ctypes.CDLL("./libtest.so")     
handle.cppcalc1.argtypes = [ctypes.c_float]

def calc(x1, x2, x3, x4, fx1, fx2, fx3, fx4):
    res = handle.cppcalc2(
        ctypes.c_float(x1), ctypes.c_float(x2), ctypes.c_float(x3), ctypes.c_float(x4),
        ctypes.c_float(fx1), ctypes.c_float(fx2), ctypes.c_float(fx3), ctypes.c_float(fx4))
    if res == 1:
        print("1")
    elif res == 2:
        print("2")
    else:
        print("else")

def save_callback():
    global got_res
    x1 = dpg.get_value("2x_1")
    x2 = dpg.get_value("2x_2")
    x3 = dpg.get_value("2x_3")
    x4 = dpg.get_value("2x_4")

    fx1 = dpg.get_value("2fx_1")
    fx2 = dpg.get_value("2fx_2")
    fx3 = dpg.get_value("2fx_3")
    fx4 = dpg.get_value("2fx_4")

    args = [x1, x2, x3, x4, fx1, fx2, fx3, fx4]
    if '' in args:
        txt = "Incorrect input."
    else:
        args = [float(x) for x in args]
        txt =   calc(args[0], args[1], args[2], args[3],
                    args[4], args[5], args[6], args[7])
    
    if got_res == False:
        dpg.add_text(f"{txt}", before="go", id="result")
        got_res = True
    else:
        dpg.delete_item("result")
        dpg.add_text(f"{txt}", before="go", id="result")
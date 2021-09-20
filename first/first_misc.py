import dearpygui.dearpygui as dpg
import ctypes

got_res = False
handle = ctypes.CDLL("./libtest.so")     
handle.cppcalc.argtypes = [ctypes.c_float]

def calc(n1, x1, n2, n22, x2):
    res = handle.cppcalc(ctypes.c_float(n1), ctypes.c_float(x1), ctypes.c_float(n2), ctypes.c_float(n22), ctypes.c_float(x2))
    if res == 1:
        return f"√{int(n1)} is more accurate."
    elif res == 2:
        return f"{int(n2)}/{int(n22)} is more accurate."
    else:
        return "Calculation error."


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
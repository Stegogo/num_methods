import dearpygui.dearpygui as dpg

def calc(n1, x1, n2, n22, x2):
    pass

def save_callback():
    print("Clicked!")
    n1 = dpg.get_value("n1")
    x1 = dpg.get_value("x1")
    n2 = dpg.get_value("n2")
    n22 = dpg.get_value("n22")
    x2 = dpg.get_value("x2")
    calc(n1, x1, n2, n22, x2)
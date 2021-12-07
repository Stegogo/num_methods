import dearpygui.dearpygui as dpg
import ctypes
from math import *
import sympy as sym
import numpy as np

got_res = False
handle = ctypes.CDLL("./libtest.so")     
handle.cppcalc1.argtypes = [ctypes.c_float]

class Expression:
    def __init__(self,function, expr, mode):
        self.function = function
        self.expr = expr
        self.mode = mode
    
    def set_sin_or_cos(self, sender, data):
        if (data == "sin"):
            self.function = "sin"
            print(self.function)
        else:
            self.function = "cos"
            print(self.function)
            
    def set_expr(self, value):
            self.expr = value
            
    def set_mode(self, sender, data):
        print("==", data)
        self.mode = data
        
expr = Expression("sin", "1", "Euler method")
        
def calc(n1, x1, n2, n22, x2):
    res = handle.cppcalc1(ctypes.c_float(n1), ctypes.c_float(x1), ctypes.c_float(n2), ctypes.c_float(n22), ctypes.c_float(x2))
    if res == 1:
        return f"√{int(n1)} is more accurate."
    elif res == 2:
        return f"{int(n2)}/{int(n22)} is more accurate."
    else:
        return "Calculation error."

def save_callback():
    expr.set_expr(dpg.get_value("6expr"))
    print(expr.function, expr.expr)
    
    global got_res
    function = expr.function
    a = dpg.get_value("6expr")
    start_x = float(dpg.get_value("6start_x"))
    start_y = float(dpg.get_value("6start_y"))
    interval_begin = float(dpg.get_value("6interval_begin"))
    interval_end = float(dpg.get_value("6interval_end"))
    h = 0.1
    
    a_parsed = sym.parse_expr(a, evaluate=True)
    func_parsed = eval(function)
    
    n = (interval_end - interval_begin)/h
    
    x_arr = [0]*100
    y_arr = [0]*100
    f_arr = [0]*100
    x_arr[0] = start_x
    y_arr[0] = start_y
    
    if (expr.mode == "Euler method"):
        print(expr.mode)
        for i in range(0, int(n)):
            x_arr[i+1] = x_arr[i]+h;
            y_arr[i+1] = y_arr[i] + (h*((func_parsed(x_arr[i]))*(y_arr[i]/a_parsed)));
            print(x_arr[i], y_arr[i])
    else:
        print(expr.mode)
        for i in range(0, int(n)):
            x_arr[i+1]=x_arr[i]+h;
            y_arr[i + 1] = y_arr[i] + h / 2 * (x_arr[i] + cos(y_arr[i] / a_parsed) + x_arr[i + 1] + cos((y_arr[i] + h * (x_arr[i] + cos(y_arr[i] / a_parsed))) / a_parsed));
            print(x_arr[i], y_arr[i])
    
    if got_res == False:
        with dpg.window(label=f"Plot for {expr.mode}", width=550, height=600, id="plot_window6"):
            datax = []
            datay = []
            for i in range(0, int(n)):
                datax.append(x_arr[i])
                datay.append(y_arr[i])
            with dpg.plot(height=500, width=500):
                dpg.add_plot_axis(dpg.mvXAxis, label="x")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", id="y_axis")
                dpg.add_line_series(datax, datay, parent="y_axis")
                
        with dpg.window(label=f"Table for {expr.mode}", id="table_window6"):
            with dpg.table(header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                
                for i in range(0, int(n)):
                    with dpg.table_row():
                        for j in range(0, 2):
                            if (j == 0):
                                dpg.add_text(f"{round(x_arr[i], 4)}")
                            else:
                                dpg.add_text(f"{round(y_arr[i], 4)}")
                
        got_res = True
    else:
        dpg.delete_item("plot_window6")
        dpg.delete_item("table_window6")
        
        with dpg.window(label=f"Plot for {expr.mode}", width=550, height=600, id="plot_window6"):
            datax = []
            datay = []
            for i in range(0, int(n)):
                datax.append(x_arr[i])
                datay.append(y_arr[i])
            with dpg.plot(height=500, width=500):
                dpg.add_plot_axis(dpg.mvXAxis, label="x")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", id="y_axis")
                dpg.add_line_series(datax, datay, parent="y_axis")
        
        with dpg.window(label=f"Table for {expr.mode}", id="table_window6"):
            with dpg.table(header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                
                for i in range(0, int(n)):
                    with dpg.table_row():
                        for j in range(0, 2):
                            if (j == 0):
                                dpg.add_text(f"{round(x_arr[i], 4)}")
                            else:
                                dpg.add_text(f"{round(y_arr[i], 4)}")
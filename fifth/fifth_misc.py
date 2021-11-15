import dearpygui.dearpygui as dpg
import ctypes
import ctypes
from math import *
import sympy as sym
import numpy as np

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

def save_callback():
    global got_res

    expr = dpg.get_value("5expr")
    x = sym.symbols('x')
    num_expr =  sym.parse_expr(expr)
    a = num_expr.subs(x, 1)
    
    

    if got_res == False:
        dpg.add_text(f"a", before="5expr", id="5_result")
        got_res = True
    else:
        dpg.delete_item("5_result")
        dpg.add_text(f"a", before="5expr", id="5_result")
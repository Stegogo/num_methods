import dearpygui.dearpygui as dpg
import ctypes
import ctypes
from math import *
import sympy as sym
import numpy as np

got_res = False
handle = ctypes.CDLL("./libtest.so")     
handle.cppcalc1.argtypes = [ctypes.c_float]

def newton(l_limit, r_limit, num_expr, diff_expr):
    arr_newton = []
    x = sym.symbols('x')
    for i in np.arange(l_limit, r_limit, 0.01):
        y1 = num_expr.subs(x, i)
        y2 = num_expr.subs(x, i+0.01)
        if (y1>0 and y2<0) or (y1<0 and y2>0):
            q = fabs(i-(i-num_expr.subs(x, i)/diff_expr.subs(x, i)))
            while (q>0.0001):
                i+=0.01
                x1=i
                x2=x1-num_expr.subs(x, x1)/diff_expr.subs(x, x1)
                x1=x2
                q=fabs(x1-x2)
            arr_newton.append(round(x1, 5))
    return arr_newton

def bisection(l_limit, r_limit, num_expr, diff_expr):
    arr_bisection = []
    x = sym.symbols('x')
    if (l_limit > r_limit) or (num_expr.subs(x, l_limit)*num_expr.subs(x, r_limit)==0):
        p = (l_limit+r_limit)/2
        y = num_expr.subs(x, p)
        p1 = l_limit
        p2 = r_limit
        while (fabs(y)>0.0001):
            if num_expr.subs(x, p1)*num_expr.subs(x, p2) < 0:
                p1=p1;
                p2=p;
                p=(p1+p2)/2;
            else:
                p1=p;
                p2=p2;
                p=(p1+p2)/2;
            y=num_expr.subs(x, p)
            c=fabs((p1-p2)/2)
        arr_bisection.append(p)
        
    else:
        arr_bisection.append("-")
    return arr_bisection
        

def save_callback():
    global got_res
    x = sym.symbols('x')
    expr = dpg.get_value("5expr")
    
    num_expr =  sym.parse_expr(expr)
    diff_expr = sym.diff(num_expr, x)
    
    l_limit = float(dpg.get_value("5_l_limit"))
    r_limit = float(dpg.get_value("5_r_limit"))
    
    arr_newton = newton(l_limit, r_limit, num_expr, diff_expr)

    if got_res == False:
        dpg.add_text(f"Newton method:\n{arr_newton}", before="5expr", id="5_result_newton")
        dpg.add_text(f"Bisection method:\n{arr_newton}", before="5_result_newton", id="5_result_bisection")
        got_res = True
    else:
        dpg.delete_item("5_result_newton")
        dpg.delete_item("5_result_bisection")
        dpg.add_text(f"Newton method: {arr_newton}", before="5expr", id="5_result_newton")
        dpg.add_text(f"Bisection method: {arr_newton}", before="5_result_newton", id="5_result_bisection")
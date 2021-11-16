import dearpygui.dearpygui as dpg
from math import *
import sympy as sym
import numpy as np

got_res = False

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

def bisection(l_limit, r_limit, num_expr):
    arr_bisection = []
    x = sym.symbols('x')
    p1 = l_limit
    p2 = r_limit
    p = float((p1+p2)/2)

    if (l_limit >= r_limit) or (num_expr.subs(x, p1) * num_expr.subs(x, p2) == 0):
       arr_bisection.append("-")

    if num_expr.subs(x, p1)*num_expr.subs(x, p) < 0:
        p2 = p
    else:
        p1 = p

    p = (p1+p2)/2

    while (abs(num_expr.subs(x, p)) > 0.0001):
        if num_expr.subs(x, p1)*num_expr.subs(x, p) < 0:
            p2 = p
        else:
            p1 = p

        p = (p1+p2)/2
        
    arr_bisection.append(round(p,5))
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
    arr_bisection = bisection(l_limit, r_limit, num_expr)

    if got_res == False:
        dpg.add_text(f"Newton method:\n{arr_newton}", before="5expr", id="5_result_newton")
        dpg.add_text(f"Bisection method:\n{arr_bisection}", before="5_result_newton", id="5_result_bisection")
        with dpg.window(label="Plot", width=550, height=600, id="plot_window5"):
            datax = []
            datay = []
            for i in np.arange(l_limit, r_limit, 0.1):
                datax.append(i)
                datay.append(num_expr.subs(x, i))
            with dpg.plot(height=500, width=500):
                dpg.add_plot_axis(dpg.mvXAxis, label="x")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", id="y_axis")
                dpg.add_line_series(datax, datay, parent="y_axis")
        got_res = True
    else:
        dpg.delete_item("plot_window5")
        dpg.delete_item("5_result_newton")
        dpg.delete_item("5_result_bisection")
        dpg.add_text(f"Newton method: {arr_newton}", before="5expr", id="5_result_newton")
        dpg.add_text(f"Bisection method: {arr_bisection}", before="5_result_newton", id="5_result_bisection")
        with dpg.window(label="Plot", width=550, height=600, id="plot_window5"):
            datax = []
            datay = []
            for i in np.arange(l_limit, r_limit, 0.1):
                datax.append(i)
                datay.append(num_expr.subs(x, i))
            with dpg.plot(height=500, width=500):
                dpg.add_plot_axis(dpg.mvXAxis, label="x")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", id="y_axis")
                dpg.add_line_series(datax, datay, parent="y_axis")
from operator import index
import dearpygui.dearpygui as dpg
import ctypes
from math import *
import sympy as sym
import numpy as np

got_res = False

def save_callback():
    global got_res
    int_up = float(dpg.get_value("4integr_up"))
    int_down = float(dpg.get_value("4integr_down"))
    expr = dpg.get_value("4expr")
    n = int(dpg.get_value("4n"))
    
    h = ((int_up - int_down)/n)
    arr_x = np.arange(int_down, int_up, h)
    arr_x_2 = np.arange(int_down, int_up+h, h)
    m_arr_x = [(x+h/2) for x in arr_x]


    x = sym.symbols('x')
    num_expr =  sym.parse_expr(expr)
    res_arr = []    # for r
    res_arr_2 = []  # for l
    m_res_arr = []  # for middle rectangles
    s_even_arr = []
    s_odd_arr = []

    for i, varx in enumerate(arr_x):
        res_arr.append(num_expr.subs(x, varx))
        if(i % 2 == 0 and i != 0 and i != n): s_even_arr.append(num_expr.subs(x, varx))
        if(i % 2 != 0 and i != 0 and i != n): s_odd_arr.append(num_expr.subs(x, varx))
    for i, varx in enumerate(arr_x_2):
        res_arr_2.append(num_expr.subs(x, varx))
    for varx in m_arr_x:
        m_res_arr.append(round(num_expr.subs(x, varx), 4))

    lrect = h*(sum(res_arr))
    rrect = h*(sum(res_arr_2)-res_arr_2[0])
    mrect = h*(sum(m_res_arr))
    simpsons = h/3*((res_arr[0] + res_arr[-1]) + 4*(sum(s_odd_arr)) + 2*(sum(s_even_arr)))
    trapezoids = h*(((res_arr[0]+res_arr[-1])/2) + (sum(res_arr)-res_arr[0]))

    if got_res == False:
        
        dpg.add_same_line(spacing=10, before="4_lrect", id="4_lrect_sline")
        dpg.add_text(f"{round(lrect, 4)}", before="4_lrect_sline", id="4_lrect_result")

        dpg.add_same_line(spacing=10, before="4_rrect", id="4_rrect_sline")
        dpg.add_text(f"{round(rrect, 4)}", before="4_rrect_sline", id="4_rrect_result")

        dpg.add_same_line(spacing=10, before="4_mrect", id="4_mrect_sline")
        dpg.add_text(f"{round(mrect, 4)}", before="4_mrect_sline", id="4_mrect_result")

        dpg.add_same_line(spacing=10, before="4_simpsons", id="4_simpsons_sline")
        dpg.add_text(f"{round(simpsons, 4)}", before="4_simpsons_sline", id="4_simpsons_result")
        
        dpg.add_same_line(spacing=10, before="4_trapezoids", id="4_trapezoids_sline")
        dpg.add_text(f"{round(trapezoids, 4)}", before="4_trapezoids_sline", id="4_trapezoids_result")
        got_res = True
    else:
        dpg.delete_item("4_lrect_sline")
        dpg.delete_item("4_lrect_result")
        dpg.add_same_line(spacing=10, before="4_lrect", id="4_lrect_sline")
        dpg.add_text(f"{round(lrect, 4)}", before="4_lrect_sline", id="4_lrect_result")

        dpg.delete_item("4_rrect_sline")
        dpg.delete_item("4_rrect_result")
        dpg.add_same_line(spacing=10, before="4_rrect", id="4_rrect_sline")
        dpg.add_text(f"{round(rrect, 4)}", before="4_rrect_sline", id="4_rrect_result")

        dpg.delete_item("4_mrect_sline")
        dpg.delete_item("4_mrect_result")
        dpg.add_same_line(spacing=10, before="4_mrect", id="4_mrect_sline")
        dpg.add_text(f"{round(mrect, 4)}", before="4_mrect_sline", id="4_mrect_result")

        dpg.delete_item("4_simpsons_sline")
        dpg.delete_item("4_simpsons_result")
        dpg.add_same_line(spacing=10, before="4_simpsons", id="4_simpsons_sline")
        dpg.add_text(f"{round(simpsons, 4)}", before="4_simpsons_sline", id="4_simpsons_result")

        dpg.delete_item("4_trapezoids_sline")
        dpg.delete_item("4_trapezoids_result")
        dpg.add_same_line(spacing=10, before="4_trapezoids", id="4_trapezoids_sline")
        dpg.add_text(f"{round(trapezoids, 4)}", before="4_trapezoids_sline", id="4_trapezoids_result")
import dearpygui.dearpygui as dpg
import ctypes

got_res = False
handle = ctypes.CDLL("./libtest.so")     
handle.cppcalc2.argtypes = [ctypes.c_double]
handle.cppcalc2.restype = ctypes.POINTER(ctypes.c_double)

def calc(x1, x2, x3, x4, fx1, fx2, fx3, fx4, point1, point2, point3, point4):
    res = handle.cppcalc2(
        ctypes.c_double(x1), ctypes.c_double(x2), ctypes.c_double(x3), ctypes.c_double(x4),
        ctypes.c_double(fx1), ctypes.c_double(fx2), ctypes.c_double(fx3), ctypes.c_double(fx4),
        ctypes.c_double(point1), ctypes.c_double(point2), ctypes.c_double(point3), ctypes.c_double(point4))
    return f"""f({point1}) = {round(res[0], 3)}\nf({point2}) = {round(res[1], 3)}\nf({point3}) = {round(res[2], 3)}\nf({point4}) = {round(res[3], 3)}\n"""

def get_points(x1, x2, x3, x4, fx1, fx2, fx3, fx4, point1, point2, point3, point4):
    res = handle.cppcalc2(
        ctypes.c_double(x1), ctypes.c_double(x2), ctypes.c_double(x3), ctypes.c_double(x4),
        ctypes.c_double(fx1), ctypes.c_double(fx2), ctypes.c_double(fx3), ctypes.c_double(fx4),
        ctypes.c_double(point1), ctypes.c_double(point2), ctypes.c_double(point3), ctypes.c_double(point4))
    return [res[0], res[1], res[2], res[3]]

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

    point1 = dpg.get_value("2dx_1")
    point2 = dpg.get_value("2dx_2")
    point3 = dpg.get_value("2dx_3")
    point4 = dpg.get_value("2dx_4")

    args = [x1, x2, x3, x4, fx1, fx2, fx3, fx4, point1, point2, point3, point4]
    if '' in args:
        txt = "Incorrect input."
        points = [0, 0, 0, 0]
    else:
        args = [float(x) for x in args]
        txt =   calc(args[0], args[1], args[2], args[3],
                    args[4], args[5], args[6], args[7],
                    args[8], args[9], args[10], args[11])
        points = get_points(args[0], args[1], args[2], args[3],
                    args[4], args[5], args[6], args[7],
                    args[8], args[9], args[10], args[11])
    
    if got_res == False:
        dpg.add_text(f"{txt}", before="go2", id="result2")
        with dpg.window(label="Plot", width=400, height=400):
            dpg.add_simple_plot(id="plot1", default_value=[points[0], points[1], points[2], points[3]], height=300)

            """sindatax = []
            sindatay = []
            for i in range(0, 100):
                sindatax.append(i / 100)
                sindatay.append(fx1*(((i-x2)*(i-x3)*(i-x4))/((x1-x2)*(x1-x3)*(x1-x4)))+fx2*(((i-x1)*(i-x3)*(i-x4))/((x2-x1)*(x2-x3)*(x2-x4)))+fx3*(((i-x1)*(i-x2)*(i-x4))/((x3-x1)*(x3-x2)*(x3-x4)))+fx4*(((i-x1)*(i-x2)*(i-x3))/((x4-x1)*(x4-x2)*(x4-x3))))
            with dpg.window(label="Plot"):

                # create plot
                with dpg.plot(height=500, width=500):

                    # REQUIRED: create x and y axes
                    dpg.add_plot_axis(dpg.mvXAxis, label="x")
                    dpg.add_plot_axis(dpg.mvYAxis, label="y", id="y_axis")

                    # series belong to a y axis
                    dpg.add_line_series(sindatax, sindatay, parent="y_axis")"""
        got_res = True
    else:
        dpg.delete_item("result2")
        dpg.delete_item("plot1")
        dpg.add_text(f"{txt}", before="go2", id="result2")
        with dpg.window(label="Plot", width=400, height=400):
            dpg.add_simple_plot(id="plot1", default_value=[points[0], points[1], points[2], points[3]], height=300)
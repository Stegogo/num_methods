import dearpygui.dearpygui as dpg
import ctypes

got_res = False
handle = ctypes.CDLL("./libtest.so")     
handle.cppcalc3.argtypes = [ctypes.c_double]
handle.cppcalc3.restype = ctypes.POINTER(ctypes.c_double)

def calc(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12,
            fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12,
            n1, n2):
    res = handle.cppcalc3(ctypes.c_double(x1), ctypes.c_double(x2), ctypes.c_double(x3),
                        ctypes.c_double(x4), ctypes.c_double(x5), ctypes.c_double(x6),
                        ctypes.c_double(x7), ctypes.c_double(x8), ctypes.c_double(x9),
                        ctypes.c_double(x10), ctypes.c_double(x11), ctypes.c_double(x12), 
                        ctypes.c_double(fx1), ctypes.c_double(fx2), ctypes.c_double(fx3),
                        ctypes.c_double(fx4), ctypes.c_double(fx5), ctypes.c_double(fx6),
                        ctypes.c_double(fx7), ctypes.c_double(fx8), ctypes.c_double(fx9),
                        ctypes.c_double(fx10), ctypes.c_double(fx11), ctypes.c_double(fx12),
                        ctypes.c_double(n1), ctypes.c_double(n2))
    print (res[0], res[1])
    return [round(res[0], 3), round(res[1], 3)]

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
        dpg.configure_item("3x_9", default_value='4.0')
        dpg.configure_item("3fx_9", default_value='4.507')
        dpg.configure_item("3x_10", default_value='4.2')
        dpg.configure_item("3fx_10", default_value='4.775')
        dpg.configure_item("3x_11", default_value='4.4')
        dpg.configure_item("3fx_11", default_value='5.159')
        dpg.configure_item("3x_12", default_value='4.6')
        dpg.configure_item("3fx_12", default_value='5.683')

        dpg.configure_item("3x_x11", default_value='2.4')
        dpg.configure_item("3x_x12", default_value='0.05')
        dpg.configure_item("3x_x21", default_value='4.04')
        dpg.configure_item("3x_x22", default_value='0.04')

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
        dpg.configure_item("3x_9", default_value='5.5')
        dpg.configure_item("3fx_9", default_value='8.862')
        dpg.configure_item("3x_10", default_value='6.0')
        dpg.configure_item("3fx_10", default_value='9.701')
        dpg.configure_item("3x_11", default_value='6.5')
        dpg.configure_item("3fx_11", default_value='11.132')
        dpg.configure_item("3x_12", default_value='7.0')
        dpg.configure_item("3fx_12", default_value='13.302')

        dpg.configure_item("3x_x11", default_value='1.6')
        dpg.configure_item("3x_x12", default_value='0.08')
        dpg.configure_item("3x_x21", default_value='6.3')
        dpg.configure_item("3x_x22", default_value='0.12')


def save_callback():
    global got_res
    x1 = dpg.get_value("3x_1")
    x2 = dpg.get_value("3x_2")
    x3 = dpg.get_value("3x_3")
    x4 = dpg.get_value("3x_4")
    x5 = dpg.get_value("3x_5")
    x6 = dpg.get_value("3x_6")
    x7 = dpg.get_value("3x_7")
    x8 = dpg.get_value("3x_8")
    x9 = dpg.get_value("3x_9")
    x10 = dpg.get_value("3x_10")
    x11 = dpg.get_value("3x_11")
    x12 = dpg.get_value("3x_12")

    fx1 = dpg.get_value("3fx_1")
    fx2 = dpg.get_value("3fx_2")
    fx3 = dpg.get_value("3fx_3")
    fx4 = dpg.get_value("3fx_4")
    fx5 = dpg.get_value("3fx_5")
    fx6 = dpg.get_value("3fx_6")
    fx7 = dpg.get_value("3fx_7")
    fx8 = dpg.get_value("3fx_8")
    fx9 = dpg.get_value("3fx_9")
    fx10 = dpg.get_value("3fx_10")
    fx11 = dpg.get_value("3fx_11")
    fx12 = dpg.get_value("3fx_12")

    n1 = (float(dpg.get_value("3x_x11")) + (float(dpg.get_value("3x_x12")) * float(dpg.get_value("3x_n1"))))
    n2 = (float(dpg.get_value("3x_x21")) - (float(dpg.get_value("3x_x22")) * float(dpg.get_value("3x_n2"))))

    args = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12,
            fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12,
            n1, n2]
    if '' in args:
        txt = "Incorrect input."
    else:
        args = [float(x) for x in args]
        txt = calc(args[0], args[1], args[2], args[3], args[4],
                    args[5], args[6], args[7], args[8], args[9], 
                    args[10], args[11], args[12], args[13],
                    args[14], args[15], args[16], args[17], args[18],
                    args[19], args[20], args[21], args[22], args[23], 
                    args[24], args[25])
        txt2 = calc(args[0], args[1], args[2], args[3], args[4],
                    args[5], args[6], args[7], args[8], args[9], 
                    args[10], args[11], args[12], args[13],
                    args[14], args[15], args[16], args[17], args[18],
                    args[19], args[20], args[21], args[22], args[23], 
                    args[25], args[24])
    dpg.configure_item("3result1", default_value=txt[0])
    dpg.configure_item("3result2", default_value=txt[1])
    dpg.configure_item("3result3", default_value=txt2[0])
    dpg.configure_item("3result4", default_value=txt2[1])
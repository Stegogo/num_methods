import os
import dearpygui.dearpygui as dpg
from dotenv import load_dotenv
load_dotenv('./envir.env')

from first import first_gui
from second import second_gui
from third import third_gui
from fourth import fourth_gui

comfortaa_path = os.environ['COMFORTAA_FONT_PATH']

with dpg.font_registry():
    dpg.add_font(comfortaa_path, 35)
    with dpg.font(comfortaa_path, 35, default_font=True):
        dpg.add_font_chars([0x221A, 0x8723, 0x03B4, 0x222B])

with dpg.window(label="Numbering Methods", id="main_window"):
    with dpg.tab_bar(id="tb1"):
        with dpg.tab(label=" 1 ", id="t1"):
            first_gui.first1()
        with dpg.tab(label=" 2 ",id="t2"):
            second_gui.second1()
        with dpg.tab(label=" 3 ", id="t3"):
            third_gui.third3()
        with dpg.tab(label=" 4 ", id="t4"):
            fourth_gui.fourth1()


dpg.setup_viewport()
dpg.set_viewport_width(700)
dpg.set_viewport_height(500)
dpg.set_primary_window("main_window", True)

with dpg.theme(default_theme=True):
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 20, 20, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10, 20, category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 117, 23], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [255, 222, 31], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 164, 0], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, [255, 117, 23], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TitleBg, [255, 117, 23], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, [255, 117, 23], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TabActive, [255, 117, 23], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TabHovered, [255, 164, 0], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_CheckMark, [255, 175, 109], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, [255, 156, 103], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, [255, 255, 153], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, [255, 191, 0, 153], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, [232, 125, 7, 103], category=dpg.mvThemeCat_Core)

    dpg.add_theme_color(dpg.mvThemeCol_PlotLines, [255, 222, 31], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvPlotCol_Line, [255, 225, 31], category=dpg.mvThemeCat_Plots)
    dpg.add_theme_style(dpg.mvPlotStyleVar_Marker, dpg.mvPlotMarker_Asterisk, category=dpg.mvThemeCat_Plots)
with dpg.theme(id="go_button"):
    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 20, 10, category=dpg.mvThemeCat_Core)


dpg.set_item_theme("go", "go_button")
dpg.set_item_theme("go2", "go_button")
dpg.set_item_theme("go3", "go_button")
dpg.set_item_theme("go4", "go_button")

dpg.start_dearpygui()

import os
from typing import Text
import dearpygui.dearpygui as dpg
from first import first_gui
from dotenv import load_dotenv
load_dotenv('./envir.env')
comfortaa_path = os.environ['COMFORTAA_FONT_PATH']

with dpg.font_registry():
    dpg.add_font(comfortaa_path, 35)
    with dpg.font(comfortaa_path, 35, default_font=True):
        dpg.add_font_chars([0x221A])


with dpg.window(label="Numbering Methods", id="main_window"):
    with dpg.tab_bar(id="tb1"):
        with dpg.tab(label=" 1 ", id="t1"):
            first_gui.first1()
        with dpg.tab(label=" 2 ",id="t2"):
            dpg.add_button(id="02")
        with dpg.tab(label=" 3 ", id="t3"):
            dpg.add_button(id="03")   


dpg.setup_viewport()
dpg.set_viewport_width(700)
dpg.set_viewport_height(300)
dpg.set_primary_window("main_window", True)

with dpg.theme(default_theme=True):
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 20, 20, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10, 10, category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 117, 23], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [255, 222, 31], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 164, 0], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TabActive, [255, 117, 23], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TabHovered, [255, 164, 0], category=dpg.mvThemeCat_Core)
with dpg.theme(id="go_button"):
    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 20, 10, category=dpg.mvThemeCat_Core)

dpg.set_item_theme("go", "go_button")

dpg.start_dearpygui()

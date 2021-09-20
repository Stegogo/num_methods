import os
from typing import Text
import dearpygui.dearpygui as dpg
from first import first_misc
from dotenv import load_dotenv
load_dotenv('./envir.env')
comfortaa_path = os.environ['COMFORTAA_FONT_PATH']

with dpg.font_registry():
    dpg.add_font(comfortaa_path, 35)
    with dpg.font(comfortaa_path, 35, default_font=True):
        dpg.add_font_chars([0x221A])


with dpg.window(label="Numbering Methods", id="main_window"):
    dpg.add_text("Determine the most accurate equation:")
    dpg.add_text("1)    √")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="n1", no_spaces=True, decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("=")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=120, id="x1", no_spaces=True, decimal=True)
    dpg.add_text("2) ")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="n2", no_spaces=True, decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("/")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="n22", no_spaces=True, decimal=True)
    dpg.add_same_line(spacing=10)
    dpg.add_text("=")
    dpg.add_same_line(spacing=10)
    dpg.add_input_text(width=100, id="x2", no_spaces=True, decimal=True)

    dpg.add_button(label="Go!", callback=first_misc.save_callback, id="go")
    dpg.set_item_pos("go", [500, 80])    


dpg.setup_viewport()
dpg.set_viewport_width(700)
dpg.set_viewport_height(200)
dpg.set_primary_window("main_window", True)

with dpg.theme(default_theme=True):
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 20, 20, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10, 10, category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 117, 23], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [255, 222, 31], category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 164, 0], category=dpg.mvThemeCat_Core)
with dpg.theme(id="go_button"):
    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 20, 10, category=dpg.mvThemeCat_Core)

dpg.set_item_theme("go", "go_button")

dpg.start_dearpygui()

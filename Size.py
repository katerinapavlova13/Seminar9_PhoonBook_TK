
window_width = 500
window_height = 250

width_add_cont = 340
height_add_cont = 150

column_width = 110
id_colums_width = 35

def X_POS(window, width):
    return (window.winfo_screenwidth() - width) // 2

def Y_POS(window, height):
    return (window.winfo_screenheight() - height) // 2

def window_geometry(window, width, height):
    return f'{width}x{height}+{X_POS(window, width)}+{Y_POS(window, height)}'
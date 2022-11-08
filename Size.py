window_width = 500
window_height = 280

width_add_cont = 300
height_add_cont = 115

column_width = 110
id_column_width = 35

def x_pos(window, width):
    return (window.winfo_screenwidth() - width) // 2

def y_pos(window, height):
    return (window.winfo_screenheight() - height) // 2

def window_geometry(window, width, height):
    return f'{width}x{height}+{x_pos(window, width)}+{y_pos(window, height)}'
from clipboard import copy

def copy_entry_value(entry_value):
    """Copy's the given value to the end users clipboard."""
    entry_value.copy()

def get_win_location(window, window_width, window_height) -> str:
    """Return a geometry string for centering an application UI Window."""
    w, h = window_width, window_height
    sx = window.winfo_screenwidth()
    sy = window.winfo_screenheight()
    x = int((sx - w) / 2)
    y = int((sy - h) / 2)
    return f'{w}x{h}+{x}+{y}'
def dpi_awareness(x):
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(x)
    except:pass
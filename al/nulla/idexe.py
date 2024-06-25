     import win32gui

     # Find the window by its title
     window_handle = win32gui.FindWindow(None, "Window Title")

     # Move the window to the upper position
     win32gui.SetWindowPos(window_handle, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOSIZE)
     
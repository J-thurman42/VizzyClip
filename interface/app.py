from customtkinter import CTk
import settings.settings as sett
import interface.widgets.widgets as wid

class MainWindow(CTk):
    """Represents the Main Window object that houses all layouts and the app's primary interface"""
    def __init__(self):
        super().__init__()

        one = wid.EntryOnlyPH(self)
        one.pack(fill='both', anchor='center')
        two = wid.LabelEntryCCB(self)
        two.pack(fill='both', anchor='center')

        self.mainloop()
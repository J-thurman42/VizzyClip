class SettingsManager():
    def __init__(self):
        super().__init__()

        self.APP_NAME = 'JT VizzyClip'
        self.APP_VERSION = '0.1.0'
        self.APP_PUBLISHER = 'Joshua Thurman'
        self.APP_INFO = 'assets/about.txt'

        # DEFAULT SETTINGS ---------------------------------
        
        # DEFAULT COLORS
        self.BACKGROUND_COLOR = "#000000"
        self.FOREGROUND_COLOR = "#0084AC"
        self.LABEL_TEXT_COLOR = '#FFFFFF'
        self.BUTTON_COLOR = "#5DCE00"
        self.BUTTON_TEXT_COLOR = "#000000"
        self.BUTTON_HOVER_COLOR = "#7BFF00"

        # DEFAULT ON-SCREEN TEXT
        self.ENTRY_LABELS = ['Enter text here...'] * 8
        self.LABELS = [f'Label-{i+1}' for i in range(8)]
        self.LABEL_FONT = ("Cambria", 12)
        self.BUTTON_FONT = ("Cambria", 10)
        self.ENTRY_FONT = ("Cambria", 12)

        # DEFAULT WINDOW SIZE AND PLACEMENT
        self.WINDOW_SIZE = str
        self.WINDOW_PLACEMENT = str
        self.LAYOUT = str


    def load(self):
        pass

    def save(self):
        pass

    def save_preset(self):
        pass
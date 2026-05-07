from customtkinter import CTkEntry, CTkButton, CTkFrame, StringVar, CTkLabel, set_appearance_mode, set_default_color_theme
import settings.settings as sett
import app_core.helpers as helpers

set_appearance_mode('DARK')
set_default_color_theme('green')

s = sett.SettingsManager()

class EntryOnlyPH(CTkFrame):
    """PH = A Widget with Entries that have Placeholder text."""
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=s.FOREGROUND_COLOR)

        self.entries: list[CTkEntry]  = []
        self.buttons: list[CTkButton] = []
        self.entry_vals: list[StringVar] = []

        self.columnconfigure(0, weight=100)
        self.columnconfigure(1, weight=1)

        for i in range(4):
            self.rowconfigure(i, weight=100)
            self.entry_vals.append(StringVar())
            entry = CTkEntry(self, placeholder_text=s.ENTRY_LABELS[i], font=s.ENTRY_FONT, height=20)
            entry.grid(column=0, row=i, sticky='EW', padx=(0, 1), pady=1)
            self.entries.append(entry)
            button = CTkButton(self, width=10, height=10, text='COPY', font=s.BUTTON_FONT, 
                               bg_color=s.FOREGROUND_COLOR, fg_color=s.BUTTON_COLOR,
                               hover_color=s.BUTTON_HOVER_COLOR, text_color=s.BUTTON_TEXT_COLOR,
                               command=lambda i=i: helpers.copy(self.entries[i].get()))
            button.grid(column=1, row=i, padx=1, pady=1)
            self.buttons.append(button)

class LabelEntryCCB(CTkFrame):
    """CCB = Copy/Clear Buttons: Four label+entry+copy-button rows plus section-level copy/clear."""

    def __init__(self, parent):
        super().__init__(master=parent, fg_color=s.FOREGROUND_COLOR)

        self.labels:  list[CTkLabel]  = []
        self.entries: list[CTkEntry]  = []
        self.buttons: list[CTkButton] = []

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=98)
        self.columnconfigure(2, weight=98)
        self.columnconfigure(3, weight=1)

        for num in range(4):
            self.rowconfigure(num, weight=1, minsize=20)
            label = CTkLabel(
                self, text=s.LABELS[num],
                text_color=s.LABEL_TEXT_COLOR, bg_color=s.FOREGROUND_COLOR,
                font=("Cambria", 12),
            )
            label.grid(column=0, row=num, sticky='ew', padx=7, pady=1)
            self.labels.append(label)

            entry = CTkEntry(self, width=120, height=20)
            entry.grid(column=1, row=num, sticky='ew', pady=1, columnspan=2)
            self.entries.append(entry)

            btn = CTkButton(
                self, text='COPY',
                text_color=s.BUTTON_TEXT_COLOR,
                font=s.BUTTON_FONT, width=10, height=20,
                fg_color=s.BUTTON_COLOR,
                hover_color=s.BUTTON_HOVER_COLOR,
                command=lambda i=num: helpers.copy(self.entries[i].get()),
            )
            btn.grid(column=3, row=num, sticky='ew', padx=3, pady=1)
            self.buttons.append(btn)

        # Section-level buttons — kept as instance attributes for color refresh
        self.copy_section_button = CTkButton(
            self, text='Copy Section',
            text_color=s.BUTTON_TEXT_COLOR,
            font=s.BUTTON_FONT, width=10, height=20,
            fg_color=s.BUTTON_COLOR,
            hover_color=s.BUTTON_HOVER_COLOR,
            command=self.copy_entries,
        )
        self.copy_section_button.grid(
            column=0, row=4, padx=2, pady=1, columnspan=2
        )

        self.clear_section_button = CTkButton(
            self, text='Clear Section',
            text_color=s.BUTTON_TEXT_COLOR,
            font=s.BUTTON_FONT, width=10, height=20,
            fg_color=s.BUTTON_COLOR,
            hover_color=s.BUTTON_HOVER_COLOR,
            command=self.clear_entries,
        )
        self.clear_section_button.grid(
            column=2, row=4, padx=2, pady=1, columnspan=2
        )

    def copy_entries(self) -> None:
        """Copy all label+entry pairs from this section to the clipboard."""
        lines = [
            f"{lbl.cget('text')} {entry.get()}"
            for lbl, entry in zip(self.labels, self.entries)
        ]
        helpers.copy("\n".join(lines))

    def clear_entries(self) -> None:
        for entry in self.entries:
            entry.delete(0, 'end')

class ToolBar(CTkFrame): # Not Converted to Modern Layout Yet
    """Bottom bar: settings icon | clock | copy-all | clear | (media controls)."""

    def __init__(self, window, bg_clr: str, lbl_txt_clr: str, button_txt_clr: str):
        super().__init__(master=window, fg_color=bg_clr)

        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=30)
        self.columnconfigure(2, weight=30)
        self.columnconfigure(3, weight=10, minsize=40)
        self.rowconfigure(0, weight=99, minsize=20)
        self.rowconfigure(1, weight=1)

        # Clock label
        self.label_0 = CTkLabel(
            self, text=con.TIME_TEMPLATE,
            text_color=lbl_txt_clr, bg_color=bg_clr,
            font=("Cambria", 12, 'bold'),
        )

        # Settings icon (acts as a button via bind in Window)
        self.settings_image = CTkImage(
            light_image=Image.open('DO-NOT-DELETE/Assets/settings.png'),
            dark_image=Image.open('DO-NOT-DELETE/Assets/settings.png'),
        )
        self.settings_button = CTkLabel(
            self, text='', image=self.settings_image, width=20, height=10
        )

        # Clear-all button
        self.button_0 = CTkButton(
            self, text="CLEAR *",
            text_color=button_txt_clr,
            font=('Cambria', 10), width=50, height=20,
            hover_color='red',
            fg_color=con.BUTTON_COLOR,
        )

        # Copy-all button
        self.copy_all_button = CTkButton(
            self, text="COPY *",
            text_color=button_txt_clr,
            font=('Cambria', 10), width=50, height=20,
            fg_color=con.BUTTON_COLOR,
            hover_color=con.BUTTON_HOVER_COLOR,
        )

        # Media controls sub-frame
        self.media_frame = CTkFrame(self, fg_color=bg_clr)
        self.media_frame.rowconfigure(0, weight=1)
        for col in range(3):
            self.media_frame.columnconfigure(col, weight=1)

        self.prev_button = CTkButton(
            self.media_frame, text="⏮", width=20, height=20,
            fg_color=con.BUTTON_COLOR, hover_color=con.BUTTON_HOVER_COLOR,
            text_color=con.BUTTON_TEXT_COLOR, command=media.prev_track,
        )
        self.play_button = CTkButton(
            self.media_frame, text="⏯", width=20, height=20,
            fg_color=con.BUTTON_COLOR, hover_color=con.BUTTON_HOVER_COLOR,
            text_color=con.BUTTON_TEXT_COLOR, command=media.play_pause,
        )
        self.next_button = CTkButton(
            self.media_frame, text="⏭", width=20, height=20,
            fg_color=con.BUTTON_COLOR, hover_color=con.BUTTON_HOVER_COLOR,
            text_color=con.BUTTON_TEXT_COLOR, command=media.next_track,
        )

        # Grid media buttons inside media_frame
        self.prev_button.grid(column=0, row=0, padx=2)
        self.play_button.grid(column=1, row=0, padx=2)
        self.next_button.grid(column=2, row=0, padx=2)

        # Grid the bar widgets
        self.settings_button.grid(column=0, row=0)
        self.label_0.grid(column=1, row=0, sticky='ew', padx=2, pady=2)
        self.copy_all_button.grid(column=3, row=0, sticky='ew', padx=2, pady=2)
        self.button_0.grid(column=4, row=0, sticky='ew', padx=2, pady=2)
        # media_frame placed/hidden by toggle_media_controls()

    def toggle_media_controls(self, show: bool) -> None:
        if show:
            self.label_0.grid_configure(column=1, columnspan=1, sticky="ew")
            self.media_frame.grid(column=2, row=0, padx=2)
        else:
            self.media_frame.grid_remove()
            self.label_0.grid_configure(column=1, columnspan=2, sticky="ew")

            if hasattr(self.master, "apply_layout"):
                layout = con.PARSER.get("OPTIONS", "selected_layout", fallback="default")
                self.master.apply_layout(layout)
from tkinter import *
from tkinter import ttk

from Boxes import Box
from scrollable_frame import ScrollableFrame
from tkinter import scrolledtext


def create_label_entry(parent_frame, entry_name, label_text, default_entry_txt):
    Label(parent_frame, text=label_text).pack(side=RIGHT, padx=5, pady=5)
    entry_name.insert(0, default_entry_txt)
    entry_name.pack(side=RIGHT)


class Combinations(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        master.geometry("800x600")

        # main frame
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

        # list of entries
        self.list_frame_entries = []
        self.list_boxes = []

        # set entries numbers
        self.big_frame = Frame(self.main_frame)
        self.big_frame.pack(fill=BOTH, expand=1, padx=5, pady=5, side=RIGHT)

        self.number_frame = Frame(self.big_frame)
        self.number_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

        self.high_frame = ScrollableFrame(self.big_frame)
        self.high_frame.pack(fill=BOTH, expand=1, padx=5, pady=50)

        self.number_entries = Entry(self.number_frame, justify=CENTER)
        create_label_entry(self.number_frame, self.number_entries, "כמות מספרים", "0")

        set_button = Button(self.number_frame, text="הצג", command=lambda: self.__set_buttons(),
                            height=1, width=20)
        set_button.pack(side=RIGHT, padx=5, pady=20)

        self.calculate_frame = Frame(self.big_frame)
        self.calculate_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        calculate_button = Button(self.calculate_frame, text="חשב", command=lambda: self.__calculate(),
                                  height=1, width=20)
        calculate_button.pack(padx=5, pady=5)

        self.text_frame = Frame(self.main_frame)
        self.text_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

        text_area = scrolledtext.ScrolledText(self.text_frame,
                                              wrap=WORD,
                                              width=40,
                                              height=50,
                                              font=("Times New Roman", 15))

        text_area.pack()

    def __set_buttons(self):
        # clean frames
        for frame_entry in self.list_frame_entries:
            frame_entry.destroy()
        self.list_frame_entries.clear()
        self.list_boxes.clear()

        for i in range(int(self.number_entries.get())):
            new_frame = Frame(self.high_frame.scrollable_frame)
            new_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
            self.list_frame_entries.append(new_frame)

            min_entry = Entry(new_frame, justify=CENTER)
            create_label_entry(new_frame, min_entry, "מינימום", "1")
            max_entry = Entry(new_frame, justify=CENTER)
            create_label_entry(new_frame, max_entry, "מקסימום", "20")

            self.list_boxes.append(Box(min_entry, max_entry))

    def __calculate(self):
        print("calculate")

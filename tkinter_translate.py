from tkinter import *
from googletrans import Translator, LANGUAGES
import pyttsx3
from tkinter import ttk
class Program:
    def __init__(self, heigth, width, title="Translate", resizable=(True, True)):
        self.root = Tk()
        self.root["bg"] = "#22baf6"
        self.root.title(title)
        self.root.geometry(f"{width}x{heigth}+250+200")
        self.root.resizable(resizable[0], resizable[1])
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)

        self.lang_list = list(LANGUAGES.values())
        self.text1 = Text(self.root, height=5, width=40, relief=GROOVE, font=("Arial", 11))
        self.text2 = Text(self.root, height=5, width=40, font=("Arial", 11), relief=GROOVE)

        self.dest_lang = ttk.Combobox(self.root, values=self.lang_list, state="readonly", width=15)
        self.dest_lang.set("english")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()
    def draw_widgets(self):
        label1 = Label(self.root, text="Translate", width=20, relief=GROOVE, font=("Arial", 14, "bold"))
        label1.pack(pady=5)
        self.text1.place(x=35, y=40)
        button = Button(self.root, text="trans", relief=GROOVE, width=10, command=self.trans)
        button.place(x=35, y=160)
        self.dest_lang.place(x=140, y=163)

        button1 = Button(self.root, text="voice", relief=GROOVE, width=10, command=self.voice)
        button1.place(x=280, y=160)
        self.text2.place(x=35, y=230)

    def trans(self):
        text_1 = self.text1.get('1.0', END).strip()
        if not text_1:
            return
        target_lang = self.dest_lang.get()
        translator = Translator()
        lang_code = [k for k, v in LANGUAGES.items() if v == target_lang][0]
        try:
            result = translator.translate(text_1, dest=lang_code)
            self.text2.delete("1.0", END)
            self.text2.insert(END, result.text)
        except Exception as e:
            print(f"Error: {e}")

    def voice(self):
        text = self.text2.get("1.0", END).strip()
        if text:
            self.engine.say(text)
            self.engine.runAndWait()


if __name__ == "__main__":
    pp = Program(400, 400)
    pp.run()
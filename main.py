import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# create morse dictionary
morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    " ": "/"
}

class App(customtkinter.CTk):
    def translate_morse_to_text(self, morse):
        text = ""
        for char in morse.split(" "):
            for key, value in morse_dict.items():
                if char == value:
                    text += key

        self.entry_morse_to_text.delete(0, "end")
        self.textbox_morse_to_text_result.delete("1.0", "end")
        self.textbox_morse_to_text_result.insert("end", text)


    def translate_text_to_morse(self, text):
        morse = ""

        for char in text.upper():
            morse += morse_dict[char] + " "

        self.entry_text_to_morse.delete(0, "end")
        self.textbox_text_to_morse_result.delete("1.0", "end")
        self.textbox_text_to_morse_result.insert("end", morse)

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Morse Translator - by AleDev")
        self.geometry(f"{600}x{550}")
        self.resizable(False, False)

        #create frame main
        self.frame_main = customtkinter.CTkFrame(self, width=600, height=500)
        self.frame_main.pack(pady=10, padx=10, fill="x")

        # create widgets
        self.label_title = customtkinter.CTkLabel(self.frame_main, text="Morse Translator", font=("Arial", 25, "bold"))
        self.label_title.pack(pady=10, padx=10, fill="x")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self.frame_main, width=600, height=500)
        self.tabview.pack(pady=10, padx=10, fill="x")

        # add tabs
        self.tabview.add("Morse to Text")
        self.tabview.add("Text to Morse")
        self.tabview.tab("Morse to Text")
        self.tabview.tab("Text to Morse")

        # create widgets for tab "Morse to Text"
        self.label_morse_to_text = customtkinter.CTkLabel(self.tabview.tab("Morse to Text"), text="Morse to Text", font=("Arial", 20, "bold"))
        self.label_morse_to_text.pack(pady=10, padx=10, fill="x")

        self.entry_morse_to_text = customtkinter.CTkEntry(self.tabview.tab("Morse to Text"), width=600)
        self.entry_morse_to_text.pack(pady=10, padx=10, fill="x")

        self.button_morse_to_text = customtkinter.CTkButton(self.tabview.tab("Morse to Text"), text="Translate", command=lambda: self.translate_morse_to_text(self.entry_morse_to_text.get()))
        self.button_morse_to_text.pack(pady=10, padx=10, fill="x")

        self.label_morse_to_text_result = customtkinter.CTkLabel(self.tabview.tab("Morse to Text"), text="Result", font=("Arial", 20, "bold"))
        self.label_morse_to_text_result.pack(pady=10, padx=10, fill="x")

        self.textbox_morse_to_text_result = customtkinter.CTkTextbox(self.tabview.tab("Morse to Text"), width=600, height=150, font=("Arial", 20, "bold"))
        self.textbox_morse_to_text_result.pack(pady=10, padx=10, fill="x")

        self.button_copy = customtkinter.CTkButton(self.tabview.tab("Morse to Text"), text="Copy Result",
                                                   command=lambda: self.clipboard_clear() or self.clipboard_append(
                                                       self.textbox_morse_to_text_result.get("1.0", "end")))
        self.button_copy.pack(pady=10, padx=10, fill="x")

        # create widgets for tab "Text to Morse"
        self.label_text_to_morse = customtkinter.CTkLabel(self.tabview.tab("Text to Morse"), text="Text to Morse", font=("Arial", 20, "bold"))
        self.label_text_to_morse.pack(pady=10, padx=10, fill="x")

        self.entry_text_to_morse = customtkinter.CTkEntry(self.tabview.tab("Text to Morse"), width=600)
        self.entry_text_to_morse.pack(pady=10, padx=10, fill="x")

        self.button_text_to_morse = customtkinter.CTkButton(self.tabview.tab("Text to Morse"), text="Translate", command=lambda: self.translate_text_to_morse(self.entry_text_to_morse.get()))
        self.button_text_to_morse.pack(pady=10, padx=10, fill="x")

        self.label_text_to_morse_result = customtkinter.CTkLabel(self.tabview.tab("Text to Morse"), text="Result", font=("Arial", 20, "bold"))
        self.label_text_to_morse_result.pack(pady=10, padx=10, fill="x")

        self.textbox_text_to_morse_result = customtkinter.CTkTextbox(self.tabview.tab("Text to Morse"), width=600, height=150, font=("Arial", 20, "bold"))
        self.textbox_text_to_morse_result.pack(pady=10, padx=10, fill="x")

        self.button_copy = customtkinter.CTkButton(self.tabview.tab("Text to Morse"), text="Copy Result",
                                                   command=lambda: self.clipboard_clear() or self.clipboard_append(
                                                       self.textbox_text_to_morse_result.get("1.0", "end")))
        self.button_copy.pack(pady=10, padx=10, fill="x")

        self.textbox_text_to_morse_result.insert("end", "Morse Translator by AleDev")
        self.textbox_morse_to_text_result.insert("end", "Morse Translator by AleDev")

if __name__ == "__main__":
    app = App()
    app.mainloop()
from tkinter import *

class Converter:
    
    def __init__(self):

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "11", "bold")
        button_fg = "#FFF7F1"

        # Set up GUI Frame
        self.temp_frame = Frame(bg = "#F1FADA")
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text = "Temperature Convertor", font =("Arial", "16", "bold" ), bg = "#F1FADA")
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and then press one of the buttons to convert it from centigrade to Fahrenheit"
        self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify="left", bg = "#F1FADA")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text=error, fg="#9C0000", bg = "#D24545")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame, text="To Celsius", bg = "#6C22A6", fg = button_fg, font = button_font, width = 12)
        self.to_celsius_button.grid(row=0, column=0, padx = 5, pady = 5)

        self.to_farenheit_button = Button(self.button_frame, text="To Farenheit", bg = "#6962AD", fg = button_fg, font = button_font,width = 12)
        self.to_farenheit_button.grid(row=0, column=1, padx = 5, pady = 5)

        self.to_help_button = Button(self.button_frame, text = "Help / Info", bg = "#83C0C1", fg = button_fg, font = button_font, width = 12)
        self.to_help_button.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.to_history_button = Button(self.button_frame, text = "History / Export", bg = "#96E9C6", fg = button_fg, font = button_font, width = 12, state = DISABLED)
        self.to_history_button.grid(row = 1, column = 1, padx = 5, pady = 5)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
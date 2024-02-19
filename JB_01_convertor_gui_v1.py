from tkinter import *

class Converter:
    
    def __init__(self):
        

        # Initialise variables a(such as feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "11", "bold")
        button_fg = "#FFF7F1"

        # Set up GUI Frame
        self.temp_frame = Frame(bg = "#83A2FF")
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text = "Temperature Convertor", font =("Arial", "16", "bold" ), bg = "#83A2FF", fg = "#001B79")
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and then press one of the buttons to convert it from Celsius to Fahrenheit"
        self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify="left", bg = "#83A2FF", fg = "#22092C")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text="", fg="#9C0000")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame, text="To Celsius", bg = "#424769", fg = button_fg, font = button_font, width = 12, command = self.to_celsius)
        self.to_celsius_button.grid(row=0, column=0, padx = 5, pady = 5)

        self.to_farenheit_button = Button(self.button_frame, text="To Farenheit", bg = "#2D3250", fg = button_fg, font = button_font,width = 12)
        self.to_farenheit_button.grid(row=0, column=1, padx = 5, pady = 5)

        self.to_help_button = Button(self.button_frame, text = "Help / Info", bg = "#7077A1", fg = button_fg, font = button_font, width = 12)
        self.to_help_button.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.to_history_button = Button(self.button_frame, text = "History / Export", bg = "#7360DF", fg = button_fg, font = button_font, width = 12, state = DISABLED, disabledforeground="#392467")
        self.to_history_button.grid(row = 1, column = 1, padx = 5, pady = 5)

    # checks user input and if it's valid, converts temperature
    def check_temp(self, min_value):
        has_error = "no"
        error = "Please enter a number that is more " "than {}".format(min_value)

        # check that user has entered a valid number

        response = self.temp_entry.get()

        try:
            response = float(response)

            if response < min_value:
                has_error = "yes"
                #self.temp_error.config(text=error)
            #else:
                #return response

        except ValueError:
            has_error = "yes"
            #self.temp_error.config(text=error)
        
        # Sets var_has_error so that entry box
        # and labels can be correctly formatted by formatting function
        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        # If we have no errors...
        else:
            # set to 'no' in case of previous errors
            self.var_has_error.set("no")

            # return number to be
            # converted and enable history button
            self.to_history_button.config(state=NORMAL)
            return response

    # check temperature is more than -459 and convert it
    def to_celsius(self):
        to_convert = self.check_temp(-459)

        if to_convert != "invalid":
        # do calculation
            self.var_feedback.set("Converting {} to " "C :)".format(to_convert))

        #self.check_temp(-459)
        self.output_answer()

    # Shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            # red text, pink entry box
            self.temp_error.config(fg="#9C0000")
            self.temp_entry.config(bg = "#F8CECC")
        
        else:
            self.temp_error.config(fg="#004C00")
            self.temp_entry.config(bg="#FFFFFF")

        self.temp_error.config(text=output)
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
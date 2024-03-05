from tkinter import *
from functools import partial # To prevent unwanted windows
#watch video 15 (1min) (u finished def get calc, just need to fix error)

class Converter:
    
    def __init__(self):
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Five item list
        # self.all_calculations = ['0 F° is -18 C°', '0 C° is 32 F°', '30 F° is -1 C°', '30 C° is 86 F°', '40 F° is 4 C°']

        # Six Item list
        self.all_calculations = ['0 F° is -18 C°', '0 C° is 32 F°', '30 F° is -1 C°', '30 C° is 86 F°', '40 F° is 4 C°']

        # set up GUI frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_history_button = Button(self.button_frame, text = "History / Export", bg ="#004C99", fg=button_fg, font=button_font, width=12,command=self.to_history(self.all_calculations))

        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

        # *** Remove when integrating!! ***
        self.to_history_button.config(state=NORMAL)

    def to_history(self, all_calculations):
        HistoryExport(self, all_calculations)

class HistoryExport:

    def __init__(self, partner, calc_list):

        # set maximu, number of calculations to 5
        # this can be changed if we want to show fewer / more calculations
        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        # Function converts contents of a calculation list into a string
        calc_string_text = self.get_calc_string(calc_list)

        # setup dialogue box and background colour
        self.history_box = Toplevel()
        
        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,partner))

        self.history_frame = Frame(self.history_box, width=300, height=200)

        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame, text = "History / Export", font=("Arial","16","bold"))

        self.history_heading_label.grid(row=0)

        # Customise text and background colour for calculation area depending on whether all or only some calculations are shown
        num_calcs = len(calc_list)

        if num_calcs > max_calcs:
            calc_background = "#FFE6CC"
            showing_all = "Here are your recent calculations " "({}/{}calculations shown). Please export your calculations to see your full calculation history".format(max_calcs, num_calcs)
        else:
            calc_background = "#B4FACB"
            showing_all = "Below is your calculation history."


        # History text and label
        hist_text = "{} \n\n All calculations are shown to the nearest degree.".format(showing_all)



        self.hist_text_label = Label(self.history_frame, text=hist_text, justify="left", wraplength=300, padx=10, pady=10)

        self.hist_text_label.grid(row=1)

        self.all_calcs_label = Label(self.history_frame, text = "Calculations go here", padx= 10, pady = 10, bg = "#ffe6cc", width=40, justify="left")

        self.all_calcs_label.grid(row=2)

        # Instructions for Saving Files
        save_text = "Either choose a custom file name (and push <Export>) or simply push <Export> to save your calculations in a text file. If the filename already exists, it will be overwritten!"
        self.save_instructions_label = Label(self.history_frame, text=save_text, wraplength=300, justify="left", width=40, padx=10, pady=10)
        self.save_instructions_label.grid(row=3)

        # Filename entry widget, white background to start
        self.filename_entry = Entry(self.history_frame, font = ("Arial", "14"), bg = "#ffffff", width = 25)
        self.filename_entry.grid(row = 4, padx=10, pady=10)

        self.filename_error_label = Label(self.history_frame, text = "File name error goes here", fg = "#9C0000", font = ("Arial", "12", "bold"))

        self.filename_error_label.grid(row=5)

        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=6)

        self.export_button = Button(self.button_frame, font = ("Arial", "12", "bold"), text="Export", bg = "#004C99", fg = "#FFFFFF", width = 12)

        self.export_button.grid(row=0, column=0, padx=10, pady=10)
        


        self.dismiss_button = Button(self.button_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#666666", fg = "#FFFFFF", width=12, command=partial(self.close_history,partner))

        self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)
    
    # closes history dialogue (used by button and x at top of dialogue)
    def close_history(self, partner):
        # Put history button back to nrmal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()

        # Initialise variables a(such as feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "11", "bold")
        button_fg = "#FFF7F1"

        # Set up GUI Frame
        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text = "Temperature Convertor", font =("Arial", "16", "bold" ), fg = "#001B79")
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and then press one of the buttons to convert it from Celsius to Fahrenheit"
        self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify="left", fg = "#22092C")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text="", fg="#9C0000")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame, text="To Celsius", bg = "#424769", fg = button_fg, font = button_font, width = 12, command = lambda: self.temp_convert(-459))
        self.to_celsius_button.grid(row=0, column=0, padx = 5, pady = 5)

        self.to_farenheit_button = Button(self.button_frame, text="To Farenheit", bg = "#2D3250", fg = button_fg, font = button_font,width = 12, command = lambda: self.temp_convert(-273))
        self.to_farenheit_button.grid(row=0, column=1, padx = 5, pady = 5)

        self.to_help_button = Button(self.button_frame, text = "Help / Info", bg = "#7077A1", fg = button_fg, font = button_font, width = 12, command = self.to_help)
        self.to_help_button.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.to_history_button = Button(self.button_frame, text = "History / Export", bg = "#7360DF", fg = button_fg, font = button_font, width = 12, state = DISABLED, disabledforeground="#392467")
        self.to_history_button.grid(row = 1, column = 1, padx = 5, pady = 5)
    #
    # checks user input and if it's valid, converts temperature
    def check_temp(self, min_value):
        has_error = "no"
        error = "Please enter a number that is more " "than {}".format(min_value)

        # check that user has entered a valid number

        #response = self.temp_entry.get()

        try:
            response = self.temp_entry.get()
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

        #if the number is invalid display error message
        if has_error == "yes":
            self.temp_error.config(text=error, fg="#9C0000")
            #self.var_has_error.set("yes")
            #self.var_feedback.set(error)
            #return "invalid"

        # If we have no errors...
        else:
            # set to 'no' in case of previous errors
            #self.var_has_error.set("no")
            self.temp_error.config(text="You are OK", fg="blue")

            # return number to be
            # converted and enable history button
            self.to_history_button.config(state=NORMAL)
            return response

    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2
        return "{:.0f}".format(var_rounded)



    # check temperature is valid and convert it
    def temp_convert(self, min_val):
        to_convert = self.check_temp(min_val)
        deg_sign = u'\N{DEGREE SIGN}'
        set_feedback = "yes"
        answer = ""
        from_to = ""

        if to_convert == "invalid":
            set_feedback = "no"
        
        # Convert to Celsius
        elif min_val == -459:
            # do calculation
            answer = (to_convert - 32) * 5 / 9
            from_to = "{} F{} is {} C{}"

        # Convert to Farenheit
        else:
            answer = to_convert * 1.8 + 32
            from_to = "{} C{} is {} F{}"
       
        if set_feedback == "yes":
            to_convert = self.round_ans(to_convert)
            answer = self.round_ans(answer)

            # create user output and add to calculation history
            feedback = from_to.format(to_convert, deg_sign, answer, deg_sign)
            
            self.var_feedback.set(feedback)

            self.all_calculations.append(feedback)

            # Delete code below when history component is working!
            print(self.all_calculations)

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
        
    # Open help / Info Dialogue Box
    def to_help(self):
        DisplayHelp(self)

class DisplayHelp:

    def __init__(self, partner):

        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()
        
        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)

        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background,text = "Help / Info", font=("Arial","14","bold"))

        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature you wish to convert and then choose to convert to either degrees Celsius (centigrade) or Fahrenheit.. \n\n" "Note that -273 degrees C, you will get an error message. \n\n" "To see your calculation history and export it to a text file, please click the 'History / Export' button."

        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wrap=350, justify="left")

        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#CC6600", fg = "#FFFFFF", command=partial(self.close_help,partner))

        self.dismiss_button.grid(row=2, padx=10, pady=10)
    
    # change calculation list into a string so that it can be outputted as a label
    def get_calc_string(self, var_calculations):
        # get maxmum calculations to display
        # (was set in __init__ function)
        max_calcs = self.var_max_calcs.get()
        calc_string = ""

        # work out how many times we need to loop
        # to output either the last five calculations
        # or all the calculations
        if len(var_calculations) >= max_calcs:
            stop = max_calcs

        else:
            stop = len(var_calculations)

        # iterate to all but last item,
        # adding item and line break to calculation string
        for item in range(0, stop - 1):
            calc_string += var_calculations[len(var_calculations) - item - 1]

            calc_string += "\n"

        # add final item without an extra linebreak
        # ie: last item on list will be fifth from the end!
        calc_string += var_calculations[-max_calcs]

        return calc_string


    # closes help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # Put help button back to nrmal...
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
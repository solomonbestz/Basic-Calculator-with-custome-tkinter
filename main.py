import customtkinter as bestz
from PIL import Image, ImageTk


# Setting default theme and appearance mode
bestz.set_default_color_theme("dark-blue") 
bestz.set_appearance_mode('dark') 

"""
Functions to build the entry components
"""

def entry_component():
    global entry_frame
    entry_frame = bestz.CTkFrame(master=root, height=180, width=240, fg_color='#FF9933')
    entry_frame.grid(row=0, column=0, padx=10, pady=20)
    entry_widget()
    

def entry_widget():
    entry_field = bestz.CTkEntry(master=entry_frame, placeholder_text='I am ayo', width=200, fg_color='#fff', border_width=0)
    entry_field.grid(row=2, column=2, padx=20, pady=50)

"""
END OF FUNCTION
"""

"""
Function to build frame for numbers and operators
"""

def num_and_op_comp():
    global numbers_op_frame
    numbers_op_frame = bestz.CTkFrame(master=root, height=180, width=250, fg_color='#001933', bg_color="#001933" )
    numbers_op_frame.grid(row=1, column=0)

"""
END OF FUNCTION
"""

"""
Functions to build the numbers component
"""
def numbers_component():
    global numbers_frame
    numbers_frame = bestz.CTkFrame(master=numbers_op_frame, height=180, width=110, fg_color='#001933', bg_color="#001933")
    numbers_frame.grid(row=0, column=0, padx=5)
    numbers_button()

def numbers_button():
    for butt in range(1, 13):
        button = bestz.CTkButton(master=numbers_frame, width=40, height=40, fg_color='#001933', hover_color='#FF9933')
        numbers(butt, button)
        special_button(butt, button)
        
def numbers(butt, button):
    if butt <= 3:
            button.configure(text=str(butt+6))
            button.grid(row=0, column=butt-1)
    elif butt <= 6:
        button.configure(text=str(butt))
        button.grid(row=1, column=butt-4)
    elif butt <= 9:
        button.configure(text=str(butt-6))
        button.grid(row=2, column=butt-7)

def special_button(butt, button):
    if butt == 10:
        button.configure(text="0")
        button.grid(row=3, column=0)
    elif butt == 11:
        button.configure(text=".")
        button.grid(row=3, column=1)
    elif butt == 12:
        button.configure(text="C")
        button.grid(row=3, column=2)

"""
END OF FUNCTION
"""

"""
Functions to build the operators component
"""

def operators_component():
    global operators_frame
    operators_frame = bestz.CTkFrame(master=numbers_op_frame, height=180, width=110, fg_color='#001933')
    operators_frame.grid(row=0, column=1, padx=5)
    operators_button()


def operators_button():

    for butt in range(6):
        button = bestz.CTkButton(master=operators_frame, width=15, height=20, fg_color="#FF9933", corner_radius=50)
        if butt <= 1:
            first_row = ['-', '/']
            button.configure(text=first_row[butt])
            button.grid(row=0, column=butt, padx=8)
        elif butt <= 3:
            if butt == 2:
                button.configure(text='+', height=50)
                button.grid(rowspan= 2, column=0, padx=8, pady=5)
            else:
                button.configure(text='x', height=20)
                button.grid(row=1, column=1, padx=8, pady=5)
        elif butt <= 5:
            if butt == 4:
                button.configure(text='%', height=20)
                button.grid(row=2, column=1, padx=8, pady=5)
            



if __name__=='__main__':

    
    root = bestz.CTk()
    root.iconbitmap('ayo_logo.ico')
    root.geometry('260x400')
    root.resizable(0, 0)
    root.config(background="#001933")
    root.title('AYO')
    
    
    # Calling Our Functions
    entry_component()
    num_and_op_comp()
    numbers_component()
    operators_component()

    root.mainloop()